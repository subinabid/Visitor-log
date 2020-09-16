# Generated by Django 3.1 on 2020-09-16 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200916_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='externalusers',
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='ntpcusers',
        ),
        migrations.AddField(
            model_name='visitor',
            name='externaluser',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET('DEL'), to='core.externaluser'),
        ),
        migrations.AddField(
            model_name='visitor',
            name='ntpcuser',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET('DEL'), to='core.ntpcuser'),
        ),
    ]
