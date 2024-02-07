# Generated by Django 5.0.1 on 2024-01-24 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0014_alter_book_date_alter_packagereview_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='search',
            field=models.CharField(choices=[('', 'どのような場所に行きたいですか'), ('greenery', '緑が多い場所'), ('animal', '生物がいる場所'), ('water', '水遊びができる場所'), ('exercise', '運動ができる場所'), ('historical_place', '歴史を感じれる場所')], default='select', max_length=50),
        ),
    ]
