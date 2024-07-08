from typing import Iterable
from django.db import models
from django.template.defaultfilters import slugify

class Note(models.Model):
    title = models.CharField('عنوان',max_length=63,help_text='این فیلد عنوان پیام شماست')
    who = models.CharField("اسم",max_length=63,help_text='این فیلد اسم شما را نشان میدهد')
    date = models.DateField('تاریخ', auto_now_add=True)
    body = models.TextField('متن',help_text='این فیلد متن پیام شما میباشد')
    slug = models.SlugField(default='',null=True,unique=True,blank=True)
    count = models.PositiveSmallIntegerField('تعداد',help_text='این فیلد تعداد خواننده ها را مشخص میکند',default=1)

    def __str__(self) -> str:
        return f'{self.title} {self.who}'

