# Generated by Django 5.0 on 2024-01-06 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_cidadesatendimento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='tipp_usuario',
            new_name='tipo_usuario',
        ),
    ]