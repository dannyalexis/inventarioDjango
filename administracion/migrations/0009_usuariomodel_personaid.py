# Generated by Django 3.1.6 on 2021-03-27 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0008_auto_20210327_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariomodel',
            name='personaId',
            field=models.ForeignKey(db_column='persona_id', default=1, on_delete=django.db.models.deletion.PROTECT, related_name='PersonaUsuario', to='administracion.personamodel'),
            preserve_default=False,
        ),
    ]