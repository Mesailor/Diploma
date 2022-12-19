from django.db import models


class TableCh1(models.Model):
    student = models.CharField(max_length=50)
    group = models.PositiveIntegerField()
    date = models.CharField(max_length=11)
    instructor1 = models.CharField(max_length=50)
    instructor2 = models.CharField(max_length=50)
    instructor3 = models.CharField(max_length=50)
    instructor4 = models.CharField(max_length=50)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh2(models.Model):
    student = models.CharField(max_length=50)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh4(models.Model):
    date = models.CharField(max_length=11)
    exercise = models.CharField(max_length=120)
    time = models.CharField(max_length=5)
    grade = models.IntegerField()
    examiner = models.CharField(max_length=50)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh5(models.Model):
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


class TableCh8(models.Model):
    date = models.CharField(max_length=11)
    type = models.CharField(max_length=10)
    times_of_day = models.CharField(max_length=10)
    flight_permit = models.CharField(max_length=100)
    meteo_height = models.PositiveSmallIntegerField()
    meteo_vis = models.PositiveSmallIntegerField()
    meteo_wind = models.PositiveSmallIntegerField()
    examiner = models.CharField(max_length=70)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh9(models.Model):
    characteristic = models.TextField()
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh10(models.Model):
    date = models.CharField(max_length=11)
    remarks = models.TextField()
    examiner = models.CharField(max_length=70)
    deletion_mark = models.CharField(max_length=100)
    objects = models.Manager()
    DoesNotExist = models.Manager


tables = {1: TableCh1,
          2: TableCh2,
          4: TableCh4,
          5: TableCh5,
          8: TableCh8,
          9: TableCh9,
          10: TableCh10}
