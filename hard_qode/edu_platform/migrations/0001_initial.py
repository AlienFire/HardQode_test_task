# Generated by Django 5.0.2 on 2024-02-29 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('start_at', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('student_count_from', models.IntegerField(default=0)),
                ('student_count_to', models.IntegerField()),
            ],
        ),
    ]
