# Generated by Django 4.0.3 on 2022-04-25 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_report_isupdated'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='isViewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
