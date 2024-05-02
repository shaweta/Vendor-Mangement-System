from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer,PerformanceSerializer
from datetime import datetime
from rest_framework.authentication import TokenAuthentication,BasicAuthentication
from rest_framework.authtoken.models import Token

# users=User.objects.all()
# for user in users:
#     Token.objects.get_or_create(user=user)

class VendorViewSet(viewsets.ModelViewSet):
    # authentication_classes=[TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
   

    @action(detail=True, methods=['get'])
    def performance(self, request, pk=None):
        vendor = self.get_object()
        serializer = PerformanceSerializer(vendor)
        return Response(serializer.data)

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    @action(detail=True, methods=['post'], url_path='acknowledge')
    def acknowledge_order(self, request, pk=None):
        purchase_order = self.get_object()
        if purchase_order.acknowledgment_date is not None:
            return Response({'message': 'Order already acknowledged.'}, status=status.HTTP_400_BAD_REQUEST)
        
        purchase_order.acknowledgment_date = datetime.now()
        purchase_order.save()
        
        return Response({'message': 'Purchase order acknowledged successfully.'})
    
