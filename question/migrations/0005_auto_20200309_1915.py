# Generated by Django 3.0.4 on 2020-03-09 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_auto_20200309_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
