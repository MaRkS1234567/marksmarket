# Generated by Django 4.0.4 on 2022-05-06 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(),
        ),
    ]
