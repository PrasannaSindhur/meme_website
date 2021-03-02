from user_navigation.models import UserDetails
from django import forms


class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['first_name', 'last_name', 'email_id', 'password', 'confirm_password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name',
                                                 'required': 'required',
                                                 'name': 'first_name',
                                                 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name',
                                                'required': 'required',
                                                'name': 'first_name',
                                                'class': 'form-control'}),
            'email_id': forms.TextInput(attrs={'placeholder': 'Email Id',
                                               'required': 'required',
                                               'name': 'first_name',
                                               'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password',
                                                   'required': 'required',
                                                   'name': 'password',
                                                   'class': 'form-control'}),
            'confirm_password': forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                           'required': 'required',
                                                           'name': 'password',
                                                           'class': 'form-control'})
        }

    def clean(self):
        data = self.cleaned_data
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")
        return data


