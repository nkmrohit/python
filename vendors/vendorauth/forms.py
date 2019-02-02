from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from vendorauth import models
from vendorauth.models import vendors

class VendorsForm(forms.ModelForm):
    """Form definition for MODELNAME."""
    fname = forms.CharField(label='First Name', max_length=100)
    mname = forms.CharField(label='Middle Name', max_length=100)
    lname = forms.CharField(label='last Name', max_length=100)
    phone = forms.IntegerField(label='Phone Number')
    email = forms.EmailInput()
    address = forms.Textarea()
    #image = forms.ImageField(label='Upload image',)
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
    confirm_password = forms.CharField(label='Confirm Password', max_length=100)

    def __init__(self, *args, **kwargs):
        super(VendorsForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'
    class Meta:
        """Meta definition for MODELNAMEform."""
        model = vendors
        fields = ('id','fname','mname','lname','phone','email','address','username','password','confirm_password','image')
      
    def clean(self):
        cleaned_data = super(VendorsForm, self).clean()
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



