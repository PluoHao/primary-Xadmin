from django.contrib import admin
from django.forms import DateTimeField
from xadmin import views
import xadmin
from .models import *
# Register your models here.

class UserXadmin(object):
    list_display = ['name','phone','score']
    list_editable = ['name','phone','score']
    date_hierarchy = DateTimeField

class BaseSetting(object):
    enable_themes = True   # 打开主题功能
    use_bootswatch = True

class GlobalSettings(object):
    site_title="后台管理系统"
    site_footer="老王总站"
    menu_style="accordion"

xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(User,UserXadmin)