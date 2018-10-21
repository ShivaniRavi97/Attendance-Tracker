from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from attend.views import signin,attend
from attend.views import signout,sgpa,cgpa,task,display_attendance
from attend.views import signup,home,add_subjects, update_attendance
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/',signin),
    path('signout/',signout),
    path('signup/',signup),
    path('task/',task),
    path('attend/',attend),
    path('', home),
    path('add/', add_subjects),
    path('update/', update_attendance),
    path('display/', display_attendance),
    path('sgpa/', sgpa),
    path('cgpa/', cgpa),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 