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

        plt.figure(figsize=(12, 8))

        pos = nx.spring_layout(self.graph)

        edge_labels = nx.get_edge_attributes(self.graph, 'weight')

        nx.draw(
            self.graph,
            pos,
            with_labels=True,
            node_color='#3b82f6',
            node_size=3500,
            font_size=9,
            font_color='white',
            edge_color='#94a3b8',
            arrows=True
        )

        nx.draw_networkx_edge_labels(
            self.graph,
            pos,
            edge_labels=edge_labels,
            font_color='red'
        )

        plt.title("Rede Emergética", fontsize=18)

        plt.show()