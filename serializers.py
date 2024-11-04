from rest_framework import serializers
from .models import deposit,createaccount
class deposit_serializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=deposit
		fields=['name','amount','accountId','date']
class createaccount_serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=createaccount
        fields=['aname','anumber','age','adate']		
