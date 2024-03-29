# Generated by Django 4.1.3 on 2023-01-21 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_book', '0019_tablech780_tablech781_tablech782_tablech783_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableCh790',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.CharField(max_length=100)),
                ('type_n_number', models.CharField(max_length=35)),
                ('aerodrome', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=5)),
                ('sum_time', models.CharField(max_length=5)),
                ('result', models.CharField(max_length=20)),
                ('examiner', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TableCh791',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preparation', models.CharField(max_length=1)),
                ('knowledge', models.CharField(max_length=1)),
                ('startup', models.CharField(max_length=1)),
                ('taxiing', models.CharField(max_length=1)),
                ('attestation', models.CharField(max_length=15)),
                ('examiner', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TableCh792',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_maneuvering', models.CharField(max_length=1)),
                ('stall_flight_conf', models.CharField(max_length=1)),
                ('stall_land_conf', models.CharField(max_length=1)),
                ('eng_fire', models.CharField(max_length=1)),
                ('one_eng_flight', models.CharField(max_length=1)),
                ('circle_entrance', models.CharField(max_length=1)),
                ('attestation', models.CharField(max_length=15)),
                ('examiner', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TableCh793',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('takeoff', models.CharField(max_length=1)),
                ('aborted_takeoff', models.CharField(max_length=1)),
                ('eng_failure', models.CharField(max_length=1)),
                ('circle_flight', models.CharField(max_length=1)),
                ('app_n_landing', models.CharField(max_length=1)),
                ('complicated_takeoff', models.CharField(max_length=1)),
                ('complicated_landing', models.CharField(max_length=1)),
                ('one_eng_landing', models.CharField(max_length=1)),
                ('missed_approach', models.CharField(max_length=1)),
                ('one_eng_mis_apr', models.CharField(max_length=1)),
                ('attestation', models.CharField(max_length=15)),
                ('examiner', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TableCh794',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attestation', models.CharField(max_length=10)),
                ('recommendations', models.CharField(max_length=200)),
                ('signature', models.ImageField(upload_to='')),
                ('examiner', models.CharField(max_length=60)),
                ('license_num', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=10)),
            ],
        ),
    ]
