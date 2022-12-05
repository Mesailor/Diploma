from django.db import models

class Table_Ch4(models.Model):
    date = models.CharField(max_length=11)
    exercise = models.CharField(max_length=120)
    time = models.CharField(max_length=5)
    grade = models.IntegerField()
    examiner = models.CharField(max_length=50)
    objects = models.Manager()
    DoesNotExist = models.Manager
