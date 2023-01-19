from django.db import models


_all_ = (
    'TableCh780',
    'TableCh781',
    'TableCh782',
    'TableCh783',
    'TableCh784',
    'TableCh785',
    'TableCh786',
    'TableCh787',
    'tables',
)


class TableCh780(models.Model):
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


class TableCh781(models.Model):
    planning = models.CharField(max_length=1)
    inspection = models.CharField(max_length=1)
    startup = models.CharField(max_length=1)
    ATC_clearance = models.CharField(max_length=1)
    takeoff = models.CharField(max_length=1)
    airway_entering = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh782(models.Model):
    maintaining_track = models.CharField(max_length=1)
    flightplan = models.CharField(max_length=1)
    reports = models.CharField(max_length=1)
    instrumental_flight = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh783(models.Model):
    hold_area_entering = models.CharField(max_length=1)
    accuracy_hold_area = models.CharField(max_length=1)
    maintaining_alt = models.CharField(max_length=1)
    wind_correction = models.CharField(max_length=1)
    hold_area_leaving = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh784(models.Model):
    initial_stage = models.CharField(max_length=1)
    landing_course = models.CharField(max_length=1)
    ILS_established = models.CharField(max_length=1)
    decision_alt = models.CharField(max_length=1)
    missed_approach = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh785(models.Model):
    initial_stage = models.CharField(max_length=1)
    landing_course = models.CharField(max_length=1)
    final_stage = models.CharField(max_length=1)
    decision_alt = models.CharField(max_length=1)
    missed_approach = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh786(models.Model):
    observation = models.CharField(max_length=1)
    flight_info = models.CharField(max_length=1)
    radio = models.CharField(max_length=1)
    IFR_knowledge = models.CharField(max_length=1)
    briefing = models.CharField(max_length=1)
    attestation = models.CharField(max_length=15)
    examiner = models.CharField(max_length=60)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh787(models.Model):
    attestation = models.CharField(max_length=10)
    dateIFT07 = models.CharField(max_length=10)
    recommendations = models.CharField(max_length=200)
    signature = models.ImageField()
    examiner = models.CharField(max_length=60)
    license_num = models.CharField(max_length=10)
    date = models.CharField(max_length=10)
    objects = models.Manager()
    DoesNotExist = models.Manager


tables = {0: TableCh780,
          1: TableCh781,
          2: TableCh782,
          3: TableCh783,
          4: TableCh784,
          5: TableCh785,
          6: TableCh786,
          7: TableCh787}
