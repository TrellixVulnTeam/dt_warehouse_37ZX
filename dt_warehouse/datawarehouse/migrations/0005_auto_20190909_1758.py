# Generated by Django 2.2.5 on 2019-09-09 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datawarehouse', '0004_campus_curso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campus',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='descricao',
        ),
        migrations.AddField(
            model_name='campus',
            name='nome',
            field=models.CharField(default=1, max_length=100, unique=True, verbose_name='Nome'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curso',
            name='nome',
            field=models.CharField(default='nome', max_length=200, unique=True, verbose_name='Nome'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('cpf', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='CPF')),
                ('campus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datawarehouse.Campus')),
                ('curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datawarehouse.Curso')),
                ('etnia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datawarehouse.Etnia')),
                ('origemEscolar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datawarehouse.OrigemEscolar')),
                ('sexo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datawarehouse.Sexo')),
            ],
        ),
    ]
