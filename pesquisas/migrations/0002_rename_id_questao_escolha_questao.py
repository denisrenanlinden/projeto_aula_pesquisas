# Generated by Django 5.1.7 on 2025-04-02 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pesquisas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='escolha',
            old_name='id_questao',
            new_name='questao',
        ),
    ]
