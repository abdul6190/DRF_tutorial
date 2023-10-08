from .models import Course
from .serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class CourseViewList(APIView):
    def get(self,req):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,req):
        serializer = CourseSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
     
class CourseViewDetails(APIView):
    def get_course(self, id):
        try:
            return Course.objects.get(id=id)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, req, id):
        course = self.get_course(id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def put(self, req, id):
        course = self.get_course(id)
        serializer = CourseSerializer(course, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, req, id):
        course = self.get_course(id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            