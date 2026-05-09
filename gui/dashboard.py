import customtkinter as ctk
import pandas as pd

class DashboardFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.configure(
            fg_color="#1e293b",
            corner_radius=15
        )

        self.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.create_widgets()

    def create_widgets(self):

        self.title_label = ctk.CTkLabel(
            self,
            text="Dashboard Emergético",
            font=("Arial", 24, "bold")
        )

        self.title_label.pack(pady=20)

        self.info_frame = ctk.CTkFrame(
            self,
            fg_color="#334155",
            corner_radius=10
        )

        self.info_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.total_process_label = ctk.CTkLabel(
            self.info_frame,
            text="Processos: 0",
            font=("Arial", 18)
        )

        self.total_process_label.pack(
            side="left",
            padx=20,
            pady=20
        )

        self.total_flow_label = ctk.CTkLabel(
            self.info_frame,
            text="Fluxos: 0",
            font=("Arial", 18)
        )

        self.total_flow_label.pack(
            side="left",
            padx=20,
            pady=20
        )

        self.total_emergy_label = ctk.CTkLabel(
            self.info_frame,
            text="Emergia Total: 0",
            font=("Arial", 18)
        )

        self.total_emergy_label.pack(
            side="left",
            padx=20,
            pady=20
        )

        self.table_frame = ctk.CTkScrollableFrame(
            self,
            width=800,
            height=300
        )

        self.table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    def update_dashboard(self, network, total_emergy):

        total_processes = len(network.graph.nodes)
        total_flows = len(network.graph.edges)

        self.total_process_label.configure(
            text=f"Processos: {total_processes}"
        )

        self.total_flow_label.configure(
            text=f"Fluxos: {total_flows}"
        )

        self.total_emergy_label.configure(
            text=f"Emergia Total: {total_emergy}"
        )

        for widget in self.table_frame.winfo_children():
            widget.destroy()

        header1 = ctk.CTkLabel(
            self.table_frame,
            text="Origem",
            font=("Arial", 16, "bold")
        )
        header1.grid(row=0, column=0, padx=20, pady=10)

        header2 = ctk.CTkLabel(
            self.table_frame,
            text="Destino",
            font=("Arial", 16, "bold")
        )
        header2.grid(row=0, column=1, padx=20, pady=10)

        header3 = ctk.CTkLabel(
            self.table_frame,
            text="Valor",
            font=("Arial", 16, "bold")
        )
        header3.grid(row=0, column=2, padx=20, pady=10)

        row_index = 1

        for source, target, data in network.graph.edges(data=True):

            source_label = ctk.CTkLabel(
                self.table_frame,
                text=str(source)
            )

            source_label.grid(
                row=row_index,
                column=0,
                padx=20,
                pady=5
            )

            target_label = ctk.CTkLabel(
                self.table_frame,
                text=str(target)
            )

            target_label.grid(
                row=row_index,
                column=1,
                padx=20,
                pady=5
            )

            value_label = ctk.CTkLabel(
                self.table_frame,
                text=str(data['weight'])
            )

            value_label.grid(
                row=row_index,
                column=2,
                padx=20,
                pady=5
            )

            row_index += 1