from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        Model=CustomUser
        fields=['bio','profile_picture','followers']
    
