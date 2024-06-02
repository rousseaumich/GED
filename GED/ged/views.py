# from django.shortcuts import render

# # Create your views here.
# from rest_framework import viewsets
# from .models import User, Document, Tag, DocumentType
# from .serializers import UserSerializer,  DocumentSerializer, TagSerializer, DocumentTypeSerializer
# from .permissions import TypeUtilisateurPermission

# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    

# class DocumentViewSet(viewsets.ModelViewSet):
#     queryset = Document.objects.all()
#     serializer_class = DocumentSerializer
#     permission_classes = [TypeUtilisateurPermission]

#     def perform_create(self, serializer):
#         serializer.save(utilisateur=self.request.user)

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         if self.request.user.type_utilisateur == 'admin':
#             return queryset
#         elif self.request.user.type_utilisateur == 'secretaire':
#             return queryset.filter(utilisateur=self.request.user)
#         elif self.request.user.type_utilisateur == 'directeur_general':
#             return queryset.filter(type__in=['important', 'confidentiel'])
#         else:
#             return queryset.none()
            
# class DocumentTypeViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = DocumentType.objects.all()
#     serializer_class = DocumentTypeSerializer

#     def perform_create(self, serializer):
#         serializer.save(utilisateur=self.request.user)

# class TagViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer


# views.py
# from rest_framework import viewsets
# from .models import Document, DocumentType, Tag
# from .serializers import DocumentSerializer, DocumentTypeSerializer, TagSerializer
# from .permissions import AdminPermission, SecretaryPermission, DirectorGeneralPermission, DocumentPermission, DocumentTypePermission, TagPermission

# class DocumentViewSet(viewsets.ModelViewSet):
#     queryset = Document.objects.all()
#     serializer_class = DocumentSerializer
#     permission_classes = [AdminPermission, SecretaryPermission, DirectorGeneralPermission, DocumentPermission]

# class DocumentTypeViewSet(viewsets.ModelViewSet):
#     queryset = DocumentType.objects.all()
#     serializer_class = DocumentTypeSerializer
#     permission_classes = [AdminPermission, SecretaryPermission, DocumentTypePermission]

# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#     permission_classes = [AdminPermission, SecretaryPermission, TagPermission]

# La classe AdminPermission vérifie si l'utilisateur est membre du groupe d'administrateurs.
# La classe SecretaryPermission vérifie si l'utilisateur est membre du groupe de secrétaires.
# La classe DirectorGeneralPermission vérifie si l'utilisateur est membre du groupe de directeurs généraux.
# La classe DocumentPermission vérifie si l'utilisateur est membre du groupe de directeurs généraux pour les actions de création, mise à jour et suppression de documents.
# La classe DocumentTypePermission vérifie si l'utilisateur est membre du groupe d'administrateurs pour les actions de création, mise à jour et suppression de types de documents.
# La classe TagPermission vérifie si l'utilisateur est membre du groupe d'administrateurs pour les actions de création, mise à jour et suppression de tags.
# Les vues DocumentViewSet, DocumentTypeViewSet et TagViewSet utilisent ces autorisations pour gérer les documents, les types de documents et les tags.

###################################################################################################################################

##### Avec le Active directory ##########

# views.py
from rest_framework import viewsets
from .models import Document, DocumentType, Tag
from .serializers import DocumentSerializer, DocumentTypeSerializer, TagSerializer
from .permissions import ActiveDirectoryPermission
from rest_framework.response import Response
from rest_framework import status

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    #permission_classes = [ActiveDirectoryPermission]

    def perform_create(self, serializer):
        serializer.save(utilisateur=self.request.user)

class DocumentTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    #permission_classes = [ActiveDirectoryPermission]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    #permission_classes = [ActiveDirectoryPermission]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
