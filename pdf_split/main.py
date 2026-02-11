import sys
import os
import ctypes
from pypdf import PdfReader, PdfWriter

def mbox(titulo, texto, estilo):
    return ctypes.windll.user32.MessageBoxW(0, texto, titulo, estilo)

def split_pdf(caminho_arquivo):
    try:
        reader = PdfReader(caminho_arquivo)
        nome_base = os.path.splitext(caminho_arquivo)[0] # Pega o nome sem .pdf
        
        # Percorre cada página do PDF
        for i, pagina in enumerate(reader.pages):
            writer = PdfWriter()
            writer.add_page(pagina)
            
            # Cria um novo nome: "arquivo_pagina_1.pdf"
            output_filename = f"{nome_base}_pagina_{i+1}.pdf"
            
            with open(output_filename, "wb") as out:
                writer.write(out)
        
        mbox("Sucesso", f"PDF separado em {len(reader.pages)} arquivos!", 64)
        
    except Exception as e:
        mbox("Erro", f"Falha ao separar PDF: {str(e)}", 16)

if __name__ == "__main__":
    arquivos = sys.argv[1:]
    
    if len(arquivos) == 0:
        mbox("Aviso", "Nenhum arquivo selecionado.", 48)
    else:
        # Para o Split, geralmente processamos um arquivo por vez
        for arquivo in arquivos:
            split_pdf(arquivo)