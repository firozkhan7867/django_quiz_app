# Generated by Django 3.1.1 on 2021-05-13 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
