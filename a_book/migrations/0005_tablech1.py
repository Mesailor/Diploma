# Generated by Django 4.1.3 on 2022-12-17 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_book', '0004_rename_table_ch4_tablech4_rename_table_ch5_tablech5'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableCh1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=50)),
                ('group', models.PositiveIntegerField()),
                ('date', models.CharField(max_length=11)),
                ('instructor1', models.CharField(max_length=50)),
                ('instructor2', models.CharField(max_length=50)),
                ('instructor3', models.CharField(max_length=50)),
                ('instructor4', models.CharField(max_length=50)),
            ],
        ),
    ]
