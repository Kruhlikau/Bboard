# Generated by Django 3.2 on 2021-04-18 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_auto_20210418_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.rubric', verbose_name='Рубрика'),
        ),
    ]
