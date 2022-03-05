from django.contrib import admin
from django.utils.html import format_html # html لكتابة أكواد 
from .models import Team

class TeamAdmin(admin.ModelAdmin): # admin site في  Team وذلك لعمل تعديل على صفحة اضار معلومات الجدول class تم تعريف 
    def thumbnail(self, object):  # لاسخراج الصوره 
        return format_html(f'<img src="{object.photo.url}" width="40" style="border-radius: 50px;" />')

    thumbnail.short_description = 'photo' # لتغيير العنوان ىالخاص بالصورة بدلا من اسم الدالة
    
    list_display = ('id', 'thumbnail', 'first_name', 'last_name', 'designation', 'created_date') # لتحديد الحقول التي سوف تظهر 
    list_display_links = ('id', 'thumbnail', 'first_name') # لتحديد الحقول التي سوف تكون على شكل رابط
    search_fields = ('first_name', 'last_name', 'designation') # لتحديد الحقول التي سيتم البحث من خلالها
    list_filter = ('designation',) # لتحديد الحقول التي سوف يتم عمل فلتر من خلالها
    
admin.site.register(Team, TeamAdmin)
