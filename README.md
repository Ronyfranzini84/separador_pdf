# Divisor de PDF

Aplicativo desktop para Windows que divide um arquivo PDF em vários arquivos, **um por página**.

Feito em Python com interface gráfica em **PySide6 (Qt)** e manipulação de PDF com **pypdf**.

## Como funciona

1. Clique no botão para selecionar o PDF (ou cole o caminho no campo de texto).
2. Clique em dividir.
3. As páginas são salvas em uma pasta ao lado do arquivo original:

```
C:\docs\contratos.pdf  ->  C:\docs\contratos_dividido\
                              contratos_001.pdf
                              contratos_002.pdf
                              ...
```

Ao terminar, a pasta é aberta automaticamente no Windows Explorer.

## Requisitos

- Windows
- Python 3.10+

## Instalação

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Executar

```bash
python main.py
```

## Gerar o executável (.exe)

```bash
pyinstaller "Divisor de PDF.spec"
```

O executável é criado em `dist\Divisor de PDF.exe`. O arquivo `versao.txt` define as informações exibidas em *Propriedades > Detalhes* do Windows, e `icone.ico` é o ícone do programa.

## Estrutura do projeto

| Arquivo | Descrição |
|---|---|
| `main.py` | Código principal (janela e lógica de divisão) |
| `separador.ui` | Interface criada no Qt Designer |
| `ui_main.py` | Interface convertida para Python (gerada a partir do `.ui`) |
| `icons.qrc` / `icons_rc.py` | Recursos de imagem do Qt |
| `baianinho.png` | Ícone da janela |
| `criar_icone.py` | Gera `icone.ico` a partir de `Pasta_Vermelha.png` |
| `Divisor de PDF.spec` | Configuração do PyInstaller |
| `versao.txt` | Informações de versão do executável |

### Regerar arquivos da interface

Se você alterar o `separador.ui` ou o `icons.qrc`:

```bash
pyside6-uic separador.ui -o ui_main.py
pyside6-rcc icons.qrc -o icons_rc.py
```

## Autor

Desenvolvido por Rony Franzini.
