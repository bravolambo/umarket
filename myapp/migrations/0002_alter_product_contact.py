# Generated by Django 5.1.4 on 2024-12-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='contact',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
