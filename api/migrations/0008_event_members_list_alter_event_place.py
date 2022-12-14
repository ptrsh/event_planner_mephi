# Generated by Django 4.1.3 on 2022-12-03 13:47

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_event_active_alter_event_free'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='members_list',
            field=models.ManyToManyField(related_name='subscribes', to='api.author'),
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.ForeignKey(default=api.models.create_default_place, on_delete=django.db.models.deletion.PROTECT, to='api.place'),
        ),
    ]
