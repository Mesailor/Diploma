from django.db import models


_all_ = (
    'TableCh7100',
    'TableCh7101',
    'TableCh7102',
    'tables',
)


class TableCh7100(models.Model):
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


class TableCh7101(models.Model):
    preparation = models.CharField(max_length=1)
    takeoff = models.CharField(max_length=1)
    circle_flight = models.CharField(max_length=1)
    eng_failure = models.CharField(max_length=1)
    one_eng_landing = models.CharField(max_length=1)
    missed_approach = models.CharField(max_length=1)
    one_eng_mis_apr = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh7102(models.Model):
    attestation = models.CharField(max_length=10)
    dateMET09 = models.CharField(max_length=10)
    recommendations = models.CharField(max_length=200)
    signature = models.ImageField()
    examiner = models.CharField(max_length=60)
    license_num = models.CharField(max_length=10)
    date = models.CharField(max_length=10)
    objects = models.Manager()
    DoesNotExist = models.Manager


tables = {0: TableCh7100,
          1: TableCh7101,
          2: TableCh7102}
