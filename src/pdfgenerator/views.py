from io import BytesIO

from django.http import FileResponse
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate
from rest_framework import permissions, status
from rest_framework.views import APIView


class PDFGenView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):

        table_name = "sample"
        styles = getSampleStyleSheet()

        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)
        Story = []
        MyStyle = ParagraphStyle(
            "yourtitle",
            # fontName="HeiseiMin-W3",
            fontSize=16,
            parent=styles["Heading2"],
            alignment=1,
            spaceAfter=14,
        )

        p = Paragraph(table_name, MyStyle)
        Story.append(p)
        doc.build(Story)

        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename="hello.pdf")
