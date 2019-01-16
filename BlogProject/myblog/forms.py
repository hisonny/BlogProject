from  django.forms import  forms

class FileUploadForm(forms.Form):
    f = forms.FileField()