# Generated by Django 4.0.2 on 2022-02-27 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='learn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competetion', models.CharField(max_length=20)),
                ('collage', models.CharField(max_length=10)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
