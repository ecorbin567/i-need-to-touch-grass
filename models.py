from django.db import models
from django.utils import timezone
from django import forms
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class ContactUsForm(forms.Form):
    your_street_address = forms.CharField(max_length=1000)
    keyword = forms.CharField(max_length=1000)
    maximum_kilometers_away = forms.IntegerField()
