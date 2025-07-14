from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
import json

class SiteSettings(models.Model):
    site_name = models.CharField(default='DEPED', null=True, blank=True)
    site_logo = models.ImageField(upload_to='site/', null=True, blank=True)
    contact_email = models.EmailField(default='info@deped.gov.ph')
    contact_phone = models.CharField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    quick_links_json = models.TextField(null=True, blank=True,default='{}',help_text='JSON format for quick links. Example: {"Bid Opportunities": "/bid-opportunities"}')
    
    class Meta:
        verbose_name_plural = "Site Settings"
    
    def save(self, *args, **kwargs):
        if self.quick_links_json:
            try:
                json.loads(self.quick_links_json)
            except ValueError:
                raise ValueError("Invalid JSON format for quick links")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.site_name
    
class VideosCitizensCharter(models.Model):
    caption = models.CharField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to='videos/%y', null=True, blank=True)
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return self.caption
    
class Videos(models.Model):
    caption = models.CharField(null=True, blank=True)
    video = models.FileField(upload_to='videos/%y', null=True, blank=True)
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return self.caption
    
    

class Awards(models.Model):
    title = models.CharField(null=True, blank=True)
    image = models.ImageField(upload_to='awards_image', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    file = models.FileField(help_text="PDF file only", upload_to='awards_file', null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title  if self.title else "Untitled"
    
    class Meta:
        verbose_name = "Awards"
        verbose_name_plural = "Awards"
        ordering = ['-date_posted']


class News(models.Model):
    title = models.CharField(null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, editable=True)  
    content = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='news_image', null=True, blank=True)
    file = models.FileField(help_text="PDF file only", upload_to='news_files/', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ['-date_posted']
    


class Program(models.Model):
    name = models.CharField(null=True, blank=True)
    image = models.ImageField(upload_to='program_image', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    file = models.FileField(help_text="PDF file only", upload_to='program_files/', null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name  if self.name else "Untitled"
    
    class Meta:
        verbose_name = "Program"
        verbose_name_plural = "Program"
        ordering = ['-date_posted']


class Announcement(models.Model):
    title = models.CharField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    file = models.FileField(help_text="PDF file only", upload_to='announcement_files/', null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
       return self.title  if self.title else "Untitled"
    
    class Meta:
        verbose_name = "Announcement"
        verbose_name_plural = "Announcement"
        ordering = ['-date_posted']




#Organizational Chart
class OrganizationalChart(models.Model):
    MANAGEMENT_CHOICES = [
        ('OSDS', 'Office of the Schools Division Superintendent'),
        ('ADMIN', 'Administrative Section'),
        ('GENERAL', 'General Service'),
        ('FINANCE', 'Finance'),
        ('CID', 'Curriculum Implementation Division'),
        ('ALS', 'Alternative Learning System'),
        ('SGOD', 'School Governance and Operations Division'),
    ]

    POSITION_PRIORITY = {
    'Schools Division Superintendent': 1,
    'Assistant Schools Division Superintendent': 2,

    'Chief Education Supervisor': 3,
    'Education Program Supervisor': 4,

    'Senior Education Program Specialist': 5,
    'Education Program Specialist VI': 6,
    'Education Program Specialist V': 7,
    'Education Program Specialist IV': 8,
    'Education Program Specialist III': 9,
    'Education Program Specialist II': 10,
    'Education Program Specialist I': 11,

    'Teacher VI': 12,
    'Teacher V': 13,
    'Teacher IV': 14,
    'Teacher III': 15,
    'Teacher II': 16,
    'Teacher I': 17,

    'DepEd Architect': 18,
    'Medical Officer III': 19,
    'Dentist II': 20,
    'Nurse II': 21,
    'Information Technology Officer I': 22,
    'Planning Officer III': 23,
    'Project Development Officer II': 24,

    'Administrative Officer VI': 25,
    'Administrative Officer V': 26,
    'Administrative Officer IV': 27,
    'Administrative Officer III': 28,
    'Administrative Officer II': 29,
    'Administrative Officer I': 30,

    'Administrative Assistant VI': 31,
    'Administrative Assistant V': 32,
    'Administrative Assistant IV': 33,
    'Administrative Assistant III': 34,
    'Administrative Assistant II': 35,
    'Administrative Assistant I': 36,

    'Administrative Aide VI': 37,
    'Administrative Aide V': 38,
    'Administrative Aide IV': 39,
    'Administrative Aide III': 40,
    'Administrative Aide II': 41,
    'Administrative Aide I': 42,

    'School Management, Monitoring & Evaluation Section (SMME)': 43,
}
    management = models.CharField(choices=MANAGEMENT_CHOICES, blank=True, null=True,verbose_name="Department")
    positions = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    image = models.ImageField(upload_to='orgchart_images/', blank=True, null=True)
    contact = models.CharField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True, help_text="Automatically set based on position hierarchy")
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.get_management_display()}" if self.name else "Untitled"

    def save(self, *args, **kwargs):
        """Auto-set priority based on position when saving"""
        self.priority = self.POSITION_PRIORITY.get(self.positions, 99)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Organizational Charts"
        ordering = ['management', 'priority', 'name']
        indexes = [
            models.Index(fields=['management']),
            models.Index(fields=['positions']),
            models.Index(fields=['priority']),
        ] 

class OrgChartWhole(models.Model):
    org_chart_image = models.ImageField(upload_to='orgchart_images/', blank=True, null=True)
    date_posted = models.DateField(default=timezone.now)
    
class CitizensCharter(models.Model):
    title = models.CharField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    file = models.FileField(help_text="PDF file only", upload_to='', null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title  if self.title else "Untitled"
    
    class Meta:
        verbose_name = "Citizens Charter"
        verbose_name_plural = "Citizens Charter"

class Mission(models.Model):
    title = models.CharField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    file = models.FileField(help_text="PDF file only", upload_to='mvmcv_files/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title  if self.title else "Untitled"
    
    class Meta:
        verbose_name = "Mission"
        verbose_name_plural = "Mission"
        ordering = ['-date_posted']
    
class Vision(models.Model):
    title = models.CharField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    file = models.FileField(help_text="PDF file only", upload_to='mvmcv_files/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title  if self.title else "Untitled"
    
    class Meta:
        verbose_name = "Vision"
        verbose_name_plural = "Vision"
        ordering = ['-date_posted']
    
class Mandate(models.Model):
    title = models.CharField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    file = models.FileField(help_text="PDF file only", upload_to='mvmcv_files/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title  if self.title else "Untitled"
    
    class Meta:
        verbose_name = "Mandate"
        verbose_name_plural = "Mandate"
        ordering = ['-date_posted']

class CoreValues(models.Model):
    title = models.CharField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    file = models.FileField(help_text="PDF file only", upload_to='mvmcv_files/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title  if self.title else "Untitled"
    
    class Meta:
        verbose_name = "Core Values"
        verbose_name_plural = "Core Values"
        ordering = ['-date_posted']
    
class QualityPolicy(models.Model):
    title = models.CharField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    file = models.FileField(help_text="PDF file only", upload_to='qualitypolicy_files/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
       return self.title  if self.title else "Untitled"
    
    class Meta:
        verbose_name = "Quality Policy"
        verbose_name_plural = "Quality Policy"
        ordering = ['-date_posted']
    

    
#class RegionalMemo(models.Model):
#    title = models.CharField(null=True, blank=True)
#    content = models.CharField(null=True, blank=True)
#    link = models.URLField(null=True, blank=True)
#    file = models.FileField(upload_to='regionalmemo/', null=True, blank=True)
#    date_posted = models.DateInput(default=timezone.now)

#    def __str__(self):
#       return self.title  if self.title else "Untitled"
    
#    class Meta:
#        verbose_name = "Regional Memo"
#        verbose_name_plural = "Regional Memo"
#        ordering = ['-date_posted']

from django.core.exceptions import ValidationError

class BaseDocumentModel(models.Model):
    YEAR_CHOICES = [(y, y) for y in range(2000, 2050)]
    MONTH_CHOICES = [
        (1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'),
        (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'),
        (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')
    ]
    
    year = models.IntegerField(choices=YEAR_CHOICES, default=timezone.now().year)
    month = models.IntegerField(choices=MONTH_CHOICES, default=1)
    
    class Meta:
        abstract = True

    def clean(self):
        super().clean()
        if not self.year:
            raise ValidationError("Year is required")
        if not self.month:
            raise ValidationError("Month is required")
        
        

#class YearMonthFileStorage(FileSystemStorage):
#    def get_upload_path(self, instance, filename):
#        if hasattr(instance, 'year') and hasattr(instance, 'month'):
#            return os.path.join(
#                super().get_upload_path(instance, filename),
#                str(instance.year),
#                str(instance.month),
#                filename
#            )
#        return super().get_upload_path(instance, filename)

#file = models.FileField(help_text="PDF file only", upload_to='divisionmemo/', null=True, blank=True, storage=YearMonthFileStorage(),
#file = models.FileField(help_text="PDF file only", upload_to='divisionmemo/', null=True, blank=True, storage=YearMonthFileStorage(),
#file = models.FileField(help_text="PDF file only", upload_to='divisionmemo/', null=True, blank=True, storage=YearMonthFileStorage(),
#file = models.FileField(help_text="PDF file only", upload_to='divisionmemo/', null=True, blank=True, storage=YearMonthFileStorage(),
#)

from django.core.files.storage import FileSystemStorage
import os

class YearMonthFileStorage(FileSystemStorage):
    def get_valid_name(self, name):
        return super().get_valid_name(name)
    
    def get_available_name(self, name, max_length=None):
        return super().get_available_name(name, max_length)
    
    def _save(self, name, title):
        # Extract year and month from the model instance
        if hasattr(title, 'instance'):
            instance = title.instance
            if hasattr(instance, 'year') and hasattr(instance, 'month'):
                path_parts = name.split('/')
                filename = path_parts[-1]
                new_path = os.path.join(
                    '/'.join(path_parts[:-1]),  # Original path
                    str(instance.year),
                    str(instance.month).zfill(2),  # Ensure 2-digit month
                    filename
                )
                name = new_path
        return super()._save(name, title)


#class DivisionMemo(models.Model):
#    title = models.CharField(null=True, blank=True)
#    link = models.URLField(null=True, blank=True)
#    file = models.FileField(help_text="PDF file only", upload_to='divisionmemo/', null=True, blank=True)
#    date_posted = models.DateField(default=timezone.now)

#    def __str__(self):
#        return self.title  if self.title else "Untitled"
    
#    class Meta:
#        verbose_name = "Division Memo"
#        verbose_name_plural = "Division Memo"
#        ordering = ['-date_posted']


class DivisionMemo(BaseDocumentModel):
    title = models.CharField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    file = models.FileField(help_text="PDF file only", upload_to='divisionmemo/', storage=YearMonthFileStorage())
    date_published = models.DateField(default=timezone.now)

    def get_month_name(self):
        """Returns the full month name for the memo's month number."""
        month_names = {
            1: 'January', 2: 'February', 3: 'March', 4: 'April',
            5: 'May', 6: 'June', 7: 'July', 8: 'August',
            9: 'September', 10: 'October', 11: 'November', 12: 'December'
        }
        return month_names.get(self.month, '')
    
    def clean(self):
        super().clean()
        # Ensure date_published is a datetime object
        if isinstance(self.date_published, str):
            from django.utils.dateparse import parse_datetime
            parsed = parse_datetime(self.date_published)
            if parsed:
                self.date_published = parsed
    
    
#class OfficeMemo(models.Model):
#    title = models.CharField(null=True, blank=True)
#    content = models.TextField(null=True, blank=True)
#    link = models.URLField(null=True, blank=True)
#    file = models.FileField(help_text="PDF file only", upload_to='officememo/', null=True, blank=True)
#    date_posted = models.DateField(default=timezone.now)

#    def __str__(self):
#        return self.title  if self.title else "Untitled"
    
#    class Meta:
#        verbose_name = "Office Memo"
#        verbose_name_plural = "Office Memo"
#        ordering = ['-date_posted']


class OfficeMemo(BaseDocumentModel):
    title = models.CharField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    file = models.FileField(help_text="PDF file only", upload_to='officememo/', storage=YearMonthFileStorage())
    date_published = models.DateField(default=timezone.now)

    def get_month_name(self):
        """Returns the full month name for the memo's month number."""
        month_names = {
            1: 'January', 2: 'February', 3: 'March', 4: 'April',
            5: 'May', 6: 'June', 7: 'July', 8: 'August',
            9: 'September', 10: 'October', 11: 'November', 12: 'December'
        }
        return month_names.get(self.month, '')
    
    def clean(self):
        super().clean()
        if isinstance(self.date_published, str):
            from django.utils.dateparse import parse_datetime
            parsed = parse_datetime(self.date_published)
            if parsed:
                self.date_published = parsed
    
#class DepedOrder(models.Model):
#    title = models.CharField(null=True, blank=True)
#    content = models.TextField(null=True, blank=True)
#    link = models.URLField(null=True, blank=True)
#    file = models.FileField(help_text="PDF file only", upload_to='depedorder/', null=True, blank=True)
#    date_posted = models.DateField(default=timezone.now)

#    def __str__(self):
#       return self.title  if self.title else "Untitled"
    
#    class Meta:
#        verbose_name = "Deped Order"
#        verbose_name_plural = "Deped Order"
#        ordering = ['-date_posted']

class DepedOrder(BaseDocumentModel):
    title = models.CharField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    file = models.FileField(help_text="PDF file only", upload_to='depedorder/', storage=YearMonthFileStorage())
    date_published = models.DateField(default=timezone.now)

    def get_month_name(self):
        """Returns the full month name for the memo's month number."""
        month_names = {
            1: 'January', 2: 'February', 3: 'March', 4: 'April',
            5: 'May', 6: 'June', 7: 'July', 8: 'August',
            9: 'September', 10: 'October', 11: 'November', 12: 'December'
        }
        return month_names.get(self.month, '')
    
    def clean(self):
        super().clean()
        if isinstance(self.date_published, str):
            from django.utils.dateparse import parse_datetime
            parsed = parse_datetime(self.date_published)
            if parsed:
                self.date_published = parsed
    
#class DepedAdvisories(models.Model):
#    title = models.CharField(null=True, blank=True)
#    content = models.TextField(null=True, blank=True, help_text="Bold Text: <strong> content... </strong> or <b> content.. </b> | Italicize: <em> content... </em> | <big> content.. </big>]")
#    link = models.URLField(null=True, blank=True)
#    file = models.FileField(help_text="PDF file only", upload_to='depedadvisories/', null=True, blank=True)
#    date_posted = models.DateField(default=timezone.now)

#    def __str__(self):
#        return self.title  if self.title else "Untitled"
    
#    class Meta:
#        verbose_name = "Deped Advisories"
#        verbose_name_plural = "Deped Advisories"
#        ordering = ['-date_posted']


class DepedAdvisories(BaseDocumentModel):
    title = models.CharField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    file = models.FileField(help_text="PDF file only", upload_to='depedadvisories/', storage=YearMonthFileStorage())
    date_published = models.DateField(default=timezone.now)

    def get_month_name(self):
        """Returns the full month name for the memo's month number."""
        month_names = {
            1: 'January', 2: 'February', 3: 'March', 4: 'April',
            5: 'May', 6: 'June', 7: 'July', 8: 'August',
            9: 'September', 10: 'October', 11: 'November', 12: 'December'
        }
        return month_names.get(self.month, '')
    
    def clean(self):
        super().clean()
        if isinstance(self.date_published, str):
            from django.utils.dateparse import parse_datetime
            parsed = parse_datetime(self.date_published)
            if parsed:
                self.date_published = parsed

    
    

    
class BidOpportunities(models.Model):
    projectname = models.CharField(null=True, blank=True)
    ref = models.IntegerField(null=True, blank=True)  
    abc = models.CharField(null=True, blank=True)  
    date_published = models.DateField(default=timezone.now)
    link = models.URLField(null=True, blank=True, verbose_name="Online Link")
    file = models.FileField(help_text="PDF file only", upload_to='bid_opportunities/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return  f"{self.ref} - {self.projectname}"

    class Meta:
        verbose_name = "Bid Opportunity"
        verbose_name_plural = "Bid Opportunities"
        ordering = ['-date_published']
    
class AwardsNotice(models.Model):
    projectname = models.CharField(null=True, blank=True)
    abc = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    awardee = models.CharField(null=True, blank=True)
    contractamount = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    dateawarded = models.DateField(null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    file = models.FileField(help_text="PDF file only", upload_to='awards_notices/%Y/%m/%d/', null=True, blank=True)  
    date_published = models.DateField(default=timezone.now)

    def __str__(self):
        return self.projectname if self.projectname else "Untitled"
    
    class Meta:
        verbose_name = "Learning and Development"
        verbose_name_plural = "Learning and Development"
        ordering = ['-date_published']
    



class RewardsRecognitions(models.Model):
    title = models.CharField(null=True, blank=True)
    file = models.FileField(upload_to='rewards_recognitions/%Y/%m/%d/')
    link = models.URLField(null=True, blank=True)
    date_published = models.DateField(default=timezone.now)
    
    def __str__(self):
         return self.title  if self.title else "Untitled"
    
    class Meta:
        verbose_name = "Rewards & Recognition"
        verbose_name_plural = "Rewards & Recognitions"
        ordering = ['-date_published']


class RecruitmentSelectionPlacement(models.Model):
    title = models.CharField(null=True, blank=True)
    file = models.FileField(help_text="PDF file only", upload_to='primehrm/%Y/%m/%d/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    date_published = models.DateField(default=timezone.now)
    
    
    def __str__(self):
         return self.title  if self.title else "Untitled"
    
    class Meta:
        verbose_name = "Recruitment Selection Placement"
        verbose_name_plural = "Recruitment Selection Placement"
        ordering = ['-date_published']

class PerformanceManagement(models.Model):
    title = models.CharField(null=True, blank=True)
    file = models.FileField(help_text="PDF file only", upload_to='performance_management/%Y/%m/%d/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    date_published = models.DateField(default=timezone.now)
    
    def __str__(self):
         return self.title  if self.title else "Untitled"
    
    class Meta:
        verbose_name = "Performance Management"
        verbose_name_plural = "Performance Management"
        ordering = ['-date_published']

class LearningDevelopment(models.Model):
    title = models.CharField(null=True, blank=True)
    file = models.FileField(help_text="PDF file only", upload_to='learning_development/%Y/%m/%d/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    date_published = models.DateField(default=timezone.now)
    
    def __str__(self):
         return self.title  if self.title else "Untitled"
    
    class Meta:
        verbose_name = "Learning and Development"
        verbose_name_plural = "Learning and Development"
        ordering = ['-date_published']


    
class Contact(models.Model):
    fullname = models.CharField()
    workemail = models.EmailField()
    organization = models.CharField(help_text="School or company name")
    message = models.TextField(help_text="Tell us more about your needs and timeline")
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname} - {self.workemail}" if f"{self.fullname} - {self.workemail}" else "Untitled"

class QuickLinks(models.Model):
    name = models.CharField(null=True, blank=True)
    links = models.URLField(null=True, blank=True)
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
         return self.name  if self.name else "Untitled"
    
    class Meta:
        verbose_name_plural = "Quick Links"
        ordering = ['-date_posted']



#from django.core.validators import MinValueValidator, MaxValueValidator


#class OfficeFormSurvey(models.Model):
#    SEX_CHOICES = [
#        ('F', 'Female'),
#        ('M', 'Male'),
#    ]

#    CUSTOMER_TYPE = [
#        ('Business', 'Business (private school, corporations, etc.)'),
#        ('Citizen', 'Citizen (general public, learners, parents, former DepEd employees, researchers, NGOs etc.)'),
#        ('Government Government', 'Government Government (current DepEd employees or employees of other government agencies & LGUs)')
#    ]

#    SDS = [
#        ('SDS', 'Schools Division Superintendent'),
#        ('ASDS', 'Assistant Schools Division Superintendent'),
#        ('Admin', 'Cash, Personnel, Records, Supply, General Services, Procurement'),
#        ('CID', 'Curriculum Implementation Division'),
#        ('Finance', 'Accounting, Budget'),
#        ('ICT', 'ICT'),
#        ('Legal', 'Legal'),
#        ('SGOD', 'School Governance and Operations Division'),
#    ]

#    SERVICE_AVAILED_SDS = [
#        ('Travel Authority', 'Travel Authority'),
#        ('Other requests/inquiries', 'Other requests/inquiries'),
#        ('Feedback/Complaint', 'Feedback/Complaint'),
#    ]

#    CITIZENS_CHARTER = [
#        ('Yes', 'Yes'),
#        ('No', 'No'),
#    ]

#    SQD_CHOICES = [
#        (5, '5 (Strongly Agree)'),
#        (4, '4 (Agree)'),
#        (3, '3 (Neutral)'),
#        (2, '2 (Disagree)'),
#        (1, '1 (Strongly Disagree)'),
#    ]

#    age = models.IntegerField(
#        validators=[MinValueValidator(1), MaxValueValidator(120)]
##    )
#    sex = models.CharField(choices=SEX_CHOICES)
#    customer_type = models.CharField(choices=CUSTOMER_TYPE)
#    office_transacted = models.CharField(choices=SDS)
#    service_availed_sds = models.CharField(choices=SERVICE_AVAILED_SDS)
#    citizens_charter = models.CharField(choices=CITIZENS_CHARTER)
    
    # Service Quality Dimensions (SQD)
#    sqd1 = models.IntegerField(choices=SQD_CHOICES, default=3, verbose_name="Time spent for transaction was acceptable")
#    sqd2 = models.IntegerField(choices=SQD_CHOICES, default=3, verbose_name="Requirements and steps were clear")
#    sqd3 = models.IntegerField(choices=SQD_CHOICES, default=3, verbose_name="Staff were competent and knowledgeable")
#    sqd4 = models.IntegerField(choices=SQD_CHOICES, default=3, verbose_name="Staff were courteous and approachable")
#    sqd5 = models.IntegerField(choices=SQD_CHOICES, default=3, verbose_name="Facilities were adequate and comfortable")
#    sqd6 = models.IntegerField(choices=SQD_CHOICES, default=3, verbose_name="Overall satisfaction with the service")
#    sqd7 = models.IntegerField(choices=SQD_CHOICES, default=3, verbose_name="Would recommend this office to others")
#    sqd8 = models.IntegerField(choices=SQD_CHOICES, default=3, verbose_name="The service met my expectations")

#    remarks = models.TextField(blank=True)
#    submission_date = models.DateTimeField(auto_now_add=True)

#    def __str__(self):
#        return f"Survey #{self.id} - {self.get_customer_type_display()} (Submitted: {self.submission_date.strftime('%Y-%m-%d')})"

#    def get_average_rating(self):
#        """Calculate average of all SQD ratings"""
#        ratings = [
#            self.sqd1, self.sqd2, self.sqd3, self.sqd4,
#            self.sqd5, self.sqd6, self.sqd7, self.sqd8
#        ]
#        return round(sum(ratings) / len(ratings), 2)

#    class Meta:
#        verbose_name = "Office Form Survey"
#        verbose_name_plural = "Office Form Surveys"
#        ordering = ['-submission_date']
#        indexes = [
#            models.Index(fields=['submission_date']),
#            models.Index(fields=['office_transacted']),
#            models.Index(fields=['customer_type']),
#        ]