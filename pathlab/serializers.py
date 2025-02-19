from rest_framework import serializers
from database.models import *

class GetCitizenBasicDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = familyMembers
        fields = ('id','memberId' , 'name', 'gender', 'age' , 'mobileNo' , 'aadharCard' , 'abhaId' , 
                  'isLabTestAdded' , 'isSampleCollected' , 'isLabTestReportGenerated' , 'area' , 'bloodCollectionLocation' )


class GetPhleboFamilyMemberDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = familyMembers
        fields = '__all__'


# class PostBloodTestReportSerialzier(serializers.ModelSerializer):
#     # barcodeNumber = serializers.CharField(max_length = 50 , required = False) 
#     barcodeNumber =  serializers.ListField(child=serializers.CharField(max_length = 50 , required = False) , required = False )
#     class Meta:
#         model = phlebotomist
#         fields = ('member','testReport', 'barcodeNumber', 'date')


#     def create(self , data):
#         TestTubes = data.pop('barcodeNumber')
#         list = TestTubes[0].split(',')
#         object = phlebotomist.objects.create(**data)
#         for barcode in list:
#             testtube_object = TestTube.objects.create( phlebo = object , barcodeNumber = barcode)
#         return data


class PostResponseLIMSAPISerialzier(serializers.ModelSerializer):
    LabTestSuggested = serializers.ListField(write_only=True , required = True)
    class Meta:
        model = PatientPathlab
        fields = ( 'patientFamilyMember' ,'CentreID' , 'bookingVisitID' , 'puid' , 'patientID' , 'LabTestSuggested' )


class GetPatientsDetailsAPISerialzier(serializers.ModelSerializer):
    class Meta:
        model = PatientPathlab
        fields = '__all__'
        # depth = 1 