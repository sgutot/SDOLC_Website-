from django import forms
from .models import *

class VideoForm(forms.ModelForm):
    class Meta:
        fields = ['date_posted', 'caption', 'video']
        widgets = {
            'caption': forms.TextInput(attrs={'class': 'form-control'}),
            'date_posted': forms.DateTimeInput(attrs={'class': 'form-control','type': 'datetime-local'}),
        }

class VideosCitizensCharterForm(forms.ModelForm):
    class Meta:
        models = VideosCitizensCharter
        fields = ['date_posted', 'caption', 'video', 'content']
        widgets = {
            'caption': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'date_posted': forms.DateTimeInput(attrs={'class': 'form-control','type': 'datetime-local'}),
        }

class VideosForm(forms.ModelForm):
    class Meta:
        models = Videos
        fields = ['date_posted', 'caption', 'video']
        widgets = {
            'caption': forms.TextInput(attrs={'class': 'form-control'}),
            'date_posted': forms.DateTimeInput(attrs={'class': 'form-control','type': 'datetime-local'}),
        }

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'image', 'file', 'link', 'date_posted']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Will be auto-generated if left blank'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'date_posted': forms.DateTimeInput(attrs={'class': 'form-control','type': 'datetime-local'}),
        }

class AwardsForm(forms.ModelForm):
    class Meta:
        model = Awards
        fields = ['title', 'image', 'content', 'file', 'date_posted']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'date_posted':  forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name', 'description', 'image', 'file', 'link' , 'date_posted']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'date_posted':  forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

class AnnouncementFrom(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'file', 'date_posted', 'link']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'date_posted':  forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

class OrganizationalChartForm(forms.ModelForm):
    class Meta:
        model = OrganizationalChart
        fields = ['management', 'positions', 'name', 'image', 'org_chart_image', 'contact', 'about', 'link', 'date_posted']
        widgets = {
            'management': forms.TextInput(attrs={'class': 'form-control'}),
            'positions': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'date_posted': forms.DateTimeInput(attrs={
                'class': 'form-control', 
                'type': 'datetime-local'
            }),
        }


class CitizensCharterForm(forms.ModelForm): 
    class Meta:
        model = CitizensCharter 
        fields = ['title', 'content', 'file', 'link', 'date_posted']  
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'date_posted': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
        
class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ['title', 'content', 'file', 'link', 'date_posted']  
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'date_posted':  forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

class VisionForm(forms.ModelForm):
    class Meta:
        model = Vision
        fields = ['title', 'content', 'file', 'link', 'date_posted']  
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'date_posted':  forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

class MandateForm(forms.ModelForm):
    class Meta:
        model = Mandate
        fields = ['title', 'content', 'file', 'link', 'date_posted']  
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'date_posted':  forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

class CoreValuesForm(forms.ModelForm):
    class Meta:
        model = CoreValues
        fields = ['title', 'content', 'file', 'link', 'date_posted']  
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'date_posted':  forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

class QualityPolicyForm(forms.ModelForm):
    class Meta:
        model = QualityPolicy
        fields = ['title', 'content', 'file', 'link', 'date_posted']  
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'date_posted':  forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }


        
#class RegionalMemoForm(forms.ModelForm):
#    class Meta:
#        model = RegionalMemo
#        fields = ['title', 'file', 'link', 'content', 'date_posted']
#        widgets = {
#            'title': forms.TextInput(attrs={'class': 'form-control'}),
#            'content': forms.Textarea(attrs={'class': 'form-control'}),
#            'link': forms.URLInput(attrs={'class': 'form-control'}),
#            'date_posted':  forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
#        }


class RequiredYearMonthForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['year'].required = True
        self.fields['month'].required = True
        self.fields['file'].required = False  
        
        # Add JS to the form
        self.fields['year'].widget.attrs.update({
            'onchange': 'updateFileField()'
        })
        self.fields['month'].widget.attrs.update({
            'onchange': 'updateFileField()'
        })

    def clean(self):
        cleaned_data = super().clean()
        # If both file and link are empty, raise validation error
        if not cleaned_data.get('file'):
            raise forms.ValidationError(
                "You must provide either a file upload or a link."
            )
        return cleaned_data

    class Media:
        js = ('admin/js/document_upload.js',)


#class DivisionMemoForm(forms.ModelForm):
#    class Meta:
#        model = DivisionMemo
#        fields = ['title', 'file', 'link', 'content', 'date_posted']
#        widgets = {
#            'title': forms.TextInput(attrs={'class': 'form-control'}),
#            'content': forms.Textarea(attrs={'class': 'form-control'}),
#            'link': forms.URLInput(attrs={'class': 'form-control'}),
#            'date_posted':  forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
#        }

class DivisionMemoForm(forms.ModelForm):
    date_published = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            },
            format='%Y-%m-%d'
        ),
        input_formats=['%Y-%m-%d', '%Y-%m-%d', '%Y-%m-%d']
    )
    
    class Meta:
        model = DivisionMemo
        fields = '__all__'

#class OfficeMemoForm(forms.ModelForm):
#    class Meta:
#        model = OfficeMemo
#        fields = ['title', 'file', 'link', 'content', 'date_posted']
#        widgets = {
#            'title': forms.TextInput(attrs={'class': 'form-control'}),
#            'content': forms.Textarea(attrs={'class': 'form-control'}),
#            'link': forms.URLInput(attrs={'class': 'form-control'}),
#            'date_posted':  forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
#        }

