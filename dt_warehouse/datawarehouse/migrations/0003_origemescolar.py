# Generated by Django 2.2.5 on 2019-09-06 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datawarehouse', '0002_auto_20190906_0425'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrigemEscolar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, unique=True, verbose_name='Descrição')),
            ],
        ),
    ]
