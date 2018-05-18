from django import forms


class LoginFrom(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=8)