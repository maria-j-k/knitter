# Generated by Django 4.0.5 on 2022-07-11 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skeins', '0002_alter_skein_web_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='skein',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
