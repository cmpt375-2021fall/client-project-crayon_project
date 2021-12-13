from django import forms
from .models import File


class UserForm(forms.Form):
    email = forms.EmailField(label = "email", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Email",'autofocus': ''}))
    password = forms.CharField(label="password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "Password"}))

class RegisterForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm your password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={'class': 'form-control'}))
   # captcha = CaptchaField(label='Verification code')

class CreateForm(forms.Form):
    name = forms.CharField(label="project name", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': "Project Name"}))

class EnterForm(forms.Form):
    room_id = forms.CharField(label="project id", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': "Project ID"}))

# Model form
class FileUploadModelForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file', )
        widgets = {
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_file(self):
        file = self.cleaned_data['file']
        ext = file.name.split('.')[-1].lower()
        if ext not in ["pdf"]:
            raise forms.ValidationError("Only pdf files are allowed.")
        # return cleaned data is very important.
        return file