from django import forms
from django.core.validators import RegexValidator, ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.db.models import Q

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
        validators=[username_validator],        
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

    def clean(self):
        cleaned_data = super().clean()
        if get_user_model().objects.filter(
            Q(username=cleaned_data.get('username')) |
            Q(email=cleaned_data.get('email'))
        ).exists():
            raise ValidationError(
                _('O nome de usuário ou o email já está sendo utilizado'),
            )
        return cleaned_data
