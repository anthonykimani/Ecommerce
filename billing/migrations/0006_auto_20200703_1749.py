# Generated by Django 3.0.7 on 2020-07-03 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0005_auto_20200702_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingprofile',
            name='customer_id',
        ),
        migrations.AddField(
            model_name='billingprofile',
            name='Mpesa_number',
            field=models.IntegerField(blank=True, max_length=120, null=True),
        ),
    ]
