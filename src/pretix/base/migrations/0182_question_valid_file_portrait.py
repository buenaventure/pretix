# Generated by Django 3.0.13 on 2021-04-19 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0181_team_can_checkin_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='valid_file_portrait',
            field=models.BooleanField(default=False),
        ),
    ]
