from django.contrib import admin
from .models import Document, Tag, DocumentType

admin.site.register(Document)
admin.site.register(Tag)
admin.site.register(DocumentType)

# Register your models here.
