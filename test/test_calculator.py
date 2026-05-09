import unittest
from core.network_model import EmergyNetwork
from core.emergy_calculator import EmergyCalculator

class TestEmergyCalculator(unittest.TestCase):

    def test_total_emergy(self):

        network = EmergyNetwork()

        network.add_process("A")
        network.add_process("B")

        network.add_flow("A", "B", 100)

        calculator = EmergyCalculator(network)

        self.assertEqual(
            calculator.calculate_total_emergy(),
            100
        )

if __name__ == "__main__":
    unittest.main()