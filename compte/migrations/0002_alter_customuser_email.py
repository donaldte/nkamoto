# Generated by Django 4.2.5 on 2023-09-12 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
