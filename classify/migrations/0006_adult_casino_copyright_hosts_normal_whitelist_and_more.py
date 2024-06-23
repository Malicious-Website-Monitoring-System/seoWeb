# Generated by Django 5.0.6 on 2024-06-22 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classify', '0005_fullsentence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Casino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Copyright',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.URLField(unique=True)),
                ('redirect', models.URLField(blank=True, null=True)),
                ('classification', models.CharField(blank=True, max_length=255, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_check_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Normal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Whitelist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='fullsentence',
            name='redirect',
        ),
        migrations.RemoveField(
            model_name='wordcount',
            name='redirect',
        ),
        migrations.AlterField(
            model_name='fullsentence',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='full_sentences', to='classify.hosts'),
        ),
        migrations.AlterField(
            model_name='wordcount',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classify.hosts'),
        ),
        migrations.DeleteModel(
            name='Host',
        ),
    ]
