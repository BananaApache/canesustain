
from django import forms

class UserDataForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

    
class UserBlogForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, required=True, label="Description")
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={"accept": "application/pdf,.png,.jpg,.jpeg"}),required=True, label="Image")

    numOfTrashPickedUp = forms.IntegerField(max_value=10000, label="Trash Picked Up")
    numOfPPl = forms.IntegerField(max_value = 100, label="Number of People")
    isPicturePublic = forms.BooleanField(initial=True, label="Do you want to make this picture public?")
    