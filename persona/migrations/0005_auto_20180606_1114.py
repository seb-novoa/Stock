# Generated by Django 2.0.6 on 2018-06-06 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_auto_20180606_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas',
            name='Gestor',
            field=models.ManyToManyField(null=True, related_name='_personas_Gestor_+', to='persona.Personas'),
        ),
    ]
