# Generated by Django 3.2.2 on 2021-05-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0190_quota_ignore_for_event_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
    ]
