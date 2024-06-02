# from rest_framework import serializers
# from .models import User, Document, Tag, DocumentType

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'type_utilisateur']


#     class Meta:
#         model = Document
#         fields = ['id', 'titre', 'fichier', 'date_creation', 'date_modification', 'utilisateur', 'type', 'tags']
        
# class DocumentTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DocumentType
#         fields = ['id', 'nom', 'dossier']

# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = ['id', 'nom']

# class DocumentSerializer(serializers.ModelSerializer):
#     utilisateur = serializers.StringRelatedField(read_only=True)
#     type = DocumentTypeSerializer(read_only=True)
#     tags = TagSerializer(many=True, read_only=True)


##############################################################################################################""

########### Avec l'active Directory ##########

# serializers.py
from rest_framework import serializers
from .models import Document, DocumentType, Tag

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'titre', 'fichier', 'date_creation', 'date_modification', 'utilisateur', 'type', 'tags']

class DocumentTypeSerializer(serializers.ModelSerializer):
    documents = DocumentSerializer(many=True, read_only=True, source='document_set')

    class Meta:
        model = DocumentType
        fields = ['id', 'nom', 'dossier','documents']

class TagSerializer(serializers.ModelSerializer):
   # tags = DocumentSerializer(many=True, read_only=True, source='tag_set')

    class Meta:
        model = Tag
        fields = ['id', 'nom']


