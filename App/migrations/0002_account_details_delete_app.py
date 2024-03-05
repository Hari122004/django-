# Generated by Django 4.2.10 on 2024-03-01 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(max_length=30)),
                ('Emails', models.CharField(max_length=30)),
                ('Contac_no', models.IntegerField(verbose_name=12)),
                ('Address', models.TextField()),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='App',
        ),
    ]
