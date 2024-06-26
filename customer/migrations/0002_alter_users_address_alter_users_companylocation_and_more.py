# Generated by Django 5.0.3 on 2024-04-26 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='Address',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='CompanyLocation',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='CompanyName',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='FirstName',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='GST_No',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='users',
            name='LastName',
            field=models.CharField(default='NA', max_length=100),
        ),
    ]
