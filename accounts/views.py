from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .forms import SignUpForm
from .tokens import confirmation_email_token_generator
from .utils import send_confirmation_email
from django.contrib.auth import get_user_model


User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            send_confirmation_email(request,user)
            return render(request, 'registration/signup_success.html')

    else:
        form = SignUpForm
    return render(request, 'registration/signup.html', {'form': form})



def activate_email(request, uid, token):
    user = get_object_or_404(User, pk=uid)
    if confirmation_email_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect('login')

    else:
        return HttpResponseBadRequest('Bad Token')