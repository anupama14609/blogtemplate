from django.db.models import fields
from script.models import GenerateMeta
from django import forms 

class GenerateMetaForm(forms.ModelForm):
    class Meta:
        model = GenerateMeta
        fields = ('title','description','keywords','url','timeStamp')
        
