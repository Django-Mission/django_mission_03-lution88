from django.contrib import admin
from .models import Answer, Faq, Inquiry
# Register your models here.

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('question','category', 'updated_at')
    list_filter = ('category', )
    search_fields = ('question', )
    search_help_text = '게시판 제목 검색이 가능합니다.'

class AsnwerInline(admin.TabularInline):
    model = Answer
    extra = 2
    min_num = 2
    max_num = 3
    
    verbose_name = '답변'
    verbose_name_plural = '답변'

def send_data(modelsadmin, request, queryset):
    for item in queryset:
        if item.status == '3':
            if item.is_email == True:
                print(f'{item.title}: 답변완료, {item.email} 내용 발송')
            if item.is_message == True:
                print(f'{item.title}: 답변완료, {item.message} 내용 발송')
            

@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'category', 'created_at', 'created_by')
    list_filter = ('category', 'status', )
    search_fields = ('created_by__username', 'title', 'email', 'message', )
    search_help_text = '게시판 제목, 이메일, 전화번호 검색이 가능합니다.'
    inlines = [AsnwerInline]
    
    actions = [send_data]
    