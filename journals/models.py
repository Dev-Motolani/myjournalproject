from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Title(models.Model):
    # Model a journal
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Entry(models.Model):
    #model an entry
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'Entries'

    def __str__(self):
        return self.text
