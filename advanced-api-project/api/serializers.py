class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=['author']
