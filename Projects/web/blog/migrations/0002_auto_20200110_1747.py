# Generated by Django 2.2.5 on 2020-01-10 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publication_date',
            new_name='published_date',
        ),
    ]
