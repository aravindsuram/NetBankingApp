# Generated by Django 3.0.3 on 2020-02-20 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NetBanking', '0003_auto_20200219_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]