import ctypes

def mbox(titulo, texto, estilo):
    return ctypes.windll.user32.MessageBoxW(0, texto, titulo, estilo)