# Generated by Django 4.0 on 2022-01-01 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributor',
            name='project_id',
        ),
        migrations.AddField(
            model_name='contributor',
            name='project_id',
            field=models.ManyToManyField(to='api.Project'),
        ),
        migrations.RemoveField(
            model_name='contributor',
            name='user_id',
        ),
        migrations.AddField(
            model_name='contributor',
            name='user_id',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issue',
            name='assignee_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to='api.user'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='author_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='api.user'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('L', 'low'), ('M', 'medium'), ('H', 'high')], max_length=6),
        ),
        migrations.AlterField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.project'),
        ),
    ]