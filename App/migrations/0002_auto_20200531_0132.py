# Generated by Django 3.0.6 on 2020-05-31 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='ProdStock',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='CatId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.Genero'),
        ),
    ]