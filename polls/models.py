from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Poll(models.Model):
    #...
    def was_published_recently(self):
        return self.pub_date >=timezone.now()-datetime.timedelta(days=1)
    def __str__(self):
        return self.question
    question=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    
class Choice(models.Model):
    #...
    def __str__(self):
        return self.choice_txt
    poll=models.ForeignKey(Poll)
    choice_txt=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)