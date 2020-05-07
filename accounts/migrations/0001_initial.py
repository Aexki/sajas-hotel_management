# Generated by Django 3.0.5 on 2020-05-03 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cabservice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('package', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='complaintservice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('room', models.IntegerField()),
                ('complaint', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='roomservice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('service', models.CharField(max_length=50)),
            ],
        ),
    ]
