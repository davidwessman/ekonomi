# Generated by Django 2.1.4 on 2019-01-01 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekonomi', '0003_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='transaction_date',
            field=models.DateField(verbose_name='date payed'),
        ),
    ]