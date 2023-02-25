from django.db import models


_all_ = (
    'TableCh740',
    'TableCh741'
    'TableCh742',
    'tables',
)


class TableCh740(models.Model):
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


class TableCh741(models.Model):
    preparation = models.CharField(max_length=1)
    inspection = models.CharField(max_length=1)
    startup = models.CharField(max_length=1)
    takeoff = models.CharField(max_length=1)
    circle_flight = models.CharField(max_length=1)
    landing = models.CharField(max_length=1)
    approach = models.CharField(max_length=1)
    missed_approach = models.CharField(max_length=1)
    radio_failure = models.CharField(max_length=1)
    eng_failure = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh742(models.Model):
    attestation = models.CharField(max_length=10)
    recommendations = models.CharField(max_length=200)
    examiner = models.CharField(max_length=60)
    license_num = models.CharField(max_length=10)
    date = models.CharField(max_length=10)
    objects = models.Manager()
    DoesNotExist = models.Manager


tables = {0: TableCh740,
          1: TableCh741,
          2: TableCh742}
