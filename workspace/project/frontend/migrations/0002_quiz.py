# Generated by Django 3.1 on 2020-10-17 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_of_sake', models.IntegerField()),
                ('firstfeeling', models.IntegerField()),
                ('secondfeeling', models.IntegerField()),
            ],
        ),
    ]
