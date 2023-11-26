from rest_framework import serializers

from .models import Registrant

class AddRegistrantSerializer(serializers.ModelSerializer):
      class Meta:
          fields = ('id','name','mobileno','email','address', 'photoFile', 'signatureFile')
          model = Registrant

      def create(self, validated_data):
          print ("val_data: ", validated_data)
          #photoFile = validated_data.pop('photoFile', None)
          #readingTestObj = ReadingTest.objects.get(pk=int(readingTestId));
          newMember = Registrant.objects.create(**validated_data)
          newMember.save()
          return newMember;
