# Generated by Django 4.0 on 2022-01-13 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_project_issue_project_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comments_id',
        ),
    ]
