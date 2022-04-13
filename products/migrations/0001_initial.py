# Generated by Django 4.0.3 on 2022-04-01 16:34

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
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('received', models.IntegerField()),
                ('in_stock', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('spoiled', models.IntegerField()),
                ('buying_price', models.IntegerField()),
                ('selling_price', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('clerk', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]