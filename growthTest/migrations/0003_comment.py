# Generated by Django 4.1.3 on 2022-12-08 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('growthTest', '0002_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.CharField(blank=True, help_text='분류', max_length=10, null=True)),
                ('stage', models.CharField(blank=True, help_text='단계', max_length=2, null=True)),
                ('content', models.CharField(blank=True, help_text='코멘트 내용', max_length=100, null=True)),
            ],
        ),
    ]