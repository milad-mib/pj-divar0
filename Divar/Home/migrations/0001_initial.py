# Generated by Django 3.0.8 on 2020-09-23 14:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Divar',
            fields=[
                ('Category', models.CharField(blank=True, choices=[('TV', 'Telvision'), ('Mobile', 'Monile'), ('Laptop', 'laptop'), ('PC', 'PC'), ('Car', 'car'), ('Camera', 'Camera')], max_length=100, null=True)),
                ('Picture', models.ImageField(default='default.jpg', upload_to='')),
                ('Ad_Titel', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.CharField(blank=True, max_length=200, null=True)),
                ('City', models.CharField(blank=True, choices=[('Tehran', 'Tehran'), ('Tabriz', 'Tabriz'), ('Mashhad', 'Mashhad'), ('Shiraz', 'Shiraz'), ('Rasht', 'Rasht'), ('Yazd', 'Yazd'), ('Kordestan', 'Kordestan')], max_length=100, null=True)),
                ('status', models.CharField(blank=True, choices=[('New', 'New'), ('Stock', 'Stock'), ('Broken', 'Broken')], max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=10, default='Agreement', max_digits=100)),
                ('Phone', models.IntegerField(blank=True, null=True)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
        ),
    ]