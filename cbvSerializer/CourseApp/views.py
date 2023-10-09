from .models import Course
from .serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics,mixins



class CourseViewList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class CourseViewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "id"


'''
class CourseViewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    def get(self, req):
        return self.list(req)
    
    def post(self, req):
        return self.create(req)


class CourseViewDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "id"
    
    def get(self, req, id):
        return self.retrieve(req, pk=id)
    
    def put(self, req, id):
        return self.update(req, pk=id)
    
    def delete(self, req, id):
        return self.destroy(req, pk=id)

'''


'''
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
'''

            