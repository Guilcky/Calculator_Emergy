import pandas as pd


class LCIManager:

    def __init__(self):
        self.data = None

    def load_csv(self, file_path):

        try:
            self.data = pd.read_csv(file_path)
            return True

        except Exception as e:
            print(e)
            return False

    def get_data(self):
        return self.data