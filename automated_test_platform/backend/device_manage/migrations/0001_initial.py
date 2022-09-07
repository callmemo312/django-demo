# Generated by Django 3.2.13 on 2022-07-03 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceBrand', models.CharField(default='', max_length=20, verbose_name='设备品牌')),
                ('deviceModel', models.CharField(default='PC', max_length=20, verbose_name='设备型号')),
                ('remarks', models.CharField(blank=True, default='', max_length=50, verbose_name='备注')),
            ],
            options={
                'verbose_name_plural': '设备类型',
            },
        ),
    ]