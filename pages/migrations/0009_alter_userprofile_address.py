# Generated by Django 4.1 on 2022-10-30 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_userprofile_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=200, null=True, verbose_name='address'),
        ),
    ]
