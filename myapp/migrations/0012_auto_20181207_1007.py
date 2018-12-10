# Generated by Django 2.1.2 on 2018-12-07 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20181207_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='restaurant',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='myapp.Restaurant'),
        ),
    ]
