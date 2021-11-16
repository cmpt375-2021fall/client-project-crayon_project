from django import forms

from crayonApp.models import Question, Response, Answer


class UserForm(forms.Form):
    email = forms.EmailField(label = "email", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Email",'autofocus': ''}))
    password = forms.CharField(label="password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "Password"}))

class RegisterForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm your password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={'class': 'form-control'}))
   # captcha = CaptchaField(label='Verification code')

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text', )

class TakeQuizForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset=Response.objects.none(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None)

    class Meta:
        model = Answer
        fields = ('answer', )

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        self.fields['answer'].queryset = question.answers.order_by('text')