# Generated by Django 4.2.4 on 2023-08-13 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_alter_taskmodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
