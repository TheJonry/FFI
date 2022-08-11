# Generated by Django 4.0.6 on 2022-08-11 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FFIapp', '0003_userprofile_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
                ('author', models.ForeignKey(null='True', on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]