from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

from django.core.urlresolvers import reverse
from tagging.fields import TagField
from django.contrib.auth.models import User
# from django.utils.text import slugify

# Create your models here.

# @python_2_unicode_compatible

class Sigudong(models.Model):
        cnum = models.CharField(primary_key=True, max_length=15)
        si = models.CharField('si', max_length=15)
        gu = models.CharField('gu', max_length=15, blank=True, null=True)
        dong = models.CharField('dong', max_length=15, blank=True, null=True)

        def __str__(self):
            return self.cnum




class Emer(models.Model):
    ordering = ['-timestamp']
    # no = models.AutoField('NO', auto_created=True)
    # no = models.AutoField('NO', primary_key=True)
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    # title = models.CharField('제목', max_length=50)
    # slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.',default="mname")
    # description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    # content = models.TextField('CONTENT')
    # create_date = models.DateTimeField('Create Date', auto_now_add=True)
    # modify_date = models.DateTimeField('Modify Date', auto_now=True)
    # tag = TagField()
    # owner = models.ForeignKey(User, null=True)

    mid = models.IntegerField('mid')
    cnum = models.ForeignKey(Sigudong, on_delete=models.CASCADE)
    mname = models.CharField('mname', max_length=20)
    mtel = models.CharField('mtel', max_length=15)
    madd = models.CharField('madd', max_length=500)
    
    def __str__(self):
        return str(self.mid) + ' ' + str(self.cnum) + ' ' + self.mname + ' ' + self.mtel + ' ' + self.madd



    class Meta:
        verbose_name = 'emer'
        verbose_name_plural = 'emers'
        db_table  = 'emer_emers'
        ordering  = ('id',)

    def __str__(self):
        return self.mname

    def get_absolute_url(self):
        return reverse('emer:change')

    # def get_previous_post(self):
    #     return self.get_previous_by_modify_date()

    # def get_next_post(self):
    #     return self.get_next_by_modify_date()

