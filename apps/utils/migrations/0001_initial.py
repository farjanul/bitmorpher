# Generated by Django 5.1a1 on 2024-06-23 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('date_time', models.DateTimeField()),
                ('path', models.CharField(max_length=200)),
                ('method', models.CharField(max_length=10)),
            ],
        ),
    ]