from django import forms
from Home import  models


class create_form (forms.ModelForm):
    class Meta:
        model = models.Divar
        fields =['Category','Picture','Ad_Titel','Description','City','status','price','Phone']
