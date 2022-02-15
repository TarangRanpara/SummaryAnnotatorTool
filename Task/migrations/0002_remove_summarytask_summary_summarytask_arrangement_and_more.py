# Generated by Django 4.0.2 on 2022-02-10 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summarytask',
            name='summary',
        ),
        migrations.AddField(
            model_name='summarytask',
            name='arrangement',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='summarytask',
            name='enoughDetails',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='summarytask',
            name='grammatical_correctness',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='summarytask',
            name='professional',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='summarytask',
            name='quality',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='summarytask',
            name='singlePoint',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='summarytask',
            name='title',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='summarytask',
            name='article',
            field=models.TextField(null=True),
        ),
    ]