from django.db import models


_all_ = (
    'TableCh31',
    'TableCh32',
    'TableCh33',
    'TableCh34',
    'TableCh35',
    'TableCh36',
    'tables',
)


class TableCh31(models.Model):
    prev_experience = models.TextField()
    head_ltk = models.CharField(max_length=30)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh32(models.Model):
    type = models.CharField(max_length=10)
    time = models.CharField(max_length=5)
    captain_time = models.CharField(max_length=5)
    route_time = models.CharField(max_length=5)
    night_time = models.CharField(max_length=5)
    instrumental_time = models.CharField(max_length=5)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh33(models.Model):
    type = models.CharField(max_length=10)
    trainer_time = models.CharField(max_length=5)
    trainer_instrumental = models.CharField(max_length=5)
    trainer_passed = models.CharField(max_length=5)
    time = models.CharField(max_length=5)
    instrumental_time = models.CharField(max_length=5)
    solo_time = models.CharField(max_length=5)
    solo_route = models.CharField(max_length=5)
    captain_time = models.CharField(max_length=5)
    captain_route = models.CharField(max_length=5)
    captain_night = models.CharField(max_length=5)
    instructor = models.CharField(max_length=30)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh34(models.Model):
    type = models.CharField(max_length=10)
    trainer_time = models.CharField(max_length=5)
    trainer_instrumental = models.CharField(max_length=5)
    trainer_passed = models.CharField(max_length=5)
    time = models.CharField(max_length=5)
    instrumental_time = models.CharField(max_length=5)
    FO_time = models.CharField(max_length=5)  # FO - First Officer
    FO_passed = models.CharField(max_length=5)
    captain_time = models.CharField(max_length=5)
    captain_route = models.CharField(max_length=5)
    captain_night = models.CharField(max_length=5)
    instructor = models.CharField(max_length=30)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh35(models.Model):
    type = models.CharField(max_length=10)
    trainer_time = models.CharField(max_length=5)
    trainer_instrumental = models.CharField(max_length=5)
    trainer_passed = models.CharField(max_length=5)
    time = models.CharField(max_length=5)
    instrumental_time = models.CharField(max_length=5)
    captain_time = models.CharField(max_length=5)
    captain_route = models.CharField(max_length=5)
    captain_night = models.CharField(max_length=5)
    instructor = models.CharField(max_length=30)
    objects = models.Manager()
    DoesNotExist = models.Manager


class TableCh36(models.Model):
    trainer_time = models.CharField(max_length=5)
    trainer_instrumental = models.CharField(max_length=5)
    trainer_passed = models.CharField(max_length=5)
    time = models.CharField(max_length=5)
    instrumental_time = models.CharField(max_length=5)
    solo_time = models.CharField(max_length=5)
    solo_route = models.CharField(max_length=5)
    FO_time = models.CharField(max_length=5)  # FO - First Officer
    FO_passed = models.CharField(max_length=5)
    captain_time = models.CharField(max_length=5)
    captain_route = models.CharField(max_length=5)
    captain_night = models.CharField(max_length=5)
    instructor = models.CharField(max_length=30)
    objects = models.Manager()
    DoesNotExist = models.Manager


tables = {1: TableCh31,
          2: TableCh32,
          3: TableCh33,
          4: TableCh34,
          5: TableCh35,
          6: TableCh36}
