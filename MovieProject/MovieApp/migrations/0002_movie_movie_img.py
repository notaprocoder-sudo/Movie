# Generated by Django 4.1.4 on 2023-02-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Movie_Img',
            field=models.ImageField(default='defimg', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
