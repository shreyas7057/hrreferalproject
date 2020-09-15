from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import Jobpost


class SignupForm(UserCreationForm):
    
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
        labels = {'email':'Email'}
        # help_texts = {
        #     'first_name':None,
        #     'last_name':None,
        #     'username': None,
        #     'email': None,
        # }

    
    def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['first_name'].widget.attrs.update({'class':'form-control','placeholder':'First Name'})
            self.fields['last_name'].widget.attrs.update({'class':'form-control','placeholder':'Last Name'})
            self.fields['username'].widget.attrs.update({'class':'form-control ','placeholder':'Username'})
            self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Email'})
            self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Password'})
            self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Confirm Password'})


            for fieldname in ['username', 'email','password1', 'password2']:
                self.fields[fieldname].help_text = None




class JobpostForm(forms.ModelForm):

    class Meta:

        model = Jobpost
        fields = ['designation','yrs_of_exp','company_name','resume']

    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['designation'].widget.attrs.update({'class':'form-control','placeholder':'Enter Designation'})
        self.fields['yrs_of_exp'].widget.attrs.update({'class':'form-control','placeholder':'Years of Exp'})
        self.fields['company_name'].widget.attrs.update({'class':'form-control','placeholder':'Company Name'})
        self.fields['resume'].widget.attrs.update({'class':'form-control'})