import sys
import os
import ctypes
from pdf2docx import Converter

def mbox(titulo, texto, estilo):
	return ctypes.windll.user32.MessageBoxW(0, texto, titulo, estilo)

