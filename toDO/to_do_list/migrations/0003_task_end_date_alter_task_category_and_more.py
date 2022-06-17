# Generated by Django 4.0.5 on 2022-06-17 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0002_remove_task_id_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='to_do_list.category'),
        ),
        migrations.AlterField(
            model_name='task',
            name='describtion',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
