# Generated by Django 4.1.3 on 2022-12-21 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('growthTest', '0008_criterion_alter_question_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='level',
            field=models.CharField(default='H', help_text='T점수 높낮이', max_length=1),
            preserve_default=False,
        ),
    ]
