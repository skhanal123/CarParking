# Generated by Django 4.1 on 2022-08-04 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_jsonupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='parkingRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(max_length=200)),
                ('start_time', models.IntegerField()),
                ('end_time', models.IntegerField()),
                ('tz', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
