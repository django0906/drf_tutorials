from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # 'GET', 'HEAD', 'OPTIONS' 중에 하나면?
        if request.method in permissions.SAFE_METHODS:
            return True
        # 그게 아니면 로그인한 유저가 작성자인지 확인
        # user instance가 같은지 비교하는 조건
        return obj.owner == request.user
