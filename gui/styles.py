import customtkinter as ctk

class AppStyles:

    BACKGROUND = "#0f172a"
    CARD = "#1e293b"

    PRIMARY = "#3b82f6"
    PRIMARY_HOVER = "#2563eb"

    SUCCESS = "#22c55e"
    SUCCESS_HOVER = "#16a34a"

    TEXT = "#f8fafc"
    SUBTEXT = "#cbd5e1"

    FONT_TITLE = ("Arial", 28, "bold")
    FONT_SUBTITLE = ("Arial", 18)
    FONT_TEXT = ("Arial", 14)

    @staticmethod
    def configure_theme():
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")