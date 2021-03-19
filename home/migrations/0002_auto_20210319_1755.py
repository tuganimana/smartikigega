# Generated by Django 3.1.6 on 2021-03-19 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farmers',
            old_name='firstname',
            new_name='fullname',
        ),
        migrations.RemoveField(
            model_name='farmers',
            name='lastname',
        ),
        migrations.AddField(
            model_name='farmers',
            name='pincode',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='farmers',
            name='Cooperative',
            field=models.CharField(default='', max_length=255),
        ),
    ]
