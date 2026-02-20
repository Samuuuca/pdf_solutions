import sys
import os
from messagebox import mbox
from pdf2docx import Converter

def converter_para_word(caminho_pdf):
    try:
        # Define o nome do arquivo de saída (.docx)
        caminho_docx = os.path.splitext(caminho_pdf)[0] + ".docx"
        
        # Faz a conversão
        cv = Converter(caminho_pdf)
        cv.convert(caminho_docx, start=0, end=None)
        cv.close()
        
        mbox("Sucesso", f"Conversão concluída!\nArquivo: {caminho_docx}", 64)
        
    except Exception as e:
        mbox("Erro", f"Falha na conversão: {str(e)}", 16)

if __name__ == "__main__":
    arquivos = sys.argv[1:]
    if not arquivos:
        mbox("Aviso", "Selecione um PDF para converter.", 48)
    else:
        for f in arquivos:
            if f.lower().endswith(".pdf"):
                converter_para_word(f)
            else:
                mbox("Aviso", "Coversão disponível apenas para PDF", 48)
                