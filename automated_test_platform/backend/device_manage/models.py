"""
moudles of device manage
"""
from concurrent.futures.process import _python_exit
from tabnanny import verbose
from django.db import models

device_type = (
    ('PC', 'PC'),
    ('MOBILE', 'MOBILE'),
    ('CLOUDMOBILE', 'CLOUDMOBILE')
)

class DeviceType(models.Model):
    """
    meta of mobile type
    """
    class Meta:
        verbose_name_plural = '设备类型'

    def __str__(self):
        return self.deviceType + ': ' + self.deviceModel

    deviceType = models.CharField(max_length=20, choices=device_type, default='', verbose_name='设备类型')
    deviceBrand = models.CharField(max_length=20, default='', verbose_name='设备品牌')
    deviceModel = models.CharField(max_length=20, default='PC', verbose_name='设备型号')
    remarks = models.CharField(max_length=50, default='', blank=True, verbose_name='备注')


class Student(models.Model):
    class Meta:
        verbose_name_plural = verbose_name = '学员信息'

    SEX_ITEMS = [
        (1, '男'),
        (2, '女'),
        (0, '未知')
    ]

    STATUS_ITEMS = [
        (0, '申请'),
        (1, '通过'),
        (2, '拒绝')
    ]

    name = models.CharField(max_length=128, verbose_name='姓名')
    sex = models.IntegerField(max_length=128, choices=SEX_ITEMS, verbose_name='姓别')
    profession = models.CharField(max_length=128, verbose_name='职业')
    email = models.EmailField(verbose_name='Email')
    qq = models.CharField(verbose_name='QQ',max_length=20)
    phone = models.CharField(verbose_name='电话',max_length=20)
    status = models.IntegerField(verbose_name='审核状态', default=0, choices=STATUS_ITEMS)
    create_time = models.DateTimeField(auto_now_add=True, editable=False,verbose_name='创建时间')

    def __str__(self):
        return f'<student: {self.name}>'

