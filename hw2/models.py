from django.db import models
from django.forms import ModelForm

# Create your models here.


class Input(models.Model):
    r = models.FloatField(default=None)


class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = '__all__'
