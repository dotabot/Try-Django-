# Generated by Django 3.2.13 on 2022-06-27 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
