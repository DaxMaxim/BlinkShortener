from django.db import models
from django.utils import timezone

# Create your models here.

class Links(models.Model):

    link = models.CharField(max_length = 10000)
    newlink = models.CharField(max_length = 50, blank=True)
    accessed = models.DateTimeField(default = timezone.now)
    count = models.IntegerField(default = 0)
    element_id = models.IntegerField(default = 0)


    class Meta:
        indexes = [models.Index(fields = ['link', 'newlink'])]
