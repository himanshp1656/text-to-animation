# Generated by Django 3.2.19 on 2023-09-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appss', '0004_teacherlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherlist',
            name='subject',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
