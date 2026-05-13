import customtkinter as ctk


class AppStyles:

    BACKGROUND = "#071226"
    CARD = "#142038"
    BORDER = "#243041"

    PRIMARY = "#3b82f6"
    GREEN = "#22c55e"
    PURPLE = "#a855f7"

    TEXT = "#ffffff"
    SUBTEXT = "#94a3b8"

    @staticmethod
    def configure_theme():

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")