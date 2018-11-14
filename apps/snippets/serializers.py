from django.contrib.auth import get_user_model

from rest_framework import serializers

from snippets.models import (
    Snippet,
)

User = get_user_model()


# UserSerializer에 대하여 여러가지 Serializer를 동시에 선언해도 됨.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
        )


class UserDetailSerializer(serializers.ModelSerializer):
    # 중복을 최대한 피함
    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + (
            'snippet_set',
        )


# ModelSerializer로 어느 model에 대해 직렬화 할것인지
# 보다 명확하게 알 수 있다(a bit more concise).
class SnippetSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    owner = UserDetailSerializer()

    class Meta:
        model = Snippet
        fields = (
            'pk',
            'owner',
            'title',
            'code',
            'linenos',
            'language',
            'style',
        )

    def create(self, validated_data):
        """
        'Snippet' 인스턴스를 생성하고,
        유효한 데이터를 받은 후 Snippet 인스턴스 리턴
        직렬화, 역직렬화
        :param validated_data:
        :return:
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        존재하는 'Snippet' 인스턴스를 업데이트하고,
        유효한 데이터를 받은 후 Snippet 인스턴스 리턴
        직렬화, 역직렬화
        :param instance:
        :param validated_data:
        :return:
        """
        instance.title = validated_data.get('title', instance.title)

        return instance

