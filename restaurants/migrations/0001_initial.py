# Generated by Django 3.1.5 on 2021-01-07 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('price', models.IntegerField(default=400)),
                ('tables', models.IntegerField(default=5)),
                ('category', models.CharField(choices=[('OUTDOOR', 'OUTDOOR'), ('CAFE', 'CAFE'), ('PUB & BAR', 'PUB & BAR'), ('BUFFET', 'BUFFET'), ('FAMILY DINING', 'FAMILY DINING')], default='0', max_length=100)),
            ],
        ),
    ]
