# Generated by Django 4.0.4 on 2022-06-28 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0012_profile_instagram_url_profile_linkedin_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactuss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('message', models.TextField()),
            ],
        ),
    ]