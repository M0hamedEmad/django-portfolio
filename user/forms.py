from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.forms import ModelForm
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm
from django import forms
from django.core.exceptions import ValidationError

class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        # exclude = ['password']

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)

        classes = """block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700
                    focus:border-purple-400 focus:outline-none
                    focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input"""
        
        self.fields['username'].widget.attrs = {'class':classes}
        self.fields['email'].widget.attrs = {'class':classes}
        self.fields['first_name'].widget.attrs = {'class':classes}
        self.fields['last_name'].widget.attrs = {'class':classes}

        self.fields['username'].help_text = ''
 

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
        'placeholder': 'Jane Doe',
        'type': 'email',
        'name': 'email'
        }))




class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    error_messages = {
        'password_mismatch': ('The two password fields didn’t match.'),
    }
    new_password1 = forms.CharField(
        label=("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
        'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
        }),
        strip=False,
    )
    new_password2 = forms.CharField(
        label= ("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
        'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
        }),
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        password_validation.validate_password(password2, self.user)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user


class PasswordChange(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChange, self).__init__(*args, **kwargs)
        
        classes =  """block w-full mt-1 text-sm dark:border-gray-600 
        dark:bg-gray-700 focus:border-purple-400 focus:outline-none 
        focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input"""

        self.fields['old_password'].widget.attrs = {
            'class': classes
        }
    
        self.fields['new_password1'].widget.attrs = {
            'class': classes
        }   
        
        self.fields['new_password2'].widget.attrs = {
            'class': classes
        }
    
   