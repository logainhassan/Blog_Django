from django import forms
from Admin.models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('content',)
        labels={
            'content':''
        }
        widgets={
            
            'content':forms.Textarea(attrs={'class':'form-control input' , 'placeholder':'Message' }),
        }