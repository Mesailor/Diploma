from django.db import models


_all_ = (
    'TableCh720',
    'TableCh721',
    'TableCh722',
    'TableCh723',
    'TableCh724',
    'TableCh725',
    'tables',
)


class TableCh720(models.Model):
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


class TableCh721(models.Model):
    research = models.CharField(max_length=1)
    planning = models.CharField(max_length=1)
    flight_plan = models.CharField(max_length=1)
    operating_proc = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh722(models.Model):
    docs_check = models.CharField(max_length=1)
    aircraft_inspection = models.CharField(max_length=1)
    startup = models.CharField(max_length=1)
    takeoff = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh723(models.Model):
    VFR = models.CharField(max_length=1)
    radio = models.CharField(max_length=1)
    circumspection = models.CharField(max_length=1)
    maintaining = models.CharField(max_length=1)
    route_changes = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh724(models.Model):
    approach_prep = models.CharField(max_length=1)
    app_n_landing = models.CharField(max_length=1)
    afterflight_proc = models.CharField(max_length=1)
    paperwork = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh725(models.Model):
    attestation = models.CharField(max_length=10)
    dateGHT01 = models.CharField(max_length=10)
    recommendations = models.CharField(max_length=200)
    examiner = models.CharField(max_length=60)
    license_num = models.CharField(max_length=10)
    date = models.CharField(max_length=10)
    objects = models.Manager()
    DoesNotExist = models.Manager


tables = {0: TableCh720,
          1: TableCh721,
          2: TableCh722,
          3: TableCh723,
          4: TableCh724,
          5: TableCh725}
