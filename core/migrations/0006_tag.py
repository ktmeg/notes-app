# Generated by Django 3.0.4 on 2020-03-17 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_delete_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.CharField(max_length=30)),
            ],
        ),
    ]