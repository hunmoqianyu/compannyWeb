from django.db import models


# Create your models here.

class Product(models.Model):
    imgs = models.ImageField(upload_to='img')
    name = models.CharField(max_length=20)
    details = models.CharField(max_length=200)
    type = models.CharField(max_length=10,
                            choices=(("1", "手持机"), ("2", "平板电脑"), ("3", "笔记本"), ("4", "防爆平板"), ("5", "其他")))
    size = models.CharField(max_length=10, choices=(("4", "4英寸"), ("5", "5英寸"), ("6", "6英寸"), ("7", "7英寸"),
                                                    ("8", "8英寸"), ("10.1", "10.1英寸"), ("12.2", "12.2英寸"),
                                                    ("13.3", "13.3英寸"),
                                                    ("14", "14英寸"), ("15.6", "15.6英寸"), ("21.5", "21.5英寸")
                                                    ))
    platform = models.CharField(max_length=10, choices=(("1", "Android"), ("2", "windows")))
    function = models.CharField(max_length=10, choices=(("1", "HF RFID"), ("2", "条码扫描 "),
                                                        ("3", "UHF RFID"), ("4", "LF RFID "), ("5", "NFC"),
                                                        ("6", "指纹识别"), ("7", "GPS  "), ("8", "摄像头"),
                                                        ("9", "身份证识别")))
