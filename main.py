import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon
from pypdf import PdfReader, PdfWriter
from ui_main import Ui_MainWindow

# No executável (PyInstaller) as imagens ficam numa pasta temporária (sys._MEIPASS).
# Mudar para essa pasta faz "baianinho.png" ser encontrada tanto no .exe quanto no .py.
os.chdir(getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__))))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # O .ui aplica fundo branco a TODOS os widgets filhos, inclusive às
        # QMessageBox. Com o Windows em modo escuro o texto delas é branco e
        # fica invisível. Aqui o fundo branco vale só para a janela principal.
        self.setStyleSheet("QMainWindow { background-color: rgb(255, 255, 255); }")
        self.setWindowTitle("PDF - Divisor de PDF")
        appIcon = QIcon("baianinho.png")
        self.setWindowIcon(appIcon)

        self.path = ""
        self.btn_open.clicked.connect(self.open_path)
        self.pushButton_2.clicked.connect(self.dividir_pdf)

    def open_path(self):
        # getOpenFileName abre UM arquivo (getExistingDirectory abre só pastas)
        # Retorna uma tupla: (caminho_do_arquivo, filtro_escolhido)
        arquivo, _ = QFileDialog.getOpenFileName(
            self,
            "Selecione o arquivo PDF",
            os.path.expanduser("~"),
            "Arquivos PDF (*.pdf)",
        )

        if not arquivo:  # usuário clicou em Cancelar
            return

        self.path = arquivo
        self.txt_path.setText(arquivo)

    def dividir_pdf(self):
        # Usa o que está no campo de texto (o usuário pode ter colado um caminho)
        self.path = self.txt_path.text().strip()

        if not self.path or not os.path.isfile(self.path):
            QMessageBox.warning(self, "Aviso", "Selecione um arquivo PDF válido primeiro.")
            return

        # Pasta de saída: mesmo lugar do PDF, com o nome do arquivo
        # Ex.: C:\docs\contratos.pdf -> C:\docs\contratos_dividido\
        pasta_origem = os.path.dirname(self.path)
        nome_base = os.path.splitext(os.path.basename(self.path))[0]
        pasta_saida = os.path.join(pasta_origem, f"{nome_base}_dividido")

        try:
            leitor = PdfReader(self.path)
            total = len(leitor.pages)
            os.makedirs(pasta_saida, exist_ok=True)

            # Cada página vira um arquivo PDF separado
            for numero, pagina in enumerate(leitor.pages, start=1):
                escritor = PdfWriter()
                escritor.add_page(pagina)
                nome_arquivo = f"{nome_base}_{numero:03d}.pdf"
                with open(os.path.join(pasta_saida, nome_arquivo), "wb") as saida:
                    escritor.write(saida)

        except Exception as erro:
            QMessageBox.critical(self, "Erro", f"Não foi possível dividir o PDF:\n{erro}")
            return

        QMessageBox.information(
            self,
            "Concluído",
            f"PDF dividido em {total} arquivo(s).\n\nSalvos em:\n{pasta_saida}",
        )
        os.startfile(pasta_saida)  # abre a pasta no Windows Explorer


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
