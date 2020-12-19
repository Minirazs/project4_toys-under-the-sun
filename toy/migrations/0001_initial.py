# Generated by Django 3.1.4 on 2020-12-19 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('brand', models.CharField(default='', max_length=50)),
                ('price', models.FloatField(default='')),
                ('country', models.CharField(choices=[('UK', 'UK'), ('US', 'US'), ('Europe', 'Europe'), ('China', 'China'), ('Korea', 'Korea'), ('Japan', 'Japan'), ('SE Asia', 'SE Asia')], default='China', max_length=50)),
                ('age', models.CharField(choices=[('0-2 years', '0-2 years'), ('3-4 years', '3-4 years'), ('5-7 years', '5-7 years'), ('8-11 years', '8-11 years'), ('12-14 years', '12-14 years'), ('14 years+', '14 years+')], default='5-7 years', max_length=50)),
                ('desc', models.TextField(default='')),
                ('features', models.TextField(default='')),
            ],
        ),
    ]
