# Generated by Django 4.0.5 on 2022-06-17 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0004_alter_task_describtion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
    ]