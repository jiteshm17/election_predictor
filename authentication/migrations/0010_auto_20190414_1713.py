# Generated by Django 2.1.7 on 2019-04-14 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_auto_20190414_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='description',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]
