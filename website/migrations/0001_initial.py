# Generated by Django 4.0.4 on 2022-04-25 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'required': 'Name must be provided.'}, max_length=150)),
                ('email', models.EmailField(blank=True, error_messages={'required': 'Email must be provided'}, max_length=254, null=True)),
                ('phone', models.CharField(error_messages={'required': 'Phone number must be provided.'}, max_length=9)),
                ('message', models.TextField(error_messages={'required': 'A valid message must be provided.'})),
            ],
        ),
    ]