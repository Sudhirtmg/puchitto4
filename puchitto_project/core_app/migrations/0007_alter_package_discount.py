# Generated by Django 5.0.1 on 2024-01-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0006_remove_package_old_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='discount',
            field=models.IntegerField(default=10, verbose_name='割引'),
        ),
    ]