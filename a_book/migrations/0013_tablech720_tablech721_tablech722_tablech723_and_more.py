# Generated by Django 4.1.3 on 2023-01-14 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_book', '0012_tablech710_tablech711_tablech712_tablech713_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableCh720',
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
            name='TableCh721',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research', models.CharField(max_length=1)),
                ('planning', models.CharField(max_length=1)),
                ('flight_plan', models.CharField(max_length=1)),
                ('operating_proc', models.CharField(max_length=1)),
                ('attestation', models.CharField(max_length=15)),
                ('examiner', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TableCh722',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docs_check', models.CharField(max_length=1)),
                ('aircraft_inspection', models.CharField(max_length=1)),
                ('startup', models.CharField(max_length=1)),
                ('takeoff', models.CharField(max_length=1)),
                ('attestation', models.CharField(max_length=15)),
                ('examiner', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TableCh723',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VFR', models.CharField(max_length=1)),
                ('radio', models.CharField(max_length=1)),
                ('circumspection', models.CharField(max_length=1)),
                ('maintaining', models.CharField(max_length=1)),
                ('route_changes', models.CharField(max_length=1)),
                ('attestation', models.CharField(max_length=15)),
                ('examiner', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TableCh724',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approach_prep', models.CharField(max_length=1)),
                ('app_n_landing', models.CharField(max_length=1)),
                ('afterflight_proc', models.CharField(max_length=1)),
                ('paperwork', models.CharField(max_length=1)),
                ('attestation', models.CharField(max_length=15)),
                ('examiner', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TableCh725',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attestation', models.CharField(max_length=10)),
                ('dateGHT01', models.CharField(max_length=10)),
                ('recommendations', models.CharField(max_length=200)),
                ('signature', models.ImageField(upload_to='')),
                ('examiner', models.CharField(max_length=60)),
                ('license_num', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=10)),
            ],
        ),
    ]
