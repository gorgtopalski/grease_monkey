# Generated by Django 4.0.6 on 2022-07-25 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('context', '0002_alter_line_options_line_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='short_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]