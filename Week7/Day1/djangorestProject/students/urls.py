
from django.urls import path
from .studentsapp.views import StudentList, StudentDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', StudentList.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student_detail'),
]
