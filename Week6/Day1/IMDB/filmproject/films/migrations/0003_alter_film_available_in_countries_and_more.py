# Generated by Django 4.2 on 2023-05-03 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_alter_film_created_in_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='available_in_countries',
            field=models.ManyToManyField(related_name='available', to='films.country'),
        ),
        migrations.AlterField(
            model_name='film',
            name='category',
            field=models.ManyToManyField(related_name='category', to='films.category'),
        ),
        migrations.AlterField(
            model_name='film',
            name='created_in_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created', to='films.country'),
        ),
        migrations.AlterField(
            model_name='film',
            name='director',
            field=models.ManyToManyField(related_name='director', to='films.director'),
        ),
    ]
