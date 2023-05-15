# Generated by Django 4.2 on 2023-05-02 08:46

import django.core.validators
from django.db import migrations, models
import polls.validators


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_post_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateField(null=True, validators=[polls.validators.date_validator]),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]