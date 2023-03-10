# Generated by Django 3.2.15 on 2023-02-20 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_mainimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='New_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgs', models.ImageField(upload_to='img')),
                ('name', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('1', '手持机'), ('2', '平板电脑'), ('3', '笔记本'), ('4', '防爆平板'), ('5', '其他')], max_length=10)),
            ],
        ),
    ]
