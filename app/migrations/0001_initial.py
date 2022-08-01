# Generated by Django 4.0.6 on 2022-07-31 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('date_of_join', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', ' Female'), ('other', 'Others')], max_length=20)),
                ('designation', models.CharField(max_length=30)),
                ('reporting_manager', models.CharField(max_length=30)),
            ],
        ),
    ]