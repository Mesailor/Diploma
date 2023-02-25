from django.db import models


_all_ = (
    'TableCh710',
    'TableCh711',
    'TableCh712',
    'TableCh713',
    'TableCh714',
    'TableCh715',
    'TableCh716',
    'TableCh717',
    'tables',
)


class TableCh710(models.Model):
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


class TableCh711(models.Model):
    preparation = models.CharField(max_length=1)
    knowledge = models.CharField(max_length=1)
    startup = models.CharField(max_length=1)
    taxiing = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh712(models.Model):
    takeoff = models.CharField(max_length=1)
    circle_flight = models.CharField(max_length=1)
    app_n_landing = models.CharField(max_length=1)
    complicated_takeoff = models.CharField(max_length=1)
    complicated_landing = models.CharField(max_length=1)
    missed_approach = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh713(models.Model):
    climb_n_descent = models.CharField(max_length=1)
    turn45 = models.CharField(max_length=1)
    turn60 = models.CharField(max_length=1)
    stall = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh714(models.Model):
    eng_failure = models.CharField(max_length=1)
    no_eng_landing = models.CharField(max_length=1)
    emerg_landing = models.CharField(max_length=1)
    eng_fire = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh715(models.Model):
    horiz_flight = models.CharField(max_length=1)
    climb_n_descent = models.CharField(max_length=1)
    turns = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh716(models.Model):
    circumspection = models.CharField(max_length=1)
    weather = models.CharField(max_length=1)
    exploitation = models.CharField(max_length=1)
    technology = models.CharField(max_length=1)
    radio = models.CharField(max_length=1)
    afterflight_proc = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh717(models.Model):
    attestation = models.CharField(max_length=10)
    recommendations = models.CharField(max_length=200)
    examiner = models.CharField(max_length=60)
    license_num = models.CharField(max_length=10)
    date = models.CharField(max_length=10)
    objects = models.Manager()
    DoesNotExist = models.Manager


tables = {0: TableCh710,
          1: TableCh711,
          2: TableCh712,
          3: TableCh713,
          4: TableCh714,
          5: TableCh715,
          6: TableCh716,
          7: TableCh717}
