# Generated by Django 3.0.3 on 2020-02-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NetBanking', '0007_auto_20200219_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='pin',
            field=models.IntegerField(blank=True, help_text='Required. 6 digits or fewer.  digits', null=True),
        ),
    ]