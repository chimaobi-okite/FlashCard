from rest_framework.permissions import BasePermission

class CardOwnerPermission(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        print(obj.editor)
        return request.user == obj.editor