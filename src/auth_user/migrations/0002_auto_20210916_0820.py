# Generated by Django 3.2.7 on 2021-09-16 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devsetup',
            old_name='email_verification',
            new_name='verification_type',
        ),
        migrations.AddField(
            model_name='devsetup',
            name='frontend_url',
            field=models.URLField(default='http://localhost:3000', help_text='this url is used while sending emails', max_length=255),
        ),
    ]
