from django.contrib import admin
from django.forms import ModelForm
from works.models import Work
from markdownx.admin import MarkdownxModelAdmin


class WorkAdminForm(ModelForm):
    class Meta:
        model = Work
        exclude = ['id']


class WorkAdmin(admin.ModelAdmin):
    form = WorkAdminForm

    def get_queryset(self, request):
        qs = Work.objects.filter(domain=request.domain)
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs


admin.site.register(Work, MarkdownxModelAdmin)