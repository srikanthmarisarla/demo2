# Generated by Django 4.2.3 on 2023-08-31 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_alter_bngjobs_address_alter_bngjobs_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hydjobs',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
