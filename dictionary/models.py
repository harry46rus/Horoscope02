from django.db import models

# Create your models here.
from django.db.models import BinaryField


class News_base(models.Model):
    date_news=models.CharField(max_length=40)
    rating_news= models.IntegerField()
    body_news = BinaryField(max_length=None,blank=False,null=False,)
