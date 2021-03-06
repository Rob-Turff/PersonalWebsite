from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('portfolio', views.project_list, name='project_list'),
    path('portfolio/<int:pk>', views.project_detail, name='project_detail'),
    path('cv', views.cv_home, name='cv_home'),
    path('cv/edu/new/', views.cv_edu_new, name='edu_new'),
    path('cv/edu/<int:pk>/', views.cv_edu_edit, name='edu_edit'),
    path('cv/skills/', views.cv_skills_edit, name='skills_edit'),
    path('cv/job/new/', views.cv_job_new, name='job_new'),
    path('cv/job/<int:pk>/', views.cv_job_edit, name='job_edit'),
    path('cv/project/new/', views.cv_project_new, name='project_new'),
    path('cv/project/<int:pk>/', views.cv_project_edit, name='project_edit'),
    path('cv/additional_info/', views.cv_additional_info_edit, name='additional_info_edit'),
    path('contact', views.contact_page, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
