# Generated by Django 4.1.1 on 2022-09-06 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cuentas', '0002_tipocuentas'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta',
            name='typeid',
            field=models.ForeignKey(db_column='typeId', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Cuentas.tipocuentas'),
            preserve_default=False,
        ),
    ]
