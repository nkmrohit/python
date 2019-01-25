from django import forms
from vendors import models
from .models import vendors
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class VendorForm(forms.Form):
      #company fields
      c_name = forms.CharField(label='Company Name', max_length=100)
      c_owner = forms.CharField(label='Company Owner Name', max_length=100)
      c_reg_no = forms.IntegerField(label='Registration Number')
      c_adress = forms.CharField(label='Comapny Address')
      c_phone  = forms.IntegerField(label='Phone Number')
      c_email = forms.EmailField(label='Email')
      c_description = forms.CharField(
            label="Description",
            max_length=2000,
            widget=forms.Textarea(attrs={'placeholder': 'Description'}),
            help_text='Write here your message!')
      #user fields
      firstname= forms.CharField(label='First Name',max_length=20)
      lastname= forms.CharField(label='Last Name',max_length=20)
      email  = forms.EmailField(label="Email")
      username= forms.CharField(label='User Name',max_length=20)
      password= forms.CharField(label='Password ',max_length=20)
      confirm_password= forms.CharField(label='Confirm password',max_length=20)

      def __init__(self, *args, **kwargs):
            super(VendorForm, self).__init__(*args, **kwargs)
            for myField in self.fields:
                  self.fields[myField].widget.attrs['class'] = 'form-control'
      class Meta:
            model=vendors #or whatever object
            fields = ['c_name','c_owner','c_reg_no','c_adress','c_phone','c_email','c_description','firstname','lastname','email','username','password','confirm_password']
      

      def clean(self):
            cleaned_data = super(VendorForm, self).clean()
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

      def clean_c_email(self):
            c_email = self.cleaned_data.get('c_email')
            return c_email
            
      def __str__(self):
            return self.name  