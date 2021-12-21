from django.forms import *
from django import forms
from .models import Profesion

# class AddForm(forms.ModelForm):
# 	class Meta:
# 		model = Profesion
# 		fields = [
# 			'ProCod',
# 			'ProDes',
# 		]
class profesionesForm(forms.ModelForm):
    class Meta:
        model = Profesion
        fields = ['ProCod', 'img']

        widgets = {
            'ProCod' :TextInput(
                attrs={
                    'required': True,
                    #'class': 'input--style-6',
                    'placeholder':'Digite nombre nuevo',
                    'autocomplete':'None'
                }
            )
        }
