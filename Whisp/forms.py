from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages

class ResetPasswordForm(forms.Form):
    email = forms.EmailField(
        label="E-mail",
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'border border-gray-300','placeholder': 'E-mail'})
    )
    new_password = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'border border-gray-300','placeholder': 'New Password'})
    )
    confirm_new_password = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={'class': 'border border-gray-300','placeholder': 'Confirm New Password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_new_password = cleaned_data.get('confirm_new_password')

        if new_password != confirm_new_password:
            raise forms.ValidationError("As senhas não coincidem. Por favor, tente novamente.")
