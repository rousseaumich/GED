# from rest_framework.permissions import IsAuthenticated
# from .models import User

# class TypeUtilisateurPermission(IsAuthenticated):
#     def has_permission(self, request, view):
#         if hasattr(request.user, 'type_utilisateur'):
#             if request.user.type_utilisateur == 'admin':
#                 return True
#             elif request.user.type_utilisateur == 'secretaire':
#                 return True
#             elif request.user.type_utilisateur == 'directeur_general':
#                 return True
#         return False
    

# # permissions.py
# from rest_framework.permissions import BasePermission

# class AdminPermission(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.groups.filter(name='admin').exists()

# class SecretaryPermission(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.groups.filter(name='secretaire').exists()

# class DirectorGeneralPermission(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.groups.filter(name='directeur_general').exists()

# class DocumentPermission(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in ['GET', 'HEAD']:
#             return True
#         elif request.method in ['POST', 'PUT', 'PATCH']:
#             return request.user.groups.filter(name='directeur_general').exists()
#         else:
#             return False

# class DocumentTypePermission(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in ['GET', 'HEAD']:
#             return True
#         else:
#             return False

# class TagPermission(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in ['GET', 'HEAD']:
#             return True
#         else:
#             return False

######## Voici un exemple de code qui implémente les autorisations suivantes :
# Les administrateurs ont accès à toutes les actions.
# Les secrétaires peuvent lister et récupérer des documents.
# Les directeurs généraux peuvent lister, récupérer, créer et mettre à jour des documents.



########################################################################################################################

######## Avec le active directory #######

# # permissions.py
from rest_framework.permissions import BasePermission

class ActiveDirectoryPermission(BasePermission):
    def has_permission(self, request, view):
        # Vérifier si l'utilisateur est authentifié via Active Directory
        if not request.user.is_authenticated:
            return False
        
        # Vérifier les autorisations de l'utilisateur en fonction de son groupe
        if request.user.groups.filter(name='admin').exists():
            return True
        elif request.user.groups.filter(name='secretaire').exists():
            return view.action in ['list', 'retrieve']
        elif request.user.groups.filter(name='directeur_general').exists():
            return view.action in ['list', 'retrieve', 'create', 'update']
        else:
            return False
    
    def has_object_permission(self, request, view, obj):
        # Vérifier les autorisations de l'utilisateur sur l'objet spécifique
        if request.user.groups.filter(name='admin').exists():
            return True
        elif request.user.groups.filter(name='secretaire').exists():
            return obj.utilisateur == request.user
        elif request.user.groups.filter(name='directeur_general').exists():
            return obj.type in ['important', 'confidentiel']
        else:
            return False
