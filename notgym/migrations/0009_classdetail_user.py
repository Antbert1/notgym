# Generated by Django 3.2.6 on 2021-08-25 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notgym', '0008_auto_20210825_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='classdetail',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
