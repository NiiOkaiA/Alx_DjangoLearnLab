class AuthorSerializer(serializers.ModelSerializer)m
    class Meta:
        model=Author
        fields=['author']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['title','publication_year','author']

    def validate(self,data):
        if data['publication_year']>2025:
            raise serializers.ValidationError("Year must not be in the future")

        return data
