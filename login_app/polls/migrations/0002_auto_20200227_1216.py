# Generated by Django 3.0.3 on 2020-02-27 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='cjoice_text',
            new_name='choice_text',
        ),
    ]
