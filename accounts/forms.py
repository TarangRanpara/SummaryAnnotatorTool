from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class LogInForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
                'id': 'username'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id': 'passwordInput'
            }
        )
    )

    def clean(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username = username)

        if not qs.exists():
            raise forms.ValidationError("This is Invalid username")

class UserRegisterationForm(forms.Form):
    username = forms.CharField(

        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id': 'passwordInput1'
            }
        )
    )

    password2 = forms.CharField(
        label = "Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id': 'passwordInput2'
            }
        )
    )

    def clean(self):
        self.check_email()
        self.check_username()

    def check_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email = email)

        if qs.exists():
            raise forms.ValidationError("This is Invalid email")

    def check_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username = username)

        if qs.exists():
            raise forms.ValidationError("This is Invalid username")
