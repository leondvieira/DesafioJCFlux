# Generated by Django 3.0.3 on 2020-02-06 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chaves', '0003_chave_pendente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chave',
            name='pendente',
        ),
    ]
