from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(label="email", required=True)

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        email = self.cleaned_data.get("email")
        user.email = email
        if commit:
            user.save()
        return user
