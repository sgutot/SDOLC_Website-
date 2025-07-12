from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from .forms import *


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'contact_email', 'contact_phone')
    fieldsets = (
        ('Basic Information', {
            'fields': ('site_name', 'site_logo')
        }),
        ('Contact Information', {
            'fields': ('contact_email', 'contact_phone', 'address')
        }),
        ('Quick Links', {
            'fields': ('quick_links_json',),
            'description': 'Enter JSON format for quick links. Example: {"Bid Opportunities": "/bid-opportunities"}'
        }),
    )
    
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()
    

@admin.register(VideosCitizensCharter)
class VideosCitizensCharterAdmin(admin.ModelAdmin):
    list_display = ('caption', 'content')
    list_filter = ('date_posted',)
    search_fields =('caption', 'content', 'date_posted')
    fields = ('caption', 'video', 'date_posted', 'content')

@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('caption',)
    list_filter = ('date_posted',)
    search_fields =('caption', 'date_posted')
    fields = ('caption', 'video', 'date_posted',)


@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image', 'date_posted', 'file')
    search_fields = ('title', 'content', 'date_posted')
    list_filter = ('date_posted',)
    readonly_fields = ('date_posted',)
    fields = ('title', 'content', 'image', 'date_posted', 'file')

    
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'updated_at')
    list_filter = ('date_posted',) 
    search_fields = ('title', 'content', 'date_posted')
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content', 'link')
        }),
        ('Media', {
            'fields': ('image', 'file')
        }),
        ('Settings', {
            'fields': ('date_posted',)
        }),
    )



@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description', 'date_posted')
    list_filter = ('name', 'date_posted')
    fields = ('name', 'image', 'description', 'link', 'file','date_posted')




@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'content', 'file')
    search_fields = ('title', 'content', 'date_posted')
    list_filter = ('date_posted',)
    readonly_fields = ('date_posted',)
    fields = ('title', 'content', 'link', 'file', 'date_posted')




@admin.register(OrganizationalChart)
class OrganizationalChartAdmin(admin.ModelAdmin):
    list_display = ('management', 'positions', 'name', 'contact', 'date_posted')
    list_filter = ('management',)  # Adds filter sidebar by category
    search_fields = ('positions', 'name', 'management', 'date_posted')
    list_per_page = 20  # Shows 20 items per page instead of default 100
    
    fieldsets = (
        ('Category Information', {
            'fields': ('management',),
            'description': 'Select the department/category for this entry'
        }),
        ('Person Details', {
            'fields': ('name', 'positions', 'image', 'contact'),
        }),
        ('Additional Information', {
            'fields': ('about', 'link', 'date_posted'),
            'classes': ('collapse',)  # Makes this section collapsible
        }),
    )
    
    # Add this if you want the management field to appear first in the add/edit form
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.fieldsets
        return super().get_fieldsets(request, obj)

@admin.register(CitizensCharter)
class CitizensCharterAdmin(admin.ModelAdmin):
    list_display = ('title', 'truncated_content', 'date_posted', 'has_file', 'has_link')
    list_filter = ('date_posted',)
    search_fields = ('title', 'content', 'date_posted')
    fields = ('title', 'content', 'file', 'link', 'date_posted')
    
    def truncated_content(self, obj):
        return obj.content[:100] + '...' if obj.content else ''
    truncated_content.short_description = 'Content Preview'
    
    def has_file(self, obj):
        return bool(obj.file)
    has_file.boolean = True
    
    def has_link(self, obj):
        return bool(obj.link)
    has_link.boolean = True

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'file', 'link',)
    search_fields = ('title', 'content', 'date_posted')
    fields = ('title', 'content', 'file', 'link', 'date_posted')

@admin.register(Vision)
class VisionAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'file', 'link',)
    search_fields = ('title', 'content', 'date_posted')
    fields = ('title', 'content', 'file', 'link', 'date_posted')

