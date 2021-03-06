# Generated by Django 2.1.7 on 2019-08-17 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0009_auto_20190817_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='purpose',
            field=models.CharField(choices=[('SP', 'startup'), ('EU', 'education'), ('ME', 'medical')], max_length=2),
        ),
        migrations.AlterField(
            model_name='donation',
            name='status',
            field=models.BooleanField(choices=[(True, 'accepted'), (False, 'not accepted')], null=True),
        ),
    ]
