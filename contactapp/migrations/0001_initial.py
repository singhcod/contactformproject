# Generated by Django 3.0 on 2021-01-13 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='oontactdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_nmae', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('company_name', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
                ('location', models.CharField(max_length=15)),
            ],
        ),
    ]
