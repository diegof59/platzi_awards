import datetime

from django.utils import timezone
from django.db import models

# Create your models here.

class Question(models.Model):
    statement = models.CharField(max_length=200)
    publication_date = models.DateTimeField("Date published")

    def __str__(self) -> str:
        return f'{self.statement}'
    
    def was_published_recently(self) -> bool:
        """ Returns true if the question was published in the last day, else false """
        return timezone.now() >= self.publication_date >= (timezone.now() - datetime.timedelta(days=1))

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Choice: {self.choice_text} Votes: {self.votes}'