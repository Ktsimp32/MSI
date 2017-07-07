from django import forms
from .models import Post, ContactInfo

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactInfo
        fields = ('FName', 'LName', 'DoB', 'Gender', 'Email', 'StreetAddress', 'City', 'State', 'Zipcode', 'PhoneNumber')