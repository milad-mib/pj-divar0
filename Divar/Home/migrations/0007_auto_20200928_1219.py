# Generated by Django 3.1.1 on 2020-09-28 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_auto_20200923_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divar',
            name='Picture',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]
