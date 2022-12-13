# Generated by Django 4.1.3 on 2022-12-13 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_book', '0002_alter_table_ch4_date_alter_table_ch4_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table_Ch5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=11)),
                ('type', models.CharField(max_length=10)),
                ('exercise', models.CharField(max_length=120)),
                ('time_hours', models.PositiveSmallIntegerField()),
                ('time_mins', models.PositiveSmallIntegerField()),
                ('instrumental_time_hours', models.PositiveSmallIntegerField()),
                ('instrumental_time_mins', models.PositiveSmallIntegerField()),
                ('grade', models.PositiveSmallIntegerField()),
                ('examiner', models.CharField(max_length=50)),
            ],
        ),
    ]
