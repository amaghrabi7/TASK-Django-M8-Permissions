from rest_framework.permissions import BasePermission

class IsBookingOwner(BasePermission):
    message = "You must be the owner of this booking."

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user