# Generated by Django 4.0.6 on 2024-09-14 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acervodigital', '0002_remove_contato_usuario_remove_emprestimo_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='capa',
            field=models.ImageField(blank=True, null=True, upload_to='capas/'),
        ),
    ]