from django import forms

class LoginForm(forms.Form):
    login_email = forms.EmailField(label="Email Address", required=True)
    login_password = forms.CharField(label="Password", widget=forms.PasswordInput(), required=True)
