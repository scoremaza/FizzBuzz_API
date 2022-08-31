import logging
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import  FizzBuzzSerializers
from rest_framework.response import Response
from rest_framework import viewsets
from .models import FizzBuzz


logger = logging.getLogger(__name__)



class FizzBuzzViewSet(viewsets.ModelViewSet):
    
    serializer_class = FizzBuzzSerializers
    queryset = FizzBuzz.objects.all()
    
    def list(self, request):
        queryset = FizzBuzz.objects.all()
        serializer = FizzBuzzSerializers(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):

        data = request.data
        serializer = self.serializer_class(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save(useragent=request.headers['User-Agent'])
        logger.info(
            f"FizzBuzz {serializer.data.get('message')} created by {serializer.data.get('useragent')}"
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = FizzBuzz.objects.all()
        fizz_buzz = get_object_or_404(queryset, fizzbuzz_id=pk)
        serializer = FizzBuzzSerializers(fizz_buzz, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)

