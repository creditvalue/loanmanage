# Generated by Django 3.2.4 on 2021-09-13 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_uhistory_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='img/usera.jpg', upload_to='alluser/img'),
        ),
    ]