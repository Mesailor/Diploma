from django.db import models


_all_ = (
    'TableCh750',
    'TableCh751',
    'TableCh752',
    'TableCh753',
    'TableCh754',
    'TableCh755',
    'TableCh756',
    'tables',
)


class TableCh750(models.Model):
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


class TableCh751(models.Model):
    research = models.CharField(max_length=1)
    route_choice = models.CharField(max_length=1)
    flightplan_prep = models.CharField(max_length=1)
    calculation = models.CharField(max_length=1)
    docs_check = models.CharField(max_length=1)
    inspection = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh752(models.Model):
    briefing = models.CharField(max_length=1)
    takeoff = models.CharField(max_length=1)
    route_entering = models.CharField(max_length=1)
    radio = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh753(models.Model):
    VFR = models.CharField(max_length=1)
    deck_operating = models.CharField(max_length=1)
    nav_proc = models.CharField(max_length=1)
    flightplan_operating = models.CharField(max_length=1)
    route_changes = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh754(models.Model):
    app_n_landing = models.CharField(max_length=1)
    info_using = models.CharField(max_length=1)
    postflight_proc = models.CharField(max_length=1)
    paperwork = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh755(models.Model):
    accuracy = models.CharField(max_length=1)
    circumspection = models.CharField(max_length=1)
    commercial = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh756(models.Model):
    attestation = models.CharField(max_length=10)
    recommendations = models.CharField(max_length=200)
    signature = models.ImageField()
    examiner = models.CharField(max_length=60)
    license_num = models.CharField(max_length=10)
    date = models.CharField(max_length=10)
    objects = models.Manager()
    DoesNotExist = models.Manager


tables = {0: TableCh750,
          1: TableCh751,
          2: TableCh752,
          3: TableCh753,
          4: TableCh754,
          5: TableCh755,
          6: TableCh756}
