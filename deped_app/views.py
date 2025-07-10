from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.db.models import Q
from .models import *
from .forms import *
import json

def search(request):
    search_query = request.GET.get('search_query', '').strip()
    is_ajax = request.GET.get('ajax') == '1'

    if not search_query:
        if is_ajax:
            return JsonResponse({'results_html': ''})
        return render(request, 'deped_app/search.html', {'query': search_query})

    # Search across ALL models
    results = {
        'awards': Awards.objects.filter(
            Q(title__icontains=search_query)|
            Q(content__icontains=search_query) 
        ).order_by('-id'),

        'news': News.objects.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query) |
            Q(slug__icontains=search_query)  
        ).order_by('-date_posted').distinct(),

        'programs': Program.objects.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        ).order_by('-date_posted'),
        
        'announcements': Announcement.objects.filter(  
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        ).order_by('-date_posted'),

        'organizational_chart': OrganizationalChart.objects.filter(
            Q(positions__icontains=search_query) | 
            Q(name__icontains=search_query)
        ).order_by('-date_posted'),
        
        'citizens_charter': CitizensCharter.objects.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        ).order_by('-date_posted'),

        'mission': Mission.objects.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        ).order_by('-date_posted'),

        'vision': Vision.objects.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        ).order_by('-date_posted'),

        'mandate': Mandate.objects.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        ).order_by('-date_posted'),
        
        'core_values': CoreValues.objects.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        ).order_by('-date_posted'),

        'quality_policy': QualityPolicy.objects.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        ).order_by('-date_posted'),

        #'regional_memo': RegionalMemo.objects.filter(
        #    Q(title__icontains=search_query) | 
        #    Q(content__icontains=search_query)
        #).order_by('-date_posted'),

        'division_memo': DivisionMemo.objects.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        ).order_by('-date_posted'),

        'office_memo': OfficeMemo.objects.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        ).order_by('-date_posted'),

        'deped_order': DepedOrder.objects.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        ).order_by('-date_posted'),

        'deped_advisories': DepedAdvisories.objects.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        ).order_by('-date_posted'),

        'bid_opportunities': BidOpportunities.objects.filter(
            Q(projectname__icontains=search_query) | 
             Q(ref__icontains=search_query)
        ).order_by('-date_posted'),

        'awards_notices': AwardsNotice.objects.filter(
            Q(projectname__icontains=search_query) | 
            Q(abc__icontains=search_query)
        ).order_by('-date_posted'), 

        'rewards_recognitions': RewardsRecognitions.objects.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query)
        ).order_by('-id'), 

        'recruitment_selection_placement': RecruitmentSelectionPlacement.objects.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query)
        ).order_by('-id'), 

        'performance_management': PerformanceManagement.objects.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query)
        ).order_by('-id'), 

        'learning_development': LearningDevelopment.objects.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query)
        ).order_by('-id'),         
    }

    # Pagination for news
    news_paginator = Paginator(results['news'], 10)
    page_number = request.GET.get('page')
    news_page = news_paginator.get_page(page_number)

    total_results = sum(len(result_list) for result_list in results.values())

    context = {
        'query': search_query,
        'results': results,
        'news_page': news_page,  # Pass the paginated news
        'total_results': total_results,
        'is_ajax': is_ajax
    }

    if is_ajax:
        results_html = render_to_string('deped_app/includes/search_results.html', context)
        return JsonResponse({'results_html': results_html})

    return render(request, 'deped_app/search.html', context)

def validate_json(value):
    try:
        json.loads(value)
    except ValueError as e:
        raise ValidationError(f"Invalid JSON: {str(e)}")
        

def home(request):
    news = News.objects.all().order_by('-date_posted')
    recent_announcements = Announcement.objects.all().order_by('-date_posted')
    programs = Program.objects.all().order_by('-date_posted')
    videos = Videos.objects.all().order_by('date_posted')
    quick_links = QuickLinks.objects.all().order_by('date_posted')
    site_settings = SiteSettings.objects.first() 
    
    context = {
        'news': news,
        'recent_announcements': recent_announcements,
        'programs': programs,
        'videos': videos,
        'quick_links': quick_links,
        'site_settings': site_settings,
    }
    return render(request, 'deped_app/index.html', context)


def site_settings(request):
    return render(request, 'deped_app/index.html', {
        'site_settings': SiteSettings.objects.all
    })

def recent_announcements(request):
    return render(request, 'deped_app/base.html', {
        'recent_announcements': Announcement.objects.all()
    })

