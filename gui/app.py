# =====================================================
# app.py COMPLETO E RESPONSIVO
# COM:
# ✔ GRÁFICO DINÂMICO
# ✔ TODOS OS MESES
# ✔ RESPONSIVIDADE
# ✔ VISUAL MODERNO
# ✔ PDF COMPLETO
# ✔ TABELA NO PDF
# ✔ VISUAL PROFISSIONAL
# =====================================================

import customtkinter as ctk
from tkinter import filedialog

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from gui.styles import AppStyles

from core.config import Config
from core.lci_manager import LCIManager
from core.network_model import EmergyNetwork
from core.emergy_calculator import EmergyCalculator
from reports.report_generator import ReportGenerator

config = Config()


class EmergyApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        # =====================================================
        # CONFIG
        # =====================================================

        AppStyles.configure_theme()

        self.title(config.APP_NAME)

        self.geometry("1600x950")

        self.minsize(1400, 850)

        self.configure(
            fg_color=AppStyles.BACKGROUND
        )

        # =====================================================
        # FECHAR
        # =====================================================

        self.protocol(
            "WM_DELETE_WINDOW",
            self.on_close
        )

        # =====================================================
        # DADOS
        # =====================================================

        self.lci_manager = LCIManager()

        self.network = EmergyNetwork()

        self.total_emergy = 0

        # =====================================================
        # LAYOUT
        # =====================================================

        self.create_layout()

    # =====================================================
    # LAYOUT
    # =====================================================

    def create_layout(self):

        # =====================================================
        # SIDEBAR
        # =====================================================

        self.sidebar = ctk.CTkFrame(
            self,
            width=300,
            fg_color="#0f172a",
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        # =====================================================
        # LOGO
        # =====================================================

        self.logo = ctk.CTkLabel(
            self.sidebar,
            text="🌱 EmergyFlow",
            font=("Arial", 30, "bold"),
            text_color="white"
        )

        self.logo.pack(
            pady=(40, 30)
        )

        # =====================================================
        # MENU
        # =====================================================

        self.create_sidebar_button(
            "📂 Importar CSV",
            self.import_lci
        )

        self.create_sidebar_button(
            "⚡ Calcular Emergia",
            self.calculate_emergy
        )

        self.create_sidebar_button(
            "🌐 Visualizar Rede",
            self.show_network
        )

        self.create_sidebar_button(
            "📄 Gerar Relatório",
            self.generate_report
        )

        # =====================================================
        # MAIN
        # =====================================================

        self.main_frame = ctk.CTkFrame(
            self,
            fg_color=AppStyles.BACKGROUND
        )

        self.main_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        # =====================================================
        # HEADER
        # =====================================================

        self.header = ctk.CTkLabel(
            self.main_frame,
            text="Dashboard Emergético",
            font=("Arial", 40, "bold"),
            text_color="white"
        )

        self.header.pack(
            anchor="w",
            padx=30,
            pady=(30, 10)
        )

        # =====================================================
        # CARDS
        # =====================================================

        self.cards_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )

        self.cards_frame.pack(
            fill="x",
            padx=30,
            pady=10
        )

        self.cards_frame.grid_columnconfigure(
            (0, 1, 2),
            weight=1
        )

        self.emergy_card = self.create_card(
            self.cards_frame,
            "Emergia Total",
            "0",
            0
        )

        self.process_card = self.create_card(
            self.cards_frame,
            "Processos",
            "0",
            1
        )

        self.flow_card = self.create_card(
            self.cards_frame,
            "Fluxos",
            "0",
            2
        )

        # =====================================================
        # CONTAINER PRINCIPAL
        # =====================================================

        self.content_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )

        self.content_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

        self.content_frame.grid_columnconfigure(
            (0, 1),
            weight=1
        )

        self.content_frame.grid_rowconfigure(
            0,
            weight=1
        )

        # =====================================================
        # GRÁFICO
        # =====================================================

        self.chart_card = ctk.CTkFrame(
            self.content_frame,
            fg_color="#142038",
            corner_radius=22
        )

        self.chart_card.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        self.chart_title = ctk.CTkLabel(
            self.chart_card,
            text="📈 Evolução Emergética",
            font=("Arial", 24, "bold"),
            text_color="white"
        )

        self.chart_title.pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        self.chart_container = ctk.CTkFrame(
            self.chart_card,
            fg_color="#142038"
        )

        self.chart_container.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # =====================================================
        # TABELA
        # =====================================================

        self.table_card = ctk.CTkFrame(
            self.content_frame,
            fg_color="#142038",
            corner_radius=22
        )

        self.table_card.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(10, 0)
        )

        self.table_title = ctk.CTkLabel(
            self.table_card,
            text="📊 Distribuição dos Fluxos",
            font=("Arial", 24, "bold"),
            text_color="white"
        )

        self.table_title.pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        self.table_frame = ctk.CTkScrollableFrame(
            self.table_card,
            fg_color="#142038"
        )

        self.table_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        # =====================================================
        # RESULTADO
        # =====================================================

        self.result_label = ctk.CTkLabel(
            self.main_frame,
            text="Aguardando importação da base LCI...",
            font=("Arial", 15),
            text_color="#94a3b8"
        )

        self.result_label.pack(
            anchor="w",
            padx=35,
            pady=(0, 20)
        )

    # =====================================================
    # BOTÃO MENU
    # =====================================================

    def create_sidebar_button(self, text, command):

        button = ctk.CTkButton(
            self.sidebar,
            text=text,
            command=command,
            height=52,
            corner_radius=14,
            font=("Arial", 16, "bold")
        )

        button.pack(
            fill="x",
            padx=20,
            pady=10
        )

    # =====================================================
    # CARD
    # =====================================================

    def create_card(self, parent, title, value, column):

        card = ctk.CTkFrame(
            parent,
            fg_color="#142038",
            corner_radius=20,
            height=160
        )

        card.grid(
            row=0,
            column=column,
            padx=10,
            sticky="nsew"
        )

        title_label = ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 18),
            text_color="#94a3b8"
        )

        title_label.pack(
            anchor="w",
            padx=20,
            pady=(20, 8)
        )

        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=("Arial", 38, "bold"),
            text_color="white"
        )

        value_label.pack(
            anchor="w",
            padx=20
        )

        return value_label

    # =====================================================
    # IMPORTAR CSV
    # =====================================================

    def import_lci(self):

        file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")]
        )

        if not file_path:
            return

        success = self.lci_manager.load_csv(file_path)

        if success:

            data = self.lci_manager.get_data()

            self.network.graph.clear()

            for _, row in data.iterrows():

                source = row["source"]
                target = row["target"]
                value = float(row["value"])

                self.network.add_process(source)
                self.network.add_process(target)

                self.network.add_flow(
                    source,
                    target,
                    value
                )

            self.process_card.configure(
                text=str(
                    len(self.network.graph.nodes)
                )
            )

            self.flow_card.configure(
                text=str(
                    len(self.network.graph.edges)
                )
            )

            self.update_table(data)

            self.result_label.configure(
                text="Base LCI carregada com sucesso!"
            )

    # =====================================================
    # CALCULAR
    # =====================================================

    def calculate_emergy(self):

        calculator = EmergyCalculator(
            self.network
        )

        self.total_emergy = (
            calculator.calculate_total_emergy()
        )

        self.emergy_card.configure(
            text=str(
                round(self.total_emergy, 2)
            )
        )

        self.result_label.configure(
            text=f"Emergia total calculada: {self.total_emergy}"
        )

        self.update_history_chart()

    # =====================================================
    # TABELA
    # =====================================================

    def update_table(self, data):

        for widget in self.table_frame.winfo_children():
            widget.destroy()

        headers = [
            "Mês",
            "Origem",
            "Destino",
            "Valor"
        ]

        for col, header in enumerate(headers):

            label = ctk.CTkLabel(
                self.table_frame,
                text=header,
                font=("Arial", 15, "bold"),
                text_color="white"
            )

            label.grid(
                row=0,
                column=col,
                padx=15,
                pady=10
            )

        for i, (_, row) in enumerate(data.iterrows(), start=1):

            values = [
                row["month"],
                row["source"],
                row["target"],
                row["value"]
            ]

            for j, value in enumerate(values):

                cell = ctk.CTkLabel(
                    self.table_frame,
                    text=str(value),
                    font=("Arial", 14),
                    text_color="#cbd5e1"
                )

                cell.grid(
                    row=i,
                    column=j,
                    padx=12,
                    pady=8
                )

    # =====================================================
    # GRÁFICO
    # =====================================================

    def update_history_chart(self):

        for widget in self.chart_container.winfo_children():
            widget.destroy()

        data = self.lci_manager.get_data()

        if data is None:
            return

        month_totals = {}

        for _, row in data.iterrows():

            month = str(row["month"]).strip()

            value = float(row["value"])

            if month not in month_totals:
                month_totals[month] = 0

            month_totals[month] += value

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

        fig, ax = plt.subplots(
            figsize=(10, 5),
            dpi=100
        )

        fig.patch.set_facecolor("#142038")

        ax.set_facecolor("#142038")

        x = list(range(len(ordered_months)))

        ax.plot(
            x,
            ordered_values,
            marker="o",
            linewidth=3,
            markersize=8
        )

        ax.fill_between(
            x,
            ordered_values,
            alpha=0.2
        )

        ax.set_xticks(x)

        ax.set_xticklabels(
            ordered_months,
            color="white",
            fontsize=10
        )

        ax.tick_params(
            axis="y",
            colors="white"
        )

        ax.grid(
            True,
            linestyle="--",
            alpha=0.2
        )

        ax.set_title(
            "Evolução Emergética Mensal",
            color="white",
            fontsize=18
        )

        ax.set_xlabel(
            "Meses",
            color="white"
        )

        ax.set_ylabel(
            "Emergia",
            color="white"
        )

        for i, value in enumerate(ordered_values):

            ax.text(
                i,
                value + 5,
                str(round(value, 1)),
                color="white",
                ha="center"
            )

        plt.tight_layout()

        canvas = FigureCanvasTkAgg(
            fig,
            master=self.chart_container
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )

        plt.close(fig)

    # =====================================================
    # REDE
    # =====================================================

    def show_network(self):

        self.network.draw_network()

    # =====================================================
    # PDF
    # =====================================================

    def generate_report(self):

        generator = ReportGenerator()

        pdf_path = generator.generate_pdf(
            filename="relatorio_emergia.pdf",
            total_emergy=self.total_emergy,
            network=self.network,
            data=self.lci_manager.get_data()
        )

        self.result_label.configure(
            text=f"Relatório gerado: {pdf_path}"
        )

    # =====================================================
    # FECHAR
    # =====================================================

    def on_close(self):

        try:

            self.quit()

            self.destroy()

        except:
            pass