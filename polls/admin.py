from django.contrib import admin
from .models import Question, Choice

# Register your models here.

# 어드민 페이지에 Question 테이블 추가
# 어드민 페이지에 들어가면 POLLS > Question 이 생성된것을 확인 할 수 있다.

# 어드민 페이지에 입력/수정 할 수 있게 되었다.


# class ChoiceInline(admin.StackedInline): 폼들이 세로정렬되어 보기 복잡시럽다.
# TabularInline은 표와같이 가로정렬되어 보기 좋다~
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                {'fields': ['question_text']}),
        ('Date information',  {'fields': ['pub_date']}),
    ]

    list_display = ('question_text', 'pub_date',
                    'was_publiched_recently')

    inlines = [ChoiceInline]
    search_field = ['question_text']


admin.site.register(Question, QuestionAdmin)
