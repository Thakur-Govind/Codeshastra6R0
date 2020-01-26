# Generated by Django 2.0.2 on 2020-01-26 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='ng_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ngo',
            name='location',
            field=models.CharField(max_length=200),
        ),
    ]
