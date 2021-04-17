# Generated by Django 3.2 on 2021-04-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_delete_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveSections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancel_about', models.BooleanField(default=False)),
                ('cancel_services', models.BooleanField(default=False)),
                ('cancel_portfolio', models.BooleanField(default=False)),
                ('cancel_experience', models.BooleanField(default=False)),
                ('cancel_contact', models.BooleanField(default=False)),
            ],
        ),
    ]