def announcements_list(request):
    announcements = Announcement.objects.all().order_by('-date_posted')
    return render(request, 'deped_app/announcements_list.html', {
        'announcements': announcements
    })

def announcement_detail(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    return render(request, 'deped_app/announcement_detail.html', {
        'announcement': announcement
    })

def awards(request):
    return render(request, 'deped_app/awards.html', {
        'awards': Awards.objects.all().order_by('date_posted')
    })



def program_list(request):
    search_query = request.GET.get('q', '')
    programs = Program.objects.all().order_by('-date_posted')
    
    if search_query:
        programs = programs.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    return render(request, 'deped_app/program_list.html', {
        'programs': programs,
        'search_query': search_query
    })

def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    related_programs = Program.objects.exclude(pk=pk).order_by('-date_posted')
    return render(request, 'deped_app/program_detail.html', {
        'program': program,
        'related_programs': related_programs
    })




# views.py
def news_list(request):
    search_query = request.GET.get('q', '')
    news_list = News.objects.all().order_by('-date_posted')
    
    if search_query:
        news_list = news_list.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query) |
            Q(slug__icontains=search_query)
        ).distinct()
    
    paginator = Paginator(news_list, 10)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)

    return render(request, 'deped_app/news.html', {
        'news': news,
        'search_query': search_query
    })

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    related_news = News.objects.exclude(id=news.id).order_by('-date_posted')
    
    # Check if Announcement model exists
    try:
        from django.apps import apps
        recent_announcements = []
        if apps.is_installed('your_app_name') and apps.get_model('your_app_name', 'Announcement'):
            recent_announcements = Announcement.objects.order_by('-date_posted')
    except:
        recent_announcements = []
    
    return render(request, 'deped_app/news_detail.html', {
        'news': news,
        'related_news': related_news,
        'recent_announcements': recent_announcements
    })


def organizational_chart(request):
    management_choices = OrganizationalChart.MANAGEMENT_CHOICES
    current_management = request.GET.get('dept', None)
    
    # Get all charts ordered by management, priority and name
    organizational_chart = OrganizationalChart.objects.all().order_by('management', 'priority', 'name')
    
    # Filter by management if specified
    if current_management and current_management != 'all':
        organizational_chart = organizational_chart.filter(management=current_management)
    
    # Group by management and then by position
    grouped_charts = {}
    for choice in management_choices:
        dept_charts = [chart for chart in organizational_chart if chart.management == choice[0]]
        if dept_charts:
            # Group by position within each department
            position_groups = {}
            for chart in dept_charts:
                if chart.positions not in position_groups:
                    position_groups[chart.positions] = []
                position_groups[chart.positions].append(chart)
            
            # Convert to list of tuples (position, [charts]) sorted by priority
            sorted_groups = sorted(position_groups.items(), 
                                 key=lambda x: OrganizationalChart.POSITION_PRIORITY.get(x[0], 99))
            grouped_charts[choice[1]] = sorted_groups
    
    context = {
        'management_choices': management_choices,
        'grouped_charts': grouped_charts,
        'current_management': current_management,
    }
    
    return render(request, 'deped_app/organizational_chart.html', context)


def citizens_charter(request):
    charters = CitizensCharter.objects.all()
    videos_citizens_charter = VideosCitizensCharter.objects.all().order_by('date_posted')
    return render(request, 'deped_app/citizens_charter.html', {
        'charters': charters,
        'videos_citizens_charter': videos_citizens_charter
    })

def citizens_charter_detail(request, pk):
    charter = get_object_or_404(CitizensCharter, pk=pk)
    return render(request, 'deped_app/citizens_charter_detail.html', {
        'charter': charter
    })

def vision_mission_core_values_mandate_quality_policy(request):
    context = {
        'vision': Vision.objects.all(),
        'mission': Mission.objects.all(),
        'mandate': Mandate.objects.all(),
        'core_values': CoreValues.objects.all(),
        'quality_policy': QualityPolicy.objects.all(),
    }
    return render(request, 'deped_app/vmcvm.html', context)

def vision(request):
    return render(request, 'deped_app/vmcvm.html', {
        'vision': Vision.objects.all()
    })

def mission(request):
    return render(request, 'deped_app/vmcvm.html', {
        'mission': Mission.objects.all()
    })

def mandate(request):
    return render(request, 'deped_app/vmcvm.html', {
        'Mandate': Mandate.objects.all()
    })

def core_values(request):
    return render(request, 'deped_app/vmcvm.html', {
        'core_values': CoreValues.objects.all()
    })

