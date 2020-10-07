from django import forms
from .models import UserModel


class UserForm(forms.ModelForm):
	class Meta:
		model = UserModel
		fields = '__all__'

		widgets ={

		'name':forms.TextInput(attrs={'class':'form-control','id':'nameid'}),
		'mobile':forms.TextInput(attrs={'class':'form-control','id':'phoneid'}),
		'password':forms.PasswordInput(attrs={'class':'form-control','id':'passid'}),

		}
