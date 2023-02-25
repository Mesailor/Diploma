from django.db import models


_all_ = (
    'TableCh760',
    'TableCh761',
    'TableCh762',
    'TableCh763',
    'TableCh764'
)


class TableCh760(models.Model):
    candidate = models.CharField(max_length=100)
    type_n_number = models.CharField(max_length=35)
    aerodrome = models.CharField(max_length=50)
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=5)
    sum_time = models.CharField(max_length=5)
    result = models.CharField(max_length=20)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh761(models.Model):
    preparation = models.CharField(max_length=1)
    knowledge = models.CharField(max_length=1)
    startup_prep = models.CharField(max_length=1)
    before_takeoff = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh762(models.Model):
    standard_maneuvers = models.CharField(max_length=1)
    turns = models.CharField(max_length=1)
    stall = models.CharField(max_length=1)
    no_eng_landing = models.CharField(max_length=1)
    emerg_landing = models.CharField(max_length=1)
    emerg_situation = models.CharField(max_length=1)
    circle_entering = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh763(models.Model):
    takeoff = models.CharField(max_length=1)
    eng_failure = models.CharField(max_length=1)
    circle_flight = models.CharField(max_length=1)
    circle_low_alt = models.CharField(max_length=1)
    app_n_landing = models.CharField(max_length=1)
    short_rw = models.CharField(max_length=1)
    missed_approach = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh764(models.Model):
    attestation = models.CharField(max_length=10)
    recommendations = models.CharField(max_length=200)
    examiner = models.CharField(max_length=60)
    license_num = models.CharField(max_length=10)
    date = models.CharField(max_length=10)
    objects = models.Manager()
    DoesNotExist = models.Manager


tables = {0: TableCh760,
          1: TableCh761,
          2: TableCh762,
          3: TableCh763,
          4: TableCh764}
