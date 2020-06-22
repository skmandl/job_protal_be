from django.contrib import admin
from django.contrib.admin import TabularInline
# Register your models here.
from .models import *
from django.utils.safestring import mark_safe


class RecuirementTabular(admin.TabularInline):
    model=Recuirement
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra


class ResponsTabular(admin.TabularInline):
    model=Responsibilities
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra


class JobListAdmin(admin.ModelAdmin):
    list_display=('job_category','post_name','company','last_date')
    search_fields=['post_name','job_category__option']

class JobdetailAdmin(admin.ModelAdmin):
    list_display=('overview',)
    inlines=[RecuirementTabular,ResponsTabular]

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','company_logo')
    readonly_fields = ["logo"]

    def logo(self, obj):
        
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.company_logo.url,
            width=obj.company_logo.width,
            height=obj.company_logo.height,
            )
    )

admin.site.register(JobList,JobListAdmin)
admin.site.register(JobDetail,JobdetailAdmin)
admin.site.register(Recuirement)
admin.site.register(Responsibilities)

admin.site.register(Category)
admin.site.register(Company,CompanyAdmin)
admin.site.register(JobType)
admin.site.register(Degree)



