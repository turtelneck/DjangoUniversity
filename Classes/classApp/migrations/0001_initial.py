# Generated by Django 3.1.5 on 2021-01-07 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('courseNumber', models.CharField(blank=True, default='', max_length=4)),
                ('instructor', models.CharField(blank=True, default='', max_length=60)),
                ('duration', models.DecimalField(decimal_places=1, default=0.0, max_digits=10000)),
            ],
        ),
    ]
