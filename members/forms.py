from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User


class userform(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2')

    def save(self, commit=True):
        user = super(userform, self).save(commit=False)
        user.email = self.cleaned_data['email']
        
       
        if commit:
            user.save()
        return user

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))

    class Meta :
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
    

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    #password = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    date_joined= forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
 


    class Meta :
        model = User
        fields = ('username','first_name','last_name','email','password','last_login','date_joined')
        #incase we dont want the particular field we can remove it from above fields.



class PasswordChangeingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))

    class Meta :
        model = User
        fields = ('oldpassword','new_password1','new_password2')        



class LoginForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))

    class Meta :
        model = User
        fields = ('username','password')
    

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] ='form-control'
        self.fields['password'].widget.attrs['class'] ='form-control'
        

