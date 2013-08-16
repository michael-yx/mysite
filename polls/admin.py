from django.contrib import admin
from polls.models import Poll,Choice

class ChoiceInline(admin.StackedInline):
    model=Choice
    extra=3

class PollAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['question']}),
               ('Date Information',{'fields':['pub_date']}),]
    inlines=[ChoiceInline]
    list_display=('question','pub_date','was_published_recently')


admin.site.register(Poll,PollAdmin)