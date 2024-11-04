from rest_framework import viewsets
from .models import deposit,createaccount
from .serializers import deposit_serializers, createaccount_serializers
class depositviewset(viewsets.ModelViewSet):
	queryset=deposit.objects.all()
	serializer_class=deposit_serializers
class createaccountviewset(viewsets.ModelViewSet):
    queryset=createaccount.objects.all()
    serializer_class=createaccount_serializers	