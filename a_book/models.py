from django.db import models

class Table_Ch4(models.Model):
    date = models.CharField(max_length=11)
    exercise = models.CharField(max_length=120)
    time = models.CharField(max_length=5)
    grade = models.IntegerField()
    examiner = models.CharField(max_length=50)
    objects = models.Manager()
    DoesNotExist = models.Manager

class Table_Ch5(models.Model):
    date = models.CharField(max_length=11)
    type = models.CharField(max_length=10)
    exercise = models.CharField(max_length=120)
    time_hours = models.PositiveSmallIntegerField()
    time_mins = models.PositiveSmallIntegerField()
    instrumental_time_hours = models.PositiveSmallIntegerField()
    instrumental_time_mins = models.PositiveSmallIntegerField()
    grade = models.PositiveSmallIntegerField()
    examiner = models.CharField(max_length=50)
    objects = models.Manager()
    DoesNotExist = models.Manager