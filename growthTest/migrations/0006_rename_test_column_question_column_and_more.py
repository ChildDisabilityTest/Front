# Generated by Django 4.1.3 on 2022-12-13 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growthTest', '0005_question_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='test_column',
            new_name='column',
        ),
        migrations.RemoveField(
            model_name='question',
            name='group',
        ),
    ]
