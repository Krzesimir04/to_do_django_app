# Generated by Django 4.0.5 on 2022-06-17 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0003_task_end_date_alter_task_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='describtion',
            field=models.TextField(null=True),
        ),
    ]