from django.urls import path
from .views import CourseViewList, CourseViewDetails

urlpatterns = [
    path('', CourseViewList.as_view(), name="course_list"),
    path('<int:id>/', CourseViewDetails.as_view(), name="course_view"),
]