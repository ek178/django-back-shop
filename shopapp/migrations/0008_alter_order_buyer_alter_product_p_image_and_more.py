# Generated by Django 4.1.4 on 2023-03-15 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0007_profile2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopapp.profile2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='p_image',
            field=models.ImageField(default='/static/images/lion-fish.jpg', upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='review',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopapp.profile2'),
        ),
    ]
