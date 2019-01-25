from django import forms
from customerauth import models
from customerauth.models import Customers
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class CustomersForm(forms.ModelForm):
    """Form definition for MODELNAME."""
    fname = forms.CharField(label='First Name', max_length=100)
    mname = forms.CharField(label='Middle Name', max_length=100)
    lname = forms.CharField(label='last Name', max_length=100)
    phone = forms.IntegerField(label='Phone Number')
    email = forms.EmailInput()
    addess =forms.CharField(
        label="Description",
        max_length=2000,
        widget=forms.Textarea(attrs={'placeholder': 'Description'}),
        help_text='Write here your message!')
    image = forms.ImageField(label='Upload image', max_length=100)
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
    confirm_password = forms.CharField(label='Confirm Password', max_length=100)

    def __init__(self, *args, **kwargs):
        super(CustomersForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'
    class Meta:
        """Meta definition for MODELNAMEform."""
        model = Customers
        fields = ('fname','mname','lname','phone','email','address','image','username','password','confirm_password')
        
    def clean(self):
        cleaned_data = super(CustomersForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
                self.add_error('confirm_password', "Password does not match")

        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        min_length = 8
        
        if not any(char.isdigit() for char in password):
                raise ValidationError(_('Password must contain at least one  digit.'))
        if not any(char.isalpha() for char in password):
                raise ValidationError(_('Password must contain at least one  letter.'))
        if not any(char in special_characters for char in password):
                raise ValidationError(_('Password must contain at least one special character.'))      
        return cleaned_data



