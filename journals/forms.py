from django.forms import ModelForm
from .models import Title, Entry


class TitleForm(ModelForm):
    class Meta:
      model = Title
      fields = ['title', 'author']


class EntryForm(ModelForm):
    class Meta:
      model = Entry
      fields = '__all__'

class TitleChangeForm(ModelForm):
    class Meta:
        model = Title
        fields = ['title']

class EntryChangeForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['text']