# Generated by Django 3.1.1 on 2020-09-21 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_limit_limit_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='limit',
            name='amount',
            field=models.CharField(default=0, max_length=12),
        ),
    ]