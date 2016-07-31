from django import forms
from django.contrib.auth.models import User
from .models import Profile
import string


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    MIN_LENGTH = 6
    MAX_LENGTH = 10
    password_is_valid = False

    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_email(self):
        cd = self.cleaned_data
        email = cd['email']
        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError(u'Email address must be unique.')
        return email

    def clean_password(self):
        cd = self.cleaned_data
        password = cd['password']

        num_check = False
        char_check = False

        letters = list(string.ascii_letters)
        numbers = [str(i) for i in range(10)]
        pass_len = len(password)
        if pass_len < self.MIN_LENGTH or pass_len > self.MAX_LENGTH:
            self.password_is_valid = False
            raise forms.ValidationError(u'Password required 6 to 10 characters.')
        for c in password:
            if c in letters:
                char_check = True
            if c in numbers:
                num_check = True
        print(num_check)
        if not num_check or not char_check:
            self.password_is_valid = False
            raise forms.ValidationError(u'Your password must include at least \
                                          one letter and at least one number.')

        return password

    def clean_password2(self):
        cd = self.cleaned_data
        # print(cd)
        if not self.password_is_valid:
            return None
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.Form):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileEditForm(forms.Form):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']
