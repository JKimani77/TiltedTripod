# Generated by Django 3.0.3 on 2020-03-02 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flutter', '0003_auto_20200302_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_description',
            field=models.CharField(max_length=300),
        ),
    ]
