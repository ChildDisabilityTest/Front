# Generated by Django 4.1.3 on 2022-12-13 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('growthTest', '0004_alter_answer_answers_alter_answer_child_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='age',
            field=models.IntegerField(blank=True, help_text='규준연령', null=True),
        ),
    ]