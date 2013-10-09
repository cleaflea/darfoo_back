
from django import forms
from models import *



class DarfoopluginForm(forms.ModelForm):
	
    class Meta:
        model = Darfooplugin
        # fields = ['packageName', 'className']
        # exclude = [] # uncomment this line and specify any field to exclude it from the form
        exclude = ['packageUrl', 'picUrl']

    def __init__(self, *args, **kwargs):
        super(DarfoopluginForm, self).__init__(*args, **kwargs)

