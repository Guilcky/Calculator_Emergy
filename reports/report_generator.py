from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

class ReportGenerator:
    def generate_pdf(self, filename, total_emergy):
        doc = SimpleDocTemplate(filename, pagesize=letter)

        styles = getSampleStyleSheet()
        elements = []

        title = Paragraph("Relatório de Emergia", styles['Title'])
        elements.append(title)

        elements.append(Spacer(1, 20))

        text = Paragraph(
            f"Emergia Total Calculada: <b>{total_emergy}</b>",
            styles['BodyText']
        )

        elements.append(text)

        doc.build(elements)

        print(f"Relatório gerado: {filename}")