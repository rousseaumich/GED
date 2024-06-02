# from django.db import models

# # Create your models here.
# from django.contrib.auth.models import AbstractUser, Permission, Group

# class User(AbstractUser):
#     TYPE_CHOICES = (
#         ('admin', 'Administrateur'),
#         ('secretaire', 'Secrétaire'), 
#         ('directeur_general', 'Directeur Général')
#     )
#     type_utilisateur = models.CharField(max_length=20, choices=TYPE_CHOICES)
#     user_permissions = models.ManyToManyField(
#         Permission,
#         verbose_name='user permissions',
#         blank=True,
#         help_text='Specific permissions for this user.',
#         related_name='ged_user_permissions',
#     )
#     groups = models.ManyToManyField(
#         Group,
#         verbose_name='groups',
#         blank=True,
#         help_text='The groups this user belongs to.',
#         related_name='ged_user_groups',
#     )
    

# class Document(models.Model):
#     titre = models.CharField(max_length=100)
#     fichier = models.FileField(upload_to='documents/')
#     date_creation = models.DateTimeField(auto_now_add=True)
#     date_modification = models.DateTimeField(auto_now=True)
#     utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
#     type = models.ForeignKey('DocumentType', on_delete=models.CASCADE)
#     tags = models.ManyToManyField('Tag')
    
# class DocumentType(models.Model):
#     nom = models.CharField(max_length=50)
#     dossier = models.CharField(max_length=100)

# class Tag(models.Model):
#     nom = models.CharField(max_length=50)


########################################################################################################################

##### Nouvelle application avec le active directory #####

# models.py
from django.db import models
from django.contrib.auth.models import User, AbstractUser

class User(AbstractUser):
    # Champs supplémentaires du modèle User
    pass

class Document(models.Model):
    titre = models.CharField(max_length=100)
    fichier = models.FileField(upload_to='documents/')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey('DocumentType', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return f"{self.titre} - {self.tags}"

class DocumentType(models.Model):
    nom = models.CharField(max_length=50)
    dossier = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} - {self.dossier}"

class Tag(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom}"
