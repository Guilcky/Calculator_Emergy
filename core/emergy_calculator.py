class EmergyCalculator:

    def __init__(self, network):

        self.network = network

    # =====================================================
    # EMERGIA TOTAL
    # =====================================================

    def calculate_total_emergy(self):

        total = 0

        for _, _, data in self.network.graph.edges(data=True):

            weight = data.get('weight', 0)

            total += weight

        return round(total, 2)

    # =====================================================
    # EMERGIA POR NÓ
    # =====================================================

    def calculate_node_emergy(self, node):

        total = 0

        for _, _, data in self.network.graph.in_edges(
                node,
                data=True
        ):

            weight = data.get('weight', 0)

            total += weight

        return round(total, 2)

    # =====================================================
    # EMERGIA DE SAÍDA
    # =====================================================

    def calculate_output_emergy(self, node):

        total = 0

        for _, _, data in self.network.graph.out_edges(
                node,
                data=True
        ):

            weight = data.get('weight', 0)

            total += weight

        return round(total, 2)

    # =====================================================
    # EFICIÊNCIA EMERGÉTICA
    # =====================================================

    def calculate_efficiency(self, node):

        input_emergy = self.calculate_node_emergy(node)

        output_emergy = self.calculate_output_emergy(node)

        if input_emergy == 0:
            return 0

        efficiency = output_emergy / input_emergy

        return round(efficiency, 2)

    # =====================================================
    # PROCESSO MAIS IMPACTANTE
    # =====================================================

    def get_most_impactful_process(self):

        max_value = 0

        max_process = None

        for node in self.network.graph.nodes:

            node_emergy = self.calculate_node_emergy(node)

            if node_emergy > max_value:

                max_value = node_emergy

                max_process = node

        return {
            "process": max_process,
            "emergy": round(max_value, 2)
        }

    # =====================================================
    # DISTRIBUIÇÃO DOS FLUXOS
    # =====================================================

    def get_flow_distribution(self):

        flows = []

        for source, target, data in self.network.graph.edges(data=True):

            flows.append({
                "source": source,
                "target": target,
                "value": data.get('weight', 0)
            })

        return flows

    # =====================================================
    # RESUMO ANALÍTICO
    # =====================================================

    def generate_summary(self):

        total_emergy = self.calculate_total_emergy()

        total_processes = len(
            self.network.graph.nodes
        )

        total_flows = len(
            self.network.graph.edges
        )

        impactful = self.get_most_impactful_process()

        return {

            "total_emergy": total_emergy,

            "total_processes": total_processes,

            "total_flows": total_flows,

            "most_impactful_process":
                impactful["process"],

            "most_impactful_value":
                impactful["emergy"]
        }