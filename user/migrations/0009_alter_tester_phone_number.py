# Generated by Django 4.1.3 on 2022-12-07 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_tester_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tester',
            name='phone_number',
            field=models.CharField(blank=True, help_text='연락처', max_length=11, null=True),
        ),
    ]
