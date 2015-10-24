from django.contrib import admin
from django.conf.urls.static import static
# Register your models here.
#ankur
#password
from .models import Question,Choice,UserInfo,TopicInfo,SubTopic


# admin.site.register(Question)


# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['published_date', 'question_text']
#
#
#     admin.site.register(Question,QuestionAdmin)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['published_date'], 'classes': ['collapse']}),
    # ]
    list_display =  ('question_text','published_date','question_type')
    inlines = [ChoiceInline]
    list_filter = ['published_date']

admin.site.register(Question, QuestionAdmin)


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("user_name","user_email","user_contact")

admin.site.register(UserInfo, UserInfoAdmin)


class SubtopicInline(admin.TabularInline):
    model = SubTopic
    extra = 2


class topicAdmin(admin.ModelAdmin):
    list_display = ("topic_name","is_active","topic_image","image_preview",)
    inlines = [SubtopicInline]
    list_editable = ("topic_name","is_active","topic_image")
    list_filter = ('is_active',)
    search_fields = ('topic_name',)

admin.site.register(TopicInfo,topicAdmin)
# admin.site.register(Choice)


class SubtopicAdmin(admin.ModelAdmin):
    list_display = ("topic","subTopic_name","subTopic_isactive",'isTheory_active','isFormula_active','isQuestion_active')
    list_editable = ("topic","subTopic_name","subTopic_isactive",'isTheory_active','isFormula_active','isQuestion_active',)
    list_filter = ('subTopic_isactive' , 'topic',)
    search_fields = ('subTopic_name',)
    #define ordering of list as field, '-' means descending order. should be tuple
    ordering = ('subTopic_name',)
    #define fields which user can edit, rest fields can't be editable, if not in list, should be tuple
    fields = ('topic','subTopic_name','isTheory_active','isFormula_active','isQuestion_active',)
admin.site.register(SubTopic,SubtopicAdmin)
