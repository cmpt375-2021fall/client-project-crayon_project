from django import forms


class UserForm(forms.Form):
    email = forms.EmailField(label = "email", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Email",'autofocus': ''}))
    password = forms.CharField(label="password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "Password"}))

class RegisterForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm your password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={'class': 'form-control'}))
   # captcha = CaptchaField(label='Verification code')

class RoomForm(forms.Form):
    room_id = forms.CharField(label="room_id", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': "Room ID"}))