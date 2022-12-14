# Generated by Django 3.2.16 on 2022-12-12 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelbooking',
            name='booking_type',
            field=models.CharField(choices=[('Pre Paid', 'Pre Paid'), ('Post Paid', 'Post Paid')], default='Post Paid', max_length=100),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='room_count',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='hotelimages',
            name='images',
            field=models.ImageField(upload_to='hotels'),
        ),
    ]
