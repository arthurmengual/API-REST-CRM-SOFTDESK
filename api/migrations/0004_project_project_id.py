# Generated by Django 4.0 on 2022-01-04 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_project_project_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
