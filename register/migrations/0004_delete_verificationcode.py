# Generated by Django 3.2.18 on 2023-03-03 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_verificationcode'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VerificationCode',
        ),
    ]
