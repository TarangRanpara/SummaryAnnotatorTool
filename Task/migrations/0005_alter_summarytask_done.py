# Generated by Django 4.0.2 on 2022-02-14 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0004_summarytask_gold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summarytask',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
