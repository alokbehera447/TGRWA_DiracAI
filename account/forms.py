from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account, FutureCustomerContacts


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

	class Meta:
		model = Account
		fields = ('firstname','lastname','email', 'username', 'password1', 'password2','usertype')

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
		except Account.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
		except Account.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)



class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")








class ContactForm(forms.ModelForm):
        email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')
        class Meta:
                model = FutureCustomerContacts
                fields = ('name','email','subject','message')

        def clean(self):
                if self.is_valid():
                        name = self.cleaned_data['name']
                        email = self.cleaned_data['email']
                        subject = self.cleaned_data['subject']
                        message =self.cleaned_data['message']








class RegistrationFormNew(UserCreationForm):
        email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

        class Meta:
                model = Account
                fields = ('email', 'username','usertype')

        def clean_email(self):
                email = self.cleaned_data['email'].lower()
                try:
                        account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
                except Account.DoesNotExist:
                        return email
                raise forms.ValidationError('Email "%s" is already in use.' % account)

        def clean_username(self):
                username = self.cleaned_data['username']
                try:
                        account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
                except Account.DoesNotExist:
                        return username
                raise forms.ValidationError('Username "%s" is already in use.' % username)












class RegistrationForm2(UserCreationForm):
        #email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')
        username = forms.CharField(max_length=20, help_text='Required. Add a valid username.') 
        class Meta:
                model = Account
                fields = ( 'username',  'usertype')# 'password1', 'password2'


        def clean_username(self):
                username = self.cleaned_data['username']
                try:
                        account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
                except Account.DoesNotExist:
                        return username
                raise forms.ValidationError('Username "%s" is already in use.' % username)


















