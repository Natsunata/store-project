# Generated by Django 4.2 on 2023-06-01 10:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('basket_history', models.JSONField(default=dict)),
                ('status', models.SmallIntegerField(choices=[('CREATED', 'Создан'), ('PAID', 'Оплачен'), ('ON_WAY', 'В пути'), ('DELIVERED', 'Доставлен')], default=0)),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
