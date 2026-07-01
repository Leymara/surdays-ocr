import re


class Parser:

    def __init__(self):
        # Referencias válidas
        self.regex_referencia = re.compile(
            r"\b(?:Z|X|JV|MC|P|G|Y|R|A)\d+\b",
            re.IGNORECASE
        )

        # Fechas tipo 24/01/25
        self.regex_fecha = re.compile(
            r"\b\d{2}/\d{2}/\d{2,4}\b"
        )

        # Importes tipo 854,20 o 40
        self.regex_importe = re.compile(
            r"\d+(?:,\d{2})?"
        )

    def analizar(self, texto):

        referencias = self.regex_referencia.findall(texto)

        fechas = self.regex_fecha.findall(texto)

        importes = self.regex_importe.findall(texto)

        return {
            "referencias": referencias,
            "fechas": fechas,
            "importes": importes
        }
