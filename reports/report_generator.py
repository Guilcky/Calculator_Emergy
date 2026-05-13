# =====================================================
# report_generator.py
# =====================================================

import os
import tempfile

import matplotlib.pyplot as plt

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet


class ReportGenerator:

    def generate_pdf(
            self,
            filename,
            total_emergy,
            network,
            data
    ):

        # =====================================================
        # DETECTAR DESKTOP AUTOMATICAMENTE
        # =====================================================

        possible_desktops = [

            os.path.join(
                os.path.expanduser("~"),
                "Desktop"
            ),

            os.path.join(
                os.path.expanduser("~"),
                "Área de Trabalho"
            ),

            os.path.join(
                os.path.expanduser("~"),
                "OneDrive",
                "Desktop"
            ),

            os.path.join(
                os.path.expanduser("~"),
                "OneDrive",
                "Área de Trabalho"
            )
        ]

        desktop = None

        for path in possible_desktops:

            if os.path.exists(path):

                desktop = path
                break

        # =====================================================
        # FALLBACK
        # =====================================================

        if desktop is None:

            desktop = os.path.expanduser("~")

        # =====================================================
        # CRIAR PDF
        # =====================================================

        pdf_path = os.path.join(
            desktop,
            filename
        )

        doc = SimpleDocTemplate(
            pdf_path,
            pagesize=letter
        )

        styles = getSampleStyleSheet()

        elements = []

        # =====================================================
        # TÍTULO
        # =====================================================

        title = Paragraph(
            "Relatório Emergético",
            styles["Title"]
        )

        elements.append(title)

        elements.append(
            Spacer(1, 20)
        )

        # =====================================================
        # RESULTADO
        # =====================================================

        result = Paragraph(
            f"""
            <b>Emergia Total Calculada:</b>
            {round(total_emergy, 2)}
            """,
            styles["BodyText"]
        )

        elements.append(result)

        elements.append(
            Spacer(1, 20)
        )

        # =====================================================
        # GRÁFICO MENSAL
        # =====================================================

        if data is not None:

            month_totals = {}

            for _, row in data.iterrows():

                month = str(
                    row["month"]
                ).strip()

                value = float(
                    row["value"]
                )

                if month not in month_totals:

                    month_totals[month] = 0

                month_totals[month] += value

            # =====================================================
            # ORDEM DOS MESES
            # =====================================================

            month_order = [
                "Jan", "Fev", "Mar", "Abr",
                "Mai", "Jun", "Jul", "Ago",
                "Set", "Out", "Nov", "Dez"
            ]

            ordered_months = []
            ordered_values = []

            for month in month_order:

                if month in month_totals:

                    ordered_months.append(month)

                    ordered_values.append(
                        month_totals[month]
                    )

            # =====================================================
            # CRIAR GRÁFICO
            # =====================================================

            fig, ax = plt.subplots(
                figsize=(8, 4)
            )

            ax.plot(
                ordered_months,
                ordered_values,
                marker="o",
                linewidth=3
            )

            ax.fill_between(
                ordered_months,
                ordered_values,
                alpha=0.2
            )

            ax.set_title(
                "Evolução Emergética Mensal"
            )

            ax.set_xlabel("Meses")

            ax.set_ylabel("Emergia")

            ax.grid(True)

            # =====================================================
            # SALVAR IMAGEM TEMP
            # =====================================================

            temp_chart = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".png"
            )

            plt.savefig(
                temp_chart.name,
                bbox_inches="tight"
            )

            plt.close()

            # =====================================================
            # ADICIONAR GRÁFICO
            # =====================================================

            chart = Image(
                temp_chart.name,
                width=500,
                height=250
            )

            elements.append(chart)

            elements.append(
                Spacer(1, 20)
            )

        # =====================================================
        # TABELA DE DADOS
        # =====================================================

        if data is not None:

            table_data = [
                [
                    "Mês",
                    "Origem",
                    "Destino",
                    "Valor"
                ]
            ]

            for _, row in data.iterrows():

                table_data.append([

                    str(row["month"]),

                    str(row["source"]),

                    str(row["target"]),

                    str(row["value"])
                ])

            table = Table(table_data)

            table.setStyle(TableStyle([

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#2563eb")
                ),

                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),

                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.grey
                ),

                (
                    "BACKGROUND",
                    (0, 1),
                    (-1, -1),
                    colors.whitesmoke
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, 0),
                    10
                )

            ]))

            elements.append(table)

            elements.append(
                Spacer(1, 20)
            )

        # =====================================================
        # FLUXOS DE EMERGIA
        # =====================================================

        flow_title = Paragraph(
            "Fluxos Emergéticos",
            styles["Heading2"]
        )

        elements.append(flow_title)

        elements.append(
            Spacer(1, 10)
        )

        for source, target, flow in network.graph.edges(data=True):

            flow_text = Paragraph(
                f"""
                <b>{source}</b>
                → {target}
                = {flow['weight']}
                """,
                styles["BodyText"]
            )

            elements.append(flow_text)

        # =====================================================
        # GERAR PDF
        # =====================================================

        doc.build(elements)

        print(
            f"Relatório salvo em: {pdf_path}"
        )

        return pdf_path