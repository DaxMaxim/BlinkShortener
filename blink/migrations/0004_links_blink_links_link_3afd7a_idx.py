# Generated by Django 4.0.4 on 2022-06-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blink', '0003_links_newlink'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='links',
            index=models.Index(fields=['link', 'newlink'], name='blink_links_link_3afd7a_idx'),
        ),
    ]
