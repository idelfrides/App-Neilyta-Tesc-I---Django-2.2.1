# Generated by Django 3.0 on 2019-12-07 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_neilytaTec1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='nomeEvento',
            new_name='nome_Evento',
        ),
    ]