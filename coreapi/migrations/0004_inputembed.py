# Generated by Django 2.2.1 on 2019-06-22 02:56

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('coreapi', '0003_auto_20190612_0439'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputEmbed',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=80)),
                ('created_on', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]