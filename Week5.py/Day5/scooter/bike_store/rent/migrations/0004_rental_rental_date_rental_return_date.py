# Generated by Django 4.2 on 2023-05-02 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_rental_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='rental_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='rental',
            name='return_date',
            field=models.DateTimeField(null=True),
        ),
    ]