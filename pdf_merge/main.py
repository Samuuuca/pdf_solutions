import sys
import ctypes
from pypdf import PdfWriter

def mbox(titulo, texto, estilo):
    """Exibe uma caixa de mensagem nativa do Windows.
    Estilos: 0 = OK, 16 = Erro (X), 64 = Informação (i)"""
    return ctypes.windll.user32.MessageBoxW(0, texto, titulo, estilo)

def unir_pdfs(lista_arquivos):
    try:
        merger = PdfWriter()
        
        for pdf in lista_arquivos:
            merger.append(pdf)
        
        # Define o nome do arquivo de saída
        output_path = lista_arquivos[0].replace(".pdf", "_unificado.pdf")
        
        with open(output_path, "wb") as f:
            merger.write(f)
            
        #mbox("Sucesso!", f"PDFs unidos com sucesso!\nSalvo em: {output_path}", 64)
        
    except Exception as e:
        mbox("Erro", f"Ocorreu um erro ao unir os PDFs:\n{str(e)}", 16)

if __name__ == "__main__":
    # O primeiro argumento (index 0) é sempre o caminho do próprio script/exe
    arquivos_selecionados = sys.argv[1:]
    
    if len(arquivos_selecionados) < 2:
        mbox("Aviso", "Por favor, selecione pelo menos 2 arquivos PDF para unir.", 48)
    else:
        unir_pdfs(arquivos_selecionados)