from django import forms

from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label="First Name", max_length=50, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(required=True, label="Last Name", max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email = forms.EmailField(required=True, label="Email", max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    username = forms.CharField(required=True, label="Username", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("The given email is already registered")
        return self.cleaned_data['email']

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']
