# Generated by Django 3.1.4 on 2021-01-06 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kit', '0003_auto_20210106_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
