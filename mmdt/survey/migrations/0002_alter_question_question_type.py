# Generated by Django 4.2.4 on 2024-03-05 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('MC', 'Multiple Choice'), ('CB', 'Check Box'), ('T', 'Text'), ('LT', 'Long Text'), ('DD', 'Drop-down'), ('SS', 'Sliding Scale')], default='T', max_length=255),
        ),
    ]
