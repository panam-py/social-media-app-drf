from rest_framework.permissions import BasePermission


class HasAccessToObject(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner != request.user:
            return False
        else:
            return True