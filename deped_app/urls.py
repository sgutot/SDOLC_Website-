from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('programs/', views.program_list, name='program_list'),
    path('programs/<int:pk>/', views.program_detail, name='program_detail'),

    path('search/', views.search, name='search'),

    path('awards/', views.awards, name='awards'),

    path('news/', views.news_list, name='news_list'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),

    path('announcements/', views.announcements_list, name='announcements_list'),
    path('announcements/<int:pk>/', views.announcement_detail, name='announcement_detail'),

    path('about/vision_mission_core_values_mandate_quality_policy/', views.vision_mission_core_values_mandate_quality_policy, name='vision_mission_core_values_mandate_quality_policy'),

    path('about/vision/', views.vision, name='vision_list'),  

    path('about/mandate/', views.mandate, name='mandate_list'),  

    path('about/core_values/', views.core_values, name='core_values'),

    path('about/citizens-charter/', views.citizens_charter, name='citizens_charter'),
    path('about/citizens-charter/<int:pk>/', views.citizens_charter_detail, name='citizens_charter_detail'),

    path('about/organizational-chart/', views.organizational_chart, name='organizational_chart'),

    #path('issuances/regional-memo/', views.regional_memo_list, name='regional_memo_list'),
    #path('issuances/regional-memo/<int:pk>/', views.regional_memo_detail, name='regional_memo_detail'),
    
    #Division Memo
    path('issuances/division-memo/', views.division_memo_list, name='division_memo_list'),
    path('issuances/division-memo/<int:pk>/', views.division_memo_detail, name='division_memo_detail'),

    #Office Memo
    path('issuances/office-memo/', views.office_memo_list, name='office_memo_list'),
    path('issuances/office-memo/<int:pk>/', views.office_memo_detail, name='office_memo_detail'),

    ##Deped Order
    path('issuances/deped-order/', views.deped_order_list, name='deped_order_list'),
    path('issuances/deped-order/<int:pk>/', views.deped_order_detail, name='deped_order_detail'),

    #Deped Advisories 
    path('issuances/deped-advisories/', views.deped_advisories_list, name='deped_advisories_list'),
    path('issuances/deped-advisories/<int:pk>/', views.deped_advisories_detail, name='deped_advisories_detail'),

    #Bid Opportunities
    path('procurements/bid-opportunities/', views.bid_opportunities, name='bid_opportunities'),
    path('procurements/bid-opportunities/<int:pk>/', views.bid_opportunity_detail, name='bid_opportunity_detail'),

    #Awards Notices
    path('procurements/awards-notices/', views.awards_notices, name='awards_notices'),
    path('procurements/awards-notices/<int:pk>/', views.awards_notices_detail, name='awards_notices_detail'),

    #Learning Development
    path('primehrm/rewards-recognitions/', views.rewards_recognitions, name='rewards_recognitions'),
    path('primehrm/rewards-recognitions/<int:pk>/', views.rewards_recognitions_detail, name='rewards_recognitions_detail'),

    #Recruitment Selection Placement
    path('primehrm/recruitment-selection-placement/', views.recruitment_selection_placement, name='recruitment_selection_placement'),
    path('primehrm/recruitment-selection-placement/<int:pk>/', views.recruitment_selection_placement_detail, name='recruitment_selection_placement_detail'),

    #Performance and Management
    path('primehrm/performance-management/', views.performance_management, name='performance_management'),
    path('primehrm/performance-management/<int:pk>/', views.performance_management_detail, name='performance_management_detail'),

    #Learning and Development
    path('primehrm/learning_development/', views.learning_development, name='learning_development'),
    path('primehrm/learning_development/<int:pk>/', views.learning_development_detail, name='learning_development_detail'),

    path('contact/', views.contact, name='contact'),

    path('survey/', views.survey_form, name='survey_form'),
    path('survey/thank-you/', views.survey_thank_you, name='survey_thank_you'),
]