from django import forms
import django.forms.utils
import django.forms.widgets


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, initial='Enter your Email ID')
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if not username and not password:
            raise forms.ValidationError('You have to write something!')

class UserRegistrationForm(forms.Form):
    FirstName = forms.CharField(
        label='First Name', max_length=100, min_length=1, required=True)
    LastName = forms.CharField(
        label='Last Name', max_length=100, min_length=1, required=True)
    Password = forms.CharField(
        label='Password', widget=forms.PasswordInput(), min_length=1, required=True)
    EmailID = forms.EmailField(
        label='Email', max_length=60, min_length=1, required=True)
    MobileNo = forms.CharField(label='Phone', min_length=10, required=False)
    Gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=[('M','Male'), ('F','Female')]), required=True)
    MaritalStatus = forms.ChoiceField(label='Marital Status', choices=[('Married','Married'), ('Single','Single')], required=True)
    DOB = forms.DateField(label='Birthdate',
                          widget=forms.DateInput(attrs={'placeholder': '__/__/____', 'class': 'date', }), required=True)
