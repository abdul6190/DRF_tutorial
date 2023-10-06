from .models import Passenger
from .serializers import PassengerSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET", "POST"])
def passenger_list(req):
    if req.method == "GET":
        passengers = Passenger.objects.all()
        serializer = PassengerSerializer(passengers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif req.method == "POST":
        serializer = PassengerSerializer(data=req.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(["GET", "PUT","DELETE"])
def passenger_details(req, id):
    try:
        passenger = Passenger.objects.get(id=id)
    except Passenger.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if req.method == "GET":
        serializer = PassengerSerializer(passenger)
        return Response(serializer.data)
    
    elif req.method == "PUT":
        serializer = PassengerSerializer(passenger, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif req.method == "DELETE":
        passenger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
    
        

