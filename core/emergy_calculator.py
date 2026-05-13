class EmergyCalculator:

    def __init__(self, network):
        self.network = network

    def calculate_total_emergy(self):

        total = 0

        for _, _, data in self.network.graph.edges(data=True):
            total += data['weight']

        return total

    def calculate_node_emergy(self, node):

        total = 0

        for _, _, data in self.network.graph.in_edges(node, data=True):
            total += data['weight']

        return total