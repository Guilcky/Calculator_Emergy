class Config:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    APP_NAME = "Sistema de Cálculo de Emergia"