# Generated by Django 4.1.3 on 2022-12-02 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_event_end_alter_event_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='free',
            field=models.BooleanField(default=True),
        ),
    ]