# Generated by Django 3.1 on 2020-09-15 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200904_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ntpcvisitors',
            name='remarks',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='ntpcvisitors',
            name='subject',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]