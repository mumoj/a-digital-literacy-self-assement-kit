# Generated by Django 3.1.4 on 2021-01-06 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kit.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='responses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
