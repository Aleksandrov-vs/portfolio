from django.contrib import admin
from django.forms import ModelForm
from .models import ContactInformation


admin.site.register(ContactInformation)


class ContactInformationAdminForm(ModelForm):
    class Meta:
        model = ContactInformation
        fields = ["email", "phone_number"]


class ContactInformationAdmin(admin.ModelAdmin):
    form = ContactInformationAdminForm

    # fields = ("name", "description", "photo", 'video')
    #
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)