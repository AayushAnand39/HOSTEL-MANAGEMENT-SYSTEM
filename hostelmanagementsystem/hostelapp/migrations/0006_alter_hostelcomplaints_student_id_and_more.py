# Generated by Django 4.2.20 on 2025-07-11 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0005_alter_authorities_isloggedin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostelcomplaints',
            name='student_id',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='messcomplaints',
            name='student_id',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
