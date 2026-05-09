import customtkinter as ctk
from tkinter import filedialog

from core.config import Config
from core.lci_manager import LCIManager
from core.network_model import EmergyNetwork
from core.emergy_calculator import EmergyCalculator
from reports.report_generator import ReportGenerator

config = Config()


class EmergyApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title(config.APP_NAME)
        self.geometry("1400x850")
        self.minsize(1200, 750)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.configure(fg_color="#081028")

        self.lci_manager = LCIManager()
        self.network = EmergyNetwork()

        self.total_emergy = 0

        self.create_layout()

    def create_layout(self):

        # =====================================================
        # SIDEBAR
        # =====================================================

        self.sidebar = ctk.CTkFrame(
            self,
            width=320,
            corner_radius=0,
            fg_color="#172033"
        )
        self.sidebar.pack(side="left", fill="y")

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
            width=52,
            height=52,
            corner_radius=14,
            fg_color="#2563eb"
        )
        self.icon_frame.pack(side="left")

        self.icon_label = ctk.CTkLabel(
            self.icon_frame,
            text="∿",
            font=("Arial", 28, "bold"),
            text_color="white"
        )
        self.icon_label.place(relx=0.5, rely=0.5, anchor="center")

        self.logo_text_frame = ctk.CTkFrame(
            self.logo_frame,
            fg_color="transparent"
        )
        self.logo_text_frame.pack(side="left", padx=15)

        self.logo_title = ctk.CTkLabel(
            self.logo_text_frame,
            text="EmergyFlow",
            font=("Arial", 30, "bold"),
            text_color="#ffffff"
        )
        self.logo_title.pack(anchor="w")

        self.logo_subtitle = ctk.CTkLabel(
            self.logo_text_frame,
            text="Análise Emergética",
            font=("Arial", 14),
            text_color="#94a3b8"
        )
        self.logo_subtitle.pack(anchor="w")

        # =====================================================
        # DIVISOR
        # =====================================================

        self.divider = ctk.CTkFrame(
            self.sidebar,
            height=1,
            fg_color="#263041"
        )
        self.divider.pack(fill="x", pady=(5, 20))

        # =====================================================
        # MENU
        # =====================================================

        self.menu_frame = ctk.CTkFrame(
            self.sidebar,
            fg_color="transparent"
        )
        self.menu_frame.pack(fill="x", padx=18)

        button_style = {
            "height": 56,
            "corner_radius": 14,
            "anchor": "w",
            "font": ("Arial", 17, "bold")
        }

        self.dashboard_button = ctk.CTkButton(
            self.menu_frame,
            text="  Dashboard",
            fg_color="#2563eb",
            hover_color="#1d4ed8",
            text_color="white",
            **button_style
        )
        self.dashboard_button.pack(fill="x", pady=8)

        self.import_button = ctk.CTkButton(
            self.menu_frame,
            text=" Importar Dados",
            command=self.import_lci,
            fg_color="transparent",
            hover_color="#1e293b",
            text_color="#e2e8f0",
            **button_style
        )
        self.import_button.pack(fill="x", pady=8)

        self.calculate_button = ctk.CTkButton(
            self.menu_frame,
            text=" Calcular Emergy",
            command=self.calculate_emergy,
            fg_color="transparent",
            hover_color="#1e293b",
            text_color="#e2e8f0",
            **button_style
        )
        self.calculate_button.pack(fill="x", pady=8)

        self.network_button = ctk.CTkButton(
            self.menu_frame,
            text="  Visualizar Rede",
            command=self.show_network,
            fg_color="transparent",
            hover_color="#1e293b",
            text_color="#e2e8f0",
            **button_style
        )
        self.network_button.pack(fill="x", pady=8)

        self.report_button = ctk.CTkButton(
            self.menu_frame,
            text=" Gerar Relatório",
            command=self.generate_report,
            fg_color="transparent",
            hover_color="#1e293b",
            text_color="#e2e8f0",
            **button_style
        )
        self.report_button.pack(fill="x", pady=8)

        # =====================================================
        # CONFIGURAÇÕES
        # =====================================================

        self.bottom_frame = ctk.CTkFrame(
            self.sidebar,
            fg_color="transparent"
        )
        self.bottom_frame.pack(
            side="bottom",
            fill="x",
            padx=20,
            pady=25
        )

        self.settings_button = ctk.CTkButton(
            self.bottom_frame,
            text="  Configurações",
            fg_color="transparent",
            hover_color="#1e293b",
            text_color="#cbd5e1",
            height=50,
            corner_radius=12,
            anchor="w",
            font=("Arial", 16, "bold")
        )
        self.settings_button.pack(fill="x")

        # =====================================================
        # ÁREA PRINCIPAL
        # =====================================================

        self.main_frame = ctk.CTkFrame(
            self,
            fg_color="#081028",
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
            font=("Arial", 42, "bold"),
            text_color="white"
        )
        self.header_title.pack(anchor="w")

        self.header_subtitle = ctk.CTkLabel(
            self.header_frame,
            text="Visão geral do sistema emergético",
            font=("Arial", 20),
            text_color="#94a3b8"
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

        self.cards_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.process_card = self.create_card(
            self.cards_frame,
            "Processos",
            "0",
            0
        )

        self.flow_card = self.create_card(
            self.cards_frame,
            "Fluxos",
            "0",
            1
        )

        self.emergy_card = self.create_card(
            self.cards_frame,
            "Emergia Total",
            "0",
            2
        )

        # =====================================================
        # PAINEL PRINCIPAL
        # =====================================================

        self.content_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="#172033",
            corner_radius=22,
            border_width=1,
            border_color="#263041"
        )
        self.content_frame.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=(20, 35)
        )

        self.content_title = ctk.CTkLabel(
            self.content_frame,
            text="Dados do Sistema",
            font=("Arial", 26, "bold"),
            text_color="white"
        )
        self.content_title.pack(
            anchor="w",
            padx=30,
            pady=(25, 10)
        )

        self.result_label = ctk.CTkLabel(
            self.content_frame,
            text="Aguardando importação da base LCI...",
            font=("Arial", 16),
            text_color="#cbd5e1"
        )
        self.result_label.pack(
            anchor="w",
            padx=30
        )

        self.table_frame = ctk.CTkScrollableFrame(
            self.content_frame,
            fg_color="#111827",
            corner_radius=15
        )
        self.table_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=25
        )

    # =====================================================
    # CARD
    # =====================================================

    def create_card(self, parent, title, value, column):

        card = ctk.CTkFrame(
            parent,
            fg_color="#172033",
            corner_radius=20,
            height=160,
            border_width=1,
            border_color="#263041"
        )

        card.grid(
            row=0,
            column=column,
            padx=12,
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
            padx=25,
            pady=(25, 8)
        )

        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=("Arial", 38, "bold"),
            text_color="white"
        )
        value_label.pack(
            anchor="w",
            padx=25
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
                    self.network.add_flow(source, target, value)

                self.process_card.configure(
                    text=str(len(self.network.graph.nodes))
                )

                self.flow_card.configure(
                    text=str(len(self.network.graph.edges))
                )

                self.update_table(data)

                self.result_label.configure(
                    text="Base LCI carregada com sucesso!"
                )

    # =====================================================
    # CALCULAR EMERGIA
    # =====================================================

    def calculate_emergy(self):

        calculator = EmergyCalculator(self.network)

        total = calculator.calculate_total_emergy()

        self.total_emergy = total

        self.emergy_card.configure(text=str(total))

        self.result_label.configure(
            text=f"Emergia total calculada: {total}"
        )

    # =====================================================
    # VISUALIZAR REDE
    # =====================================================

    def show_network(self):
        self.network.draw_network()

    # =====================================================
    # GERAR RELATÓRIO
    # =====================================================

    def generate_report(self):

        generator = ReportGenerator()

        generator.generate_pdf(
            "relatorio_emergia.pdf",
            self.total_emergy
        )

        self.result_label.configure(
            text="Relatório PDF gerado com sucesso!"
        )

    # =====================================================
    # TABELA
    # =====================================================

    def update_table(self, data):

        for widget in self.table_frame.winfo_children():
            widget.destroy()

        headers = ["Origem", "Destino", "Valor"]

        for i, header in enumerate(headers):

            label = ctk.CTkLabel(
                self.table_frame,
                text=header,
                font=("Arial", 16, "bold"),
                text_color="white"
            )

            label.grid(
                row=0,
                column=i,
                padx=40,
                pady=18
            )

        for row_index, (_, row) in enumerate(data.iterrows(), start=1):

            values = [
                row['source'],
                row['target'],
                row['value']
            ]

            for column_index, value in enumerate(values):

                cell = ctk.CTkLabel(
                    self.table_frame,
                    text=str(value),
                    font=("Arial", 15),
                    text_color="#cbd5e1"
                )

                cell.grid(
                    row=row_index,
                    column=column_index,
                    padx=40,
                    pady=12
                )