from rest_framework.permissions import BasePermission
from datetime import date

class IsBookingOwner(BasePermission):
    message = "You must be the owner of this booking."

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user

class IsOverThreeDays(BasePermission):
    message = "Only bookings that are in more than 3 days of scheduled departure can be updated/deleted."

    def has_object_permission(self, request, view, obj):
        return ((obj.date - date.today()).days) > 3