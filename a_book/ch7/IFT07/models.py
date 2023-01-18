from django.db import models


_all_ = (
    'TableCh730',
    'TableCh731',
    'TableCh732',
    'TableCh733',
    'TableCh734',
    'TableCh735',
    'tables',
)


class TableCh770(models.Model):
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


class TableCh771(models.Model):
    preparation = models.CharField(max_length=1)
    pref_inspection = models.CharField(max_length=1)
    deck_check = models.CharField(max_length=1)
    pref_proc = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh772(models.Model):
    turns30 = models.CharField(max_length=1)
    spirals = models.CharField(max_length=1)
    turns45 = models.CharField(max_length=1)
    maneuvering = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh773(models.Model):
    climb_n_descent = models.CharField(max_length=1)
    stby_spirals = models.CharField(max_length=1)
    stby_maneuvering = models.CharField(max_length=1)
    compl_spatial_pos = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh774(models.Model):
    takeoff_n_land = models.CharField(max_length=1)
    nav_operating = models.CharField(max_length=1)
    radio = models.CharField(max_length=1)
    eng_operating = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh775(models.Model):
    attestation = models.CharField(max_length=10)
    recommendations = models.CharField(max_length=200)
    signature = models.ImageField()
    examiner = models.CharField(max_length=60)
    license_num = models.CharField(max_length=10)
    date = models.CharField(max_length=10)
    objects = models.Manager()
    DoesNotExist = models.Manager


tables = {0: TableCh770,
          1: TableCh771,
          2: TableCh772,
          3: TableCh773,
          4: TableCh774,
          5: TableCh775}
