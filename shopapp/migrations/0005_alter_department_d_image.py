# Generated by Django 4.1.4 on 2023-02-23 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0004_alter_department_d_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='d_image',
            field=models.ImageField(default='/images/static/lion-fish.jpg', upload_to='static/images'),
        ),
    ]