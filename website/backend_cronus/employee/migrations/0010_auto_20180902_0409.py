# Generated by Django 2.1 on 2018-09-01 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_auto_20180902_0237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='bookedTill',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='currentProject',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='isStaffed',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='skillSets',
        ),
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
