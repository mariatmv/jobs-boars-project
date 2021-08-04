# Generated by Django 3.2.6 on 2021-08-04 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_remove_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='contact_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