@admin.register(Mandate)
class MandateAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'file', 'link',)
    search_fields = ('title', 'content', 'date_posted')
    fields = ('title', 'content', 'file', 'link', 'date_posted')

@admin.register(CoreValues)
class CoreValuesAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'file', 'link')
    search_fields = ('title', 'content', 'date_posted')
    list_filter = ('date_posted',)
    date_hierarchy = 'date_posted'
    
@admin.register(QualityPolicy)
class QualityPolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'file', 'link',)
    search_fields = ('title', 'content')
    fields = ('title', 'content', 'file', 'link', 'date_posted')




#ISSUANCES

#@admin.register(RegionalMemo)
#class RegionalMemoAdmin(admin.ModelAdmin):
#    list_display = ('title', 'content', 'file', 'link',)
#    search_fields = ('title',)
 #   fields = ('title', 'file', 'link', 'content', 'date_posted')



@admin.register(DivisionMemo)
class DivisionMemoAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'get_month_name', 'date_published')
    list_filter = ('year', 'month')  # Add this to enable filtering by year and month
    form = DivisionMemoForm
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['date_published'].widget = forms.DateTimeInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            },
            format='%Y-%m-%dT%H:%M'
        )
        return form

#@admin.register(OfficeMemo)
#class OfficeMemoAdmin(admin.ModelAdmin):
#    list_display = ('title', 'content', 'file', 'link',)
#    search_fields = ('title', 'date_posted')
#    fields = ('title', 'file', 'link', 'content', 'date_posted')

@admin.register(OfficeMemo)
class OfficeMemoAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'get_month_name', 'date_published')
    list_filter = ('year', 'month') 
    form = OfficeMemoForm
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['date_published'].widget = forms.DateTimeInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            },
            format='%Y-%m-%dT%H:%M'
        )
        return form

#@admin.register(DepedOrder)
#class DepedOrderAdmin(admin.ModelAdmin):
#    list_display = ('title', 'content', 'file', 'link',)
#    search_fields = ('title', 'date_posted')
#    fields = ('title', 'file', 'link', 'content', 'date_posted')

@admin.register(DepedOrder)
class DepedOrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'get_month_name', 'date_published')
    list_filter = ('year', 'month') 
    form = DepedOrderForm
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['date_published'].widget = forms.DateTimeInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            },
            format='%Y-%m-%dT%H:%M'
        )
        return form


#@admin.register(DepedAdvisories)
#class DepedAdvisoriesAdmin(admin.ModelAdmin):
#    list_display = ('title', 'file', 'link', 'content',)
#    search_fields = ('title', 'date_posted')
#    fields = ('title', 'file', 'link', 'content', 'date_posted')

@admin.register(DepedAdvisories)
class DepedAdvisoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'get_month_name', 'date_published')
    list_filter = ('year', 'month') 
    form = DepedAdvisoriesForm
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['date_published'].widget = forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            },
            format='%Y-%m-%dT%H:%M'
        )
        return form






@admin.register(AwardsNotice)
class AwardsNoticeAdmin(admin.ModelAdmin):
    list_display = ('projectname', 'awardee', 'abc', 'contractamount', 'dateawarded', 'has_link', 'has_file')
    search_fields = ('projectname', 'awardee', 'date_published')
    list_filter = ('dateawarded',)
    fields = ('projectname', 'abc', 'awardee', 'contractamount', 'dateawarded', 'abstract', 'link', 'file', 'date_posted')
    
    def has_link(self, obj):
        return bool(obj.link)
    has_link.boolean = True
    
    def has_file(self, obj):
        return bool(obj.file)
    has_file.boolean = True
    has_file.short_description = 'Has File'