def quality_policy(request):
    return render(request, 'deped_app/vmcvm.html', {
        'quality_policy': QualityPolicy.objects.all()
    })




#def regional_memo_list(request):
#    return render(request, 'deped_app/regional_memo.html', {
#        'regional_memo': RegionalMemo.objects.all()
#    })

#def regional_memo_detail(request, pk): 
#    memo = get_object_or_404(RegionalMemo, pk=pk)
#    return render(request, 'deped_app/regional_memo_detail.html', {
#        'memo': memo
#    })

def division_memo_list(request):
    search_query = request.GET.get('q', '')
    division_memo = DivisionMemo.objects.all().order_by('-date_posted')
    
    if search_query:
        division_memo = division_memo.filter(
            Q(
                title__icontains=search_query) | 
            Q(content__icontains=search_query)
        )
    
    # Add pagination
    paginator = Paginator(division_memo, 10)  # Show 10 bids per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'deped_app/division_memo.html', {
        'division_memo': page_obj,
        'search_query': search_query
    })

def division_memo_detail(request, pk):
    memo = get_object_or_404(DivisionMemo, pk=pk)
    return render(request, 'deped_app/division_memo_detail.html', {
        'memo': memo
    })

def office_memo_list(request):
    search_query = request.GET.get('q', '')
    office_memo = OfficeMemo.objects.all().order_by('-date_posted')
    
    if search_query:
        office_memo = office_memo.filter(
            Q(
                title__icontains=search_query) | 
            Q(content__icontains=search_query)
        )
    
    # Add pagination
    paginator = Paginator(office_memo, 10)  # Show 10 bids per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'deped_app/office_memo.html', {
        'office_memo': page_obj,
        'search_query': search_query
    })

def office_memo_detail(request, pk):
    memo = get_object_or_404(OfficeMemo, pk=pk)
    return render(request, 'deped_app/office_memo_detail.html', {
        'memo': memo
    })

def deped_order_list(request):
    search_query = request.GET.get('q', '')
    deped_order = DepedOrder.objects.all().order_by('-date_posted')
    
    if search_query:
        deped_order = deped_order.filter(
            Q(
                title__icontains=search_query) | 
            Q(content__icontains=search_query)
        )
    
    # Add pagination
    paginator = Paginator(deped_order, 10)  # Show 10 bids per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'deped_app/deped_order.html', {
        'deped_order': page_obj,
        'search_query': search_query
    })

def deped_order_detail(request, pk):
    order = get_object_or_404(DepedOrder, pk=pk)
    return render(request, 'deped_app/deped_order_detail.html', {
        'order': order
    })

def deped_advisories_list(request):
    search_query = request.GET.get('q', '')
    deped_advisories = DepedAdvisories.objects.all().order_by('-date_posted')
    
    if search_query:
        deped_advisories = deped_advisories.filter(
            Q(
                title__icontains=search_query) | 
            Q(content__icontains=search_query)
        )
    
    # Add pagination
    paginator = Paginator(deped_advisories, 10)  # Show 10 bids per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'deped_app/deped_advisories.html', {
        'deped_advisories': page_obj,
        'search_query': search_query
    })

    

def deped_advisories_detail(request, pk):
    advisories = get_object_or_404(DepedAdvisories, pk=pk)
    return render(request, 'deped_app/deped_advisories_detail.html', {
        'advisories': advisories
    })




#def bid_opportunities(request):
#    return render(request, 'deped_app/bid_opportunities.html', {
#        'bid_opportunities': BidOpportunities.objects.all()
#    })


def bid_opportunities(request):
    search_query = request.GET.get('q', '')
    bids = BidOpportunities.objects.all().order_by('-date_posted')
    
    if search_query:
        bids = bids.filter(
            Q(
                projectname__icontains=search_query) | 
            Q(ref__icontains=search_query)
        )
    
    # Add pagination
    paginator = Paginator(bids, 10)  # Show 10 bids per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'deped_app/bid_opportunities.html', {
        'bids': page_obj,
        'search_query': search_query
    })

def bid_opportunity_detail(request, pk):
    bid = get_object_or_404(BidOpportunities, pk=pk)
    return render(request, 'deped_app/bid_opportunity_detail.html', {
        'bid': bid
    })




