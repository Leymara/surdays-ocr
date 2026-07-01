import io

import cv2
import fitz
import numpy as np
from PIL import Image


class ImageProcessor:

	def obtener_primera_pagina(self, ruta_pdf):

		documento = fitz.open(ruta_pdf)

		pagina = documento.load_page(0)

		pix = pagina.get_pixmap(matrix=fitz.Matrix(4, 4))

		imagen = Image.open(io.BytesIO(pix.tobytes("png")))

		documento.close()

		return imagen

	def preparar_para_ocr(self, imagen):

		img = np.array(imagen)

		# Escala de grises
		gris = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

		# Aumentar contraste
		gris = cv2.equalizeHist(gris)

		# Binarización automática
		_, binaria = cv2.threshold(
			gris,
			0,
			255,
			cv2.THRESH_BINARY + cv2.THRESH_OTSU
		)

		return Image.fromarray(binaria)

