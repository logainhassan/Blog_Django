# Generated by Django 3.0.3 on 2020-02-22 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(max_length=500, upload_to='Images/'),
        ),
    ]
