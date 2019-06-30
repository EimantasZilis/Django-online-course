from django import forms
from AppTwo.models import Users

class NewUserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"
