from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle,
    PageBreak
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

import matplotlib.pyplot as plt
import networkx as nx


class ReportGenerator:

    def generate_pdf(
            self,
            filename,
            total_emergy,
            network,
            historical_data=None
    ):

        doc = SimpleDocTemplate(
            filename,
            pagesize=letter
        )

        styles = getSampleStyleSheet()
        elements = []

        # =====================================================
        # TÍTULO
        # =====================================================

        title = Paragraph(
            "Relatório Emergético",
            styles['Title']
        )

        elements.append(title)
        elements.append(Spacer(1, 20))

        # =====================================================
        # RESUMO
        # =====================================================

        summary = Paragraph(
            f"""
            <b>Emergia Total Calculada:</b> {total_emergy}<br/><br/>
            <b>Total de Processos:</b> {len(network.graph.nodes)}<br/><br/>
            <b>Total de Fluxos:</b> {len(network.graph.edges)}
            """,
            styles['BodyText']
        )

        elements.append(summary)
        elements.append(Spacer(1, 20))

        # =====================================================
        # TABELA DE FLUXOS
        # =====================================================

        table_data = [
            ["Origem", "Destino", "Valor Emergético"]
        ]

        for source, target, data in network.graph.edges(data=True):
            table_data.append([
                source,
                target,
                data['weight']
            ])

        table = Table(table_data, colWidths=[180, 180, 120])

        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2563eb')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ]))

        elements.append(
            Paragraph(
                "Fluxos Emergéticos",
                styles['Heading2']
            )
        )

        elements.append(Spacer(1, 10))
        elements.append(table)
        elements.append(Spacer(1, 25))

        # =====================================================
        # GRÁFICO HISTÓRICO
        # =====================================================

        if historical_data:

            months = list(historical_data.keys())
            values = list(historical_data.values())

            plt.figure(figsize=(8, 4))

            plt.plot(
                months,
                values,
                marker='o'
            )

            plt.title("Comparação Emergética")
            plt.xlabel("Período")
            plt.ylabel("Emergia")
            plt.grid(True)

            chart_path = "historical_chart.png"
            plt.savefig(chart_path)
            plt.close()

            elements.append(
                Paragraph(
                    "Comparação com Períodos Anteriores",
                    styles['Heading2']
                )
            )

            elements.append(Spacer(1, 10))

            chart = Image(
                chart_path,
                width=450,
                height=250
            )

            elements.append(chart)
            elements.append(Spacer(1, 25))

        # =====================================================
        # VISUALIZAÇÃO DA REDE
        # =====================================================

        plt.figure(figsize=(8, 6))

        pos = nx.spring_layout(network.graph)

        edge_labels = nx.get_edge_attributes(
            network.graph,
            'weight'
        )

        nx.draw(
            network.graph,
            pos,
            with_labels=True,
            node_color='lightblue',
            node_size=2500,
            font_size=10,
            arrows=True
        )

        nx.draw_networkx_edge_labels(
            network.graph,
            pos,
            edge_labels=edge_labels
        )

        plt.title("Fluxo de Emergia")

        network_image = "network.png"

        plt.savefig(network_image)
        plt.close()

        elements.append(
            Paragraph(
                "Visualização da Rede Emergética",
                styles['Heading2']
            )
        )

        elements.append(Spacer(1, 10))

        network_img = Image(
            network_image,
            width=450,
            height=320
        )

        elements.append(network_img)
        elements.append(Spacer(1, 25))

        # =====================================================
        # CONCLUSÃO
        # =====================================================

        conclusion = Paragraph(
            f"""
            O sistema analisado apresentou uma emergia total
            de <b>{total_emergy}</b>, considerando todos os
            fluxos modelados na rede emergética.
            """,
            styles['BodyText']
        )

        elements.append(conclusion)

        # =====================================================
        # GERAÇÃO FINAL
        # =====================================================

        doc.build(elements)

        print(f"Relatório gerado com sucesso: {filename}")