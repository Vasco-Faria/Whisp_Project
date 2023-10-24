from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .forms import ResetPasswordForm
from django.contrib import messages

def reset_password(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            new_password = form.cleaned_data['new_password']
            try:
                user = User.objects.get(email=email)
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Password Changed")
                return redirect('/')
            except User.DoesNotExist:
                pass
        else:
            messages.error(request, "Password Change Failed. Please check your inputs.")
    else:
        form = ResetPasswordForm()

    return render(request, 'account/reset_password.html', {'form': form})

