# Generated by Django 3.0.5 on 2020-05-02 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(default='aj', max_length=128)),
                ('message', models.TextField(default='Anji', max_length=128)),
            ],
        ),
    ]
