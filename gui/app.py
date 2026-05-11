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
        # FECHAMENTO SEGURO
        # =====================================================

        self.protocol(
            "WM_DELETE_WINDOW",
            self.on_close
        )

        AppStyles.configure_theme()

        self.title(config.APP_NAME)

        self.geometry("1500x900")
        self.minsize(1400, 850)

        self.configure(
            fg_color="#071226"
        )

        self.lci_manager = LCIManager()
        self.network = EmergyNetwork()

        self.total_emergy = 0

        # =====================================================
        # HISTÓRICO DE EMERGIA
        # =====================================================

        self.history_values = [120, 180, 160]

        self.history_months = [
            "Jan",
            "Fev",
            "Mar"
        ]

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
            width=320,
            corner_radius=0,
            fg_color="#142038"
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        # =====================================================
        # LOGO
        # =====================================================

        self.logo_frame = ctk.CTkFrame(
            self.sidebar,
            fg_color="transparent"
        )

        self.logo_frame.pack(
            fill="x",
            padx=28,
            pady=(35, 30)
        )

        self.icon_frame = ctk.CTkFrame(
            self.logo_frame,
            width=60,
            height=60,
            corner_radius=18,
            fg_color=AppStyles.PRIMARY
        )

        self.icon_frame.pack(side="left")

        self.icon_label = ctk.CTkLabel(
            self.icon_frame,
            text="∿",
            font=("Arial", 30, "bold"),
            text_color="white"
        )

        self.icon_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        self.logo_text_frame = ctk.CTkFrame(
            self.logo_frame,
            fg_color="transparent"
        )

        self.logo_text_frame.pack(
            side="left",
            padx=15
        )

        self.logo_title = ctk.CTkLabel(
            self.logo_text_frame,
            text="EmergyFlow",
            font=("Arial", 34, "bold"),
            text_color="white"
        )

        self.logo_title.pack(anchor="w")

        self.logo_subtitle = ctk.CTkLabel(
            self.logo_text_frame,
            text="Análise Emergética",
            font=("Arial", 15),
            text_color=AppStyles.SUBTEXT
        )

        self.logo_subtitle.pack(anchor="w")

        # =====================================================
        # DIVISOR
        # =====================================================

        divider = ctk.CTkFrame(
            self.sidebar,
            height=1,
            fg_color="#263041"
        )

        divider.pack(
            fill="x",
            pady=(5, 20)
        )

        # =====================================================
        # MENU
        # =====================================================

        self.menu_frame = ctk.CTkFrame(
            self.sidebar,
            fg_color="transparent"
        )

        self.menu_frame.pack(
            fill="x",
            padx=18
        )

        button_style = {
            "height": 58,
            "corner_radius": 16,
            "anchor": "w",
            "font": ("Arial", 17, "bold"),
            "border_width": 0,
            "hover_color": "#243b5a"
        }

        self.dashboard_button = ctk.CTkButton(
            self.menu_frame,
            text="  Dashboard",
            fg_color=AppStyles.PRIMARY,
            text_color="white",
            **button_style
        )

        self.dashboard_button.pack(
            fill="x",
            pady=8
        )

        self.import_button = ctk.CTkButton(
            self.menu_frame,
            text="  Importar Dados",
            command=self.import_lci,
            fg_color="transparent",
            text_color="#e2e8f0",
            **button_style
        )

        self.import_button.pack(
            fill="x",
            pady=8
        )

        self.calculate_button = ctk.CTkButton(
            self.menu_frame,
            text="  Calcular Emergia",
            command=self.calculate_emergy,
            fg_color="transparent",
            text_color="#e2e8f0",
            **button_style
        )

        self.calculate_button.pack(
            fill="x",
            pady=8
        )

        self.network_button = ctk.CTkButton(
            self.menu_frame,
            text="  Visualizar Rede",
            command=self.show_network,
            fg_color="transparent",
            text_color="#e2e8f0",
            **button_style
        )

        self.network_button.pack(
            fill="x",
            pady=8
        )

        self.report_button = ctk.CTkButton(
            self.menu_frame,
            text="  Gerar Relatório",
            command=self.generate_report,
            fg_color="transparent",
            text_color="#e2e8f0",
            **button_style
        )

        self.report_button.pack(
            fill="x",
            pady=8
        )

        # =====================================================
        # MAIN FRAME
        # =====================================================

        self.main_frame = ctk.CTkFrame(
            self,
            fg_color="#071226",
            corner_radius=0
        )

        self.main_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        # =====================================================
        # HEADER
        # =====================================================

        self.header_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )

        self.header_frame.pack(
            fill="x",
            padx=40,
            pady=(35, 20)
        )

        self.header_title = ctk.CTkLabel(
            self.header_frame,
            text="Dashboard",
            font=("Arial", 52, "bold"),
            text_color="white"
        )

        self.header_title.pack(anchor="w")

        self.header_subtitle = ctk.CTkLabel(
            self.header_frame,
            text="Visão geral do sistema emergético",
            font=("Arial", 22),
            text_color=AppStyles.SUBTEXT
        )

        self.header_subtitle.pack(anchor="w")

        # =====================================================
        # CARDS
        # =====================================================

        self.cards_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )

        self.cards_frame.pack(
            fill="x",
            padx=40,
            pady=10
        )

        self.cards_frame.grid_columnconfigure(
            (0, 1, 2),
            weight=1
        )

        self.emergy_card = self.create_card(
            self.cards_frame,
            title="Emergia Total",
            value="0",
            subtitle="sej",
            color=AppStyles.PRIMARY,
            column=0
        )

        self.process_card = self.create_card(
            self.cards_frame,
            title="Processos Ativos",
            value="0",
            subtitle="processos",
            color=AppStyles.GREEN,
            column=1
        )

        self.flow_card = self.create_card(
            self.cards_frame,
            title="Fluxos",
            value="0",
            subtitle="conexões",
            color=AppStyles.PURPLE,
            column=2
        )

        # =====================================================
        # ANALYTICS
        # =====================================================

        self.analytics_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )

        self.analytics_frame.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=(10, 25)
        )

        self.analytics_frame.grid_columnconfigure(
            (0, 1),
            weight=1
        )

        # =====================================================
        # CHART CARD
        # =====================================================

        self.chart_card = ctk.CTkFrame(
            self.analytics_frame,
            fg_color=AppStyles.CARD,
            corner_radius=22,
            border_width=1,
            border_color=AppStyles.BORDER
        )

        self.chart_card.grid(
            row=0,
            column=0,
            padx=10,
            sticky="nsew"
        )

        chart_title = ctk.CTkLabel(
            self.chart_card,
            text="Evolução da Emergia",
            font=("Arial", 28, "bold"),
            text_color="white"
        )

        chart_title.pack(
            anchor="w",
            padx=24,
            pady=(24, 12)
        )

        self.chart_container = ctk.CTkFrame(
            self.chart_card,
            fg_color="transparent"
        )

        self.chart_container.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # =====================================================
        # PIE CARD
        # =====================================================

        self.pie_card = ctk.CTkFrame(
            self.analytics_frame,
            fg_color=AppStyles.CARD,
            corner_radius=22,
            border_width=1,
            border_color=AppStyles.BORDER
        )

        self.pie_card.grid(
            row=0,
            column=1,
            padx=10,
            sticky="nsew"
        )

        pie_title = ctk.CTkLabel(
            self.pie_card,
            text="Distribuição dos Fluxos",
            font=("Arial", 28, "bold"),
            text_color="white"
        )

        pie_title.pack(
            anchor="w",
            padx=24,
            pady=(24, 12)
        )

        self.pie_container = ctk.CTkFrame(
            self.pie_card,
            fg_color="transparent"
        )

        self.pie_container.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # =====================================================
        # RESULTADO
        # =====================================================

        self.result_label = ctk.CTkLabel(
            self.main_frame,
            text="Aguardando importação da base LCI...",
            font=("Arial", 16),
            text_color="#cbd5e1"
        )

        self.result_label.pack(
            anchor="w",
            padx=50,
            pady=(0, 20)
        )

    # =====================================================
    # CARD
    # =====================================================

    def create_card(
            self,
            parent,
            title,
            value,
            subtitle,
            color,
            column
    ):

        card = ctk.CTkFrame(
            parent,
            fg_color=AppStyles.CARD,
            corner_radius=22,
            border_width=1,
            border_color=AppStyles.BORDER,
            height=210
        )

        card.grid(
            row=0,
            column=column,
            padx=14,
            sticky="nsew"
        )

        title_label = ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 18),
            text_color=AppStyles.SUBTEXT
        )

        title_label.pack(
            anchor="w",
            padx=24,
            pady=(24, 8)
        )

        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=("Arial", 38, "bold"),
            text_color="white"
        )

        value_label.pack(
            anchor="w",
            padx=24
        )

        subtitle_label = ctk.CTkLabel(
            card,
            text=subtitle,
            font=("Arial", 15),
            text_color=AppStyles.SUBTEXT
        )

        subtitle_label.pack(
            anchor="w",
            padx=24,
            pady=(5, 20)
        )

        return value_label

    # =====================================================
    # IMPORTAR CSV
    # =====================================================

    def import_lci(self):

        file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")]
        )

        if file_path:

            success = self.lci_manager.load_csv(file_path)

            if success:

                data = self.lci_manager.get_data()

                self.network.graph.clear()

                for _, row in data.iterrows():

                    source = row['source']
                    target = row['target']
                    value = row['value']

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

        total = calculator.calculate_total_emergy()

        self.total_emergy = total

        self.emergy_card.configure(
            text=str(total)
        )

        next_month = f"M{len(self.history_months)+1}"

        self.history_months.append(next_month)

        self.history_values.append(total)

        self.update_history_chart()

        self.update_pie_chart()

        self.result_label.configure(
            text=f"Emergia total calculada: {total}"
        )

    # =====================================================
    # GRÁFICO HISTÓRICO
    # =====================================================

    def update_history_chart(self):

        for widget in self.chart_container.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(
            figsize=(5, 3),
            dpi=100
        )

        fig.patch.set_facecolor('#1b2940')

        ax.set_facecolor('#1b2940')

        ax.plot(
            self.history_months,
            self.history_values,
            marker='o',
            linewidth=3
        )

        ax.set_title(
            'Evolução da Emergia',
            color='white',
            fontsize=14
        )

        ax.tick_params(colors='white')

        ax.grid(True, alpha=0.3)

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
    # GRÁFICO PIZZA
    # =====================================================

    def update_pie_chart(self):

        for widget in self.pie_container.winfo_children():
            widget.destroy()

        labels = []
        values = []

        for source, target, data in self.network.graph.edges(data=True):

            labels.append(
                f"{source}->{target}"
            )

            values.append(
                data['weight']
            )

        if not values:
            return

        fig, ax = plt.subplots(
            figsize=(5, 3),
            dpi=100
        )

        fig.patch.set_facecolor('#1b2940')

        ax.pie(
            values,
            labels=labels,
            autopct='%1.1f%%'
        )

        ax.set_title(
            'Distribuição dos Fluxos',
            color='white',
            fontsize=14
        )

        canvas = FigureCanvasTkAgg(
            fig,
            master=self.pie_container
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
            historical_data=dict(
                zip(
                    self.history_months,
                    self.history_values
                )
            )
        )

        self.result_label.configure(
            text=f"Relatório gerado em: {pdf_path}"
        )

    # =====================================================
    # FECHAR APP
    # =====================================================

    def on_close(self):

        plt.close('all')

        self.destroy()