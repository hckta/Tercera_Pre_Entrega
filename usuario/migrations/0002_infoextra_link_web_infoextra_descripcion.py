# Generated by Django 4.2.2 on 2023-07-09 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoextra',
            name='Link_web',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='infoextra',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
