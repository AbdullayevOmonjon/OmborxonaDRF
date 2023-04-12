from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import action
from  rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class ClintModelSetView(ModelViewSet):
  queryset=Client.objects.all()
  serializer_class=ClentSerializers
  
# class ClintAPIView(APIView):
#   def get(self,request):
#     client=Client.objects.all()
#     serializer=ClentSerializers(client,many=True)
#     return Response(serializer.data)
  
  
#   def post(self,request):
#     client=request.data
#     serializer=ClentSerializers(data=client)
#     if serializer.is_valid():
#       Client.objects.create(
#         nom=serializer.validated_data.get('ism'),
#         manzil=serializer.validated_data.get('manzil'),
#         ism=serializer.validated_data.get('ism'),
#         tel=serializer.validated_data.get('tel'),
#         qarz=serializer.validated_data.get('qarz'),
#         ombor=serializer.validated_data.get('ombor'),
#       )
#       return Response(serializer.data)
#     return Response(serializer.errors)
  
#   def put(self,request,pk):
#     client=Client.objects.get(id=pk)
#     serializer=ClentSerializers(client,data=request.data)
#     if serializer.is_valid():
#       # client.nom=serializer.validated_data.get('nom')
#       # client.ism=serializer.validated_data.get('ism'),
#       # client.tel=serializer.validated_data.get('tel'),
#       # client.qarz=serializer.validated_data.get('qarz'),
#       # client.save()
#       serializer.save()
#       return Response(serializer.data)
#     return Response(serializer.errors)
  
  
#   def delete(self,request,pk):
#     client=Client.objects.filter(id=pk).delete
#     serializer=ClentSerializers(serializer.data)
#     return Response(serializer.data)
  

class MahsulotSetview(ModelViewSet):
  permission_classes = [IsAuthenticated]
  queryset=Mahsulot.objects.all()
  serializer_class=MahsulotSerializers
  
  
  @action(detail=True,methods=['GET','POST'])
  def qoshiqcrete(self,request,pk):
    if request. method == 'POST':
      serializer=MahsulotSerializers(data=request.data)
      if serializer.is_valid():
        serializer.save(albom=Mahsulot.objects.get(id=pk))
        return Response(serializer.data)
    qoshiq=Mahsulot.objects.get(albom__id=pk)
    serializer=MahsulotSerializers(qoshiq,many=True)
    return Response(serializer.data)
  
  
  
  
  
# class OmborxonaAPIView(APIView):
#   def get(self,request):
#     ombor=Ombor.objects.all()
#     serializer=OmborSerializers(ombor,many=True)
#     return Response(serializer.data)
  
#   def post(self,request):
#     ombor=request.data
#     serializer=OmborSerializers(data=ombor)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     return Response(serializer.errors)
  
#   def put(self,request,pk):
#     ombor=Ombor.objects.get(id=pk)
#     serializer=OmborSerializers(ombor,data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     return Response(serializer.errors)
  
class OmborModelSetView(ModelViewSet):
  authentication_classes=[JWTAuthentication]
  permission_classes = [IsAuthenticated]
  queryset=Ombor.objects.all()
  serializer_class=OmborSerializers 