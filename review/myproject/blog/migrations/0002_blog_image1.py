# Generated by Django 3.0.8 on 2020-07-16 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image1',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
