# Generated by Django 4.1.2 on 2022-11-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saraeurope', '0003_pictures_alter_productimage_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.TextField()),
            ],
            options={
                'verbose_name': 'About Us',
                'verbose_name_plural': 'About Us',
            },
        ),
    ]
