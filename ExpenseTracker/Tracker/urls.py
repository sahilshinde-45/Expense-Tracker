from django.urls import path
from .views import *
from . import views


app_name = 'Tracker'
urlpatterns = [
   path('',views.home_page,name='home'),
  
   path('historytracker/<int:id>/',views.track_history,name='historytracker'),
   path('edittracker/<int:id>/',views.edit_expenses,name='edittracker'),
   path('register/',views.register_user,name='registeruser'),
   path('login/',views.login_user,name='login'),
   path('logout/',views.logout_user,name='logout'),
   path('report/',views.report,name='report'),
   path('report-data/',views.report_data,name ='report-data'),
   path('upload/',views.upload_file,name='upload'),
  #path('conversion/',views.conversion,name='conversion'),
   path('trail/',views.trial,name='trail'),
]
