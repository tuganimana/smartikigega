# Generated by Django 3.1.6 on 2021-03-22 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ussd', '0002_auto_20210322_2057'),
        ('home', '0004_auto_20210321_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvestrecord',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ussd.farmers'),
        ),
        migrations.DeleteModel(
            name='Farmers',
        ),
    ]