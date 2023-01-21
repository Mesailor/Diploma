from django.db import models


_all_ = (
    'TableCh710',
    'TableCh711',
    'TableCh712',
    'TableCh713',
    'TableCh714',
    'tables',
)


class TableCh790(models.Model):
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


class TableCh791(models.Model):
    preparation = models.CharField(max_length=1)
    knowledge = models.CharField(max_length=1)
    startup = models.CharField(max_length=1)
    taxiing = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh792(models.Model):
    standard_maneuvering = models.CharField(max_length=1)
    stall_flight_conf = models.CharField(max_length=1)
    stall_land_conf = models.CharField(max_length=1)
    eng_fire = models.CharField(max_length=1)
    one_eng_flight = models.CharField(max_length=1)
    circle_entrance = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh793(models.Model):
    takeoff = models.CharField(max_length=1)
    aborted_takeoff = models.CharField(max_length=1)
    eng_failure = models.CharField(max_length=1)
    circle_flight = models.CharField(max_length=1)
    app_n_landing = models.CharField(max_length=1)
    complicated_takeoff = models.CharField(max_length=1)
    complicated_landing = models.CharField(max_length=1)
    one_eng_landing = models.CharField(max_length=1)
    missed_approach = models.CharField(max_length=1)
    one_eng_mis_apr = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh794(models.Model):
    attestation = models.CharField(max_length=10)
    recommendations = models.CharField(max_length=200)
    signature = models.ImageField()
    examiner = models.CharField(max_length=60)
    license_num = models.CharField(max_length=10)
    date = models.CharField(max_length=10)
    objects = models.Manager()
    DoesNotExist = models.Manager


tables = {0: TableCh790,
          1: TableCh791,
          2: TableCh792,
          3: TableCh793,
          4: TableCh794}
