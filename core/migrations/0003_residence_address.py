# Generated by Django 4.2.3 on 2023-12-27 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_residence_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='residence',
            name='address',
            field=models.CharField(default='123 Main Street.', max_length=100),
        ),
    ]
