# Generated by Django 3.1.6 on 2021-02-26 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesProvided',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField()),
            ],
        ),
    ]
