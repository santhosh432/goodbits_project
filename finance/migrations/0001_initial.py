# Generated by Django 3.2.3 on 2021-05-27 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('project_name', models.CharField(help_text='Please specify project name', max_length=100)),
                ('amount', models.FloatField(help_text='Please specify amount')),
                ('status', models.BooleanField(default=False, help_text='Check for invoice')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('paid_on', models.DateTimeField(blank=True, null=True)),
                ('paid_status', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(help_text='Customer', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
