# Generated by Django 4.1.3 on 2022-12-13 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('growthTest', '0007_alter_question_column'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criterion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column', models.CharField(choices=[('발달지수', '발달지수'), ('자폐경향성', '자폐경향성'), ('ADHD경향성', 'ADHD경향성')], help_text='규준컬럼', max_length=7)),
                ('age', models.IntegerField(help_text='규준연령')),
                ('origin_score', models.IntegerField(help_text='원점수')),
                ('percentile', models.IntegerField(help_text='백분위')),
                ('T_score', models.IntegerField(help_text='T점수')),
                ('level', models.CharField(help_text='T점수 높낮이', max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='age',
            field=models.IntegerField(default=1, help_text='규준연령'),
            preserve_default=False,
        ),
    ]