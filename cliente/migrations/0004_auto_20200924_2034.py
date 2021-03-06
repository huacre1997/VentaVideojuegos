# Generated by Django 3.1.1 on 2020-09-25 01:34

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20200924_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domicilio',
            name='distrito',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='provincia', chained_model_field='provincia', on_delete=django.db.models.deletion.CASCADE, to='cliente.distrito'),
        ),
        migrations.AlterField(
            model_name='domicilio',
            name='provincia',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='departamento', chained_model_field='departamento', on_delete=django.db.models.deletion.CASCADE, to='cliente.provincia'),
        ),
    ]
