# Generated by Django 4.0 on 2022-05-25 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estrenos', '0003_rename_usuario_pelicula_usuarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='usuarios',
            field=models.ManyToManyField(blank=True, null=True, to='estrenos.Usuario'),
        ),
    ]
