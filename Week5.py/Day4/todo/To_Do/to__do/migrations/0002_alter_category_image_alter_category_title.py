# Generated by Django 4.2 on 2023-04-26 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to__do', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.URLField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]