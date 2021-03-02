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


class QuestionForm(forms.Form):
    number = forms.IntegerField(min_value=1, max_value=50)
    question = forms.CharField(max_length=300)
    options = forms.MultipleChoiceField()
    answer = forms.IntegerField(min_value=1, max_value=4)
    explanation = forms.CharField(max_length=500)

    def __init__(self, number, question, option1, option2, option3, option4, answer, explanation, *args, **kwargs):
        self.number = number
        self.question = question
        options_list = (
            ('a', option1),
            ('b', option2),
            ('c', option3),
            ('d', option4)
        )
        self.options = forms.MultipleChoiceField(choices=options_list)
        self.answer = answer
        self.explanation = explanation
        super(QuestionForm, self).__init__(*args, **kwargs)
