# Generated by Django 2.2 on 2020-03-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish', '0002_auto_20200312_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='granted_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
