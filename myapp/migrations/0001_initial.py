# Generated by Django 4.1.7 on 2023-04-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=122)),
                ('name', models.CharField(max_length=122)),
                ('contact', models.CharField(max_length=12)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]