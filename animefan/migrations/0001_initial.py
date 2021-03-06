# Generated by Django 3.1.2 on 2020-10-06 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime_id', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('animetype', models.CharField(max_length=100)),
                ('episodes', models.IntegerField(null=True)),
                ('rating', models.FloatField(null=True)),
                ('members', models.IntegerField(null=True)),
                ('mood', models.CharField(max_length=15)),
            ],
        ),
    ]
