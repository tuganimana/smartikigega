# Generated by Django 3.1.6 on 2021-03-20 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210319_1755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farmers',
            old_name='fullname',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='farmers',
            name='lastname',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
