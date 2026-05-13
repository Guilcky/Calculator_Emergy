import networkx as nx
import matplotlib.pyplot as plt


class EmergyNetwork:

    def __init__(self):
        self.graph = nx.DiGraph()

    # =====================================================
    # ADICIONAR PROCESSO
    # =====================================================

    def add_process(self, process_name):
        self.graph.add_node(process_name)

    # =====================================================
    # ADICIONAR FLUXO
    # =====================================================

    def add_flow(self, source, target, value):
        self.graph.add_edge(
            source,
            target,
            weight=value
        )

    # =====================================================
    # VISUALIZAÇÃO MODERNA DA REDE
    # =====================================================

    def draw_network(self):

        if len(self.graph.nodes) == 0:
            print("Nenhuma rede carregada.")
            return

        plt.close('all')

        fig = plt.figure(
            figsize=(16, 10),
            facecolor="#071226"
        )

        ax = plt.gca()
        ax.set_facecolor("#071226")

        # =====================================================
        # POSICIONAMENTO
        # =====================================================

        pos = nx.spring_layout(
            self.graph,
            k=1.8,
            seed=42
        )

        # =====================================================
        # PESOS DAS ARESTAS
        # =====================================================

        weights = [
            self.graph[u][v]['weight']
            for u, v in self.graph.edges()
        ]

        max_weight = max(weights) if weights else 1

        edge_widths = [
            1 + (w / max_weight) * 6
            for w in weights
        ]

        # =====================================================
        # NÓS
        # =====================================================

        nx.draw_networkx_nodes(
            self.graph,
            pos,
            node_color="#2563eb",
            node_size=5000,
            edgecolors="#60a5fa",
            linewidths=2.5,
            alpha=0.95
        )

        # =====================================================
        # ARESTAS
        # =====================================================

        nx.draw_networkx_edges(
            self.graph,
            pos,
            edge_color="#38bdf8",
            width=edge_widths,
            arrows=True,
            arrowsize=28,
            arrowstyle='-|>',
            connectionstyle='arc3,rad=0.08'
        )

        # =====================================================
        # LABELS DOS NÓS
        # =====================================================

        nx.draw_networkx_labels(
            self.graph,
            pos,
            font_size=11,
            font_weight='bold',
            font_color='white'
        )

        # =====================================================
        # LABELS DAS ARESTAS
        # =====================================================

        edge_labels = {
            (u, v): f"{d['weight']} sej"
            for u, v, d in self.graph.edges(data=True)
        }

        nx.draw_networkx_edge_labels(
            self.graph,
            pos,
            edge_labels=edge_labels,
            font_color="#facc15",
            font_size=10,
            rotate=False,
            bbox=dict(
                facecolor="#0f172a",
                edgecolor="#1e293b",
                boxstyle="round,pad=0.3",
                alpha=0.9
            )
        )

        # =====================================================
        # TÍTULO
        # =====================================================

        plt.title(
            "Rede de Fluxo Emergético",
            fontsize=24,
            color="white",
            fontweight='bold',
            pad=25
        )

        # =====================================================
        # INFO INFERIOR
        # =====================================================

        total_nodes = len(self.graph.nodes)
        total_edges = len(self.graph.edges)

        plt.figtext(
            0.5,
            0.02,
            f"Processos: {total_nodes}    |    Fluxos: {total_edges}",
            ha='center',
            fontsize=12,
            color='#94a3b8'
        )

        # =====================================================
        # REMOVER EIXOS
        # =====================================================

        plt.axis('off')

        plt.tight_layout()

        plt.show()