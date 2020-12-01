from django.contrib import admin
from works.models import Work
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Work, MarkdownxModelAdmin)
