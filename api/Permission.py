from rest_framework.permissions import BasePermission

class Isowner(BasePermission):
    message = "You must be the author of this article."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.owner == request.user):
            return True
        else:
            return False