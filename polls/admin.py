from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

# Register your models here.

########### Simple
# admin.site.register(Poll)
# admin.site.register(Choice)

########### Custom


# class ChoiceInline(admin.StackedInline):   # Row per field
class ChoiceInline(admin.TabularInline):   # Column per field
  model = Choice
  extra = 3

class PollAdmin(admin.ModelAdmin):
  fieldsets = [
    (None,               {'fields': ['question']}),
    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
  ]
  inlines = [ChoiceInline]
  
  list_display = ('question', 'pub_date', 'was_published_recently')   # fields to display in main list of Polls
  list_filter = ['pub_date']
  search_fields = ['question']

  
admin.site.register(Poll, PollAdmin)