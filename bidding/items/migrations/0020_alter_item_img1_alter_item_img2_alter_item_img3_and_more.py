# Generated by Django 4.2.4 on 2023-08-10 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0019_item_sendwinmail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='item',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='item',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='item',
            name='img4',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
    ]