from datetime import datetime
import json
from .models import *

def site_settings(request):
    
    context = {
        'org_chart': None,
        'citizens_charter': None,
        'mission_vision': None,
        'site_settings': {},
        'site_programs': Program.objects.none(),
        'recent_announcements': Announcement.objects.none(),
        'featured_news': News.objects.none(),
        'quick_links': [],
        'current_year': datetime.now().year,
        'site_settings': None,
    }

    try:
        context['site_settings'] = SiteSettings.objects.first() or {}
        context['org_chart'] = OrganizationalChart.objects.first()
        context['citizens_charter'] = CitizensCharter.objects.first()
        context['mission'] = Mission.objects.first()
        context['vision'] = Vision.objects.first()
        context['mandate'] = Mandate.objects.first()
        context['core_values'] = CoreValues.objects.first()
        context['site_programs'] = Program.objects.all().order_by('name')
        context['recent_announcements'] = Announcement.objects.all().order_by('-date_posted')
        context['featured_news'] = News.objects.filter(is_featured=True).order_by('-date_posted')
        context['quick_links'] = QuickLinks.objects.first()

        quick_links = {
            'Bid Opportunities': '/bid_opportunities',
            'Issuances': '/issuances',
            'Awards & Notices': '/awards_notices',
            'Contact Us': '/contact',
            'Rewards Recognitions': '/rewards_recognitions',
            'Recruitment Selection Placement': '/recruitment_selection_placement',
            'Performance Management': '/performance_management',
            'Learning and Development': '/learning_development',
            'Division Memo': '/division_memo',
            'Quick Links': 'quick_links',
        }
        
        if context['site_settings'].quick_links_json:
            try:
                custom_links = json.loads(context['site_settings'].quick_links_json)
                quick_links.update(custom_links)
            except json.JSONDecodeError:
                pass
                
        context['quick_links'] = quick_links

    except Exception as e:
        pass
    
    return context