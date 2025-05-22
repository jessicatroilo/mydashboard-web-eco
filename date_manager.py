from datetime import datetime
import locale

# On force la locale FR pour les dates (à adapter selon l'OS)
try:
    locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
except locale.Error:
    locale.setlocale(locale.LC_TIME, "fr_FR")  # fallback Windows

class DateManager:
    def __init__(self, format_str="%A %d %B %Y"):
        self.format_str = format_str

    def get_current_date(self):
        return datetime.now().strftime(self.format_str)