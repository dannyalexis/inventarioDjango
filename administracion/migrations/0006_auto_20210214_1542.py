# Generated by Django 3.1.6 on 2021-02-14 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0005_categoriamodel_categoriaestado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personamodel',
            name='personaEstado',
            field=models.BooleanField(db_column='persona_estado', default=True),
        ),
        migrations.AlterField(
            model_name='usuariomodel',
            name='usuarioEstado',
            field=models.BooleanField(db_column='usuario_estado', default=True),
        ),
    ]
