# Generated by Django 3.2.2 on 2021-05-10 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_pub', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('cover_pic', models.ImageField(upload_to='blogcover/')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=25)),
                ('pic', models.ImageField(upload_to='staff_pic/')),
            ],
        ),
    ]