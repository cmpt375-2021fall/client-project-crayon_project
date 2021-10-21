from django import forms


class UserForm(forms.Form):
    email = forms.EmailField(label = "email", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Email",'autofocus': ''}))
    password = forms.CharField(label="password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "Password"}))