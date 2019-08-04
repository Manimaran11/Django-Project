# Run migrations to tell django that changes have been made to models
#  and to see the changes stored in migration 0001py_initial.py
# python manage.py sqlmigrate polls 0001

import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200) #necessary to give max_length for char field
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text  #otherwise query will return Object set(eg query:Question.obkeccts.all())

    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) #default value is set to 0

    def __str__(self):
            return self.choice_text

