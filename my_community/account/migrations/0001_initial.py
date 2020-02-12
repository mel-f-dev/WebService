# Generated by Django 2.2.5 on 2020-02-12 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='member_images')),
            ],
        ),
    ]
