from django.urls import path

from .views import PDFGenView

app_name = "pdfgenerator"

urlpatterns = [
    path("pdf-export/", PDFGenView.as_view(), name="'pdf-gen-api"),
]
