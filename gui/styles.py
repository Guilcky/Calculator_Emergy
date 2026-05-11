import customtkinter as ctk


class AppStyles:

    # =====================================================
    # CORES
    # =====================================================

    BACKGROUND = "#081028"

    SIDEBAR = "#172033"

    CARD = "#1b2940"

    BORDER = "#2a3b57"

    PRIMARY = "#2563eb"
    PRIMARY_HOVER = "#1d4ed8"

    GREEN = "#00c853"

    ORANGE = "#ff6d00"

    PURPLE = "#a855f7"

    CYAN = "#06b6d4"

    TEXT = "#ffffff"

    SUBTEXT = "#94a3b8"

    # =====================================================
    # FONTES
    # =====================================================

    FONT_TITLE = ("Arial", 38, "bold")

    FONT_SUBTITLE = ("Arial", 20)

    FONT_CARD_TITLE = ("Arial", 18)

    FONT_CARD_VALUE = ("Arial", 38, "bold")

    FONT_TEXT = ("Arial", 15)

    # =====================================================
    # TEMA
    # =====================================================

    @staticmethod
    def configure_theme():

        ctk.set_appearance_mode("dark")

        ctk.set_default_color_theme("blue")