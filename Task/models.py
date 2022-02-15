from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class SummaryTask(models.Model):
    
    summaryID = models.IntegerField(null=True)

    article = models.TextField(null=True)
    gold = models.TextField(null=True)
    title = models.TextField(null=True)
    
    grammatical_correctness = models.IntegerField(default=5)
    arrangement = models.IntegerField(default=5)
    quality = models.IntegerField(default=5)

    # professional = models.IntegerField(default=5)
    singlePoint = models.IntegerField(default=5)
    enoughDetails = models.IntegerField(default=5)

    subjectiveScore = models.IntegerField(null=True, default=5)

    done = models.BooleanField(default=False)
    annotator = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    
    def __str__(self):
        return f'article: {self.id}, {self.annotator}'
