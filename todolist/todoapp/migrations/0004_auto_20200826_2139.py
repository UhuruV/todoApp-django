# Generated by Django 2.2.3 on 2020-08-26 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_auto_20200826_2132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='todolist',
            old_name='date_created',
            new_name='created',
        ),
    ]
