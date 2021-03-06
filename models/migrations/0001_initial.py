# Generated by Django 4.0.6 on 2022-07-09 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('context', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BottleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='modelo')),
                ('blueprint', models.CharField(max_length=100, unique=True, verbose_name='plano maqueta')),
            ],
            options={
                'ordering': ['blueprint'],
            },
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='fecha inicio')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='fecha final')),
                ('finished', models.BooleanField(default=False, verbose_name='finalizada?')),
                ('speed', models.IntegerField(default=0, verbose_name='velocidad')),
                ('sections', models.IntegerField(default=0, verbose_name='secciones')),
                ('weight', models.IntegerField(default=0, verbose_name='peso')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='context.color', verbose_name='color')),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='context.line', verbose_name='línea')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='models.bottlemodel', verbose_name='modelo')),
            ],
        ),
    ]
