from django.urls import path, include
# from .views import CourseViewList, CourseViewDetails
from rest_framework.routers import DefaultRouter
from .views import CourseViewSets


router = DefaultRouter()
router.register('',CourseViewSets)

urlpatterns = [
    path('', include(router.urls)),
]


# urlpatterns = [
#     path('', CourseViewList.as_view(), name="course_list"),
#     path('<int:id>/', CourseViewDetails.as_view(), name="course_view"),
# ]