# Generated by Django 3.0.5 on 2020-04-08 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='auth_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
