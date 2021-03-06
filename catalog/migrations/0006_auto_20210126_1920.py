# Generated by Django 3.1.5 on 2021-01-26 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20210126_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='language',
            old_name='language',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, null=True, verbose_name='died'),
        ),
    ]
