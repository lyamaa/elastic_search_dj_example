# Generated by Django 3.2.3 on 2021-05-21 14:54

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import searches.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Hotel Name')),
                ('description', models.TextField(default='', verbose_name='Hotel Descriptions')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', slugify=searches.models.slugify, verbose_name='Hotel Slug')),
                ('is_active', models.BooleanField(default=True)),
                ('config_choice', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='commons.configchoice')),
            ],
            options={
                'verbose_name': 'Hotel',
                'verbose_name_plural': 'Hotels',
            },
        ),
        migrations.CreateModel(
            name='HotelSpecifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Hotel Spec Name')),
            ],
            options={
                'verbose_name': 'Hotel Specification',
                'verbose_name_plural': 'Hotel Specifications',
            },
        ),
        migrations.CreateModel(
            name='HotelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Hotel Types Name')),
            ],
            options={
                'verbose_name': 'Hotel Type',
                'verbose_name_plural': 'Hotel Types',
            },
        ),
        migrations.CreateModel(
            name='HotelSpecificationValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(help_text='Hotel specification value (maximum of 255 words', max_length=255, verbose_name='Value')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='searches.hotel')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='searches.hotelspecifications')),
            ],
            options={
                'verbose_name': 'Hotel Specification Value',
                'verbose_name_plural': 'Hotel Specification Values',
            },
        ),
        migrations.AddField(
            model_name='hotelspecifications',
            name='hotel_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='searches.hoteltype'),
        ),
        migrations.CreateModel(
            name='HotelImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('image_urls', models.URLField(help_text='Images Urls', verbose_name='Hotel Image URLs')),
                ('caption', models.CharField(blank=True, help_text='Please add alturnative text', max_length=255, null=True, verbose_name='Alternative text')),
                ('is_feature', models.BooleanField(default=False)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_image', to='searches.hotel')),
            ],
            options={
                'verbose_name': 'Hotel Image',
                'verbose_name_plural': 'Hotel Images',
            },
        ),
        migrations.CreateModel(
            name='HotelAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commons.address')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_addres', to='searches.hotel')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='searches.hoteltype'),
        ),
    ]
