# Generated by Django 3.1.4 on 2020-12-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toy', '0004_auto_20201224_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='country',
            field=models.CharField(choices=[('UK & Europe', 'UK & Europe'), ('US & Canada', 'US & Canada'), ('China', 'China'), ('Korea', 'Korea'), ('Japan', 'Japan'), ('SE Asia', 'SE Asia')], default='', max_length=50),
        ),
    ]
