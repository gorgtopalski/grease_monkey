# Generated by Django 4.0.6 on 2022-07-24 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0003_transportcontrol_convoyer_l11a_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportcontrol',
            name='convoyer_l11a',
            field=models.BooleanField(default=True, verbose_name='L11A desfile / convoyer'),
        ),
        migrations.AlterField(
            model_name='transportcontrol',
            name='convoyer_l11b',
            field=models.BooleanField(default=True, verbose_name='L11B desfile / convoyer'),
        ),
    ]
