from django.db import models


_all_ = (
    'TableCh7110',
    'TableCh7111',
    'TableCh7112',
    'TableCh7113',
    'TableCh7114',
    'TableCh7115',
    'tables',
)


class TableCh7110(models.Model):
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


class TableCh7111(models.Model):
    preparation = models.CharField(max_length=1)
    inspection = models.CharField(max_length=1)
    startup = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh7112(models.Model):
    takeoff = models.CharField(max_length=1)
    landing = models.CharField(max_length=1)
    eng_failure = models.CharField(max_length=1)
    one_eng_landing = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh7113(models.Model):
    airway_entrance = models.CharField(max_length=1)
    airway_navigation = models.CharField(max_length=1)
    hold_area = models.CharField(max_length=1)
    precision_app = models.CharField(max_length=1)
    nonprecision_app = models.CharField(max_length=1)
    missed_approach = models.CharField(max_length=1)
    low_alt_circle = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh7114(models.Model):
    radio = models.CharField(max_length=1)
    observation = models.CharField(max_length=1)
    visual_maneuvering = models.CharField(max_length=1)
    team_work = models.CharField(max_length=1)
    missed_approach = models.CharField(max_length=1)
    emergency = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh7115(models.Model):
    attestation = models.CharField(max_length=10)
    dateGHT06 = models.CharField(max_length=10)
    dateIRT08 = models.CharField(max_length=10)
    dateMET09 = models.CharField(max_length=10)
    dateMET10 = models.CharField(max_length=10)
    recommendations = models.CharField(max_length=200)
    examiner = models.CharField(max_length=60)
    license_num = models.CharField(max_length=10)
    date = models.CharField(max_length=10)
    objects = models.Manager()
    DoesNotExist = models.Manager


tables = {0: TableCh7110,
          1: TableCh7111,
          2: TableCh7112,
          3: TableCh7113,
          4: TableCh7114,
          5: TableCh7115}
