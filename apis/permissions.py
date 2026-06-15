from rest_framewort.permissions import BasePermission


class IsMedecin(BasePermission):
    def has_permission(self, request, view):
     return request.user.groups.filter(name='Medecin').exists()




class IsReceptionniste(BasePermission):
    def has_permission(self, request, view):
     return request.user.groups.filter(name='Receptionniste').exists()




class IsComptable(BasePermission):
    def has_permission(self, request, view):
     return request.user.groups.filter(name='Comptable').exists()