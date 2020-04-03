from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _

name_validator = RegexValidator(
    r'^[A-Za-z ](?i){2,}$',
    message=_('Digite um nome válido')
)

username_validator = RegexValidator(
    r'^\w{3,16}$',
    message=_('Digite um nome de usuário válido'),
)

class UserForm(forms.Form):
    username = forms.SlugField(
        required=True,
        validators=[username_validator]
    )
    first_name = forms.CharField(
        required=True,
        validators=[name_validator]
    )
    last_name = forms.CharField(
        required=True,
        validators=[name_validator]
    )
    email = forms.EmailField(
        required=True,
    )
    password = forms.CharField(
        required=True,
        min_length=8,                
    )