# Generated by Django 4.2 on 2023-04-10 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seg_Roles',
            fields=[
                ('cod_rol', models.AutoField(default=-1, primary_key=True, serialize=False)),
                ('tip_roles', models.CharField(default=-1, max_length=20)),
            ],
            options={
                'db_table': 'seg_roles',
            },
        ),
    ]
