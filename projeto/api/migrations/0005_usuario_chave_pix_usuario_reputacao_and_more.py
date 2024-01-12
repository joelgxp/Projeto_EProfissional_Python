# Generated by Django 5.0 on 2024-01-12 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_usuario_celular_alter_usuario_cpf_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='chave_pix',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='reputacao',
            field=models.FloatField(default=5, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.CharField(choices=[(1, 'Profissional'), (2, 'Cliente')], max_length=1, null=True),
        ),
    ]
