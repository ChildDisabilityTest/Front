# Generated by Django 4.1.3 on 2022-12-07 07:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_tester_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tester',
            name='phone_number',
            field=models.CharField(help_text='연락처', max_length=11, unique=True, validators=[django.core.validators.RegexValidator(regex='^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')]),
        ),
    ]