class OfficeMemoForm(forms.ModelForm):
    date_published = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            },
            format='%Y-%m-%d'
        ),
        input_formats=['%Y-%m-%d', '%Y-%m-%d', '%Y-%m-%d']
    )
    
    class Meta:
        model = OfficeMemo
        fields = '__all__'


#class DepedOrderForm(forms.ModelForm):
#    class Meta:
#        model = DepedOrder
#        fields = ['title', 'file', 'link', 'content', 'date_posted']
#        widgets = {
#            'title': forms.TextInput(attrs={'class': 'form-control'}),
#            'content': forms.Textarea(attrs={'class': 'form-control'}),
#            'link': forms.URLInput(attrs={'class': 'form-control'}),
#            'date_posted':  forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
#        }

class DepedOrderForm(forms.ModelForm):
    date_published = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            },
            format='%Y-%m-%d'
        ),
        input_formats=['%Y-%m-%d', '%Y-%m-%d', '%Y-%m-%d']
    )
    
    class Meta:
        model = DepedOrder
        fields = '__all__'

#class DepedAdvisoriesForm(forms.ModelForm):
#    class Meta:
#        model = DepedAdvisories
#        fields = ['title', 'file', 'link', 'content', 'date_posted']
#        widgets = {
#            'title': forms.TextInput(attrs={'class': 'form-control'}),
#            'content': forms.Textarea(attrs={'class': 'form-control'}),
#            'link': forms.URLInput(attrs={'class': 'form-control'}),
#            'date_posted':  forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#        }

class DepedAdvisoriesForm(forms.ModelForm):
    date_published = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            },
            format='%Y-%m-%d'
        ),
        input_formats=['%Y-%m-%d', '%Y-%m-%d', '%Y-%m-%d']
    )
    
    class Meta:
        model = DepedAdvisories
        fields = '__all__'




class BidOpportunityForm(forms.ModelForm):
    class Meta:
        model = BidOpportunities
        fields = ['projectname', 'ref', 'ref', 'link', 'date_published']
        widgets = {
            'projectname': forms.TextInput(attrs={'class': 'form-control'}),
            'ref': forms.NumberInput(attrs={'class': 'form-control'}),
            'abc': forms.NumberInput(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'date_published':  forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class AwardsNoticeForm(forms.ModelForm):
    class Meta:
        model = AwardsNotice
        fields = ['projectname', 'abc', 'awardee', 'contractamount', 'dateawarded', 'abstract', 'link', 'date_published']
        widgets = {
            'projectname': forms.TextInput(attrs={'class': 'form-control'}),
            'abc': forms.NumberInput(attrs={'class': 'form-control'}),
            'awardee': forms.TextInput(attrs={'class': 'form-control'}),
            'contractamount': forms.NumberInput(attrs={'class': 'form-control'}),
            'dateawarded': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'abstract': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'date_published':  forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }



class RewardsRecognitionsForm(forms.ModelForm):
    class Meta:
        model = RewardsRecognitions
        fields = ['title', 'file', 'link', 'date_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'date_published':  forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class RecruitmentSelectionPlacementForm(forms.ModelForm):
    class Meta:
        model = RecruitmentSelectionPlacement
        fields = ['title', 'file', 'link', 'date_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'date_published':  forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class PerformanceManagementForm(forms.ModelForm):
    class Meta:
        model = PerformanceManagement
        fields = ['title', 'file', 'link', 'date_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'date_published':  forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class LearningDevelopmentForm(forms.ModelForm):
    class Meta:
        model = LearningDevelopment
        fields = ['title', 'file', 'link', 'date_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'date_published':  forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['fullname', 'workemail', 'organization', 'message'] 
        
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'workemail': forms.EmailInput(attrs={'class': 'form-control'}),
            'organization': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }


class QuickLinksForm(forms.ModelForm):
    class Meta:
        model = QuickLinks
        fields = ['name', 'links', 'date_posted']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'links': forms.URLInput(attrs={'class': 'form-control'}),
            'date_posted': forms.DateInput(attrs={'class': 'form-control'}),
        }



#class OfficeFormSurveyForm(forms.ModelForm):
#    class Meta:
#        model = OfficeFormSurvey
#        fields = '__all__'
#        widgets = {
#            'age': forms.NumberInput(attrs={'min': 1, 'max': 120}),
#            'remarks': forms.Textarea(attrs={'rows': 3}),
#            'submission_date': forms.HiddenInput(),
#            'sex': forms.RadioSelect(),
#            'customer_type': forms.RadioSelect(),
#            'office_transacted': forms.RadioSelect(),
#            'service_availed_sds': forms.RadioSelect(),
#            'citizens_charter': forms.RadioSelect(),
#            'sqd1': forms.Select(attrs={'class': 'form-select rating-select'}),
#            'sqd2': forms.Select(attrs={'class': 'form-select rating-select'}),
#            'sqd3': forms.Select(attrs={'class': 'form-select rating-select'}),
#            'sqd4': forms.Select(attrs={'class': 'form-select rating-select'}),
#            'sqd5': forms.Select(attrs={'class': 'form-select rating-select'}),
#            'sqd6': forms.Select(attrs={'class': 'form-select rating-select'}),
#            'sqd7': forms.Select(attrs={'class': 'form-select rating-select'}),
#            'sqd8': forms.Select(attrs={'class': 'form-select rating-select'}),
#        }