def awards_notices(request):
    search_query = request.GET.get('q', '')
    awards_notices = AwardsNotice.objects.all().order_by('-date_posted')
    
    if search_query:
        awards_notices = awards_notices.filter(
            Q(
                projectname__icontains=search_query) | 
            Q(awardee__icontains=search_query)
        )
    
    # Add pagination
    paginator = Paginator(awards_notices, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'deped_app/awards_notices.html', {
        'awards_notices': page_obj,
        'search_query': search_query
    })

def awards_notices_detail(request, pk):
    notices = get_object_or_404(AwardsNotice, pk=pk)
    return render(request, 'deped_app/awards_notices_detail.html', {
        'notices': notices
    })

    



def rewards_recognitions(request):
    search_query = request.GET.get('q', '')
    rewards_recognitions = RewardsRecognitions.objects.all().order_by('-date_posted')
    
    if search_query:
        rewards_recognitions = rewards_recognitions.filter(
            Q(
                title__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Add pagination
    paginator = Paginator(rewards_recognitions, 10)  # Show 10 bids per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'deped_app/rewards_recognitions.html', {
        'rewards_recognitions': page_obj,
        'search_query': search_query
    })

def rewards_recognitions_detail(request, pk):
    documents = get_object_or_404(RewardsRecognitions, pk=pk)
    return render(request, 'deped_app/rewards_recognitions_detail.html', {
        'documents': documents
    })

def recruitment_selection_placement(request):
    search_query = request.GET.get('q', '')
    recruitment_selection_placement = RecruitmentSelectionPlacement.objects.all().order_by('-date_posted')
    
    if search_query:
        recruitment_selection_placement = recruitment_selection_placement.filter(
            Q(
                title__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Add pagination
    paginator = Paginator(recruitment_selection_placement, 10)  # Show 10 bids per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'deped_app/recruitment_selection_placement.html', {
        'recruitment_selection_placement': page_obj,
        'search_query': search_query
    })


def recruitment_selection_placement_detail(request, pk):
    documents = get_object_or_404(RecruitmentSelectionPlacement, pk=pk)
    return render(request, 'deped_app/recruitment_selection_placement_detail.html', {
        'documents': documents
    })

#Performance Management
def performance_management(request):
    search_query = request.GET.get('q', '')
    performance_management = PerformanceManagement.objects.all().order_by('-date_posted')
    
    if search_query:
        performance_management = performance_management.filter(
            Q(
                title__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Add pagination
    paginator = Paginator(performance_management, 10)  # Show 10 bids per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'deped_app/performance_management.html', {
        'performance_management': page_obj,
        'search_query': search_query
    })

def performance_management_detail(request, pk):
    documents = get_object_or_404(PerformanceManagement, pk=pk)
    return render(request, 'deped_app/performance_management_detail.html', {
        'documents': documents
    })


#Learning Development
def learning_development(request):
    search_query = request.GET.get('q', '')
    learning_development = LearningDevelopment.objects.all().order_by('-date_posted')
    
    if search_query:
        learning_development = learning_development.filter(
            Q(
                title__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Add pagination
    paginator = Paginator(learning_development, 10)  # Show 10 bids per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'deped_app/learning_development.html', {
        'learning_development': page_obj,
        'search_query': search_query
    })

def learning_development_detail(request, pk):
    documents = get_object_or_404(LearningDevelopment, pk=pk)
    return render(request, 'deped_app/learning_development_detail.html', {
        'documents': documents
    })




def contact(request):
    site_settings = SiteSettings.objects.first()  # Get the first (and presumably only) settings
    form = ContactForm(request.POST or None)  # Handles both GET and POST in one line
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    
    context = {
        'site_settings': site_settings,
        'form': form,
    }
    return render(request, 'deped_app/contact.html', context)


def quick_links(request):
    return render(request, 'deped_app/index.html', {
        'quick_links': QuickLinks.objects.all()
    })
         



#def survey_form(request):
#    if request.method == 'POST':
#        form = OfficeFormSurveyForm(request.POST)
#        if form.is_valid():
#            try:
#                form.save()
#                messages.success(request, "Thank you for your feedback! Your survey has been submitted successfully.")
#                return redirect('survey_thank_you')
#            except Exception as e:
#                messages.error(request, f"There was an error submitting your survey: {str(e)}")
#        else:
#            messages.error(request, "Please correct the errors below.")
#    else:
#        form = OfficeFormSurveyForm()
    
    return render(request, 'deped_app/office_survey.html', {'form': form})

def survey_thank_you(request):
    return render(request, 'deped_app/survey_thank_you.html')


from django.http import JsonResponse
import os

def debug_env(request):
    return JsonResponse(dict(os.environ))