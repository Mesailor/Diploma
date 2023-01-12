# Generated by Django 4.1.3 on 2022-12-28 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_book', '0010_tablech6'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableCh31',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prev_experience', models.TextField()),
                ('head_ltk', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TableCh32',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=5)),
                ('captain_time', models.CharField(max_length=5)),
                ('route_time', models.CharField(max_length=5)),
                ('night_time', models.CharField(max_length=5)),
                ('instrumental_time', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='TableCh33',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('trainer_time', models.CharField(max_length=5)),
                ('trainer_instrumental', models.CharField(max_length=5)),
                ('trainer_passed', models.CharField(max_length=5)),
                ('time', models.CharField(max_length=5)),
                ('instrumental_time', models.CharField(max_length=5)),
                ('solo_time', models.CharField(max_length=5)),
                ('solo_route', models.CharField(max_length=5)),
                ('captain_time', models.CharField(max_length=5)),
                ('captain_route', models.CharField(max_length=5)),
                ('captain_night', models.CharField(max_length=5)),
                ('instructor', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TableCh34',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('trainer_time', models.CharField(max_length=5)),
                ('trainer_instrumental', models.CharField(max_length=5)),
                ('trainer_passed', models.CharField(max_length=5)),
                ('time', models.CharField(max_length=5)),
                ('instrumental_time', models.CharField(max_length=5)),
                ('FO_time', models.CharField(max_length=5)),
                ('FO_passed', models.CharField(max_length=5)),
                ('captain_time', models.CharField(max_length=5)),
                ('captain_route', models.CharField(max_length=5)),
                ('captain_night', models.CharField(max_length=5)),
                ('instructor', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TableCh35',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('trainer_time', models.CharField(max_length=5)),
                ('trainer_instrumental', models.CharField(max_length=5)),
                ('trainer_passed', models.CharField(max_length=5)),
                ('time', models.CharField(max_length=5)),
                ('instrumental_time', models.CharField(max_length=5)),
                ('captain_time', models.CharField(max_length=5)),
                ('captain_route', models.CharField(max_length=5)),
                ('captain_night', models.CharField(max_length=5)),
                ('instructor', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TableCh36',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_time', models.CharField(max_length=5)),
                ('trainer_instrumental', models.CharField(max_length=5)),
                ('trainer_passed', models.CharField(max_length=5)),
                ('time', models.CharField(max_length=5)),
                ('instrumental_time', models.CharField(max_length=5)),
                ('solo_time', models.CharField(max_length=5)),
                ('solo_route', models.CharField(max_length=5)),
                ('FO_time', models.CharField(max_length=5)),
                ('FO_passed', models.CharField(max_length=5)),
                ('captain_time', models.CharField(max_length=5)),
                ('captain_route', models.CharField(max_length=5)),
                ('captain_night', models.CharField(max_length=5)),
                ('instructor', models.CharField(max_length=30)),
            ],
        ),
    ]
