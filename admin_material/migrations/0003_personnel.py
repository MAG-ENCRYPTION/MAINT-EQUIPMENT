# Generated by Django 4.2.3 on 2023-07-23 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_material', '0002_rapportmaintenace_demandeintervention_capteur_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('matricule', models.AutoField(db_column='matricule', primary_key=True, serialize=False)),
                ('nom', models.CharField(db_column='nom', max_length=100)),
                ('prenom', models.CharField(db_column='prenom', max_length=100)),
                ('Poste', models.CharField(db_column='poste', max_length=100)),
                ('Telephone', models.IntegerField(db_column='tel', max_length=100)),
                ('email', models.EmailField(db_column='mail', max_length=100)),
            ],
        ),
    ]
