# Generated by Django 3.0.8 on 2020-09-23 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_remove_divar_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='divar',
            name='Author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
