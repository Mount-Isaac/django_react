# Generated by Django 4.2.1 on 2023-05-17 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization_', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login_model',
            old_name='username',
            new_name='email',
        ),
    ]
