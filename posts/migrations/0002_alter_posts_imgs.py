# Generated by Django 4.2.7 on 2023-12-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='imgs',
            field=models.ImageField(upload_to='media/'),
        ),
    ]