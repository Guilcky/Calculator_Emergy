import networkx as nx
import matplotlib.pyplot as plt

class EmergyNetwork:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_process(self, process_name):
        self.graph.add_node(process_name)

    def add_flow(self, source, target, value):
        self.graph.add_edge(source, target, weight=value)

    def draw_network(self):
        pos = nx.spring_layout(self.graph)

        edge_labels = nx.get_edge_attributes(self.graph, 'weight')

        nx.draw(
            self.graph,
            pos,
            with_labels=True,
            node_color='lightblue',
            node_size=2500,
            font_size=10,
            arrows=True
        )

        nx.draw_networkx_edge_labels(
            self.graph,
            pos,
            edge_labels=edge_labels
        )

        plt.title("Rede de Fluxo de Emergia")
        plt.show()