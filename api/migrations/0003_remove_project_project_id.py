# Generated by Django 4.0 on 2022-01-04 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_contributor_project_id_contributor_project_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_id',
        ),
    ]
