# Generated by Django 3.2.3 on 2021-06-17 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0193_auto_20210611_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='canceled',
            field=models.BooleanField(default=False),
        ),
    ]
