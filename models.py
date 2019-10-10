from django.db import models
from datetime import datetime
class Diary(models.Model):
    text=models.TextField()
    date_time=models.DateTimeField(default=datetime.now,primary_key=True)