@admin.register(BidOpportunities)
class BidOpportunitiesAdmin(admin.ModelAdmin):
    list_display = ('projectname', 'ref', 'abc', 'link', 'file')
    search_fields = ('projectname', 'ref', 'date_published')
    fields = ('projectname', 'ref', 'abc', 'date_published', 'link', 'file')
    
    def has_link(self, obj):
        return bool(obj.link)
    has_link.boolean = True
    has_link.short_description = 'Has Link?'
    
    def has_file(self, obj):
        return bool(obj.file)
    has_file.boolean = True
    has_file.short_description = 'Has File'




@admin.register(RewardsRecognitions)
class RewardsRecognitionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'has_file', 'has_link')
    search_fields = ('title', 'date_published')
    list_filter = ('title',)
    fields = ('title', 'file', 'link', 'date_published')
    
    def has_file(self, obj):
        return bool(obj.file)
    has_file.boolean = True
    has_file.short_description = 'Has File?'
    
    def has_link(self, obj):
        return bool(obj.link)
    has_link.boolean = True
    has_link.short_description = 'Has Link?'

@admin.register(RecruitmentSelectionPlacement)
class RecruitmentSelectionPlacementAdmin(admin.ModelAdmin):
    list_display = ('title', 'has_file', 'has_link')
    search_fields = ('title',  'date_published')
    list_filter = ('title',)
    fields = ('title',  'file', 'link', 'date_published')
    
    def has_file(self, obj):
        return bool(obj.file)
    has_file.boolean = True
    has_file.short_description = 'Has File?'
    
    def has_link(self, obj):
        return bool(obj.link)
    has_link.boolean = True

@admin.register(PerformanceManagement)
class PerformanceManagementAdmin(admin.ModelAdmin):
    list_display = ('title', 'has_file', 'has_link')
    search_fields = ('title',  'date_published')
    list_filter = ('title',)
    fields = ('title',  'file', 'link', 'date_published')
    
    
    def has_file(self, obj):
        return bool(obj.file)
    has_file.boolean = True
    has_file.short_description = 'Has File?'
    
    def has_link(self, obj):
        return bool(obj.link)
    has_link.boolean = True
    has_link.short_description = 'Has Link?'

@admin.register(LearningDevelopment)
class LearningDevelopmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'has_file', 'has_link')
    search_fields = ('title', 'date_published')
    list_filter = ('title',)
    fields = ('title',  'file', 'link', 'date_published')

    def has_file(self, obj):
        return bool(obj.file)
    has_file.boolean = True
    has_file.short_description = 'Has File?'
    
    def has_link(self, obj):
        return bool(obj.link)
    has_link.boolean = True
    has_link.short_description = 'Has Link?'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'workemail', 'organization', 'submitted_at')  
    list_filter = ('submitted_at',)
    readonly_fields = ('submitted_at',) 
    fields = ('fullname', 'workemail', 'organization', 'message', 'submitted_at') 

@admin.register(QuickLinks)
class QuickLinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'links')
    search_fields = ('name',)
    list_filter = ('date_posted',)
    readonly_fields = ('date_posted',)
    fields = ('name', 'links', 'date_posted')
    


#@admin.register(OfficeFormSurvey)
#class OfficeFormSurveyAdmin(admin.ModelAdmin):
#    list_display = ('id', 'customer_type', 'office_transacted', 'service_availed_sds', 'submission_date')
#    list_filter = ('customer_type', 'office_transacted', 'submission_date')
#    search_fields = ('remarks', 'customer_type')
#    readonly_fields = ('submission_date',)
    
#    fieldsets = (
#        ('Personal Information', {
#            'fields': ('age', 'sex', 'customer_type')
#        }),
#        ('Transaction Details', {
#            'fields': ('office_transacted', 'service_availed_sds')
#        }),
#        ('Survey Responses', {
#            'fields': ('citizens_charter', 'remarks', 'submission_date')
#        }),
#        ('Service Quality Dimensions', {
#            'fields': (('sqd1', 'sqd2', 'sqd3', 'sqd4'), 
#                      ('sqd5', 'sqd6', 'sqd7', 'sqd8')),
#            'classes': ('collapse',)
#        }),
#    )