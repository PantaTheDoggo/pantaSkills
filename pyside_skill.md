# Skill: PySide6 GUI Development — Referência Consolidada

> **PySide6** (Qt6) — versão atual recomendada. Python 3.9+. Última revisão: 2026-05.

---

## Índice Rápido

| # | Seção |
|---|---|
| 1 | [Instalação](#instalação) |
| 2 | [Imports Essenciais](#imports-essenciais) |
| 3 | [Estrutura da Aplicação](#estrutura-da-aplicação) |
| 4 | [QWidget — Propriedades e Métodos](#qwidget--propriedades-e-métodos) |
| 5 | [QMainWindow](#qmainwindow) |
| 6 | [Qt Style Sheets (QSS)](#qt-style-sheets-qss) |
| 7 | [Layout Management](#layout-management) |
| 8 | [Sinais e Slots](#sinais-e-slots) |
| 9 | [Eventos](#eventos) |
| 10 | [Timers](#timers) |
| 11 | [Threading — QThread e QRunnable](#threading--qthread-e-qrunnable) |
| 12 | [Animações — QPropertyAnimation](#animações--qpropertyanimation) |
| 13 | [Referência de Widgets](#referência-de-widgets) |
| 14 | [Validação de Entrada](#validação-de-entrada) |
| 15 | [Desenhando Formas — QPainter](#desenhando-formas--qpainter) |
| 16 | [QPixmap e QImage](#qpixmap-e-qimage) |
| 17 | [Graphics View Framework](#graphics-view-framework) |
| 18 | [Model/View Architecture](#modelview-architecture) |
| 19 | [Drag and Drop](#drag-and-drop) |
| 20 | [Dialogs Built-in](#dialogs-built-in) |
| 21 | [QSettings — Configurações Persistentes](#qsettings--configurações-persistentes) |
| 22 | [QSystemTrayIcon](#qsystemtrayicon) |
| 23 | [QClipboard](#qclipboard) |
| 24 | [QSplashScreen](#qsplashscreen) |
| 25 | [Database — QtSql](#database--qtsql) |
| 26 | [QStandardItemModel](#qstandarditemmodel) |
| 27 | [QTreeWidget e QTableWidget](#qtreewidget-e-qtablewidget) |
| 28 | [QtNetwork — HTTP Requests](#qtnetwork--http-requests) |
| 29 | [QDesktopServices e QFileSystemWatcher](#qdesktopservices-e-qfilesystemwatcher) |
| 30 | [QUndoStack — Undo/Redo](#qundostack--undoredo) |
| 31 | [Sistema de Recursos (.qrc)](#sistema-de-recursos-qrc) |
| 32 | [Deploy e Empacotamento](#deploy-e-empacotamento) |
| 33 | [Migração para PySide6](#migração-pyside-legado--pyside6) |
| 34 | [Erros Comuns](#erros-comuns) |
| 35 | [Checklist Geral](#checklist-geral) |
| 36 | [Ferramentas de Desenvolvimento](#ferramentas-de-desenvolvimento) |
| 37 | [Qt Designer — Workflow Completo](#qt-designer--workflow-completo) |
| 38 | [Paradigma Model-View](#paradigma-model-view) |
| 39 | [Widgets Reutilizáveis e Customizados](#widgets-reutilizáveis-e-customizados) |
| 40 | [Temas e Estilização da Aplicação](#temas-e-estilização-da-aplicação) |
| 41 | [File I/O — Texto, CSV, JSON](#file-io--texto-csv-json) |
| 42 | [SQLite com sqlite3](#sqlite-com-sqlite3) |
| 43 | [REST APIs com requests + QThread](#rest-apis-com-requests--qthread) |
| 44 | [Multimídia — QMediaPlayer e QVideoWidget](#multimídia--qmediaplayer-e-qvideowidget) |
| 45 | [Projetos Completos](#projetos-completos) |
| 46 | [Multithreading e Tarefas Assíncronas](#multithreading-e-tarefas-assíncronas) |
| 47 | [GUIs Responsivas e Operações Longas](#guis-responsivas-e-operações-longas) |
| 48 | [Tratamento de Erros e Debugging](#tratamento-de-erros-e-debugging) |
| 49 | [Testes Automatizados de GUI](#testes-automatizados-de-gui) |
| 50 | [UX e Design de Interface](#ux-e-design-de-interface) |
| 51 | [Atalhos de Teclado, Menus e Toolbars](#atalhos-de-teclado-menus-e-toolbars) |
| 52 | [Acessibilidade](#acessibilidade) |
| 53 | [Internacionalização e Localização](#internacionalização-e-localização) |
| 54 | [Qt Quick / QML — Referência Básica](#qt-quick--qml--referência-básica) |
| A | [Troubleshooting e FAQ](#appendix-a--troubleshooting-e-faq) |


---

## Instalação

PySide6 é o binding oficial Python para o Qt6, mantido pela The Qt Company. Diferente do PyQt6 (licença GPL/comercial), o PySide6 usa a licença LGPL, o que permite uso em aplicações comerciais sem royalties. O pacote `PySide6` no PyPI instala automaticamente tudo que é necessário para começar.

**Instalar Python por plataforma:**

```bash
# macOS
brew install python

# Linux (Debian/Ubuntu)
sudo apt-get update && sudo apt-get install python3 python3-pip

# Windows: baixar de python.org e marcar "Add Python to PATH"
```

**Criar e ativar virtual environment (obrigatório):**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

**Regra**: sempre use virtual environment — o prompt exibirá `(venv)` como confirmação. Evite instalar PySide6 no Python do sistema.

```bash
pip install PySide6
pip install --upgrade PySide6          # atualizar
python -c "import PySide6; print(PySide6.__version__)"
```

Instala automaticamente: `PySide6-Essentials` + `PySide6-Addons` + `shiboken6`.

Para ambientes de produção, fixe a versão no `requirements.txt`:
```
PySide6>=6.7,<7
```

**Regra**: para projetos comerciais prefira PySide6 (LGPL); PyQt6 exige licença comercial separada para apps proprietários.

> (Fonte "pysideNew.txt" diverge: livro indica Python 3.8+ como requisito mínimo para PyQt6/PySide6; PySide6 6.x requer Python 3.9+.)

---

## Imports Essenciais

O Qt distribui suas classes em módulos separados (`QtCore`, `QtWidgets`, `QtGui`, etc.) para que apenas o necessário seja carregado em tempo de inicialização. Prefira sempre imports explícitos — eles tornam as dependências rastreáveis, evitam conflitos de nomes e são obrigatórios em produção.

```python
import sys
from PySide6.QtCore import (
    Qt, QTimer, QDateTime, QTime, QDate, QEvent, QThread, QObject,
    QRunnable, QThreadPool, QPropertyAnimation, QEasingCurve,
    QSortFilterProxyModel, QSettings, QRegularExpression, Signal, Slot
)
from PySide6.QtGui import (
    QIcon, QFont, QAction, QKeySequence, QPainter, QPen, QBrush, QColor,
    QPixmap, QImage, QIntValidator, QDoubleValidator,
    QRegularExpressionValidator, QCursor, QDesktopServices
)
from PySide6.QtWidgets import (
    QApplication, QWidget, QMainWindow,
    QLabel, QPushButton, QLineEdit, QTextEdit, QPlainTextEdit,
    QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QStackedLayout,
    QStatusBar, QToolBar, QMenuBar, QDockWidget,
    QMessageBox, QFileDialog, QInputDialog, QColorDialog, QFontDialog,
    QDialog, QCheckBox, QRadioButton, QButtonGroup, QComboBox,
    QSpinBox, QDoubleSpinBox, QDial, QSlider, QLCDNumber,
    QProgressBar, QProgressDialog, QScrollArea, QSplitter,
    QGroupBox, QTabWidget, QStackedWidget, QToolBox,
    QTableView, QListView, QTreeView, QListWidget, QListWidgetItem,
    QDataWidgetMapper, QCompleter, QSystemTrayIcon,
    QMdiArea, QMdiSubWindow, QGraphicsView, QGraphicsScene,
    QSplashScreen
)
from PySide6.QtSql import (
    QSqlDatabase, QSqlQuery, QSqlQueryModel,
    QSqlTableModel, QSqlRelationalTableModel, QSqlRelation, QSqlDriver
)
```

**Regra**: prefira imports explícitos. Nunca use `from PySide6.QtWidgets import *` em produção.

### Módulos Principais

| Módulo | Conteúdo |
|---|---|
| `QtCore` | Sinais/slots, timers, threads, event loop, tipos básicos, QSettings |
| `QtWidgets` | Widgets visuais: QWidget, QLabel, QPushButton, layouts, dialogs |
| `QtGui` | Fontes, ícones, cores, eventos de teclado/mouse, QPainter, QAction, QPixmap |
| `QtSql` | Banco de dados |
| `QtNetwork` | HTTP, TCP/UDP (`QNetworkAccessManager`) |
| `QtPrintSupport` | `QPrinter`, `QPrintDialog`, `QPrintPreviewDialog` |
| `QtMultimedia` | Áudio e vídeo (`QMediaPlayer`, `QCamera`) |
| `QtCharts` | Gráficos (`QChartView`, `QLineSeries`, `QPieSeries`) |
| `QtWebEngineWidgets` | Navegador embutido (`QWebEngineView`) |

---

## Estrutura da Aplicação

Toda aplicação Qt gira em torno do **event loop**: `QApplication.exec()` inicia um laço que captura eventos do SO (cliques, teclas, timers), despacha para os objetos corretos e aguarda o próximo evento. Deve existir exatamente **uma** instância de `QApplication` por processo, e ela precisa ser criada **antes** de qualquer widget — o programa só encerra quando o event loop termina.

### Mínima (script rápido)

```python
import sys
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtCore import Qt

app = QApplication(sys.argv)   # DEVE ser criado antes de qualquer widget
label = QLabel("Hello, World!")
label.setWindowTitle("Minha Primeira App")
label.setGeometry(300, 300, 250, 175)
label.setAlignment(Qt.AlignmentFlag.AlignCenter)
label.show()
sys.exit(app.exec())            # inicia o loop de eventos
```

### Padrão OOP (recomendado)

```python
import sys
from PySide6.QtWidgets import QApplication, QWidget

class SampleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        self.setWindowTitle("Sample Window")
        self.setGeometry(300, 300, 400, 300)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SampleWindow()
    window.show()
    sys.exit(app.exec())
```

### Boas práticas de inicialização

```python
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("MinhaApp")       # usado pelo QSettings
    app.setOrganizationName("MinhaOrg")      # usado pelo QSettings
    app.setOrganizationDomain("minhaorg.com")
    app.setApplicationVersion("1.0.0")
    app.setStyle("Fusion")                   # estilo multiplataforma consistente
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
```

**Regras críticas do QApplication**:
- `QApplication(sys.argv)` deve ser criado **antes** de qualquer widget
- Deve existir **apenas uma** instância por processo
- `app.exec()` inicia o loop de eventos — o programa fica bloqueado aqui
- `setApplicationName` + `setOrganizationName` habilitam `QSettings` sem parâmetros

### Organização do Projeto

Separe responsabilidades em módulos distintos para facilitar manutenção, testes e colaboração:

```
my_app/
├── main.py
├── views/
│   ├── main_window.py
│   ├── main_window.ui
│   └── dialogs.py
├── models/
│   ├── user_model.py
│   └── data_manager.py
├── controllers/
│   └── app_controller.py
├── resources/
│   ├── icons/
│   ├── images/
│   └── styles/
└── utils/
    └── helpers.py
```

| Diretório | Responsabilidade |
|---|---|
| `views/` | Arquivos `.ui` e classes de janela |
| `models/` | Dados e regras de negócio |
| `controllers/` | Lógica e coordenação |
| `resources/` | Imagens, ícones, stylesheets |
| `utils/` | Helpers e utilitários |

**Convenções:**
- `main_window.py` → classe `MainWindow`; `settings_dialog.py` → classe `SettingsDialog`
- `objectName` no `.ui` alinhado com variáveis Python correspondentes
- Paths de recursos relativos à raiz do projeto (não hard-coded)

---

## QWidget — Propriedades e Métodos

`QWidget` é a classe base de todo elemento visual no Qt. Cada widget possui uma área retangular, gerencia sua própria pintura e recebe eventos de input. Subclasses especializadas — como `QPushButton` ou `QLabel` — herdam esse comportamento e adicionam funcionalidade específica. Todo widget sem pai é uma janela independente; com pai, é embutido na área do pai.

```python
# Geometria
widget.setWindowTitle("Título")
widget.setGeometry(x, y, largura, altura)
widget.move(x, y)
widget.resize(largura, altura)
widget.setMinimumSize(largura, altura)
widget.setMaximumSize(largura, altura)
widget.setFixedSize(largura, altura)   # proíbe redimensionamento
widget.setMinimumWidth(250)
widget.setMinimumHeight(100)

# Visibilidade
widget.show()
widget.hide()
widget.setVisible(bool)
widget.close()
widget.repaint()     # força redesenho imediato (prefira update())
widget.update()      # agenda redesenho — mais eficiente

# Foco
widget.setFocus()
widget.clearFocus()
widget.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
```

### Ícone — QIcon

```python
from PySide6.QtGui import QIcon

self.setWindowIcon(QIcon("app_icon.png"))   # relativo ao CWD

# QIcon com temas do sistema
icon = QIcon.fromTheme("document-save")
```

| `QIcon.Mode` | Quando usar |
|---|---|
| `Normal` | Disponível, sem interação |
| `Disabled` | Indisponível |
| `Active` | Disponível e usuário interagindo |
| `Selected` | Item selecionado |

### Tooltip

```python
from PySide6.QtWidgets import QToolTip
from PySide6.QtGui import QFont

QToolTip.setFont(QFont("Arial", 9))
widget.setToolTip("Texto do <b>tooltip</b>")   # suporta HTML básico
```

### Centralizar na Tela

```python
def center(self) -> None:
    screen = QApplication.primaryScreen().availableGeometry()
    frame  = self.frameGeometry()
    frame.moveCenter(screen.center())
    self.move(frame.topLeft())
# Chamar center() ANTES de show()
```

### Cursores

```python
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt

widget.setCursor(Qt.CursorShape.WaitCursor)
widget.setCursor(Qt.CursorShape.PointingHandCursor)
widget.unsetCursor()
```

---

## QMainWindow

`QMainWindow` oferece uma estrutura de janela pré-definida com zonas dedicadas para barra de menu, toolbars, widget central, painéis laterais (*dock widgets*) e barra de status — poupando o trabalho de compor esse layout manualmente com `QWidget`. O widget central (obrigatório) é a área principal de trabalho da aplicação.

```
QMainWindow
├── Menu Bar       (QMenuBar — topo)
├── Toolbar(s)     (QToolBar — sob o menu, lados ou baixo)
├── Central Widget (área central — obrigatório)
├── Dock Widgets   (laterais/flutuantes — opcional)
└── Status Bar     (QStatusBar — rodapé)
```

```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 800, 600)

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)    # OBRIGATÓRIO

        self._create_actions()
        self._create_menus()
        self._create_toolbar()
        self._create_status_bar()
        self._create_dock_widgets()
```

### Status Bar

```python
def _create_status_bar(self):
    bar = self.statusBar()
    bar.showMessage("Pronto", 2000)   # some após 2 s; 0 = persiste

    self.perm_label = QLabel("v1.0")
    bar.addPermanentWidget(self.perm_label)  # lado direito, não é apagado por showMessage

# Uso posterior
self.statusBar().showMessage("Arquivo salvo", 2000)
```

### Menu Bar + QAction

```python
def _create_actions(self):
    self.new_action = QAction(
        QIcon("new.png"), "&New", self,
        shortcut=QKeySequence.StandardKey.New,
        statusTip="Criar arquivo",
        triggered=self._new_file
    )
    self.exit_action = QAction(
        "E&xit", self,
        shortcut="Ctrl+Q",
        triggered=self.close
    )

def _create_menus(self):
    file_menu = self.menuBar().addMenu("&File")
    file_menu.addAction(self.new_action)
    file_menu.addSeparator()
    file_menu.addAction(self.exit_action)

    edit_menu = self.menuBar().addMenu("&Edit")
    edit_menu.addAction(QAction(
        "C&opy", self,
        shortcut=QKeySequence.StandardKey.Copy,
        triggered=self.text_edit.copy
    ))
```

### Atalhos padrão QKeySequence

```python
QKeySequence.StandardKey.New        # Ctrl+N
QKeySequence.StandardKey.Open       # Ctrl+O
QKeySequence.StandardKey.Save       # Ctrl+S
QKeySequence.StandardKey.SaveAs     # Ctrl+Shift+S
QKeySequence.StandardKey.Close      # Ctrl+W
QKeySequence.StandardKey.Cut        # Ctrl+X
QKeySequence.StandardKey.Copy       # Ctrl+C
QKeySequence.StandardKey.Paste      # Ctrl+V
QKeySequence.StandardKey.Undo       # Ctrl+Z
QKeySequence.StandardKey.Redo       # Ctrl+Y
QKeySequence.StandardKey.SelectAll  # Ctrl+A
QKeySequence.StandardKey.Find       # Ctrl+F
QKeySequence.StandardKey.Print      # Ctrl+P
```

### Toolbar

```python
def _create_toolbar(self):
    toolbar = self.addToolBar("Main")
    toolbar.setObjectName("MainToolbar")   # necessário para salvar estado
    toolbar.addAction(self.new_action)
    toolbar.addSeparator()

    # Controle de posicionamento
    toolbar.setAllowedAreas(Qt.ToolBarArea.TopToolBarArea | Qt.ToolBarArea.BottomToolBarArea)
    toolbar.setMovable(True)

    # Widget diretamente na toolbar
    from PySide6.QtWidgets import QLineEdit
    search = QLineEdit()
    search.setPlaceholderText("Buscar...")
    search.setMaximumWidth(200)
    toolbar.addWidget(search)
```

### Dock Widgets

```python
def _create_dock_widgets(self):
    from PySide6.QtWidgets import QDockWidget, QListWidget
    dock = QDockWidget("Painel", self)
    dock.setObjectName("PainelDock")       # necessário para salvar estado
    dock.setWidget(QListWidget())
    dock.setAllowedAreas(
        Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea
    )
    self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock)
```

### Salvar/Restaurar Geometria e Estado

```python
def closeEvent(self, event):
    settings = QSettings()
    settings.setValue("window/geometry", self.saveGeometry())
    settings.setValue("window/state", self.saveState())
    super().closeEvent(event)

def _restore_window(self):
    settings = QSettings()
    if geom := settings.value("window/geometry"):
        self.restoreGeometry(geom)
    if state := settings.value("window/state"):
        self.restoreState(state)
```

---

## Qt Style Sheets (QSS)

QSS usa sintaxe similar ao CSS para separar a aparência visual da lógica da aplicação. Pode ser aplicado globalmente no `QApplication` (afeta todos os widgets) ou em widgets individuais (sobrepõe o estilo global). Pseudo-estados como `:hover` e `:disabled` permitem estilizar comportamentos interativos sem código Python adicional.

### Aplicação global

```python
app.setStyleSheet("""
    QMainWindow {
        background-color: #1e1e1e;
    }
    QPushButton {
        background-color: #3498db;
        color: white;
        border: none;
        padding: 6px 16px;
        border-radius: 4px;
        font-size: 13px;
    }
    QPushButton:hover {
        background-color: #2980b9;
    }
    QPushButton:pressed {
        background-color: #1f618d;
    }
    QPushButton:disabled {
        background-color: #95a5a6;
    }
    QLineEdit {
        border: 1px solid #bdc3c7;
        border-radius: 4px;
        padding: 4px 8px;
        selection-background-color: #3498db;
    }
    QLineEdit:focus {
        border-color: #3498db;
    }
""")
```

### Seletores comuns

```python
# Por tipo
"QPushButton { ... }"

# Por nome de objeto
button.setObjectName("saveBtn")
"QPushButton#saveBtn { background-color: green; }"

# Por classe-filha
"QDialog QPushButton { font-size: 12px; }"

# Por propriedade dinâmica
button.setProperty("role", "danger")
"QPushButton[role='danger'] { background-color: #e74c3c; }"
# Forçar re-avaliação após mudar propriedade:
button.style().unpolish(button)
button.style().polish(button)
```

### Pseudo-estados úteis

| Pseudo-estado | Quando ativa |
|---|---|
| `:hover` | Cursor sobre o widget |
| `:pressed` | Botão pressionado |
| `:checked` | QCheckBox/QRadioButton marcado |
| `:disabled` | Widget desabilitado |
| `:focus` | Widget com foco |
| `:enabled` | Widget habilitado |
| `:selected` | Item selecionado em lista/combo |
| `:on` / `:off` | Estado ligado/desligado (toggle buttons) |

### Carregar QSS de arquivo

```python
with open("style.qss", "r") as f:
    app.setStyleSheet(f.read())
```

### Tema escuro rápido (Fusion + palette)

```python
from PySide6.QtGui import QPalette, QColor

app.setStyle("Fusion")
palette = QPalette()
palette.setColor(QPalette.ColorRole.Window,          QColor(45, 45, 45))
palette.setColor(QPalette.ColorRole.WindowText,      QColor(220, 220, 220))
palette.setColor(QPalette.ColorRole.Base,            QColor(35, 35, 35))
palette.setColor(QPalette.ColorRole.AlternateBase,   QColor(53, 53, 53))
palette.setColor(QPalette.ColorRole.Button,          QColor(53, 53, 53))
palette.setColor(QPalette.ColorRole.ButtonText,      QColor(220, 220, 220))
palette.setColor(QPalette.ColorRole.Highlight,       QColor(42, 130, 218))
palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))
app.setPalette(palette)
```

### Sub-Controles QSS

Sub-controles (`::nome`) estilizam partes internas de widgets compostos. `subcontrol-origin` define a área de referência e `subcontrol-position` o canto/lado dentro dela.

```css
/* áreas de origem: margin | border | padding | content */
QSpinBox::down-button {
    image: url(:/images/spindown.png);
    subcontrol-origin: padding;
    subcontrol-position: right bottom;
}
QSpinBox::up-button {
    subcontrol-origin: border;
    subcontrol-position: right top;
}
```

### Gradiente Linear e border-image

```css
/* qlineargradient — spread: pad | reflect | repeat; x1/y1 e x2/y2 em 0.0–1.0 */
#panel {
    background-color: qlineargradient(spread:reflect,
        x1:0.5, y1:0, x2:0, y2:0,
        stop:0 rgba(91, 204, 233, 100),
        stop:1 rgba(32, 80, 96, 100));
}

/* border-image: escala a imagem com o widget (diferente de background-image, que não escala) */
#centralWidget { border-image: url(:/images/bg.png); }
```

> (Fonte "qt6_cpp_cookbook_skill" acrescenta: no QSS, `rgba(R,G,B,A)` usa Alpha no intervalo 0–255 — diferente do CSS padrão que usa 0.0–1.0.)

> (Fonte "qt6_cpp_cookbook_skill" acrescenta: pseudo-estados adicionais de QPushButton — `:open` (menu popup aberto), `:flat` (botão flat), `:default` (botão padrão do diálogo); e `:active` (widget em janela ativa) aplicável a qualquer widget.)

---

## Layout Management

Gerenciadores de layout descrevem *relações* entre widgets em vez de posições absolutas: o Qt calcula automaticamente onde cada elemento deve ficar e o redimensiona quando a janela muda. Isso garante que a interface funcione corretamente em diferentes resoluções, escalas de DPI e sistemas operacionais — ao contrário do posicionamento absoluto, que é estático e não se adapta.

### Absolute Positioning (evitar)

```python
widget.move(x, y)
widget.resize(w, h)
# Não responde a resize, mudanças de fonte ou DPI. Somente para protótipos rápidos.
```

### QHBoxLayout / QVBoxLayout

```python
# Horizontal
layout = QHBoxLayout()
layout.addWidget(QPushButton("Button 1"))
layout.addWidget(QPushButton("Button 2"))
self.setLayout(layout)

# Vertical com espaço elástico
layout = QVBoxLayout()
layout.addWidget(QPushButton("Top"))
layout.addStretch()
layout.addWidget(QPushButton("Bottom"))
self.setLayout(layout)
```

| Método | Descrição |
|---|---|
| `addWidget(widget)` | Adiciona widget |
| `addWidget(w, stretch)` | Adiciona com fator de estiramento |
| `addSpacing(px)` | Espaço fixo em pixels |
| `addStretch(factor=0)` | Espaço elástico |
| `addLayout(layout)` | Sublayout aninhado |
| `setContentsMargins(l, t, r, b)` | Margem externa |
| `setSpacing(px)` | Espaço entre widgets |
| `insertWidget(idx, widget)` | Insere em posição específica |

### QGridLayout

```python
layout = QGridLayout()
layout.addWidget(QPushButton("1"), 0, 0)           # linha, coluna
layout.addWidget(QPushButton("2"), 0, 1)
layout.addWidget(QPushButton("3"), 1, 0, 1, 2)     # rowspan=1, colspan=2
layout.setColumnStretch(0, 1)                       # coluna 0 elástica
layout.setRowMinimumHeight(0, 40)
self.setLayout(layout)
```

### QFormLayout

```python
layout = QFormLayout()
layout.addRow("Nome:", QLineEdit())
layout.addRow("Senha:", QLineEdit())
layout.addRow(QLabel("Observação:"), QTextEdit())
layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
self.setLayout(layout)
```

### QStackedLayout / QStackedWidget

```python
# QStackedLayout — em um widget container
stack = QStackedLayout()
stack.addWidget(page1)   # índice 0
stack.addWidget(page2)   # índice 1
combo.currentIndexChanged.connect(stack.setCurrentIndex)

# QStackedWidget — widget autônomo
stacked = QStackedWidget()
stacked.addWidget(page1)
stacked.setCurrentIndex(1)
stacked.setCurrentWidget(page2)
```

### QSplitter

```python
from PySide6.QtWidgets import QSplitter

splitter = QSplitter(Qt.Orientation.Horizontal)
splitter.addWidget(left_widget)
splitter.addWidget(right_widget)
splitter.setSizes([300, 500])         # tamanhos iniciais em pixels
splitter.setStretchFactor(1, 1)       # o segundo painel estica
self.setCentralWidget(splitter)
```

> (Fonte "qt6_cpp_cookbook_skill" acrescenta: `QSpacerItem` pode ser instanciado diretamente quando se precisa de tamanho e política de expansão explícitos — `QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)` — mas `addStretch()` e `addSpacing()` cobrem a maioria dos casos.)

---

## Sinais e Slots

Sinais e slots são o mecanismo central de comunicação entre objetos no Qt. Um **sinal** é emitido quando algo acontece (botão clicado, valor alterado); um **slot** é qualquer callable que reage a esse sinal. A conexão é feita em tempo de execução e os objetos não precisam conhecer um ao outro diretamente — baixo acoplamento por design. Um sinal pode conectar-se a múltiplos slots e vice-versa.

### Sintaxe moderna PySide6

```python
# Conectar
button.clicked.connect(self.my_slot)
timer.timeout.connect(self.update_time)
dial.valueChanged.connect(spin.setValue)
spin.valueChanged.connect(dial.setValue)
line_edit.textChanged.connect(self.on_text_changed)
line_edit.returnPressed.connect(self.on_enter)

# Desconectar
button.clicked.disconnect(self.my_slot)
button.clicked.disconnect()    # desconecta todos os slots

# Lambda (use com cuidado — difícil de desconectar)
button.clicked.connect(lambda: print("clicado"))
```

### Sinal customizado

```python
from PySide6.QtCore import QObject, Signal

class MyWorker(QObject):
    started   = Signal()
    progress  = Signal(int)          # int 0-100
    finished  = Signal(str)          # resultado como string
    error     = Signal(Exception)    # sinal com tipo qualquer

    def run(self):
        self.started.emit()
        for i in range(100):
            self.progress.emit(i + 1)
        self.finished.emit("concluído")
```

### Decorator @Slot

```python
from PySide6.QtCore import Slot

class MyWindow(QWidget):
    @Slot(int)
    def on_value_changed(self, value: int):
        print(f"Novo valor: {value}")
```

O decorator `@Slot` é opcional em PySide6, mas melhora performance e introspection.

**Regra**: sinais são atributos de **classe** (`Signal()`), não de instância. O acesso via `self.signal.emit()` funciona porque PySide6 os promove automaticamente para descriptors de instância.

### Conexões possíveis

- Um sinal → múltiplos slots
- Múltiplos sinais → um slot
- Sinal → outro sinal (encadeamento)
- Sinal com argumento → slot sem argumento (argumentos extras ignorados)

### blockSignals

```python
# Evitar loops de sinalização (ex: dial↔spin)
spin.blockSignals(True)
spin.setValue(50)
spin.blockSignals(False)
```

### Signals de Widgets Comuns

| Widget | Signals |
|---|---|
| `QPushButton` | `clicked()`, `clicked(bool)`, `pressed()`, `released()`, `toggled(bool)` |
| `QComboBox` | `activated(int)`, `currentIndexChanged(int)`, `currentTextChanged(str)`, `highlighted(int)` |
| `QLineEdit` | `textChanged(str)`, `textEdited(str)`, `editingFinished()`, `returnPressed()` |
| `QSpinBox` | `valueChanged(int)`, `valueChanged(str)` |
| `QSlider` | `valueChanged(int)`, `sliderMoved(int)`, `sliderPressed()`, `sliderReleased()` |

> (Fonte "qt6_cpp_cookbook_skill" acrescenta: em lambdas conectadas a sinais de longa duração, capture apenas as variáveis necessárias — captura excessiva pode manter objetos vivos além do esperado e dificultar a desconexão.)

---

## Eventos

No Qt, toda interação com o usuário e notificação do SO chegam como objetos `QEvent` despachados pelo event loop (introduzido em [Estrutura da Aplicação](#estrutura-da-aplicação)). Cada widget pode sobrescrever handlers específicos (`keyPressEvent`, `mousePressEvent`, etc.) para tratar o que lhe interessa e chamar `super()` para propagar o restante. Para monitorar eventos de *outros* widgets sem subclassificar, use event filters.

### Event Loop

```
QApplication.exec()  →  busca eventos nativos  →  converte em QEvent
→  despacha para QObject alvo  →  aguarda próximo evento
```

**Regra crítica**: reaja rapidamente e retorne ao loop. Para operações longas use `QThread`.

```python
from PySide6.QtCore import QCoreApplication
QCoreApplication.processEvents()    # força processar eventos pendentes (use com cuidado)
```

### Reimplementando Event Handlers

```python
class MyWidget(QWidget):
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()
        else:
            super().keyPressEvent(event)   # propaga eventos não tratados

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.close()

    def mousePressEvent(self, event):
        print(f"Clique em ({event.position().x():.0f}, {event.position().y():.0f})")

    def resizeEvent(self, event):
        print(f"Redimensionado para {event.size().width()}×{event.size().height()}")

    def closeEvent(self, event):
        # Confirmar fechamento
        resp = QMessageBox.question(self, "Sair", "Confirmar saída?")
        if resp == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def mouseMoveEvent(self, event):
        print(f"Mouse em ({event.position().x():.0f}, {event.position().y():.0f})")

    def wheelEvent(self, event):
        delta = event.angleDelta().y()
        print(f"Scroll: {delta}")
```

> (Fonte "qt6_cpp_cookbook_skill" acrescenta: para que `mouseMoveEvent` seja disparado sem botão pressionado, chame `setMouseTracking(True)` tanto na janela principal quanto no `centralWidget` — definir apenas em um dos dois não é suficiente.)

```python
self.setMouseTracking(True)
self.centralWidget().setMouseTracking(True)
```

### Teclas modificadoras

```python
def keyPressEvent(self, event):
    if event.key() == Qt.Key.Key_S and \
       event.modifiers() == Qt.KeyboardModifier.ControlModifier:
        self._save()

    # Combinação múltipla (Ctrl+Shift+Z)
    if event.key() == Qt.Key.Key_Z and \
       event.modifiers() == (Qt.KeyboardModifier.ControlModifier |
                             Qt.KeyboardModifier.ShiftModifier):
        self._redo()
```

| Modificador | Tecla |
|---|---|
| `Qt.KeyboardModifier.ControlModifier` | Ctrl |
| `Qt.KeyboardModifier.ShiftModifier` | Shift |
| `Qt.KeyboardModifier.AltModifier` | Alt |
| `Qt.KeyboardModifier.MetaModifier` | Win / Cmd |

### Reimplementando event() — para Tab e setas

```python
from PySide6.QtCore import QEvent

def event(self, event):
    if event.type() == QEvent.Type.KeyRelease and \
       event.key() == Qt.Key.Key_Tab:
        self.next_field.setFocus()
        return True
    return super().event(event)
```

### Event Filters

```python
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.line_edit.installEventFilter(self)   # monitora eventos de line_edit

    def eventFilter(self, receiver, event):
        if receiver is self.line_edit and \
           event.type() == QEvent.Type.KeyPress and \
           event.key() == Qt.Key.Key_Return:
            self._submit()
            return True
        return super().eventFilter(receiver, event)  # SEMPRE retornar super
```

---

## Timers

`QTimer` integra-se ao event loop do Qt (ver [Estrutura da Aplicação](#estrutura-da-aplicação)), disparando o sinal `timeout` em intervalos regulares sem bloquear a interface. Por ser baseado no mesmo event loop, não exige threads adicionais para tarefas periódicas simples — a regra é que o slot de `timeout` deve retornar rapidamente para não congelar a UI.

```python
from PySide6.QtCore import QTimer, QDateTime, QTime

# Timer repetitivo
timer = QTimer(self)
timer.timeout.connect(self.update_time)
timer.start(1000)     # a cada 1000 ms
timer.stop()
timer.setInterval(500)   # muda intervalo sem reiniciar

# Timer de disparo único
QTimer.singleShot(2000, self.my_slot)

# Hora atual
now = QDateTime.currentDateTime()
now.toString("hh:mm:ss")    # "14:30:05"
now.toString("dd/MM/yyyy")  # "18/05/2026"
QTime.currentTime().toString("hh:mm:ss")

# Parse de string para QDateTime
dt = QDateTime.fromString("2024-05-21 14:30:00", "yyyy-MM-dd hh:mm:ss")
s = QDateTime.currentDateTime().toString("dd/MM/yy hh:mm")
```

**Interoperabilidade com `datetime` nativo**:
```python
from datetime import datetime

# datetime → string → QDateTime
py_dt = datetime(2024, 5, 21, 14, 30, 0)
s = py_dt.strftime("%Y-%m-%d %H:%M:%S")
qdt = QDateTime.fromString(s, "yyyy-MM-dd hh:mm:ss")

# QDateTime → string → datetime
s2 = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
py_dt2 = datetime.strptime(s2, "%Y-%m-%d %H:%M:%S")
```

### QLCDNumber

```python
from PySide6.QtWidgets import QLCDNumber

display = QLCDNumber(self)
display.setSegmentStyle(QLCDNumber.SegmentStyle.Filled)  # Outline / Filled / Flat
display.setDigitCount(8)
display.display("14:30:05")
```

---

## Threading — QThread e QRunnable

A regra fundamental do Qt é que **apenas a thread principal pode acessar widgets**. Para operações longas (I/O, cálculos pesados) que travariam o event loop (ver [Estrutura da Aplicação](#estrutura-da-aplicação)), mova o trabalho para uma thread separada e use sinais (ver [Sinais e Slots](#sinais-e-slots)) para enviar resultados de volta à UI — nunca toque em widgets diretamente de outra thread.

### Padrão recomendado: Worker + moveToThread

Use quando precisar de um canal de comunicação bidirecional (sinais de progresso, resultado).

```python
from PySide6.QtCore import QObject, QThread, Signal, Slot

class Worker(QObject):
    started  = Signal()
    progress = Signal(int)
    result   = Signal(object)
    error    = Signal(str)
    finished = Signal()

    def __init__(self, data):
        super().__init__()
        self._data = data

    @Slot()
    def run(self):
        self.started.emit()
        try:
            for i, item in enumerate(self._data):
                # ... processar item ...
                self.progress.emit(int((i + 1) / len(self._data) * 100))
            self.result.emit("concluído")
        except Exception as exc:
            self.error.emit(str(exc))
        finally:
            self.finished.emit()


class MainWindow(QMainWindow):
    def _start_task(self):
        self.thread = QThread()
        self.worker = Worker(data=[1, 2, 3])

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.worker.progress.connect(self.progress_bar.setValue)
        self.worker.result.connect(self._on_result)
        self.worker.error.connect(self._on_error)

        self.thread.start()

    def _on_result(self, value):
        self.statusBar().showMessage(f"Resultado: {value}", 3000)

    def _on_error(self, msg):
        QMessageBox.critical(self, "Erro", msg)
```

### QRunnable + QThreadPool (fire-and-forget)

Use para tarefas independentes sem comunicação de retorno.

```python
from PySide6.QtCore import QRunnable, QThreadPool, Slot

class MyTask(QRunnable):
    def __init__(self, n: int):
        super().__init__()
        self._n = n

    @Slot()
    def run(self):
        result = sum(range(self._n))
        print(f"Resultado: {result}")   # não pode emitir sinais diretamente aqui

pool = QThreadPool.globalInstance()
pool.setMaxThreadCount(4)
pool.start(MyTask(1_000_000))
```

### QMutex — proteção de dados compartilhados

```python
from PySide6.QtCore import QMutex, QMutexLocker

mutex = QMutex()

# Lock manual
mutex.lock()
shared_data += 1
mutex.unlock()

# RAII — preferível (garante unlock mesmo com exceção)
with QMutexLocker(mutex):
    shared_data += 1
```

### QReadWriteLock — leitura simultânea, escrita exclusiva

```python
from PySide6.QtCore import QReadWriteLock, QReadLocker, QWriteLocker

rw_lock = QReadWriteLock()

with QReadLocker(rw_lock):    # múltiplos threads simultâneos
    value = shared_data

with QWriteLocker(rw_lock):   # exclusivo — bloqueia leitores e escritores
    shared_data = new_value
```

**Regra**: use `QReadWriteLock` quando o dado é lido muito mais frequentemente do que escrito.

### concurrent.futures (alternativa a QtConcurrent — não disponível no PySide6)

```python
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=4)
future = executor.submit(my_function, arg1, arg2)
result = future.result()   # bloqueia até concluir (use em thread separada ou com callback)
```

### Regras de Thread Safety

- **Nunca** acesse ou modifique widgets fora da thread principal.
- Use sinais para enviar resultados de volta para a UI.
- `QObject.moveToThread()` transfere a afinidade de thread do objeto.
- `QtConcurrent` **não está disponível** no PySide6 — use `QThreadPool`/`concurrent.futures`.
- Evite `QCoreApplication.processEvents()` como substituto de threading.

---

## Animações — QPropertyAnimation

`QPropertyAnimation` anima qualquer `Q_PROPERTY` de um `QObject` (geometria, opacidade, cor) interpolando valores ao longo do tempo com uma curva de *easing*. O controle de tempo é gerenciado pelo event loop (ver [Estrutura da Aplicação](#estrutura-da-aplicação)), sem necessidade de threads. Para animações compostas, use `QSequentialAnimationGroup` (em série) ou `QParallelAnimationGroup` (em paralelo).

```python
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QRect, QPoint

# Mover widget
anim = QPropertyAnimation(widget, b"geometry")
anim.setDuration(600)
anim.setStartValue(QRect(0, 0, 100, 30))
anim.setEndValue(QRect(250, 250, 100, 30))
anim.setEasingCurve(QEasingCurve.Type.OutBounce)
anim.start()

# Fade in/out (requer GraphicsEffect)
from PySide6.QtWidgets import QGraphicsOpacityEffect
effect = QGraphicsOpacityEffect(widget)
widget.setGraphicsEffect(effect)

fade = QPropertyAnimation(effect, b"opacity")
fade.setDuration(400)
fade.setStartValue(0.0)
fade.setEndValue(1.0)
fade.setEasingCurve(QEasingCurve.Type.InOutQuad)
fade.start()
```

### Curvas de easing comuns

| Curva | Comportamento |
|---|---|
| `Linear` | Velocidade constante |
| `InOutQuad` | Acelera e desacelera suavemente |
| `OutBounce` | Quica ao final |
| `OutElastic` | Elástico ao final |
| `InOutCubic` | Suave aceleração/desaceleração mais pronunciada |
| `OutBack` | Ultrapassa o alvo levemente antes de estabilizar |

### QSequentialAnimationGroup / QParallelAnimationGroup

```python
from PySide6.QtCore import QSequentialAnimationGroup, QParallelAnimationGroup

# Sequencial
group = QSequentialAnimationGroup()
group.addAnimation(anim1)
group.addPause(200)          # pausa de 200ms entre animações
group.addAnimation(anim2)
group.start()

# Paralelo
parallel = QParallelAnimationGroup()
parallel.addAnimation(move_anim)
parallel.addAnimation(fade_anim)
parallel.start()
```

> (Fonte "qt6_cpp_cookbook_skill" acrescenta: grupos de animação podem ser aninhados — um `QParallelAnimationGroup` pode ser adicionado a um `QSequentialAnimationGroup`, criando hierarquias; `start()` deve ser chamado apenas no grupo externo.)

### QEasingCurve — parâmetros avançados

```python
from PySide6.QtCore import QEasingCurve

curve = QEasingCurve()
curve.setType(QEasingCurve.Type.OutBounce)
curve.setAmplitude(1.00)    # intensidade do bounce/spring
curve.setOvershoot(1.70)    # quanto ultrapassa o valor final
curve.setPeriod(0.30)       # frequência (menor = mais rápido)
anim.setEasingCurve(curve)

anim.setLoopCount(-1)       # -1 = loop infinito; N = N repetições
```

> (Fonte "qt6_cpp_cookbook_skill" acrescenta: amplitude, overshoot e period não se aplicam a todos os tipos — `OutBounce` usa amplitude; `OutElastic` usa amplitude e period; `OutBack` usa overshoot.)

Curvas adicionais: `InQuad`, `OutQuad`, `InBack`, `InElastic`, `OutCirc`, `InOutSine`.

### QStateMachine

```python
from PySide6.QtStateMachine import QStateMachine, QState, QEventTransition
from PySide6.QtCore import QEvent

machine = QStateMachine(self)
s1 = QState()
s2 = QState()

# assignProperty: valor que a propriedade assume ao entrar no estado
s1.assignProperty(label, "text", "Estado: 1")
s2.assignProperty(label, "text", "Estado: 2")

# Transição por evento de mouse + animação suavizada
anim = QPropertyAnimation(button, b"geometry")
anim.setEasingCurve(QEasingCurve.Type.OutBounce)

t1 = QEventTransition(button, QEvent.Type.MouseButtonPress)
t1.setTargetState(s2)
t1.addAnimation(anim)
s1.addTransition(t1)

t2 = QEventTransition(button, QEvent.Type.MouseButtonPress)
t2.setTargetState(s1)
t2.addAnimation(anim)
s2.addTransition(t2)

machine.addState(s1)
machine.addState(s2)
machine.setInitialState(s1)
machine.start()
```

**Regra**: use `assignProperty()` em vez de `setStartValue`/`setEndValue` na `QStateMachine` — a animação associada à transição interpolará automaticamente entre os valores dos estados de/para.

### Animação com QTimer — atualização manual

```python
self.timer = QTimer(self)
self.timer.setInterval(16)   # ~60 fps
self.timer.timeout.connect(self.update_animation)
self.timer.start()

def update_animation(self):
    # atualizar propriedades manualmente
    self.update()   # agenda repaint via paintEvent
```

### Métodos de animação Qt

| Método | Uso típico |
|---|---|
| `QTimer` | Mudança manual de propriedade por tick (~60 fps) |
| `QPropertyAnimation` | Interpolação automática com easing curve |
| `QStateMachine` | Animações acionadas por transições de estado |
| Graphics View | Animação 2D de alta performance via `advance()` |
| QML Animators | Animações na render thread sem bloquear UI |

---

## Referência de Widgets

Todos os widgets herdam de `QWidget` (ver [QWidget — Propriedades e Métodos](#qwidget--propriedades-e-métodos)) e compartilham a mesma base de geometria, visibilidade e eventos. A escolha entre um widget "simples" (ex.: `QListWidget`) e a combinação model/view (ex.: `QListView` + modelo) depende do volume de dados e da necessidade de reuso: widgets simples são convenientes para listas estáticas; o padrão model/view é preferível quando os dados são dinâmicos ou compartilhados entre múltiplas views.

`from PySide6.QtWidgets import ...`

### Entrada e Exibição

| Widget | Descrição |
|---|---|
| `QLabel` | Texto ou imagem estática; suporta HTML |
| `QLineEdit` | Campo de texto de uma linha |
| `QTextEdit` | Área de texto multilinha (HTML ou plain text) |
| `QPlainTextEdit` | Área de texto plain text (performance melhor que QTextEdit) |
| `QCheckBox` | Caixa de marcação (pode ter estado tristate) |
| `QRadioButton` | Botão de seleção exclusiva dentro do grupo |
| `QPushButton` | Botão de comando |
| `QToolButton` | Botão compacto (toolbars); suporta menu popup |
| `QComboBox` | Lista suspensa; `setEditable(True)` para editar |
| `QSpinBox` | Inteiros com setas |
| `QDoubleSpinBox` | Floats com setas |
| `QDial` | Controle circular (potenciômetro) |
| `QSlider` | Deslizador horizontal ou vertical |
| `QLCDNumber` | Display estilo LCD |
| `QProgressBar` | Barra de progresso; `setRange(0,0)` = indeterminado |
| `QDateEdit` | Edição de data |
| `QTimeEdit` | Edição de hora |
| `QDateTimeEdit` | Edição de data e hora |
| `QFontComboBox` | ComboBox de famílias de fonte |
| `QCalendarWidget` | Calendário mensal interativo |
| `QScrollBar` | Barra de rolagem independente |
| `QKeySequenceEdit` | Captura atalho de teclado do usuário |

### Exibição de Dados (Model/View)

| Widget | Descrição |
|---|---|
| `QListView` | View de lista sobre modelo |
| `QTableView` | View de tabela sobre modelo |
| `QTreeView` | View de árvore sobre modelo |
| `QColumnView` | View de colunas hierárquica |
| `QListWidget` | Lista simples (sem modelo externo) |
| `QTableWidget` | Tabela simples (sem modelo externo) |
| `QTreeWidget` | Árvore simples (sem modelo externo) |
| `QDataWidgetMapper` | Mapeia colunas do modelo para widgets |

### Organizadores

| Widget | Descrição |
|---|---|
| `QGroupBox` | Frame com título e borda |
| `QButtonGroup` | Agrupa botões (exclusividade configurável) |
| `QSplitter` | Divide área em painéis redimensionáveis |
| `QStackedWidget` | Pilha — um widget visível por vez |
| `QTabWidget` | Pilha com abas |
| `QToolBox` | Coluna de itens expansíveis (acordeão) |
| `QScrollArea` | Área rolável para widgets grandes |
| `QFrame` | Frame com estilos de borda variados |

---

## Validação de Entrada

A validação de entrada deve ocorrer na borda do sistema — antes que dados externos entrem na lógica da aplicação. O Qt oferece três estratégias complementares: `QValidator` (restringe caracteres durante a digitação), `setInputMask()` (força um formato fixo de caractere por posição) e `QCompleter` (sugere valores válidos), que podem ser combinados no mesmo campo.

### QValidator

```python
from PySide6.QtGui import QIntValidator, QDoubleValidator, QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

# Inteiro 0–100
line_edit.setValidator(QIntValidator(0, 100, self))

# Float com 2 casas decimais
line_edit.setValidator(QDoubleValidator(0.0, 9999.99, 2, self))

# Regex (ex: e-mail simples)
re = QRegularExpression(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")
line_edit.setValidator(QRegularExpressionValidator(re, self))
```

### Input Masks

```python
# Máscara de IP
line_edit.setInputMask("000.000.000.000;_")

# Telefone BR
line_edit.setInputMask("(99) 99999-9999;_")

# Data ISO
line_edit.setInputMask("9999-99-99;_")
```

| Caractere | Aceita |
|---|---|
| `9` | Dígito (0–9), obrigatório |
| `0` | Dígito, opcional |
| `A` | Letra ou dígito, obrigatório |
| `a` | Letra ou dígito, opcional |
| `N` | Letra, obrigatório |
| `n` | Letra, opcional |
| `X` | Qualquer caractere, obrigatório |
| `x` | Qualquer caractere, opcional |

### Outras propriedades de QLineEdit

```python
line_edit.setMaxLength(50)
line_edit.setPlaceholderText("Digite aqui...")
line_edit.setEchoMode(QLineEdit.EchoMode.Password)     # campo de senha
line_edit.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
line_edit.setReadOnly(True)
line_edit.setAlignment(Qt.AlignmentFlag.AlignRight)
```

### QCompleter

```python
from PySide6.QtWidgets import QCompleter

words = ["Python", "PySide6", "PyQt6", "Qt"]
completer = QCompleter(words, self)
completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
line_edit.setCompleter(completer)

# Completer baseado em modelo
from PySide6.QtCore import QStringListModel
model = QStringListModel(["alpha", "beta", "gamma"])
completer = QCompleter(model, self)
line_edit.setCompleter(completer)
```

---

## Desenhando Formas — QPainter

`QPainter` é a API de desenho 2D do Qt: linhas, retângulos, elipses, texto e caminhos bezier são todos desenhados com o mesmo objeto configurado com caneta (`QPen`) e pincel (`QBrush`). O código de desenho deve ficar **dentro do `paintEvent()`**; para widgets customizados, `self.update()` agenda um repaint quando os dados mudam. Passe `self` diretamente ao construtor — não use `begin()`/`end()` em `QWidget`.

```python
from PySide6.QtGui import QPainter, QPen, QBrush, QColor, QPainterPath
from PySide6.QtCore import Qt, QRect, QRectF, QPointF

def paintEvent(self, event):
    painter = QPainter(self)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    painter.setRenderHint(QPainter.RenderHint.TextAntialiasing)

    pen = QPen(QColor("#3498db"), 2, Qt.PenStyle.SolidLine)
    painter.setPen(pen)
    painter.setBrush(QBrush(QColor(200, 200, 0, 180)))  # RGBA com alpha

    rect = QRect(10, 20, 80, 60)
    painter.drawRect(rect)
    painter.drawRoundedRect(rect, 10, 10)
    painter.drawEllipse(rect)
    painter.drawArc(rect, 30 * 16, 120 * 16)    # ângulos em 1/16 de grau
    painter.drawLine(rect.bottomLeft(), rect.topRight())
    painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, "Hello")

    # QPainterPath — formas complexas
    path = QPainterPath()
    path.moveTo(QPointF(50, 100))
    path.lineTo(QPointF(100, 50))
    path.cubicTo(QPointF(150, 0), QPointF(200, 0), QPointF(250, 50))
    path.closeSubpath()
    painter.drawPath(path)
```

| Método | Descrição |
|---|---|
| `drawPoint()` | Ponto único |
| `drawLine()` | Linha entre dois pontos |
| `drawRect()` | Retângulo |
| `drawRoundedRect()` | Retângulo arredondado |
| `drawEllipse()` | Elipse |
| `drawArc()` | Arco (ângulos em 1/16°) |
| `drawPie()` | Setor circular |
| `drawChord()` | Corda |
| `drawPolygon()` | Polígono |
| `drawPolyline()` | Polilinha aberta |
| `drawImage()` | QImage |
| `drawPixmap()` | QPixmap |
| `drawPath()` | QPainterPath |
| `drawText()` | Texto Unicode |
| `fillRect()` | Preenche retângulo sem borda |

### Transformações

```python
painter.save()              # salva estado (transformações, pen, brush, clip)
painter.translate(cx, cy)   # move origem
painter.scale(sx, sy)       # escala
painter.rotate(angulo)      # graus, sentido horário
painter.shear(sh, sv)       # cisalhamento
painter.restore()           # restaura estado salvo
# SEMPRE parear save()/restore() para isolar transformações
```

### Custom Widget com timer (relógio analógico)

```python
from PySide6.QtCore import QTime

class AnalogClock(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)
        self.setMinimumSize(200, 200)

    def paintEvent(self, event):
        side = min(self.width(), self.height())
        time = QTime.currentTime()
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(side / 200.0, side / 200.0)
        # Tick marks — NÃO usa save/restore: rotação de 6° acumula por iteração
        for i in range(60):
            if i % 5 != 0:
                painter.drawLine(92, 0, 96, 0)
            else:
                painter.drawLine(86, 0, 96, 0)
            painter.rotate(6.0)

        # Ponteiros — USA save/restore para isolar cada rotação
        time = QTime.currentTime()
        hour_hand = [QPoint(4,4), QPoint(-4,4), QPoint(0,-40)]
        painter.save()
        painter.rotate((time.hour() * 360) / 12)
        painter.setBrush(Qt.GlobalColor.black)
        painter.drawConvexPolygon(hour_hand)
        painter.restore()
```

> (Fonte "qt6_cpp_cookbook_skill" acrescenta: marcações do mostrador NÃO usam `save()`/`restore()` — a rotação de 6° acumula corretamente no loop. Ponteiros DEVEM usar `save()`/`restore()` para que cada um gire a partir do centro sem herdar a rotação do anterior.)

### Exportar para SVG

```python
from PySide6.QtSvg import QSvgGenerator
from PySide6.QtWidgets import QFileDialog

path, _ = QFileDialog.getSaveFileName(self, "Salvar SVG", "", "SVG files (*.svg)")
if path:
    generator = QSvgGenerator()
    generator.setFileName(path)
    generator.setSize(self.size())
    generator.setViewBox(self.rect())
    generator.setTitle("SVG Example")          # metadados opcionais no XML
    generator.setDescription("Generated by Qt")
    painter = QPainter()
    painter.begin(generator)
    # ... todos os drawXxx() aqui ...
    painter.end()
```

**Regra**: usar a mesma função de pintura tanto para `paintEvent` quanto para exportação SVG, trocando apenas o `paint device`. Não criar múltiplos `QPainter` com `QSvgGenerator` — gera XML inválido.

### Modos de Composição

```python
# Aplicar modo antes de desenhar; resetar após
painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Difference)
painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Overlay)
painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Xor)
painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SoftLight)
# Reset para padrão:
painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
```

---

## QPixmap e QImage

O Qt mantém dois tipos de imagem com propósitos distintos: `QPixmap` é otimizado para exibição na tela (pode residir na GPU) e só pode ser usado na thread principal; `QImage` permite acesso direto a pixels em qualquer thread e é voltado para leitura, escrita e processamento. Converta entre os dois conforme o uso: exibição → `QPixmap`, manipulação → `QImage`.

### QPixmap — exibição

```python
from PySide6.QtGui import QPixmap

pixmap = QPixmap("image.png")
pixmap = QPixmap(200, 200)          # pixmap em branco

# Escalar mantendo proporção
scaled = pixmap.scaled(
    200, 200,
    Qt.AspectRatioMode.KeepAspectRatio,
    Qt.TransformationMode.SmoothTransformation
)
label.setPixmap(scaled)

# Outras operações
cropped = pixmap.copy(QRect(10, 10, 50, 50))
pixmap.save("output.png")
pixmap.save("output.jpg", quality=85)

# Criar pixmap com fundo transparente
pm = QPixmap(200, 200)
pm.fill(Qt.GlobalColor.transparent)
painter = QPainter(pm)
# ... desenhar ...
painter.end()   # NECESSÁRIO ao usar QPainter em QPixmap (não em QWidget)
```

### QImage — manipulação de pixels

```python
from PySide6.QtGui import QImage, QColor

img = QImage("image.png")
img = QImage(200, 200, QImage.Format.Format_ARGB32)
img.fill(QColor(255, 255, 255))

# Acesso por pixel (lento — use para poucos pixels)
color = QColor(img.pixel(x, y))
img.setPixel(x, y, QColor(255, 0, 0).rgb())

# Conversão
pixmap = QPixmap.fromImage(img)
img2   = pixmap.toImage()

# Bytes brutos (integração com numpy)
import numpy as np
ptr    = img.bits()
arr    = np.frombuffer(ptr, dtype=np.uint8).reshape((img.height(), img.width(), 4))
```

| | `QPixmap` | `QImage` |
|---|---|---|
| **Otimizado para** | Exibição na tela | Manipulação de pixels, I/O |
| **Thread safety** | Só na thread principal | Seguro em threads |
| **Acesso pixel** | Indireto via toImage() | Direto |
| **Uso típico** | `QLabel`, ícones, texturas | Processamento, conversão |

### Programa de Pintura — QImage como canvas off-screen

```python
class PaintWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.image = QImage(self.size(), QImage.Format.Format_RGB32)
        self.image.fill(Qt.GlobalColor.white)
        self.drawing = False
        self.brush_color = Qt.GlobalColor.black
        self.brush_size = 2
        self.last_point = QPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.MouseButton.LeftButton) and self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size,
                                Qt.PenStyle.SolidLine,
                                Qt.PenCapStyle.RoundCap,
                                Qt.PenJoinStyle.RoundJoin))
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(self.rect(), self.image, self.image.rect())

    def save_canvas(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save", "", "PNG (*.png);;JPEG (*.jpg)")
        if path:
            self.image.save(path)

    def clear_canvas(self):
        self.image.fill(Qt.GlobalColor.white)
        self.update()
```

**Regra**: o `QImage` serve como canvas off-screen — o `paintEvent` apenas copia o `QImage` para o widget. Dessa forma, o conteúdo desenhado sobrevive a eventos de `resize` e `repaint`.

---

## Graphics View Framework

O Graphics View Framework separa a **cena** (espaço lógico de coordenadas onde os itens existem) da **view** (viewport que projeta a cena na tela). Esse desacoplamento permite zoom, rotação e pan sem mover os itens; múltiplas views podem exibir a mesma cena simultaneamente. É a escolha certa para diagramas, editores gráficos e jogos 2D — para conteúdo estático simples, `QPainter` diretamente no `paintEvent` (ver [Desenhando Formas — QPainter](#desenhando-formas--qpainter)) é mais simples.

| Classe | Papel |
|---|---|
| `QGraphicsScene` | Container lógico de itens 2D |
| `QGraphicsItem` | Item base (abstract) |
| `QGraphicsView` | Widget viewport que exibe a cena |

```python
from PySide6.QtWidgets import (
    QGraphicsView, QGraphicsScene,
    QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsTextItem
)
from PySide6.QtGui import QBrush, QPen, QColor

class DiagramView(QGraphicsView):
    def __init__(self):
        super().__init__()
        scene = QGraphicsScene(self)
        scene.setSceneRect(-200, -200, 400, 400)

        rect = QGraphicsRectItem(-50, -30, 100, 60)
        rect.setBrush(QBrush(QColor("#3498db")))
        rect.setPen(QPen(QColor("#1a5276"), 2))
        rect.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        rect.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        scene.addItem(rect)

        text = QGraphicsTextItem("Olá")
        text.setPos(-20, -10)
        scene.addItem(text)

        self.setScene(scene)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.show()

# Transformações na view (não alteram a cena)
view.scale(1.5, 1.5)
view.rotate(45)
view.fitInView(scene.itemsBoundingRect(), Qt.AspectRatioMode.KeepAspectRatio)
```

### Flags de QGraphicsItem

```python
from PySide6.QtWidgets import QGraphicsItem

item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
item.setZValue(2)               # ordem de sobreposição (maior = frente)
item.setVisible(False)
item.setOpacity(0.5)
item.setToolTip("Item")
```

### Efeitos Gráficos em Itens

```python
from PySide6.QtWidgets import (
    QGraphicsDropShadowEffect, QGraphicsBlurEffect,
    QGraphicsColorizeEffect, QGraphicsOpacityEffect
)

shadow = QGraphicsDropShadowEffect()
shadow.setBlurRadius(10)
shadow.setOffset(3, 3)
shadow.setColor(QColor(0, 0, 0, 160))
item.setGraphicsEffect(shadow)

colorize = QGraphicsColorizeEffect()
colorize.setColor(QColor(255, 0, 0))   # tom vermelho
item.setGraphicsEffect(colorize)

blur = QGraphicsBlurEffect()
blur.setBlurRadius(12)
item.setGraphicsEffect(blur)

alpha = QGraphicsOpacityEffect()
alpha.setOpacity(0.2)                  # 20%
item.setGraphicsEffect(alpha)
```

> ⚠ Evite: usar o mesmo objeto de efeito em múltiplos widgets — crie instâncias separadas para cada um.

---

## Model/View Architecture

A arquitetura Model/View separa **dados** (modelo) de **apresentação** (view), permitindo que os mesmos dados sejam exibidos em múltiplas views simultaneamente e que a lógica de negócio nunca dependa de como os dados são mostrados. Um *delegate* controla renderização e edição de cada célula; um *proxy model* filtra ou ordena dados sem alterar o modelo original. Para dados estáticos simples, `QListWidget`/`QTableWidget` são mais diretos — use o padrão completo quando houver volume, dinamismo ou reuso.

### Visão Geral

```
Modelo (QAbstractItemModel) → dados brutos
View  (QAbstractItemView)  → exibição
Delegate (QAbstractItemDelegate) → renderização e edição de células
ProxyModel (QSortFilterProxyModel) → filtragem/ordenação sem tocar no modelo original
```

### QSortFilterProxyModel

```python
from PySide6.QtCore import QSortFilterProxyModel

proxy = QSortFilterProxyModel(self)
proxy.setSourceModel(source_model)
proxy.setFilterKeyColumn(1)    # filtra na coluna 1; -1 = todas as colunas
proxy.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
proxy.setSortCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)

# Conectar campo de busca
search_edit.textChanged.connect(proxy.setFilterFixedString)
# ou regex
search_edit.textChanged.connect(proxy.setFilterRegularExpression)

view.setModel(proxy)
view.setSortingEnabled(True)   # clique no cabeçalho ordena
```

### Modelo customizado simples — QAbstractTableModel

```python
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex

class DataModel(QAbstractTableModel):
    _headers = ["Nome", "Idade", "Cidade"]

    def __init__(self, data: list[list], parent=None):
        super().__init__(parent)
        self._data = data

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self._data)

    def columnCount(self, parent=QModelIndex()) -> int:
        return len(self._headers)

    def data(self, index: QModelIndex, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.ItemDataRole.DisplayRole:
            return str(self._data[index.row()][index.column()])
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self._headers[section]
            return str(section + 1)
        return None

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole) -> bool:
        if role == Qt.ItemDataRole.EditRole:
            self._data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index, [role])
            return True
        return False

    def flags(self, index):
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable
```

---

## Drag and Drop

Drag-and-drop no Qt usa o protocolo MIME: os dados arrastados são empacotados em um `QMimeData` com um tipo MIME que descreve o formato (texto, URL, imagem, tipo customizado). O widget de destino inspeciona os tipos disponíveis no `dragEnterEvent` para decidir se aceita o drop — essa negociação garante interoperabilidade entre aplicações diferentes.

```python
from PySide6.QtWidgets import QListWidget, QListWidgetItem
from PySide6.QtCore import Qt

class DnDListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QListWidget.DragDropMode.DragDrop)
        self.setDefaultDropAction(Qt.DropAction.MoveAction)
```

### Drag personalizado com MIME

```python
from PySide6.QtCore import QMimeData
from PySide6.QtGui import QDrag

def mousePressEvent(self, event):
    if event.button() == Qt.MouseButton.LeftButton:
        mime = QMimeData()
        mime.setText("dados para arrastar")
        drag = QDrag(self)
        drag.setMimeData(mime)
        drag.exec(Qt.DropAction.MoveAction)

def dragEnterEvent(self, event):
    if event.mimeData().hasText():
        event.acceptProposedAction()

def dropEvent(self, event):
    text = event.mimeData().text()
    event.acceptProposedAction()
```

| Evento | Quando |
|---|---|
| `QDragEnterEvent` | Drag entra no widget |
| `QDragLeaveEvent` | Drag sai do widget |
| `QDragMoveEvent` | Drag se move dentro do widget |
| `QDropEvent` | Drop finalizado |

---

## Dialogs Built-in

Diálogos modais bloqueiam a janela pai até o usuário responder — adequados para confirmações e coleta de dados críticos. O Qt fornece diálogos pré-construídos para os casos mais comuns; use as funções estáticas (e.g., `QFileDialog.getOpenFileName`) para simplicidade e portabilidade entre SOs, ou instancie a classe diretamente para controle fino sobre filtros, modos e aparência.

| Classe | Propósito |
|---|---|
| `QFileDialog` | Selecionar arquivos ou diretórios |
| `QInputDialog` | Receber um único valor do usuário |
| `QColorDialog` | Escolher cor (com canal alpha opcional) |
| `QFontDialog` | Selecionar fonte |
| `QMessageBox` | Informação/confirmação modal |
| `QProgressDialog` | Feedback de operação longa com opção de cancelar |
| `QErrorMessage` | Exibir erros com opção "não mostrar novamente" |
| `QWizard` | Assistente passo a passo |
| `QPrintDialog` | Configurar impressora (QtPrintSupport) |
| `QPrintPreviewDialog` | Prévia de impressão (QtPrintSupport) |

### QFileDialog

```python
from PySide6.QtWidgets import QFileDialog

# Abrir (forma recomendada — estática)
file_name, _ = QFileDialog.getOpenFileName(
    self, "Abrir Arquivo", "c:/", "Text files (*.txt);;All files (*)"
)

# Múltiplos filtros
filters = "Images (*.png *.jpg *.bmp);;Text (*.txt);;All (*)"
file_name, selected_filter = QFileDialog.getOpenFileName(self, filter=filters)

file_name, _  = QFileDialog.getSaveFileName(self, filter=filters)
dir_path      = QFileDialog.getExistingDirectory(self, "Selecionar Pasta")
files, _      = QFileDialog.getOpenFileNames(self, filter=filters)  # múltiplos

# Via instância (controle fino)
dialog = QFileDialog(self)
dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
dialog.setNameFilter("Todos (*);;Python (*.py)")
dialog.setDirectory("c:/projetos")
if dialog.exec():
    print(dialog.selectedFiles())
```

| FileMode | Comportamento |
|---|---|
| `AnyFile` | Qualquer nome (para salvar) |
| `ExistingFile` | Arquivo existente (para abrir) |
| `Directory` | Diretório |
| `ExistingFiles` | Múltiplos arquivos existentes |

### QInputDialog

```python
from PySide6.QtWidgets import QInputDialog

text,  ok = QInputDialog.getText(self,   "Título", "Rótulo:", text="padrão")
value, ok = QInputDialog.getInt(self,    "Título", "Rótulo:", 0, 0, 100, 1)
value, ok = QInputDialog.getDouble(self, "Título", "Rótulo:", 0.0, 0.0, 100.0, 2)
item,  ok = QInputDialog.getItem(
    self, "Título", "Escolha:", ["Opção A", "Opção B"], 0, editable=False
)
if ok:
    print(text)
```

### QColorDialog

```python
from PySide6.QtWidgets import QColorDialog
from PySide6.QtGui import QColor

color = QColorDialog.getColor(QColor(255, 0, 0), self, "Escolher Cor")
if color.isValid():
    widget.setStyleSheet(f"background-color: {color.name()}")

# Com canal alpha
color = QColorDialog.getColor(
    QColor(255, 0, 0, 128), self,
    options=QColorDialog.ColorDialogOption.ShowAlphaChannel
)
if color.isValid():
    print(color.name(QColor.NameFormat.HexArgb))  # "#80ff0000"
```

### QMessageBox

```python
from PySide6.QtWidgets import QMessageBox

QMessageBox.information(self, "Info", "Operação concluída.")
QMessageBox.warning(self,     "Atenção", "Arquivo não encontrado.")
QMessageBox.critical(self,    "Erro", "Falha crítica.")
QMessageBox.about(self,       "Sobre", "MinhaApp v1.0")
QMessageBox.aboutQt(self,     "Sobre Qt")

resp = QMessageBox.question(
    self, "Confirmação", "Deseja salvar antes de sair?",
    QMessageBox.StandardButton.Save |
    QMessageBox.StandardButton.Discard |
    QMessageBox.StandardButton.Cancel
)
if resp == QMessageBox.StandardButton.Save:
    self._save()
elif resp == QMessageBox.StandardButton.Cancel:
    return
```

### QProgressDialog

```python
from PySide6.QtWidgets import QProgressDialog
from PySide6.QtCore import Qt

progress = QProgressDialog("Processando...", "Cancelar", 0, 100, self)
progress.setWindowModality(Qt.WindowModality.WindowModal)
progress.setMinimumDuration(500)   # só aparece se tarefa demorar >500ms

for i in range(100):
    if progress.wasCanceled():
        break
    progress.setValue(i + 1)
    QApplication.processEvents()
```

### Custom Dialog — QDialog

```python
from PySide6.QtWidgets import QDialog, QDialogButtonBox

class FindDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Buscar")
        self._build_ui()

    def _build_ui(self):
        self.find_label  = QLabel("Buscar &texto:")
        self.line_edit   = QLineEdit()
        self.find_label.setBuddy(self.line_edit)     # Alt+T foca o campo
        self.case_check  = QCheckBox("&Diferenciar maiúsculas")

        # QDialogButtonBox — botões OK/Cancel padronizados
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok |
            QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(self.find_label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.case_check)
        layout.addWidget(buttons)
        self.setLayout(layout)

    def search_text(self) -> str:
        return self.line_edit.text()

    def is_case_sensitive(self) -> bool:
        return self.case_check.isChecked()

# Uso
dialog = FindDialog(self)
if dialog.exec() == QDialog.DialogCode.Accepted:
    print(dialog.search_text())
```

### QPrintDialog

```python
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from PySide6.QtGui import QTextDocument

def print_doc(self):
    printer = QPrinter()
    dialog  = QPrintDialog(printer, self)
    if dialog.exec() == QDialog.DialogCode.Accepted:
        QTextDocument(self.text_edit.toPlainText()).print_(printer)
```

---

## MDI — Multiple Document Interface

MDI (*Multiple Document Interface*) é um padrão onde documentos abertos vivem como subjanelas dentro de uma área central gerenciada pela aplicação. `QMdiArea` organiza as subjanelas em cascata ou grade; cada `QMdiSubWindow` pode conter qualquer widget como conteúdo. É adequado para aplicações de edição onde múltiplos documentos precisam estar visíveis ao mesmo tempo.

```python
from PySide6.QtWidgets import QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit

class MDIApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mdi_area = QMdiArea()
        self.mdi_area.setViewMode(QMdiArea.ViewMode.SubWindowView)
        self.setCentralWidget(self.mdi_area)
        self.setWindowTitle("MDI Application")

    def _new_document(self):
        count  = len(self.mdi_area.subWindowList()) + 1
        editor = QTextEdit()
        editor.setWindowTitle(f"Documento {count}")
        sub = QMdiSubWindow()
        sub.setWidget(editor)
        sub.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)   # libera ao fechar
        self.mdi_area.addSubWindow(sub)
        sub.show()

# Controle de layout
self.mdi_area.tileSubWindows()       # grade
self.mdi_area.cascadeSubWindows()    # cascata
self.mdi_area.activeSubWindow()      # subjanela ativa (ou None)
self.mdi_area.subWindowList()        # lista de todas as subjanelas
```

---

## QSettings — Configurações Persistentes

`QSettings` abstrai o mecanismo de persistência específico do SO — registro do Windows, arquivos `.plist` no macOS, arquivos `.ini` no Linux — por trás de uma API chave-valor uniforme. Configurar `setApplicationName` e `setOrganizationName` no `QApplication` (ver [Estrutura da Aplicação](#estrutura-da-aplicação)) permite usar `QSettings()` sem parâmetros em qualquer ponto do código, com o caminho de armazenamento resolvido automaticamente.

```python
from PySide6.QtCore import QSettings

# Com app/org configurados no QApplication (recomendado)
settings = QSettings()

# Explícito
settings = QSettings("MinhaOrg", "MinhaApp")

# Escrita
settings.setValue("window/geometry",  self.saveGeometry())
settings.setValue("window/state",     self.saveState())
settings.setValue("editor/font_size", 12)
settings.setValue("recent_files",     ["a.txt", "b.txt"])

# Leitura
geom      = settings.value("window/geometry")
font_size = settings.value("editor/font_size", defaultValue=12, type=int)
files     = settings.value("recent_files",     defaultValue=[],  type=list)

# Grupos
settings.beginGroup("database")
settings.setValue("host", "localhost")
settings.setValue("port", 5432)
settings.endGroup()

with settings.group("database"):   # context manager (Python ≥ 3.10 pattern)
    host = settings.value("host")

# Remover
settings.remove("window/geometry")
settings.remove("database")    # remove grupo inteiro

# Verificar existência
if settings.contains("editor/font_size"):
    ...

# Onde são gravadas
print(settings.fileName())
```

---

## QSystemTrayIcon

O ícone na bandeja do sistema permite que a aplicação permaneça ativa em segundo plano sem ocupar espaço na barra de tarefas. O mecanismo de sinais (ver [Sinais e Slots](#sinais-e-slots)) conecta eventos de ativação (clique simples, duplo-clique) a ações da aplicação; o menu de contexto é um `QMenu` padrão atachado ao ícone.

```python
from PySide6.QtWidgets import QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QAction

class TrayApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self._create_tray()

    def _create_tray(self):
        if not QSystemTrayIcon.isSystemTrayAvailable():
            QMessageBox.critical(None, "Bandeja", "Sistema não suporta system tray.")
            return

        self.tray = QSystemTrayIcon(QIcon("icon.png"), self)
        self.tray.setToolTip("MinhaApp está rodando")

        menu = QMenu()
        menu.addAction(QAction("Mostrar", self, triggered=self.show))
        menu.addAction(QAction("Esconder", self, triggered=self.hide))
        menu.addSeparator()
        menu.addAction(QAction("Sair", self, triggered=QApplication.quit))
        self.tray.setContextMenu(menu)

        self.tray.activated.connect(self._tray_activated)
        self.tray.show()

    def _tray_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            self.show()

    def _notify(self, title: str, msg: str):
        self.tray.showMessage(
            title, msg,
            QSystemTrayIcon.MessageIcon.Information,
            3000   # ms
        )

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self._notify("MinhaApp", "Minimizado para a bandeja.")
```

---

## QClipboard

A área de transferência do SO usa o mesmo protocolo MIME do drag-and-drop (ver [Drag and Drop](#drag-and-drop)): dados são empacotados em `QMimeData` com tipos que descrevem o formato (texto, imagem, URLs, dados customizados). `QApplication.clipboard()` retorna o objeto global compartilhado entre todas as janelas da aplicação.

```python
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPixmap

clipboard = QApplication.clipboard()

# Texto
clipboard.setText("Hello, World!")
text = clipboard.text()

# Imagem
clipboard.setPixmap(QPixmap("image.png"))
pixmap = clipboard.pixmap()

# Reagir a mudanças
clipboard.dataChanged.connect(self._on_clipboard_changed)

# MIME genérico
from PySide6.QtCore import QMimeData
mime = QMimeData()
mime.setText("texto")
mime.setUrls([QUrl.fromLocalFile("/tmp/file.txt")])
clipboard.setMimeData(mime)

urls = clipboard.mimeData().urls()
```

---

## QSplashScreen

A tela de splash exibe uma imagem enquanto a aplicação inicializa recursos pesados (conexão com banco, carregamento de plugins, criação de janelas), melhorando a percepção de desempenho. Ela deve ser mostrada antes da janela principal e fechada com `splash.finish(window)` assim que a janela estiver pronta — o Qt garante que o fechamento ocorra suavemente após `window.show()`.

```python
from PySide6.QtWidgets import QSplashScreen, QApplication
from PySide6.QtGui import QPixmap, QFont, QColor
from PySide6.QtCore import Qt

if __name__ == "__main__":
    app = QApplication(sys.argv)

    pixmap = QPixmap("splash.png")
    splash = QSplashScreen(pixmap)
    splash.show()

    # Mensagem na tela de carregamento
    splash.showMessage(
        "Carregando módulos...",
        Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter,
        QColor("white")
    )
    app.processEvents()

    # ... inicializar recursos, banco de dados, etc. ...

    window = MainWindow()
    splash.finish(window)   # fecha o splash quando a janela estiver pronta
    window.show()
    sys.exit(app.exec())
```

---

## Database — QtSql

O módulo `QtSql` oferece uma camada de abstração sobre diferentes bancos relacionais, expondo uma API uniforme independente do driver (SQLite, PostgreSQL, MySQL, ODBC). **Queries parametrizadas** (*prepared statements*) são o único modo seguro de incorporar dados externos em SQL — nunca concatene strings de entrada do usuário diretamente em queries, pois isso abre vulnerabilidade a SQL Injection.

### Conectando

```python
from PySide6.QtSql import QSqlDatabase

# SQLite (recomendado para apps locais)
db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("myapp.db")   # ou ":memory:" para banco em memória
if not db.open():
    QMessageBox.critical(None, "DB Error", db.lastError().text())
    sys.exit(1)

# PostgreSQL
db = QSqlDatabase.addDatabase("QPSQL", "connPg")
db.setHostName("localhost")
db.setPort(5432)
db.setDatabaseName("mydb")
db.setUserName("user")
db.setPassword("pass")
db.open()

# Encerrar corretamente (importante: destruir queries/models antes)
QSqlDatabase.removeDatabase("connPg")
```

| Driver | Banco |
|---|---|
| `QSQLITE` | SQLite (incluso no Qt) |
| `QMYSQL` | MySQL / MariaDB |
| `QPSQL` | PostgreSQL |
| `QODBC` | ODBC (SQL Server, Access) |
| `QOCI` | Oracle |

**Boa prática**: abrir a conexão logo após `QApplication`, antes de exibir a janela.

### QSqlQuery — Execução de Queries

```python
from PySide6.QtSql import QSqlQuery

query = QSqlQuery()
query.exec("""
    CREATE TABLE IF NOT EXISTS employee (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name  TEXT,
        age        INTEGER,
        income     REAL
    )
""")

if not query.exec("SELECT * FROM employee"):
    print(query.lastError().text())
```

### Prepared Queries (obrigatório para inputs externos — previne SQL Injection)

```python
# Named binding (preferido)
query.prepare("""
    INSERT INTO employee (first_name, last_name, age, income)
    VALUES (:first_name, :last_name, :age, :income)
""")
for fname, lname, age, income in data:
    query.bindValue(":first_name", fname)
    query.bindValue(":last_name",  lname)
    query.bindValue(":age",        age)
    query.bindValue(":income",     income)
    query.exec()

# Positional binding
query.prepare("INSERT INTO employee VALUES (NULL, ?, ?, ?, ?)")
for fname, lname, age, income in data:
    query.addBindValue(fname)
    query.addBindValue(lname)
    query.addBindValue(age)
    query.addBindValue(income)
    query.exec()
```

### Navegando Registros

```python
query.exec("SELECT id, first_name, income FROM employee WHERE age > :min_age")
query.bindValue(":min_age", 30)
query.exec()

while query.next():
    rec_id = query.value(0)   # Python nativo — sem .toInt()/.toString()
    name   = query.value("first_name")   # por nome de coluna
    salary = query.value(2)

# Forward-only (melhor performance, sem navegação reversa)
query.setForwardOnly(True)    # chamar ANTES de exec()

# Utilidades
query.lastInsertId()           # ID do último INSERT AUTOINCREMENT
query.numRowsAffected()        # linhas afetadas por UPDATE/DELETE
query.finish()                 # libera resultado sem destruir o objeto
```

> **Nunca use `SELECT *` com `value(n)` por posição** — liste colunas explicitamente.

### Transações

```python
from PySide6.QtSql import QSqlDriver

db = QSqlDatabase.database()
if db.driver().hasFeature(QSqlDriver.DriverFeature.Transactions):
    db.transaction()
    try:
        query = QSqlQuery()
        query.exec("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
        query.exec("UPDATE accounts SET balance = balance + 100 WHERE id = 2")
        db.commit()
    except Exception:
        db.rollback()
        raise
```

### QSqlQueryModel (somente leitura)

```python
from PySide6.QtSql import QSqlQueryModel

model = QSqlQueryModel()
model.setQuery("SELECT first_name, last_name FROM employee ORDER BY last_name")
model.setHeaderData(0, Qt.Orientation.Horizontal, "Nome")
model.setHeaderData(1, Qt.Orientation.Horizontal, "Sobrenome")

view = QTableView()
view.setModel(model)
```

### QSqlTableModel (editável)

```python
from PySide6.QtSql import QSqlTableModel

model = QSqlTableModel()
model.setTable("employee")
model.setFilter("age > 40")
model.setSort(1, Qt.SortOrder.AscendingOrder)
model.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
model.select()

model.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
model.setHeaderData(1, Qt.Orientation.Horizontal, "Nome")

record = model.record(0)
record.setValue("income", 9000.00)
model.setRecord(0, record)

model.removeRow(2)
model.submitAll()    # confirma no banco
# model.revertAll()  # descarta mudanças pendentes
```

| EditStrategy | Comportamento |
|---|---|
| `OnFieldChange` | Aplica ao banco imediatamente ao mudar campo |
| `OnRowChange` | Aplica ao banco ao mudar de linha |
| `OnManualSubmit` | Acumula até `submitAll()` |

### QSqlRelationalTableModel (chaves estrangeiras)

```python
from PySide6.QtSql import QSqlRelationalTableModel, QSqlRelation, QSqlRelationalDelegate

model = QSqlRelationalTableModel()
model.setTable("employee")
model.setRelation(2, QSqlRelation("department", "id", "name"))
model.select()    # setRelation() DEVE ser chamado ANTES de select()

view = QTableView()
view.setModel(model)
view.setItemDelegate(QSqlRelationalDelegate(view))   # ComboBox para FK
```

### QDataWidgetMapper (form view — um registro por vez)

```python
from PySide6.QtWidgets import QDataWidgetMapper

FIRST_NAME, LAST_NAME, AGE, INCOME = 1, 2, 3, 4

mapper = QDataWidgetMapper(self)
mapper.setSubmitPolicy(QDataWidgetMapper.SubmitPolicy.ManualSubmit)
mapper.setModel(model)
mapper.addMapping(self.first_edit,  FIRST_NAME)   # section = índice de coluna no MODELO
mapper.addMapping(self.last_edit,   LAST_NAME)
mapper.addMapping(self.age_spin,    AGE)
mapper.toFirst()

# Navegar
mapper.toPrevious()
mapper.toNext()
mapper.toLast()
mapper.setCurrentIndex(row)

# Salvar / descartar
mapper.submit()    # grava edições no modelo
mapper.revert()    # descarta edições da linha atual
```

### QTableWidget com dados SQL (abordagem manual)

```python
self.table.setColumnHidden(0, True)  # ocultar coluna ID
self.has_init = False

query = QSqlQuery("SELECT id, name, age FROM employee")
while query.next():
    row = self.table.rowCount()
    self.table.setRowCount(row + 1)
    self.table.setItem(row, 0, QTableWidgetItem(str(query.value(0))))
    self.table.setItem(row, 1, QTableWidgetItem(str(query.value(1))))
    self.table.setItem(row, 2, QTableWidgetItem(str(query.value(2))))

self.has_init = True   # ativa slot de edição somente após carga inicial
self.table.itemChanged.connect(self.on_item_changed)

def on_item_changed(self, item):
    if not self.has_init:
        return
    row_id = self.table.item(item.row(), 0).text()
    name   = self.table.item(item.row(), 1).text()
    query = QSqlQuery()
    query.prepare("UPDATE employee SET name=:name WHERE id=:id")
    query.bindValue(":name", name)
    query.bindValue(":id",   row_id)
    query.exec()
```

**Preferir model-view** (`QSqlTableModel + QTableView`) quando possível; `QTableWidget + SQL` manual é útil apenas quando se precisa de controle total sobre cada célula.

---

## QStandardItemModel

`QStandardItemModel` é um modelo genérico de árvore hierárquica, pronto para uso com qualquer view (`QListView`, `QTableView`, `QTreeView`) sem necessidade de subclassificar `QAbstractItemModel`. Cada célula é um `QStandardItem` que pode carregar texto, ícone, tooltip, checkbox e dados arbitrários via `UserRole`. Use-o quando os dados couberem em memória e não precisarem de fonte customizada — para dados de banco ou API use `QAbstractTableModel` (ver [Model/View Architecture](#modelview-architecture)).

```python
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QTableView, QListView, QTreeView

# ── Tabela ──────────────────────────────────────────────────
model = QStandardItemModel(0, 3)   # 0 linhas, 3 colunas
model.setHorizontalHeaderLabels(["Nome", "Idade", "Cidade"])

row = [QStandardItem("Ana"), QStandardItem("30"), QStandardItem("SP")]
row[0].setCheckable(True)           # coluna 0 com checkbox
model.appendRow(row)

# Inserir linha em posição
item_row = [QStandardItem("Bob"), QStandardItem("25"), QStandardItem("RJ")]
model.insertRow(0, item_row)

view = QTableView()
view.setModel(model)
view.horizontalHeader().setStretchLastSection(True)

# ── Lista ────────────────────────────────────────────────────
list_model = QStandardItemModel()
for text in ["Alpha", "Beta", "Gamma"]:
    item = QStandardItem(text)
    item.setIcon(QIcon("icon.png"))
    list_model.appendRow(item)

list_view = QListView()
list_view.setModel(list_model)

# ── Árvore ───────────────────────────────────────────────────
tree_model = QStandardItemModel()
tree_model.setHorizontalHeaderLabels(["Nome", "Valor"])

root = tree_model.invisibleRootItem()
parent = QStandardItem("Categoria A")
parent.appendRow([QStandardItem("Item 1"), QStandardItem("100")])
parent.appendRow([QStandardItem("Item 2"), QStandardItem("200")])
root.appendRow(parent)

tree_view = QTreeView()
tree_view.setModel(tree_model)
tree_view.expandAll()
```

### Acessar e modificar células

```python
# Por índice (linha, coluna)
item = model.item(0, 1)
item.setText("Novo Valor")
item.setData(42, Qt.ItemDataRole.UserRole)   # dado arbitrário
value = item.data(Qt.ItemDataRole.UserRole)

# Por QModelIndex
index = model.index(0, 1)
model.setData(index, "Novo", Qt.ItemDataRole.DisplayRole)
text = model.data(index)

# Remover linhas
model.removeRow(0)
model.removeRows(0, 3)   # remove 3 linhas a partir de 0

# Contar
model.rowCount()
model.columnCount()
```

### QStandardItem — flags úteis

```python
item = QStandardItem("texto")
item.setCheckable(True)
item.setCheckState(Qt.CheckState.Checked)
item.setEditable(False)
item.setEnabled(False)
item.setForeground(QColor("red"))
item.setBackground(QColor("#f0f0f0"))
item.setFont(QFont("Arial", 10, QFont.Weight.Bold))
item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
item.setToolTip("Dica de ferramenta")
```

---

## QTreeWidget e QTableWidget

`QTreeWidget` e `QTableWidget` são alternativas "convenientes" que combinam modelo e view em um único widget, dispensando configuração explícita de modelo. São adequados para dados estáticos ou pequenos volumes. Para dados dinâmicos, filtros ou ordenação, prefira `QStandardItemModel` + view (ver [QStandardItemModel](#qstandarditemmodel)) ou o padrão completo Model/View (ver [Model/View Architecture](#modelview-architecture)).

### QTreeWidget

```python
from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem

tree = QTreeWidget()
tree.setColumnCount(2)
tree.setHeaderLabels(["Nome", "Tamanho"])

# Item raiz
root = QTreeWidgetItem(tree, ["Documentos", ""])
root.setExpanded(True)

# Filhos
child1 = QTreeWidgetItem(root, ["relatorio.pdf", "1.2 MB"])
child2 = QTreeWidgetItem(root, ["planilha.xlsx", "340 KB"])
child1.setIcon(0, QIcon("pdf.png"))

# Adicionar ao widget diretamente
tree.addTopLevelItem(QTreeWidgetItem(["Imagens", ""]))

# Navegar
selected = tree.selectedItems()           # lista de QTreeWidgetItem
current  = tree.currentItem()
tree.setCurrentItem(child1)

# Sinal
tree.itemClicked.connect(lambda item, col: print(item.text(col)))
tree.itemDoubleClicked.connect(self._on_double_click)
```

### QTableWidget

```python
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

table = QTableWidget(5, 3)   # 5 linhas, 3 colunas
table.setHorizontalHeaderLabels(["Nome", "Nota", "Status"])
table.horizontalHeader().setStretchLastSection(True)
table.verticalHeader().setVisible(False)
table.setAlternatingRowColors(True)
table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)  # somente leitura

# Preencher
table.setItem(0, 0, QTableWidgetItem("Alice"))
table.setItem(0, 1, QTableWidgetItem("9.5"))

# Widget em célula
from PySide6.QtWidgets import QProgressBar
bar = QProgressBar()
bar.setValue(75)
table.setCellWidget(0, 2, bar)

# Ler
text = table.item(0, 0).text() if table.item(0, 0) else ""

# Sinais
table.cellClicked.connect(lambda r, c: print(f"Célula ({r},{c})"))
table.itemChanged.connect(lambda item: print(item.text()))

# Ajustar colunas
table.resizeColumnsToContents()
table.setColumnWidth(0, 200)
```

---

## QtNetwork — HTTP Requests

`QNetworkAccessManager` executa requisições HTTP de forma **assíncrona**, integrado ao event loop do Qt (ver [Estrutura da Aplicação](#estrutura-da-aplicação)) — a resposta chega via sinal `finished` sem bloquear a interface. Um único manager deve ser reutilizado por toda a aplicação para aproveitar o pool de conexões e o cache HTTP interno.

```python
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide6.QtCore import QUrl, QUrlQuery, QByteArray, QJsonDocument
```

### GET simples

```python
class HttpClient(QObject):
    data_ready = Signal(dict)
    error      = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._manager = QNetworkAccessManager(self)

    def get(self, url: str):
        req = QNetworkRequest(QUrl(url))
        req.setHeader(QNetworkRequest.KnownHeaders.ContentTypeHeader, "application/json")
        req.setRawHeader(b"Authorization", b"Bearer TOKEN")
        reply = self._manager.get(req)
        reply.finished.connect(lambda: self._handle_reply(reply))

    def _handle_reply(self, reply: QNetworkReply):
        if reply.error() != QNetworkReply.NetworkError.NoError:
            self.error.emit(reply.errorString())
        else:
            raw  = reply.readAll()
            doc  = QJsonDocument.fromJson(raw)
            self.data_ready.emit(doc.object())
        reply.deleteLater()
```

### POST com JSON

```python
def post_json(self, url: str, payload: dict):
    req = QNetworkRequest(QUrl(url))
    req.setHeader(QNetworkRequest.KnownHeaders.ContentTypeHeader, "application/json")

    doc  = QJsonDocument.fromVariant(payload)
    body = doc.toJson(QJsonDocument.JsonFormat.Compact)

    reply = self._manager.post(req, body)
    reply.finished.connect(lambda: self._handle_reply(reply))
```

### POST com formulário (form-encoded)

```python
def post_form(self, url: str, fields: dict):
    req = QNetworkRequest(QUrl(url))
    req.setHeader(
        QNetworkRequest.KnownHeaders.ContentTypeHeader,
        "application/x-www-form-urlencoded"
    )
    query = QUrlQuery()
    for k, v in fields.items():
        query.addQueryItem(k, str(v))
    reply = self._manager.post(req, query.toString(QUrl.ComponentFormattingOption.FullyEncoded).encode())
    reply.finished.connect(lambda: self._handle_reply(reply))
```

### Download de arquivo com progresso

```python
def download(self, url: str, dest_path: str):
    reply = self._manager.get(QNetworkRequest(QUrl(url)))
    reply.downloadProgress.connect(
        lambda received, total: self.progress.emit(
            int(received / total * 100) if total > 0 else 0
        )
    )

    def _save():
        with open(dest_path, "wb") as f:
            f.write(reply.readAll().data())
        reply.deleteLater()

    reply.finished.connect(_save)
```

### Configurar proxy e SSL

```python
from PySide6.QtNetwork import QNetworkProxy, QSslConfiguration

# Proxy
proxy = QNetworkProxy(QNetworkProxy.ProxyType.HttpProxy, "proxy.host", 8080)
QNetworkProxy.setApplicationProxy(proxy)

# SSL permissivo (apenas dev/testes)
ssl_config = QSslConfiguration.defaultConfiguration()
ssl_config.setPeerVerifyMode(QSslSocket.PeerVerifyMode.VerifyNone)
req.setSslConfiguration(ssl_config)
```

### TCP Server + Client

```python
from PySide6.QtNetwork import QTcpServer, QTcpSocket, QHostAddress

class ChatServer(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.all_clients: list[QTcpSocket] = []
        self.server = QTcpServer()
        self.server.setMaxPendingConnections(10)
        self.server.newConnection.connect(self.new_client_connection)
        self.server.listen(QHostAddress.SpecialAddress.Any, 8001)

    def new_client_connection(self):
        client = self.server.nextPendingConnection()
        client.readyRead.connect(self.socket_read_ready)
        client.disconnected.connect(self.socket_disconnected)
        self.all_clients.append(client)

    def socket_disconnected(self):
        self.all_clients.remove(self.sender())

    def socket_read_ready(self):
        client = self.sender()
        data = client.readAll().data().decode()
        for c in self.all_clients:
            if c.isOpen() and c.isWritable():
                c.write(data.encode())

# Cliente TCP simples
socket = QTcpSocket()
socket.readyRead.connect(lambda: print(socket.readAll().data().decode()))
socket.connectToHost("127.0.0.1", 8001)
socket.write(b"Hello Server")
```

| Estado (`QAbstractSocket.SocketState`) | Significado |
|---|---|
| `UnconnectedState` | Não conectado |
| `HostLookupState` | Resolvendo DNS |
| `ConnectingState` | Estabelecendo conexão |
| `ConnectedState` | Conectado |
| `ClosingState` | Encerrando |

| Protocolo | Características | Uso típico |
|---|---|---|
| TCP | Confiável, ordenado, com handshake | Chat, web, banco de dados |
| UDP | Não confiável, sem ordenação | Jogos online, streaming, DNS |

### FTP via Python stdlib (`ftplib`)

Qt 6 removeu FTP do `QNetworkAccessManager`. Use `ftplib` da stdlib em um `QThread`:

```python
import ftplib
from PySide6.QtCore import QObject, QThread, Signal, Slot

class FtpClient:
    def __init__(self, host, user, password):
        self.ftp = ftplib.FTP()
        self.ftp.connect(host, 21)
        self.ftp.login(user, password)

    def list_files(self) -> list:
        files = []
        self.ftp.retrlines("LIST", files.append)
        return files

    def upload(self, local_path, remote_name):
        with open(local_path, "rb") as f:
            self.ftp.storbinary(f"STOR {remote_name}", f)

    def download(self, remote_name, local_path):
        with open(local_path, "wb") as f:
            self.ftp.retrbinary(f"RETR {remote_name}", f.write)

    def close(self):
        self.ftp.quit()

class FtpWorker(QObject):
    file_list_ready = Signal(list)
    error           = Signal(str)

    def __init__(self, host, user, password):
        super().__init__()
        self._host, self._user, self._pwd = host, user, password

    @Slot()
    def connect_and_list(self):
        try:
            self.client = FtpClient(self._host, self._user, self._pwd)
            self.file_list_ready.emit(self.client.list_files())
        except Exception as e:
            self.error.emit(str(e))

# Integrar com UI
thread = QThread()
worker = FtpWorker("ftp.example.com", "user", "pass")
worker.moveToThread(thread)
thread.started.connect(worker.connect_and_list)
worker.file_list_ready.connect(lambda files: print(files))
thread.start()
```

---

## QDesktopServices e QFileSystemWatcher

`QDesktopServices` e `QFileSystemWatcher` integram a aplicação com o SO anfitrião sem depender de APIs nativas: o primeiro delega ações (abrir URL, arquivo, pasta) ao aplicativo padrão configurado pelo usuário; o segundo monitora mudanças no sistema de arquivos usando mecanismos nativos do SO (inotify no Linux, FSEvents no macOS, ReadDirectoryChangesW no Windows), sem polling.

### QDesktopServices — abrir com app padrão do SO

```python
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl

# Abrir URL no navegador
QDesktopServices.openUrl(QUrl("https://www.qt.io"))

# Abrir arquivo com app padrão do SO
QDesktopServices.openUrl(QUrl.fromLocalFile("/caminho/para/arquivo.pdf"))

# Abrir pasta
QDesktopServices.openUrl(QUrl.fromLocalFile("/caminho/para/pasta"))

# Localização de diretórios especiais
from PySide6.QtCore import QStandardPaths

docs_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DocumentsLocation)
data_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppDataLocation)
temp_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.TempLocation)
home_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.HomeLocation)
```

| `StandardLocation` | Caminho típico (Windows) |
|---|---|
| `DocumentsLocation` | `C:\Users\user\Documents` |
| `AppDataLocation` | `C:\Users\user\AppData\Roaming\Org\App` |
| `AppLocalDataLocation` | `C:\Users\user\AppData\Local\Org\App` |
| `TempLocation` | `C:\Users\user\AppData\Local\Temp` |
| `HomeLocation` | `C:\Users\user` |
| `DesktopLocation` | `C:\Users\user\Desktop` |
| `DownloadLocation` | `C:\Users\user\Downloads` |

### QFileSystemWatcher — vigiar arquivos e pastas

```python
from PySide6.QtCore import QFileSystemWatcher

watcher = QFileSystemWatcher(self)
watcher.addPath("/caminho/para/arquivo.json")
watcher.addPath("/caminho/para/pasta")

watcher.fileChanged.connect(self._on_file_changed)
watcher.directoryChanged.connect(self._on_dir_changed)

def _on_file_changed(self, path: str):
    print(f"Arquivo modificado: {path}")
    # Arquivo pode ter sido deletado — re-adicionar se necessário
    if path not in watcher.files():
        watcher.addPath(path)

def _on_dir_changed(self, path: str):
    print(f"Pasta alterada: {path}")

# Remover
watcher.removePath("/caminho/para/arquivo.json")
print(watcher.files())        # arquivos monitorados
print(watcher.directories())  # pastas monitoradas
```

---

## QUndoStack — Undo/Redo

O padrão **Command** encapsula cada operação do usuário como um objeto com métodos `redo()` e `undo()`. `QUndoStack` mantém a pilha desses comandos e expõe ações de desfazer/refazer que se integram diretamente ao menu da aplicação via sinais (ver [Sinais e Slots](#sinais-e-slots)), gerenciando automaticamente o texto descritivo e o estado habilitado/desabilitado das ações.

```python
from PySide6.QtGui import QUndoStack, QUndoCommand
```

### Definir comandos

```python
class RenameCommand(QUndoCommand):
    def __init__(self, item, old_name: str, new_name: str):
        super().__init__(f"Renomear '{old_name}' → '{new_name}'")
        self._item     = item
        self._old_name = old_name
        self._new_name = new_name

    def redo(self):
        self._item.setName(self._new_name)

    def undo(self):
        self._item.setName(self._old_name)


class MoveCommand(QUndoCommand):
    def __init__(self, item, old_pos, new_pos):
        super().__init__("Mover item")
        self._item    = item
        self._old_pos = old_pos
        self._new_pos = new_pos

    def redo(self):
        self._item.setPos(self._new_pos)

    def undo(self):
        self._item.setPos(self._old_pos)

    def mergeWith(self, other) -> bool:
        # Mesclar movimentos consecutivos em um único comando
        if other.id() == self.id():
            self._new_pos = other._new_pos
            return True
        return False

    def id(self) -> int:
        return 1   # comandos com mesmo id podem ser mesclados
```

### Usar a stack

```python
class Editor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.undo_stack = QUndoStack(self)

        # Ações integradas com a stack
        undo_action = self.undo_stack.createUndoAction(self, "&Desfazer")
        undo_action.setShortcut(QKeySequence.StandardKey.Undo)
        redo_action = self.undo_stack.createRedoAction(self, "&Refazer")
        redo_action.setShortcut(QKeySequence.StandardKey.Redo)

        edit_menu = self.menuBar().addMenu("&Editar")
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)

    def _rename_item(self, item, new_name: str):
        cmd = RenameCommand(item, item.name(), new_name)
        self.undo_stack.push(cmd)    # executa redo() automaticamente

    def _mark_saved(self):
        self.undo_stack.setClean()   # marca posição "salvo"

    def _is_modified(self) -> bool:
        return not self.undo_stack.isClean()
```

### Comandos macros (agrupados)

```python
self.undo_stack.beginMacro("Formatar seleção")
self.undo_stack.push(BoldCommand(selection))
self.undo_stack.push(ColorCommand(selection, QColor("red")))
self.undo_stack.endMacro()   # aparece como um único item na pilha
```

---

## Sistema de Recursos (.qrc)

O Qt Resource System empacota arquivos estáticos (imagens, QSS, fontes) diretamente dentro do binário Python gerado, eliminando dependências de caminhos do sistema de arquivos. Recursos são acessados pelo prefixo `:/` em vez de caminhos absolutos, o que os torna portáveis entre sistemas operacionais e facilita o deploy (ver [Deploy e Empacotamento](#deploy-e-empacotamento)).

### 1. Criar arquivo .qrc

```xml
<!-- resources.qrc -->
<!DOCTYPE RCC>
<RCC version="1.0">
  <qresource prefix="/icons">
    <file alias="new.png">assets/icons/new.png</file>
    <file alias="save.png">assets/icons/save.png</file>
  </qresource>
  <qresource prefix="/styles">
    <file>assets/style.qss</file>
  </qresource>
  <qresource prefix="/fonts">
    <file>assets/fonts/Inter-Regular.ttf</file>
  </qresource>
</RCC>
```

### 2. Compilar para Python

```bash
pyside6-rcc resources.qrc -o resources_rc.py
```

### 3. Importar e usar

```python
import resources_rc   # registra os recursos no Qt; não precisa usar o módulo explicitamente

from PySide6.QtGui import QIcon, QPixmap, QFontDatabase

# Caminho com prefixo ":"
icon = QIcon(":/icons/new.png")
pixmap = QPixmap(":/icons/save.png")

# Carregar QSS do recurso
with open(":/styles/style.qss", "r") as f:   # QFile também funciona
    app.setStyleSheet(f.read())

# Registrar fonte embutida
font_id = QFontDatabase.addApplicationFont(":/fonts/Inter-Regular.ttf")
families = QFontDatabase.applicationFontFamilies(font_id)
app.setFont(QFont(families[0]))
```

### Usar QFile para binários

```python
from PySide6.QtCore import QFile, QIODeviceBase

f = QFile(":/icons/save.png")
f.open(QIODeviceBase.OpenModeFlag.ReadOnly)
data = f.readAll()   # QByteArray
f.close()
```

---

## Deploy e Empacotamento

Distribuir uma aplicação PySide6 significa empacotar o interpretador Python, as bibliotecas Qt e todos os assets em um executável autossuficiente. Ferramentas como PyInstaller e Nuitka analisam os imports em tempo de compilação; assets declarados no Qt Resource System (ver [Sistema de Recursos (.qrc)](#sistema-de-recursos-qrc)) são embutidos automaticamente. Sempre teste o executável gerado em uma máquina sem Python instalado antes de distribuir.

### PyInstaller (mais popular)

```bash
pip install pyinstaller

# Executável único
pyinstaller --onefile --windowed main.py

# Com ícone
pyinstaller --onefile --windowed --icon=app.ico main.py

# Com spec customizado
pyside6-deploy main.py        # gera .spec otimizado para PySide6
```

**`main.spec` — pontos de customização:**

```python
# Incluir arquivos de dados
datas = [
    ("assets/", "assets/"),
    ("resources_rc.py", "."),
]

# Excluir módulos desnecessários (reduz tamanho)
excludes = ["tkinter", "unittest", "email"]
```

### Nuitka (compilação C++ — melhor performance)

```bash
pip install nuitka

python -m nuitka --standalone --onefile \
    --plugin-enable=pyside6 \
    --windows-icon-from-ico=app.ico \
    --output-dir=dist \
    main.py
```

### pyside6-deploy (ferramenta oficial Qt)

```bash
pip install pyside6-deploy

# Gera pysidedeploy.spec e binário
pyside6-deploy main.py
```

### Estrutura recomendada de projeto

```
meu_projeto/
├── main.py                  # entry point
├── requirements.txt         # PySide6>=6.7,<7
├── resources.qrc            # arquivo de recursos
├── resources_rc.py          # gerado por pyside6-rcc
├── app/
│   ├── __init__.py
│   ├── main_window.py
│   ├── dialogs/
│   │   └── find_dialog.py
│   ├── models/
│   │   └── data_model.py
│   ├── workers/
│   │   └── import_worker.py
│   └── utils/
│       └── settings.py
└── assets/
    ├── icons/
    ├── fonts/
    └── style.qss
```

### Dependências de build

```bash
pip install wheel pip-tools
```

`wheel` — build e distribuição de pacotes; `pip-tools` — resolução e pinagem de dependências (`pip-compile requirements.in`).

### Checklist de deploy
- [ ] `resources_rc.py` incluído e importado em `main.py`
- [ ] Caminhos de arquivo via `QStandardPaths` ou recursos embutidos — nunca hardcoded
- [ ] `app.setApplicationName` + `setOrganizationName` configurados (QSettings)
- [ ] `--windowed` / `--noconsole` para app GUI (sem janela de terminal)
- [ ] Testar o executável em máquina limpa (sem Python instalado)
- [ ] Assinar o executável (Windows: `signtool`; macOS: `codesign`) para evitar alertas de antivírus

### Plataformas alvo — formatos e expectativas

| Plataforma | Formato esperado | Observação |
|---|---|---|
| Windows | `.exe` + DLLs ou installer (Inno Setup / NSIS) | Usuários esperam installer ou EXE único |
| macOS | `.app` bundle dentro de `.dmg` | Requer codesign + notarização para macOS moderno |
| Linux | AppImage (portátil), `.deb` (Debian/Ubuntu), Flatpak/Snap | AppImage é o mais simples e amplo |

- PyInstaller **deve rodar na plataforma alvo**: build Windows em Windows, macOS em Mac, Linux em Linux. Cross-build via CI/CD com runners nativos é a prática padrão.
- Builds Qt costumam ser pesados (~100–300 MB); excluir plugins Qt não usados reduz o tamanho (`excludes` no `.spec`).
- Assets (ícones, `.ui`, configs) devem ser referenciados via Qt Resource System ou paths resolvidos dinamicamente — nunca caminhos relativos que quebram pós-empacotamento:

```python
import sys, os

if getattr(sys, 'frozen', False):   # PyInstaller
    BASE = sys._MEIPASS
else:
    BASE = os.path.dirname(__file__)

icon_path = os.path.join(BASE, "assets", "app.ico")
```

### Ambientes virtuais e gerenciamento de dependências

Use um **virtual environment dedicado** com apenas as dependências do projeto — isso garante builds menores e reproduzíveis e evita que PyInstaller inclua pacotes irrelevantes.

```bash
# Criar e ativar (Windows)
python -m venv .venv
.venv\Scripts\activate

# Criar e ativar (macOS/Linux)
python -m venv .venv
source .venv/bin/activate

# Instalar dependências
pip install PySide6 requests

# Exportar snapshot exato
pip freeze > requirements.txt

# Restaurar em outra máquina
pip install -r requirements.txt
```

**Alternativas modernas:**

| Ferramenta | Uso |
|---|---|
| `pip-tools` | `pip-compile requirements.in` → `requirements.txt` determinístico com apenas dependências diretas |
| `pyproject.toml` + Poetry / uv | Descriptor único para dependências, build e metadados do projeto |
| `pipreqs` | Gera `requirements.txt` a partir dos imports reais do código-fonte |

Mantenha `requirements.txt` (ou lockfile equivalente) no controle de versão e atualize ao adicionar/atualizar dependências.

### Versionamento semântico e configuração do usuário

**Versionamento** — use `major.minor.patch` (ex.: `1.2.3`):

| Número | Muda quando |
|---|---|
| `major` | Breaking change — incompatibilidade com versão anterior |
| `minor` | Nova funcionalidade retrocompatível |
| `patch` | Bugfix / pequena melhoria |

Embutir a versão no código:

```python
__version__ = "1.2.3"

# Exibir no About dialog
QMessageBox.about(self, "Sobre", f"App v{__version__}")
```

**Verificação de atualização assíncrona** (não bloqueia a UI):

```python
import threading, urllib.request, json

def check_for_update(current: str):
    def _fetch():
        try:
            url = "https://example.com/version.json"
            data = json.loads(urllib.request.urlopen(url, timeout=5).read())
            latest = data["version"]
            if latest != current:
                # Emitir sinal para notificar a UI na thread principal
                update_signal.emit(latest)
        except Exception:
            pass
    threading.Thread(target=_fetch, daemon=True).start()
```

**Configuração do usuário com `QSettings`** — persiste preferências entre sessões:

```python
from PySide6.QtCore import QSettings

# Setup (uma vez no main)
app.setApplicationName("MeuApp")
app.setOrganizationName("MinhaEmpresa")

# Salvar preferências (ex.: no closeEvent)
settings = QSettings()
settings.setValue("window/size", self.size())
settings.setValue("window/pos", self.pos())
settings.setValue("theme", "dark")

# Restaurar (ex.: no __init__)
settings = QSettings()
self.resize(settings.value("window/size", self.sizeHint()))
self.move(settings.value("window/pos", self.rect().topLeft()))
```

`QSettings` armazena em local nativo por padrão (registro no Windows, `.plist` no macOS, `.ini` no Linux). Para forçar INI portátil:

```python
settings = QSettings("config.ini", QSettings.Format.IniFormat)
```

---

## Migração PySide legado → PySide6

O Qt6 unificou enumerações em namespaces fortemente tipados (e.g., `Qt.AlignmentFlag.AlignCenter` em vez de `Qt.AlignCenter`) e removeu o sufixo `_()` dos métodos `exec`, `open` e similares. A ferramenta `pyside6-codemods` automatiza parte da migração, mas os usos de enums e a reorganização de módulos (ex.: `QAction` saiu de `QtWidgets` para `QtGui`) precisam ser revisados manualmente.

**PyQt6 vs PySide6**: PyQt6 exige nomes de enum completamente qualificados em todos os casos; PySide6 mantém suporte mais flexível (aceita a forma curta em alguns contextos). Para código que precisa rodar em ambos os bindings, use o padrão de import agnóstico:

```python
try:
    from PyQt6.QtWidgets import QApplication, QLabel
    from PyQt6.QtCore import Qt
except ImportError:
    from PySide6.QtWidgets import QApplication, QLabel
    from PySide6.QtCore import Qt
```

| API legada (Qt4/PySide ou Qt5/PySide2) | PySide6 |
|---|---|
| `from PySide.QtGui import QMainWindow, QAction, QHBoxLayout, ...` | `from PySide6.QtWidgets import ...` / `from PySide6.QtGui import ...` |
| `myApp.exec_()` / `dialog.exec_()` / `query.exec_("SQL")` | `.exec()` (sem underscore) |
| `self.connect(obj, SIGNAL("sig()"), slot)` | `obj.sig.connect(slot)` |
| `Qt.AlignCenter` | `Qt.AlignmentFlag.AlignCenter` |
| `Qt.Key_Escape` | `Qt.Key.Key_Escape` |
| `Qt.ControlModifier` | `Qt.KeyboardModifier.ControlModifier` |
| `QEvent.KeyPress` | `QEvent.Type.KeyPress` |
| `Qt.NoPen` | `Qt.PenStyle.NoPen` |
| `Qt.AscendingOrder` | `Qt.SortOrder.AscendingOrder` |
| `Qt.Horizontal` | `Qt.Orientation.Horizontal` |
| `QIcon.Active` | `QIcon.Mode.Active` |
| `QLCDNumber.Filled` | `QLCDNumber.SegmentStyle.Filled` |
| `QKeySequence.New` | `QKeySequence.StandardKey.New` |
| `QMessageBox.Yes` | `QMessageBox.StandardButton.Yes` |
| `QDialog.Accepted` | `QDialog.DialogCode.Accepted` |
| `QFileDialog.AnyFile` | `QFileDialog.FileMode.AnyFile` |
| `QInputDialog.getInteger()` | `QInputDialog.getInt()` |
| `QPrinter` / `QPrintDialog` (em QtGui) | `from PySide6.QtPrintSupport import ...` |
| `QDesktopWidget().availableGeometry()` | `QApplication.primaryScreen().availableGeometry()` |
| `qApp` | `QApplication.instance()` |
| `QListWidget.IconMode` | `QListWidget.ViewMode.IconMode` |
| `QGraphicsItemAnimation` (removido Qt5) | `QPropertyAnimation` |
| `QPainter(); painter.begin(self)` ... `painter.end()` | `QPainter(self)` — sem begin/end para QWidget |
| `QWorkspace` (removido Qt5) | `QMdiArea` + `QMdiSubWindow` |
| `QSqlTableModel.OnManualSubmit` | `QSqlTableModel.EditStrategy.OnManualSubmit` |
| `QSqlDriver.Transactions` | `QSqlDriver.DriverFeature.Transactions` |
| `QDataWidgetMapper.ManualSubmit` | `QDataWidgetMapper.SubmitPolicy.ManualSubmit` |
| `query.value(n).toInt()` / `.toString()` | `query.value(n)` — Python nativo direto |
| `Qt.AA_EnableHighDpiScaling` | Removido Qt6 — high DPI habilitado por padrão |
| `QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)` | Desnecessário no Qt6 |
| `QStateMachine` em `PySide2.QtCore` | `from PySide6.QtStateMachine import QStateMachine` |
| `QRegExp` | `QRegularExpression` (mesma API) ou módulo `re` nativo |

### C++ → Python: equivalências diretas

| C++ | Python / PySide6 |
|-----|-----------------|
| `QString` | `str` |
| `QVector<T>` / `QList<T>` | `list` |
| `QMap<K,V>` | `dict` |
| `QVariant` | objeto Python (duck typing) |
| `nullptr` / `NULL` | `None` |
| `this->method()` | `self.method()` |
| `new QObject(this)` | `QObject(self)` |
| `delete obj` | não necessário (GC) |
| `qDebug() << x` | `print(x)` |
| `qWarning() << x` | `import warnings; warnings.warn(x)` |
| `Q_OBJECT` | não necessário (implícito ao herdar `QObject`) |
| `signals:` | `signal = Signal(tipo)` na classe |
| `public slots:` | método comum (+ `@Slot()` opcional) |
| `emit signal()` | `self.signal.emit()` |
| `Q_INVOKABLE` | método Python comum (todos são invocáveis) |
| `Q_PROPERTY(...)` | `@Property(tipo, notify=signal)` |

### Regex em Python (preferir `re` a `QRegularExpression`)

```python
import re

text = "Jacky has 3 carrots and 15 apples."

numbers = re.findall(r"\d+", text)       # → ["3", "15"]
m = re.search(r"\d+", "abc123")
if m:
    print(m.group(0))                    # "123"
result = re.sub(r"\d+", "N", text)      # "Jacky has N carrots and N apples."
```

### Ferramentas de análise estática Python

| Ferramenta | Uso |
|---|---|
| `mypy` | Type checking estático |
| `pylint` / `ruff` | Linting e convenções de código |
| `pyupgrade` | Modernizar código Python antigo |

---

## Erros Comuns

A tabela abaixo mapeia sintomas frequentes a causas e soluções. A maioria dos erros envolve violação de três invariantes críticos do Qt: `QApplication` deve existir antes de qualquer widget; a thread principal é a única que pode acessar widgets (ver [Threading](#threading--qthread-e-qrunnable)); e o event loop deve estar livre para processar eventos durante operações longas.

| Erro / Sintoma | Causa | Solução |
|---|---|---|
| `RuntimeError: QApplication already created` | Múltiplas instâncias | Uma única por processo |
| Widget não aparece | `show()` não chamado | `widget.show()` em todo top-level widget |
| App fecha imediatamente | `exec()` não chamado | `sys.exit(app.exec())` no main |
| `ModuleNotFoundError: PySide6` | Não instalado | `pip install PySide6` |
| App congela / trava | Operação longa na thread principal | Usar `QThread` + Worker pattern |
| Janela não centraliza | `center()` chamado após `show()` | Chamar `center()` **antes** de `show()` |
| `QDesktopWidget` não existe | API removida Qt6 | `QApplication.primaryScreen()` |
| Hora não aparece no LCD | Slot não chamado antes de `timer.start()` | Chamar o slot uma vez antes de `timer.start()` |
| Ícone não aparece | Arquivo não no CWD | Usar caminho absoluto ou Qt resource system |
| `Tab key` não detectado em `keyPressEvent` | Qt intercepta Tab | Reimplementar `event()` ou usar `eventFilter` |
| Loop de sinais (dial↔spin) | Sem guarda no ciclo | `blockSignals(True/False)` |
| `paintEvent` não chamado | `update()` não chamado | `self.update()` quando dados mudarem |
| `QPainter not active` | `begin()` sem `end()` (legado) | `QPainter(self)` — sem begin/end |
| `eventFilter` engole eventos | Não retorna `super()` | Sempre retornar `super().eventFilter(...)` |
| `setCentralWidget()` não chamado | QMainWindow sem widget central | Obrigatório em toda QMainWindow |
| `AttributeError: qApp` | Removido PySide6 | `QApplication.instance()` |
| `getOpenFileName` retorna tupla | Segundo valor = filtro selecionado | `fname, _ = QFileDialog.getOpenFileName(...)` |
| `painter.save()` sem `restore()` | Transformações acumulam | Sempre parear `save()`/`restore()` |
| Arquivo `.db` não criado | `open()` antes de `setDatabaseName()` | `setDatabaseName()` **antes** de `open()` |
| `SELECT *` com `value(n)` errado | Ordem implícita | Listar colunas explicitamente |
| `submitAll()` sem efeito | `EditStrategy` errada | `OnManualSubmit` **antes** de `select()` |
| `setRelation()` não resolve nomes | Chamado após `select()` | `setRelation()` **antes** de `select()` |
| QSS não aplica após `setProperty()` | Qt não reavalia automaticamente | `style().unpolish(w); style().polish(w)` |
| Widget atualiza na thread errada | Acesso ao widget fora da thread principal | Emitir sinal para atualizar; nunca chamar direto |
| `QSettings` não persiste | `app/org` não configurado | `setApplicationName` + `setOrganizationName` |
| Tray icon não aparece | `show()` não chamado | `tray.show()` obrigatório |

---

## Checklist Geral

Este checklist consolida as boas práticas discutidas nas seções anteriores em itens verificáveis. Use-o como revisão antes de publicar código ou fechar um PR — cada item corresponde a uma regra documentada no guia e pode ser rastreada de volta à seção correspondente.

### Setup e Application
- [ ] `QApplication(sys.argv)` criado **antes** de qualquer widget — uma única instância
- [ ] `app.setApplicationName()` + `app.setOrganizationName()` configurados (habilita `QSettings`)
- [ ] `sys.exit(app.exec())` no final do `main()` (sem underscore)
- [ ] Código dentro de `if __name__ == "__main__":`
- [ ] Imports explícitos (`from PySide6.QtWidgets import ...`) — sem `import *`
- [ ] PySide6 em projetos novos (não PySide ou PySide2)

### Janelas e Widgets
- [ ] Herdar de `QWidget` ou `QMainWindow`; `super().__init__()` no construtor
- [ ] Lógica de UI separada em `_build_ui()` / `_create_actions()` / `_create_menus()`
- [ ] `widget.show()` chamado em todo widget de nível superior
- [ ] `center()` chamado **antes** de `show()` para centralizar
- [ ] `QMainWindow`: `setCentralWidget()` obrigatoriamente chamado
- [ ] Salvar/restaurar geometria e estado via `QSettings` no `closeEvent`

### Layouts
- [ ] Usar containers de layout — nunca absolute positioning em produção
- [ ] `QFormLayout.addRow(label, field)` para formulários label+campo
- [ ] `setContentsMargins` e `setSpacing` para espaçamento consistente

### Estilo (QSS)
- [ ] Estilos globais no `QApplication.setStyleSheet()`; específicos no widget
- [ ] `setObjectName()` para seletores `#id` em QSS
- [ ] Usar propriedades dinâmicas (`setProperty`) + `unpolish/polish` para estados customizados

### Sinais e Slots
- [ ] Sintaxe moderna: `signal.connect(slot)` — não usar `SIGNAL()`/`SLOT()`
- [ ] `@Slot(tipo)` para marcar slots explicitamente
- [ ] `Signal(tipo)` na classe para sinais customizados
- [ ] `blockSignals(True/False)` para evitar ciclos de sinalização

### Eventos
- [ ] Handlers específicos (`keyPressEvent`, `closeEvent`) para casos simples
- [ ] Sempre chamar `super().eventHandler(event)` para eventos não tratados
- [ ] `event()` para Tab/setas/espaço interceptados pelo Qt
- [ ] `eventFilter` + `installEventFilter(self)` para monitorar outros widgets
- [ ] Sempre retornar `super().eventFilter(...)` quando não tratar o evento

### Threading
- [ ] **Nunca** executar tarefas longas na thread principal
- [ ] Usar Worker (`QObject.moveToThread`) para tarefas com feedback/sinais
- [ ] Usar `QRunnable` + `QThreadPool` para tarefas fire-and-forget
- [ ] **Nunca** acessar/modificar widgets fora da thread principal

### Animações
- [ ] `QPropertyAnimation` para animações de propriedades (`geometry`, `pos`, `size`)
- [ ] `QGraphicsOpacityEffect` + `QPropertyAnimation` para fade in/out
- [ ] `QSequentialAnimationGroup` / `QParallelAnimationGroup` para composição

### Validação de Entrada
- [ ] `QIntValidator` / `QDoubleValidator` para campos numéricos
- [ ] `QRegularExpressionValidator` para padrões customizados
- [ ] `setInputMask()` para formatos fixos (telefone, IP, data)
- [ ] `QCompleter` para auto-complete em `QLineEdit`

### Desenho
- [ ] `QPainter(self)` no `paintEvent` (sem `begin()`/`end()`)
- [ ] `QPainter(pixmap)` exige `painter.end()` explícito ao terminar
- [ ] `self.update()` para forçar repaint quando dados mudarem
- [ ] Ângulos de arco/pie/chord em **1/16 de grau** (graus × 16)
- [ ] `save()`/`restore()` para isolar cada transformação

### Dialogs
- [ ] Dialogs built-in via funções estáticas — forma mais simples
- [ ] `fname, _ = QFileDialog.getOpenFileName(...)` — desempacotar sempre
- [ ] `QDialogButtonBox` para botões padronizados em QDialog customizado
- [ ] `dialog.exec()` para modal; `show()` para não-modal
- [ ] `label.setBuddy(widget)` para atalhos Alt+letra

### QSettings
- [ ] `QSettings()` sem parâmetros (exige `setApplicationName` + `setOrganizationName`)
- [ ] `value(key, defaultValue=..., type=int)` com `type` explícito para evitar strings
- [ ] Salvar geometria no `closeEvent`; restaurar no `__init__` antes de `show()`

### MDI
- [ ] `QMdiArea` como `centralWidget` + `QMdiSubWindow` para cada documento
- [ ] `sub.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)` para liberar memória

### Database
- [ ] Conectar ao banco **antes** de criar/exibir a janela principal
- [ ] Verificar `db.open()` e exibir `db.lastError().text()` em falha
- [ ] Prepared queries (`prepare` + `bindValue` + `exec`) para **todo** input externo (previne SQL injection)
- [ ] `setForwardOnly(True)` em queries grandes sem necessidade de navegação reversa
- [ ] `query.value(n)` retorna Python nativo — sem `.toInt()` / `.toString()`
- [ ] `QSqlTableModel.EditStrategy.OnManualSubmit` + `submitAll()` para controle de commit
- [ ] `setRelation()` **antes** de `select()` em `QSqlRelationalTableModel`
- [ ] Transações: `db.transaction()` → operações → `db.commit()` / `db.rollback()`
- [ ] `QSqlDatabase.removeDatabase(name)` ao encerrar para liberar o driver

### Model/View
- [ ] `QStandardItemModel` para modelos simples (lista, tabela, árvore) — sem necessidade de subclasse
- [ ] `QSortFilterProxyModel` para filtrar/ordenar sem tocar no modelo original
- [ ] `view.setSortingEnabled(True)` para ordenar ao clicar no cabeçalho
- [ ] `QAbstractTableModel` ao precisar de fonte de dados customizada (DB, API, arquivo)
- [ ] `QTableWidget` / `QTreeWidget` apenas para dados estáticos simples; preferir model/view para dados dinâmicos

### QtNetwork
- [ ] `QNetworkAccessManager` criado uma vez (reutilizar entre requests)
- [ ] Sempre conectar `reply.finished` e chamar `reply.deleteLater()` no handler
- [ ] Usar prepared queries / encodeamento correto para parâmetros na URL
- [ ] Tratar `reply.error() != NoError` antes de ler dados

### Undo/Redo
- [ ] `QUndoStack.push(cmd)` executa `redo()` automaticamente — não chamar redo manualmente
- [ ] `createUndoAction` / `createRedoAction` para actions integradas com atalhos
- [ ] `setClean()` após salvar; `isClean()` para detectar alterações não salvas
- [ ] `beginMacro` / `endMacro` para agrupar operações relacionadas

### Recursos e Deploy
- [ ] `pyside6-rcc resources.qrc -o resources_rc.py` ao modificar assets
- [ ] `import resources_rc` no `main.py` antes de usar caminhos `:/`
- [ ] Caminhos de dados via `QStandardPaths` — nunca hardcoded para garantir portabilidade
- [ ] Testar executável gerado em máquina limpa antes de distribuir

---

## Ferramentas de Desenvolvimento

### Qt Designer

Ferramenta visual para construir layouts `.ui` sem escrever código de posicionamento. Integra-se ao workflow via `pyside6-uic` (converte `.ui` para Python).

**PySide6**: incluído no Qt Tools oficial — instalar via Qt Online Installer (qt.io) → "Qt Tools → Qt Designer":

```bash
designer
```

**PyQt6**: disponível via Qt Online Installer ou distribuição Anaconda.

**Regra**: desenhe layouts no Qt Designer e carregue `.ui` no Python — separa layout da lógica de negócio; nunca edite o arquivo gerado manualmente.

> (Fonte "pysideNew.txt" acrescenta: o Designer oferece **preview mode** — teste espaçamento, alinhamento e comportamento de layouts antes de integrar com Python, sem escrever código. Object names definidos no Designer servem como identificadores para acesso direto em Python (`window.submitButton`, `window.inputField`). Escolha template ao criar: Main Window, Dialog ou Widget.)

### Verificar instalação

```python
# check_qt.py
try:
    from PySide6.QtWidgets import QApplication
    print("PySide6 is working.")
except ImportError:
    print("PySide6 not installed.")
```

```bash
python check_qt.py
```

> ⚠ Evite: executar sem virtual environment ativo — pacotes podem conflitar com o Python do sistema.

---

## Qt Designer — Workflow Completo

Qt Designer permite construir interfaces arrastando widgets numa tela visual. O resultado é um arquivo `.ui` (XML) que pode ser carregado dinamicamente em Python ou convertido numa classe Python. A separação entre layout visual e lógica Python é o principal benefício: mudanças de design no Designer refletem automaticamente no código sem regeneração (carregamento dinâmico) ou com um único passo de conversão.

### Criando um arquivo .ui

1. Abrir o Designer e escolher o template: **Main Window**, **Dialog** ou **Widget**.
2. Arrastar widgets da toolbox para o canvas; redimensionar e alinhar.
3. Aplicar gerenciadores de layout diretamente no Designer (vertical, horizontal, grid, aninhados).
4. Editar propriedades no **Property Editor**: object name, texto, tooltip, valor mínimo/máximo, stylesheet.
5. Usar **Preview Mode** para verificar espaçamento e comportamento antes de integrar com Python.
6. Salvar como `form.ui`.

**Regra**: use `objectName` descritivo para cada widget referenciado em Python — é o identificador que permite acesso direto (`window.submitButton`, `window.inputField`).

> ⚠ Evite: editar manualmente o arquivo `.ui` (XML) — use sempre o Designer para alterações de layout.

### Carregamento dinâmico (recomendado para prototipagem)

Qualquer modificação no Designer reflete imediatamente no Python sem regenerar arquivos.

**PyQt6:**

```python
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

app = QApplication([])
window = uic.loadUi("form.ui")
window.submitButton.clicked.connect(lambda: print(window.inputField.text()))
window.show()
app.exec()
```

**PySide6:**

```python
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile

app = QApplication([])
loader = QUiLoader()
file = QFile("form.ui")
file.open(QFile.OpenModeFlag.ReadOnly)
window = loader.load(file)
file.close()
window.show()
app.exec()
```

### Converter .ui em classe Python (recomendado para produção)

Gera um módulo Python que representa a interface como classe. Usar quando se quer separação clara entre UI gerada e lógica de negócio.

```bash
# PyQt6
pyuic6 form.ui -o form_ui.py

# PySide6
pyside6-uic form.ui -o form_ui.py
```

```python
from PyQt6.QtWidgets import QApplication, QMainWindow
from form_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)                              # inicializa todos os widgets do .ui
        self.submitButton.clicked.connect(self.handle_submit)

    def handle_submit(self):
        print(self.inputField.text())

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
```

**Regra**: o arquivo `.ui` é a fonte de verdade do design — a classe Python gerada nunca deve ser editada manualmente.

### Misturando Designer e código

Carregar o `.ui` e depois adicionar widgets programaticamente nas layouts do Designer:

```python
from PyQt6.QtWidgets import QApplication, QListWidget
from PyQt6 import uic

app = QApplication([])
window = uic.loadUi("form.ui")

# Acessar layout do Designer pelo objectName e injetar widget dinâmico
dynamic_list = QListWidget()
dynamic_list.addItems(["Item 1", "Item 2", "Item 3"])
window.verticalLayout.addWidget(dynamic_list)    # verticalLayout = objectName no Designer

# Widgets criados em código conectam-se a sinais normalmente
for i in range(5):
    from PyQt6.QtWidgets import QPushButton
    btn = QPushButton(f"Ação {i}")
    btn.clicked.connect(lambda checked, idx=i: print(f"Botão {idx} clicado"))
    window.verticalLayout.addWidget(btn)

window.show()
app.exec()
```

| Caso | Abordagem recomendada |
|---|---|
| Prototipagem rápida, layout muda frequentemente | Carregamento dinâmico (`uic.loadUi` / `QUiLoader`) |
| Produção, integração com CI/CD, linting | Converter para classe Python (`pyuic6` / `pyside6-uic`) |
| Widgets gerados em runtime (DB, API) | Código puro ou injetar em layout do .ui |
| Layout fixo + conteúdo dinâmico | Híbrido: Designer para estrutura, código para conteúdo |

### Boas práticas de organização

- Colocar arquivos `.ui` em diretório dedicado (ex.: `views/`).
- `objectName` descritivo e consistente com o nome da variável Python correspondente.
- Definir stylesheets globais no `QApplication`; estilizações específicas de layout no Designer.
- Nunca alterar o arquivo gerado (`form_ui.py`) — regenere com `pyuic6` / `pyside6-uic` após mudanças no `.ui`.

> (Fonte "qt6_cpp_cookbook_skill" acrescenta: para ter controle preciso de tamanho de um widget num layout no Designer, use _Morph into → QWidget_ — converte o item num container QWidget com política de tamanho configurável.)

> (Fonte "qt6_cpp_cookbook_skill" acrescenta: para remover as margens internas da janela principal, defina _centralWidget → Contents Margins_ como 0 em todas as direções no Property Editor do Qt Designer.)


---

## Estrutura de Projeto Real e Padrões de Arquitetura

### Paradigma Model-View

Separa dados (model) de apresentação (view). Views atualizam automaticamente quando o model muda; múltiplas views podem compartilhar o mesmo model sem duplicar lógica.

| Model | Uso |
|---|---|
| `QStringListModel` | Listas simples de strings |
| `QStandardItemModel` | Tabelas e dados hierárquicos |
| `QAbstractTableModel` | Dados customizados, controle total |
| `QAbstractItemModel` | Estruturas complexas/árvores |

```python
from PySide6.QtWidgets import QApplication, QListView
from PySide6.QtCore import QStringListModel

app = QApplication([])
view = QListView()
model = QStringListModel(["Alice", "Bob", "Charlie"])
view.setModel(model)
view.show()
app.exec()
```

**Custom model subclassando QAbstractTableModel:**

```python
from PySide6.QtCore import Qt, QAbstractTableModel

class UserTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data  # list of lists

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data[0]) if self._data else 0

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]
        return None
```

- Emitir `dataChanged` após mutações para notificar views
- Sorting e filtering: usar `QSortFilterProxyModel` como intermediário entre model e view

---

### Widgets Reutilizáveis e Customizados

Encapsular UI + lógica em classes reutilizáveis via subclasse de `QWidget` ou `QFrame`.

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Signal

class InfoPanel(QWidget):
    closed = Signal()  # sinal customizado para comunicar com o pai

    def __init__(self, title, message, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        layout.addWidget(QLabel(title))
        layout.addWidget(QLabel(message))
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self._on_close)
        layout.addWidget(close_btn)
        self.setLayout(layout)

    def _on_close(self):
        self.closed.emit()
        self.close()
```

**Boas práticas:**
- Usar `Signal` para comunicar com o pai (não referenciar a janela pai diretamente)
- Aceitar parâmetros no `__init__` para configurar comportamento
- Expor métodos públicos para controle programático externo
- Aplicar stylesheet no próprio widget para estilo isolado e reutilizável

---

### Temas e Estilização da Aplicação

Stylesheet global via `QApplication` garante tema unificado:

```python
app.setStyleSheet("""
QPushButton {
    background-color: #3498db;
    color: white;
    border-radius: 5px;
    padding: 5px 15px;
}
QPushButton:hover {
    background-color: #2980b9;
}
QLabel {
    font-family: Arial;
    font-size: 14px;
    color: #2c3e50;
}
""")
```

**Dark mode dinâmico:**

```python
def enable_dark_mode(window):
    window.setStyleSheet("""
    QWidget {
        background-color: #2c3e50;
        color: #ecf0f1;
    }
    QPushButton {
        background-color: #34495e;
        color: #ecf0f1;
    }
    """)
```

| Técnica | Aplicação |
|---|---|
| `app.setStyleSheet(...)` | Tema global |
| `widget.setStyleSheet(...)` | Estilo local (sobrescreve global) |
| `QApplication.setPalette(...)` | Paleta de cores nativa do sistema |
| Propriedades (`font`, `palette`) | Ajustes precisos por widget |

- Stylesheet global definido em código; Designer para ajustes de layout estático
- Dark/light mode: trocar stylesheet em runtime via ação do usuário ou `QStyleHints.colorScheme()`

---

## File I/O — Texto, CSV, JSON

### Texto

```python
# Leitura
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()       # string completa
    lines   = f.readlines()  # lista de linhas

# Escrita / Append
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("linha 1\n")

with open("log.txt", "a", encoding="utf-8") as f:
    f.write("mais uma linha\n")
```

### CSV

```python
import csv

# Leitura (como dicionário)
with open("data.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["email"])

# Escrita
with open("out.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "email"])
    writer.writeheader()
    writer.writerow({"name": "Alice", "email": "alice@ex.com"})
```

### JSON

```python
import json

with open("config.json", "r", encoding="utf-8") as f:
    data = json.load(f)          # dict/list

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
```

### Integração Qt — Abrir/Salvar via diálogo

```python
from PySide6.QtWidgets import QFileDialog

path, _ = QFileDialog.getOpenFileName(
    self, "Abrir", "", "CSV (*.csv);;JSON (*.json);;Texto (*.txt)"
)
if path:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

save_path, _ = QFileDialog.getSaveFileName(self, "Salvar", "", "JSON (*.json)")
if save_path:
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
```

| Formato | Módulo | Caso de uso |
|---|---|---|
| `.txt` | built-in | logs, notas, config simples |
| `.csv` | `csv` | tabelas, listas exportáveis |
| `.json` | `json` | configurações, estado da app, APIs |

**Qt JSON API** (use apenas quando `QJsonDocument` é necessário para interoperar com QML ou `QVariant`; prefira `json` nativo em todos os outros casos):

```python
from PySide6.QtCore import QJsonDocument, QJsonObject, QByteArray

raw = QByteArray(b'{"name": "Alice", "age": 30}')
doc = QJsonDocument.fromJson(raw)
obj = doc.object()
print(obj["name"].toString())    # "Alice"
print(obj["age"].toInt())        # 30

# Serializar de volta
new_obj = QJsonObject()
new_obj["name"] = "Bob"
new_obj["age"] = 25
print(QJsonDocument(new_obj).toJson().data().decode())
```

- Sempre use `encoding="utf-8"` para portabilidade cross-platform
- Use `newline=""` em CSV para evitar linhas duplas no Windows

---

## SQLite com sqlite3

### Setup e criação de tabela

```python
import sqlite3

def init_db(path="app.db"):
    with sqlite3.connect(path) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                name  TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
```

### CRUD básico

```python
def add_contact(name, email, path="app.db"):
    with sqlite3.connect(path) as conn:
        conn.execute(
            "INSERT INTO contacts (name, email) VALUES (?, ?)", (name, email)
        )

def load_contacts(path="app.db") -> list[tuple]:
    with sqlite3.connect(path) as conn:
        return conn.execute("SELECT id, name, email FROM contacts").fetchall()

def delete_contact(contact_id, path="app.db"):
    with sqlite3.connect(path) as conn:
        conn.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))

def update_contact(contact_id, name, email, path="app.db"):
    with sqlite3.connect(path) as conn:
        conn.execute(
            "UPDATE contacts SET name=?, email=? WHERE id=?", (name, email, contact_id)
        )
```

### Popula QTableWidget a partir do banco

```python
from PySide6.QtWidgets import QTableWidgetItem

def refresh_table(table_widget, path="app.db"):
    rows = load_contacts(path)
    table_widget.setRowCount(len(rows))
    for r, (row_id, name, email) in enumerate(rows):
        table_widget.setItem(r, 0, QTableWidgetItem(name))
        table_widget.setItem(r, 1, QTableWidgetItem(email))
```

### Acesso por nome de coluna

```python
conn.row_factory = sqlite3.Row
cursor = conn.execute("SELECT * FROM contacts")
for row in cursor:
    print(row["name"], row["email"])  # acesso pelo nome
```

| Dica | Detalhe |
|---|---|
| `with sqlite3.connect(...)` | Commit automático no `__exit__` |
| Parâmetros `?` | Previne SQL injection — nunca use f-strings em SQL |
| `sqlite3.Row` como `row_factory` | Acesso por nome de coluna |
| Arquivo `.db` em produção | Empacotar com o executável; caminhos relativos ao executável |

---

## REST APIs com requests + QThread

### Thread genérica para fetch assíncrono

```python
from PySide6.QtCore import QThread, Signal
import requests

class FetchThread(QThread):
    data_ready = Signal(object)  # emite list/dict
    error      = Signal(str)

    def __init__(self, url, params=None, headers=None):
        super().__init__()
        self.url     = url
        self.params  = params  or {}
        self.headers = headers or {}

    def run(self):
        try:
            resp = requests.get(
                self.url, params=self.params,
                headers=self.headers, timeout=10
            )
            resp.raise_for_status()
            self.data_ready.emit(resp.json())
        except Exception as e:
            self.error.emit(str(e))
```

### Uso na janela

```python
from PySide6.QtWidgets import QWidget, QListWidget, QPushButton, QVBoxLayout, QMessageBox

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.list_widget = QListWidget()
        self.btn = QPushButton("Buscar")
        self.btn.clicked.connect(self.start_fetch)
        layout = QVBoxLayout(self)
        layout.addWidget(self.list_widget)
        layout.addWidget(self.btn)

        self._thread = FetchThread("https://jsonplaceholder.typicode.com/users")
        self._thread.data_ready.connect(self._on_data)
        self._thread.error.connect(lambda e: QMessageBox.warning(self, "Erro", e))

    def start_fetch(self):
        self.btn.setEnabled(False)
        self.list_widget.clear()
        self._thread.start()

    def _on_data(self, users):
        self.btn.setEnabled(True)
        for u in users:
            self.list_widget.addItem(f"{u['name']} — {u['email']}")
```

### POST e autenticação

```python
# POST com JSON body
resp = requests.post(url, json={"key": "value"}, timeout=10)

# Bearer token
resp = requests.get(url, headers={"Authorization": f"Bearer {token}"}, timeout=10)

# Query params (GET)
resp = requests.get(url, params={"search": query, "page": 1}, timeout=10)
```

| Item | Recomendação |
|---|---|
| Timeout | Sempre definir `timeout=` para não bloquear a thread |
| API keys | Variáveis de ambiente ou config file — nunca hardcoded |
| Erro HTTP | `resp.raise_for_status()` levanta exceção em 4xx/5xx |
| Sinal `error` | Mostrar `QMessageBox` no slot conectado |
| Thread reuse | Não chame `start()` em thread já rodando; crie nova instância ou aguarde |

---

## Multimídia — QMediaPlayer e QVideoWidget

### Reprodução de áudio

```python
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl

audio_output = QAudioOutput()
player = QMediaPlayer()
player.setAudioOutput(audio_output)
player.setSource(QUrl.fromLocalFile("media/sound.mp3"))

player.play()
player.pause()
player.stop()
audio_output.setVolume(0.8)  # 0.0 – 1.0
```

### Reprodução de vídeo

```python
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QVBoxLayout

video_widget = QVideoWidget()
player.setVideoOutput(video_widget)
player.setSource(QUrl.fromLocalFile("media/video.mp4"))
player.play()

layout = QVBoxLayout(self)
layout.addWidget(video_widget)
```

### Barra de progresso sincronizada

```python
from PySide6.QtWidgets import QSlider
from PySide6.QtCore import Qt

slider = QSlider(Qt.Orientation.Horizontal)
player.durationChanged.connect(slider.setMaximum)
player.positionChanged.connect(slider.setValue)
slider.sliderMoved.connect(player.setPosition)
```

### Carregar imagem da web em QPixmap

```python
import requests
from PySide6.QtCore import QByteArray
from PySide6.QtGui import QPixmap

resp = requests.get("https://example.com/avatar.jpg", timeout=10)
if resp.status_code == 200:
    pixmap = QPixmap()
    pixmap.loadFromData(QByteArray(resp.content))
    label.setPixmap(pixmap)
```

| Classe | Módulo | Uso |
|---|---|---|
| `QMediaPlayer` | `QtMultimedia` | Controle central de reprodução |
| `QAudioOutput` | `QtMultimedia` | Volume e dispositivo de saída |
| `QVideoWidget` | `QtMultimediaWidgets` | Widget de exibição de vídeo |
| `QUrl.fromLocalFile` | `QtCore` | Converte caminho local para URL Qt |

- Instale `PySide6-Addons` se `QtMultimedia` não estiver disponível
- Codecs dependem do sistema; use formatos amplamente suportados (mp3, mp4/H.264)

---

## Projetos Completos

> Quatro aplicações completas que consolidam layouts, sinais/slots, persistência de dados e widgets customizados.

| # | Projeto | Foco Principal |
|---|---|---|
| 6.1 | Calculator | Widgets, sinais/slots, QGridLayout |
| 6.2 | Notes App | QTextEdit, File I/O, QFileDialog |
| 6.3 | Image Viewer | QPixmap, resizeEvent, widget customizado |
| 6.4 | Web Browser | QWebEngineView, navegação embutida |

---

### 6.1 Calculator App — Core Widgets e Signals

A calculadora reúne botões (QPushButton), display (QLineEdit/QLabel), QGridLayout e o ciclo sinal→slot→atualização de UI.

**Estrutura básica:**

```python
from PySide6.QtWidgets import (
    QApplication, QWidget, QLineEdit,
    QPushButton, QGridLayout
)
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.expression = ""

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)

        grid = QGridLayout()
        grid.addWidget(self.display, 0, 0, 1, 4)

        buttons = [
            ("7","8","9","/"),
            ("4","5","6","*"),
            ("1","2","3","-"),
            ("0","C","=","+"),
        ]
        for row, row_labels in enumerate(buttons):
            for col, label in enumerate(row_labels):
                btn = QPushButton(label)
                btn.clicked.connect(lambda _, l=label: self.on_button(l))
                grid.addWidget(btn, row + 1, col)

        self.setLayout(grid)

    def on_button(self, label: str):
        if label == "=":
            try:
                self.display.setText(str(eval(self.expression)))
            except Exception:
                self.display.setText("Error")
            self.expression = ""
        elif label == "C":
            self.expression = ""
            self.display.clear()
        else:
            self.expression += label
            self.display.setText(self.expression)

app = QApplication(sys.argv)
win = Calculator()
win.show()
sys.exit(app.exec())
```

**Pontos-chave:**
- `QGridLayout` espelha o layout físico de uma calculadora
- Use `lambda _, l=label:` para capturar o valor do loop corretamente
- Separe lógica de avaliação do UI para facilitar testes

---

### 6.2 Notes App — Text Editing e Data Persistence

Introduz `QTextEdit` para edição de texto e operações de arquivo com `QFileDialog`.

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit,
    QFileDialog, QMenuBar, QMessageBox
)
from PySide6.QtGui import QAction
import sys

class NotesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notes")
        self.current_file = None
        self.unsaved = False

        self.editor = QTextEdit()
        self.editor.textChanged.connect(self._mark_unsaved)
        self.setCentralWidget(self.editor)

        self._build_menu()

    def _build_menu(self):
        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        for name, slot in [
            ("New",   self.new_file),
            ("Open",  self.open_file),
            ("Save",  self.save_file),
            ("Save As", self.save_as),
        ]:
            act = QAction(name, self)
            act.triggered.connect(slot)
            file_menu.addAction(act)

    def _mark_unsaved(self):
        self.unsaved = True

    def _confirm_discard(self) -> bool:
        if not self.unsaved:
            return True
        reply = QMessageBox.question(
            self, "Unsaved changes",
            "Discard unsaved changes?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        return reply == QMessageBox.StandardButton.Yes

    def new_file(self):
        if self._confirm_discard():
            self.editor.clear()
            self.current_file = None
            self.unsaved = False

    def open_file(self):
        if not self._confirm_discard():
            return
        path, _ = QFileDialog.getOpenFileName(self, "Open", "", "Text Files (*.txt);;All Files (*)")
        if path:
            with open(path, "r", encoding="utf-8") as f:
                self.editor.setPlainText(f.read())
            self.current_file = path
            self.unsaved = False

    def save_file(self):
        if self.current_file:
            self._write(self.current_file)
        else:
            self.save_as()

    def save_as(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save As", "", "Text Files (*.txt);;All Files (*)")
        if path:
            self._write(path)
            self.current_file = path

    def _write(self, path: str):
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.editor.toPlainText())
        self.unsaved = False

app = QApplication(sys.argv)
win = NotesApp()
win.resize(800, 600)
win.show()
sys.exit(app.exec())
```

**Pontos-chave:**
- `toPlainText()` retorna o conteúdo como string pura
- Conecte `textChanged` a um flag para rastrear alterações não salvas
- `QFileDialog.getOpenFileName` / `getSaveFileName` retornam `(path, filter)`

---

### 6.3 Image Viewer — Arquivos e Widget Customizado

Ensina `QPixmap`, `resizeEvent` e encapsulamento em widget reutilizável.

**Carregamento básico:**

```python
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys

class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        self.original_pixmap = None

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)

        self.open_image()

    def open_image(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "",
            "Images (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        if path:
            self.original_pixmap = QPixmap(path)
            self.update_image()

    def resizeEvent(self, event):
        self.update_image()
        super().resizeEvent(event)

    def update_image(self):
        if self.original_pixmap:
            scaled = self.original_pixmap.scaled(
                self.image_label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.image_label.setPixmap(scaled)

app = QApplication(sys.argv)
viewer = ImageViewer()
viewer.resize(800, 600)
viewer.show()
sys.exit(app.exec())
```

**Widget reutilizável (`ImageDisplay`):**

```python
class ImageDisplay(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._pixmap = None

    def set_image(self, file_path: str):
        self._pixmap = QPixmap(file_path)
        self.update_display()

    def resizeEvent(self, event):
        self.update_display()
        super().resizeEvent(event)

    def update_display(self):
        if self._pixmap:
            self.setPixmap(
                self._pixmap.scaled(
                    self.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
            )
```

**Pontos-chave:**
- Armazene `original_pixmap` e reescale em `resizeEvent` para evitar distorção
- Subclassear `QLabel` encapsula lógica de imagem e permite reutilização
- Extensões comuns: zoom, atalhos de teclado, drag-and-drop, metadados EXIF

---

### 6.4 Web Browser — QWebEngineView

Embute um navegador Chromium completo no app. Requer `PySide6-WebEngine`.

```bash
pip install PySide6-WebEngine
```

**Browser básico:**

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QToolBar,
    QLineEdit
)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
import sys

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Browser")

        self.view = QWebEngineView()
        self.setCentralWidget(self.view)

        # Toolbar com barra de URL
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self._navigate)
        toolbar.addWidget(self.url_bar)

        for label, slot in [
            ("←", self.view.back),
            ("→", self.view.forward),
            ("↺", self.view.reload),
        ]:
            from PySide6.QtGui import QAction
            act = QAction(label, self)
            act.triggered.connect(slot)
            toolbar.addAction(act)

        # Sincroniza barra de URL com navegação
        self.view.urlChanged.connect(
            lambda url: self.url_bar.setText(url.toString())
        )
        self.view.loadProgress.connect(
            lambda p: self.statusBar().showMessage(f"Loading… {p}%")
        )
        self.view.loadFinished.connect(
            lambda _: self.statusBar().clearMessage()
        )

        self.view.setUrl(QUrl("https://www.example.com"))

    def _navigate(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.view.setUrl(QUrl(url))

app = QApplication(sys.argv)
win = Browser()
win.resize(1200, 800)
win.show()
sys.exit(app.exec())
```

**Carregar arquivo local:**

```python
from PySide6.QtCore import QUrl
import pathlib

# Converter caminho local para file:/// URL
path = pathlib.Path("index.html").resolve()
view.setUrl(QUrl.fromLocalFile(str(path)))
```

**Executar JavaScript na página:**

```python
view.page().runJavaScript("document.title", lambda result: print(result))
```

**Pontos-chave:**
- `QWebEngineView` usa Chromium em processo separado — crashes são isolados
- Sinais úteis: `loadStarted`, `loadProgress`, `loadFinished`, `urlChanged`, `titleChanged`
- Sempre use `QUrl.fromLocalFile()` para arquivos locais
- Para múltiplas abas: múltiplas instâncias de `QWebEngineView` em `QTabWidget`

| Método / Signal | Descrição |
|---|---|
| `setUrl(QUrl)` | Navega para URL |
| `load(QUrl)` | Alias de setUrl |
| `back()` / `forward()` / `reload()` | Navegação |
| `page().runJavaScript(code, cb)` | Executa JS, retorna resultado via callback |
| `urlChanged` | Emitido quando URL muda |
| `loadFinished(bool)` | True = sucesso, False = erro |

**Carregar HTML e conteúdo binário:**
```python
# HTML inline
view.setHtml(html_string)

# Conteúdo binário (ex: imagem)
with open("tux.png", "rb") as f:
    view.page().setContent(f.read(), "image/png")

# Forçar esquema HTTP na URL
url = QUrl(address_bar.text())
url.setScheme("http")
view.page().load(url)
```

**Configurações do WebEngine:**
```python
from PySide6.QtWebEngineCore import QWebEngineSettings

settings = view.page().settings()
settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, False)
settings.setAttribute(QWebEngineSettings.WebAttribute.AutoLoadImages, False)
```

**JavaScript → Python via QWebChannel:**
```python
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtCore import QObject, Slot

class Backend(QObject):
    @Slot(str)
    def my_slot(self, message):
        print(f"JS disse: {message}")

backend = Backend()
channel = QWebChannel(view)
channel.registerObject("backend", backend)
view.page().setWebChannel(channel)
```

```javascript
// Lado JavaScript — incluir qwebchannel.js
new QWebChannel(qt.webChannelTransport, function(channel) {
    channel.objects.backend.my_slot("olá do JavaScript");
});
```

**Remote debugging:**
```python
import os
os.environ["QTWEBENGINE_REMOTE_DEBUGGING"] = "1234"
# Acessível em http://127.0.0.1:1234 no Chrome/Chromium
# Remover antes de produção
```

---

## Multithreading e Tarefas Assíncronas

**Regra fundamental:** a GUI deve sempre rodar na thread principal. Nunca atualize widgets de uma worker thread.

Qt usa **worker objects** que vivem em threads separadas e se comunicam com a GUI via signals/slots — evitando race conditions.

### QThread — Padrão Correto

Subclassifique `QObject` para o worker (não `QThread`), mova-o para a thread com `moveToThread()`.

```python
from PySide6.QtCore import QObject, QThread, Signal
import time

class Worker(QObject):
    progress = Signal(int)
    finished = Signal()

    def run(self):
        for i in range(1, 101):
            time.sleep(0.05)
            self.progress.emit(i)
        self.finished.emit()

class MainWindow(QWidget):
    def start_task(self):
        self.thread = QThread()
        self.worker = Worker()

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.progress.connect(self.progress_bar.setValue)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
```

**Pontos-chave:**
- Worker faz o trabalho, thread hospeda o worker, signals movem dados, GUI reage
- `deleteLater()` garante cleanup automático
- Nunca chame métodos de widget diretamente de dentro do worker

### QThreadPool + QRunnable — Tarefas Curtas

Para múltiplas tarefas curtas (processamento de arquivos, redimensionamento de imagens).

```python
from PySide6.QtCore import QRunnable, QThreadPool, Signal, QObject
import time

class TaskSignals(QObject):
    result = Signal(str)

class Task(QRunnable):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.signals = TaskSignals()

    def run(self):
        time.sleep(1)
        self.signals.result.emit(f"Processed {self.value}")

class MainWindow(QWidget):
    def run_tasks(self):
        pool = QThreadPool.globalInstance()
        for i in range(5):
            task = Task(i)
            task.signals.result.connect(print)
            pool.start(task)
```

### Assíncrono Sem Threads — QTimer

Para execução diferida sem bloquear:

```python
from PySide6.QtCore import QTimer

def delayed_action():
    print("Executed later without blocking")

QTimer.singleShot(2000, delayed_action)
```

**Erros comuns:**
- Atualizar widgets de worker thread → crash eventual
- `time.sleep()` na thread principal → UI congela
- Não limpar threads → memory leaks

---

## GUIs Responsivas e Operações Longas

Quando `app.exec()` inicia o event loop, qualquer operação lenta dentro de um slot bloqueia esse loop — a janela congela.

**Solução:** mover tarefas intensivas para fora da thread principal.

```python
import sys, time
from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QProgressBar

class Worker(QObject):
    progress = Signal(int)
    finished = Signal()

    def run(self):
        for i in range(1, 101):
            time.sleep(0.03)
            self.progress.emit(i)
        self.finished.emit()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.progress_bar = QProgressBar()
        self.button = QPushButton("Start Work")
        self.button.clicked.connect(self.start_work)

        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def start_work(self):
        self.thread = QThread()
        self.worker = Worker()

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.progress.connect(self.progress_bar.setValue)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
```

**Regras críticas:**
- Apenas a thread principal modifica widgets
- Signals entre threads são enfileirados pelo event loop (thread-safe)
- Para muitas tarefas concorrentes curtas: `QThreadPool` + `QRunnable`

---

## Tratamento de Erros e Debugging

### Exceções em Slots

Nunca deixe exceções propagarem de dentro de um slot — pode causar comportamento indefinido no event loop. Capture localmente e comunique falhas ao usuário.

```python
def open_file(self):
    try:
        text = self.read_file(self.current_path)
        self.text_edit.setPlainText(text)
    except FileNotFoundError as e:
        QMessageBox.warning(self, "File Error", f"Cannot open file: {e}")
    except Exception as e:
        QMessageBox.critical(self, "Unknown Error", f"Unexpected problem: {e}")
```

### Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)

def process_data(data):
    logging.debug(f"Processing data: {data}")
    # lógica de processamento aqui
```

**Níveis:** `DEBUG` → `INFO` → `WARNING` → `ERROR` → `CRITICAL`

### Debugging de Signals/Slots

Signals desacoplam código, mas são difíceis de rastrear. Estratégias:

- Conecte slots de debug temporários que fazem log quando signals disparam
- Use breakpoints no IDE — o debugger não quebra automaticamente em emissão de signal
- Adicione logging ao redor de `connect()` e `emit()` para confirmar o fluxo esperado

**Padrão profissional:** combinar tratamento de exceções direcionado + logging persistente + debugger interativo para casos de comportamento incorreto sem crash.

---

## Testes Automatizados de GUI

### pytest + pytest-qt

`pytest-qt` fornece o fixture `qtbot` para criar widgets, simular cliques, digitar texto e aguardar signals.

**Instalar:**
```bash
pip install pytest pytest-qt
```

**Estrutura básica de teste:**
```python
# test_my_app.py
def test_button_click(qtbot):
    widget = MainWindow()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.button, Qt.LeftButton)

    assert widget.label.text() == "Clicked!"
```

**Aguardar signals:**
```python
def test_worker_finishes(qtbot):
    worker = Worker()
    with qtbot.waitSignal(worker.finished, timeout=5000):
        worker.run()
```

### Separação de Lógica e UI

Teste lógica de negócio independentemente da GUI:

```python
# Lógica em classe separada (sem widgets)
class DataProcessor:
    def calculate(self, values):
        return sum(values) / len(values)

# Teste puro (sem qtbot)
def test_calculate():
    proc = DataProcessor()
    assert proc.calculate([10, 20, 30]) == 20.0
```

### QTest (baixo nível)

`QtTest.QTest` oferece simulação direta de teclado/mouse — útil quando integrado a frameworks de teste.

```python
from PySide6.QtTest import QTest
from PySide6.QtCore import Qt

QTest.keyClick(widget.line_edit, Qt.Key_Return)
QTest.mouseClick(widget.button, Qt.LeftButton)
```

**Boas práticas:**
- Misture unit tests de lógica + testes de interação de UI
- `pytest-qt` integra bem com CI/CD — testes rodam automaticamente ao commitar
- Evite duplicar testes de lógica no nível de widget — teste cada camada onde ela vive
- `qtbot.waitSignal()` e `qtbot.waitCallback()` evitam flakiness em testes assíncronos

| Ferramenta | Uso |
|---|---|
| `pytest` | Framework base, execução e relatórios |
| `pytest-qt` / `qtbot` | Simulação de interações de widget, espera de signals |
| `QTest` | Simulação de input de baixo nível (teclas, mouse) |
| `unittest` | Alternativa padrão ao pytest |

---

## UX e Design de Interface

Interfaces bem-projetadas guiam o usuário sem que ele perceba. Os princípios abaixo se aplicam diretamente ao desenvolvimento PySide6.

**Princípios fundamentais:**
- Agrupar controles relacionados visualmente — proximidade transmite relação
- Sempre usar o sistema de layouts (`QVBoxLayout`, `QHBoxLayout`, `QGridLayout`) em vez de coordenadas fixas — garante adaptação a diferentes DPIs, fontes e resoluções
- Ícones ao lado de texto aceleram a leitura; use `QAction` para unificar ícone + label + atalho entre menus, toolbars e context menus
- Feedback visual em operações longas — `QProgressBar`, `QStatusBar`, desabilitar botão durante processamento

```python
from PySide6.QtWidgets import QProgressBar, QStatusBar, QPushButton

# Desabilitar botão durante operação longa
self.btn_processar.setEnabled(False)
self.status_bar.showMessage("Processando...")
# ... ao terminar:
self.btn_processar.setEnabled(True)
self.status_bar.showMessage("Concluído.", 3000)
```

**Testar layouts com dados extremos:** texto longo, imagens grandes, janela redimensionada — widgets devem expandir/envolver corretamente sem sobreposição.

| Princípio | Implementação Qt |
|---|---|
| Agrupamento | `QGroupBox`, `QFrame`, espaçadores |
| Feedback de progresso | `QProgressBar`, `QStatusBar` |
| Consistência de ações | `QAction` compartilhada em menus e toolbars |
| Responsividade a resize | Layouts gerenciados (nunca `setGeometry` fixo) |

---

## Atalhos de Teclado, Menus e Toolbars

O mesmo `QAction` deve estar por trás de um item de menu e de um botão de toolbar — define-se ícone, label e atalho uma vez só.

```python
from PySide6.QtWidgets import QMainWindow, QToolBar
from PySide6.QtGui import QAction, QKeySequence, QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Criar ação reutilizável
        open_action = QAction(QIcon("open.png"), "&Abrir", self)
        open_action.setShortcut(QKeySequence("Ctrl+O"))
        open_action.setStatusTip("Abrir arquivo")
        open_action.triggered.connect(self.abrir_arquivo)

        # Menu
        menu = self.menuBar().addMenu("&Arquivo")
        menu.addAction(open_action)

        # Toolbar
        toolbar: QToolBar = self.addToolBar("Principal")
        toolbar.addAction(open_action)
```

**Aceleradores mnemônicos:** prefixo `&` em labels de menu/botão ativa o controle via `Alt+letra`.

```python
menu.addAction("&Salvar")   # Alt+S foca este item
```

**Boas práticas:**
- Toolbars só para ações frequentes — não duplicar todo o menu
- Widgets interativos (busca, combo) podem ser adicionados diretamente à toolbar via `toolbar.addWidget()`
- Atalhos padrão (`Ctrl+O`, `Ctrl+S`, `Ctrl+Z`) devem ser respeitados — usuários os memorizam

| Elemento | Classe Qt |
|---|---|
| Ação unificada | `QAction` |
| Menu principal | `QMenuBar` / `QMenu` |
| Toolbar | `QToolBar` |
| Atalho | `QKeySequence` |
| Mnemônico | `&` no label |

---

## Acessibilidade

Qt expõe metadados de widgets (papel, label, foco) para APIs de acessibilidade nativas de cada plataforma, alimentando leitores de tela e interfaces braille automaticamente.

**Navegação por teclado:**
- Tab / Shift+Tab — percorrer controles na ordem visual
- Setas — navegação dentro de listas e tabelas
- Escape — fechar diálogos
- Controles devem ter indicador de foco visível

```python
# Definir ordem de foco explícita
from PySide6.QtWidgets import QWidget

widget_a.setTabOrder(widget_a, widget_b)
widget_a.setTabOrder(widget_b, widget_c)

# Adicionar tooltip acessível
btn.setToolTip("Salvar documento (Ctrl+S)")
btn.setAccessibleName("Botão Salvar")
btn.setAccessibleDescription("Salva o documento atual no disco")
```

**Contraste e escalabilidade:**
- Não transmitir informação só por cor — combinar cor com ícone ou texto
- Layouts gerenciados + fontes relativas respeitam configurações de DPI e acessibilidade do sistema
- Testar com tamanhos de fonte aumentados: `app.setFont(QFont("Arial", 14))`

```python
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication

app = QApplication([])
app.setFont(QFont("Segoe UI", 12))   # escala uniformemente a UI
```

| Aspecto | Mecanismo Qt |
|---|---|
| Metadados para leitores de tela | `setAccessibleName()`, `setAccessibleDescription()` |
| Ordem de foco | `setTabOrder()` |
| Tooltip | `setToolTip()` |
| Escalabilidade de fonte | `QApplication.setFont()` |
| Texto + cor | evitar cor como único canal de informação |

---

## Internacionalização e Localização

Qt fornece infraestrutura completa para traduzir strings e adaptar formatos de data, número e direção de texto.

**Fluxo de trabalho:**

1. Marcar strings traduzíveis com `self.tr()` em subclasses de `QObject`
2. Extrair com `lupdate` → arquivo `.ts`
3. Traduzir no Qt Linguist
4. Compilar com `lrelease` → arquivo `.qm`
5. Carregar em runtime com `QTranslator`

```python
from PySide6.QtCore import QTranslator, QLocale
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication([])

translator = QTranslator()
locale = QLocale.system().name()          # ex: "pt_BR"
translator.load(f"app_{locale}.qm")
app.installTranslator(translator)

# Em classes QObject — strings traduzíveis
class MainWindow(QMainWindow):
    def setup_ui(self):
        label = QLabel(self.tr("Bem-vindo"))          # marcada para extração
        btn   = QPushButton(self.tr("Abrir Arquivo"))
```

**Adaptação de locale:**

```python
from PySide6.QtCore import QLocale

locale = QLocale(QLocale.Portuguese, QLocale.Brazil)

# Formatar número e data respeitando convenções locais
print(locale.toString(1234567.89, 'f', 2))    # "1.234.567,89"
print(locale.toString(QDate.currentDate(), QLocale.ShortFormat))
```

**Checklist:**
- Todo label, tooltip, mensagem de erro e item de menu deve passar por `tr()`
- Layouts flexíveis — texto traduzido pode ser 30-50 % mais longo que o original
- Suporte a RTL (árabe, hebraico): `QApplication.setLayoutDirection(Qt.RightToLeft)`
- Testar com pseudo-localização antes de obter traduções reais

| Etapa | Ferramenta |
|---|---|
| Marcar strings | `self.tr("texto")` |
| Extrair strings | `lupdate` (CLI Qt) |
| Traduzir | Qt Linguist |
| Compilar | `lrelease` → `.qm` |
| Carregar em runtime | `QTranslator` + `installTranslator()` |
| Formatos de locale | `QLocale` |

---

## Qt Quick / QML — Referência Básica

Qt Quick é o framework declarativo do Qt para UIs modernas. Arquivos `.qml` descrevem a interface em linguagem própria; propriedades, bindings e animações são expressas de forma reativa.

### Estrutura básica

```qml
import QtQuick 6.2
import QtQuick.Window 6.2

Window {
    width: 800; height: 600; visible: true
    Rectangle {
        color: "#80000000"    // ARGB hex: Alpha=0x80, R=0, G=0, B=0
        radius: 15
        anchors.centerIn: parent
    }
}
```

**Regra**: use `#AARRGGBB` para cores com transparência em QML (Alpha primeiro); em QSS use `rgba(R,G,B,A)` com A em 0–255.

### Âncoras

| Propriedade | Descrição |
|---|---|
| `anchors.fill: parent` | Preenche o item pai |
| `anchors.centerIn: parent` | Centraliza no pai |
| `anchors.top` / `anchors.bottom` | Ancora borda superior/inferior |
| `anchors.horizontalCenter` | Centraliza horizontalmente |
| `anchors.left` / `anchors.right` | Ancora laterais |

### Integração C++↔QML

```cpp
// Registrar classe C++ para uso em QML
qmlRegisterType<MyLabel>("MyLabelLib", 1, 0, "MyLabel");

// Q_INVOKABLE torna o método chamável do QML
class MyLabel : public QObject {
    Q_OBJECT
public:
    Q_INVOKABLE void SetMyObject(QObject* obj);
};
```

```qml
import MyLabelLib 1.0
MyLabel { id: mylabel }
Label {
    id: helloLabel
    Component.onCompleted: { mylabel.SetMyObject(helloLabel); }
}
```

```cpp
// Modificar propriedade QML via C++
myObject->setProperty("visible", QVariant(true));
myObject->setProperty("text",    QVariant("Bye!"));
// Chamar função QML via C++
QMetaObject::invokeMethod(myObject, "myQMLFunction");
```

**Regra**: declare `Q_OBJECT` na classe e `Q_INVOKABLE` em cada método que precisa ser chamável do QML.

### Integração Python↔QML

**Carregar QML em Python:**
```python
from PySide6.QtQml import QQmlApplicationEngine

engine = QQmlApplicationEngine()
engine.load("main.qml")
if not engine.rootObjects():
    sys.exit(-1)
```

**Expor objeto Python ao QML via `setContextProperty`:**
```python
from PySide6.QtCore import QObject, Signal, Slot, Property

class MyLabel(QObject):
    textChanged = Signal(str)

    def __init__(self):
        super().__init__()
        self._text = ""

    @Slot(QObject)
    def set_my_object(self, obj):
        self._obj = obj

    @Property(str, notify=textChanged)
    def text(self):
        return self._text

engine.rootContext().setContextProperty("myLabel", MyLabel())
```

**Regra**: use `Signal`/`Slot`/`Property` do `PySide6.QtCore` (não decoradores genéricos do Python) para que o objeto seja visível ao motor QML.

**Registrar tipo Python como componente QML:**
```python
from PySide6.QtQml import qmlRegisterType

qmlRegisterType(MyClass, "MyLib", 1, 0, "MyClass")   # antes de engine.load()
```
```qml
import MyLib 1.0
MyClass { id: myobj }
```

**Manipular objeto QML pelo Python (findChild + setProperty):**
```python
root = engine.rootObjects()[0]
message_text = root.findChild(QObject, "messageText")
message_text.setProperty("text", "Controlled by Python!")
message_text.setProperty("color", "green")
```

### Animações QML

```qml
// State + ColorAnimation: muda cor com transição suave ao clicar
Rectangle {
    id: bg; color: "blue"; state: "RELEASED"
    states: [
        State { name: "PRESSED";  PropertyChanges { target: bg; color: "blue" } },
        State { name: "RELEASED"; PropertyChanges { target: bg; color: "red"  } }
    ]
    transitions: [
        Transition { from: "PRESSED";  to: "RELEASED"; ColorAnimation { duration: 200 } },
        Transition { from: "RELEASED"; to: "PRESSED";  ColorAnimation { duration: 200 } }
    ]
    MouseArea {
        anchors.fill: parent
        onPressed:  bg.state = "PRESSED"
        onReleased: bg.state = "RELEASED"
    }
}

// SequentialAnimation de cores em loop
SequentialAnimation on color {
    ColorAnimation { to: "yellow"; duration: 1000 }
    ColorAnimation { to: "red";    duration: 1000 }
    ColorAnimation { to: "blue";   duration: 1000 }
    loops: Animation.Infinite
}

// NumberAnimation: opacidade piscando + rotação simultânea
Text {
    text: "Hello"; color: "white"; font.pointSize: 15
    anchors.centerIn: parent
    SequentialAnimation on opacity {
        NumberAnimation { to: 0.0; duration: 200 }
        NumberAnimation { to: 1.0; duration: 200 }
        loops: Animation.Infinite
    }
    NumberAnimation on rotation {
        from: 0; to: 360; duration: 2000; loops: Animation.Infinite
    }
}
```

**Tipos de animação QML:** `AnchorAnimation`, `ColorAnimation`, `NumberAnimation`, `ParentAnimation`, `PathAnimation`, `PropertyAnimation`, `RotationAnimation`, `Vector3dAnimation`, `SpringAnimation`.

### Behavior on — animação automática de propriedade

```qml
// Qualquer mudança em "y" usa SpringAnimation automaticamente
Button {
    Behavior on y { SpringAnimation { spring: 2; damping: 0.2 } }
    onClicked: { button1.y += 135 }
}

// RotationAnimation com pause/resume
Image {
    RotationAnimation on rotation {
        id: rotAnim
        loops: Animation.Infinite
        from: 0; to: -360; duration: 1000
    }
    MouseArea { onPressed: { rotAnim.paused ? rotAnim.resume() : rotAnim.pause() } }
}

// SequentialAnimation em loop moverido no eixo X
SequentialAnimation on x {
    loops: Animation.Infinite
    PropertyAnimation { to: 150; duration: 1500 }
    PropertyAnimation { to: 50;  duration: 500 }
}
```

### Animators QML — render thread

```qml
// Animators rodam na render thread (melhor performance para escala/rotação contínua)
// O valor da propriedade QML só é atualizado ao fim da animação
ParallelAnimation {
    ScaleAnimator {
        target: myBox; from: 5; to: 1; duration: 2000
        easing.type: Easing.InOutElastic
        easing.amplitude: 2.0
        easing.period: 1.5
    }
    RotationAnimator { target: myBox; from: 0; to: 360; duration: 1000 }
    running: true
}
```

**Regra**: prefira Animators (`ScaleAnimator`, `RotationAnimator`, `OpacityAnimator`) para animações contínuas de render — rodam na render thread sem bloquear a UI thread.

### AnimatedSprite QML — sprite sheet

```qml
AnimatedSprite {
    id: sprite
    source: "qrc:///horse.png"
    frameCount: 11
    frameWidth: 128; frameHeight: 128
    frameRate: 25
    loops: Animation.Infinite
    running: true
}
MouseArea {
    anchors.fill: parent
    onClicked: { sprite.paused ? sprite.resume() : sprite.pause() }
}
// Animar posição do sprite
NumberAnimation {
    target: sprite; property: "x"
    from: -128; to: 512; duration: 3000
    loops: Animation.Infinite; running: true
}
```

### Canvas 2D QML

```qml
Canvas {
    id: myCanvas
    width: 640; height: 480

    onPaint: {
        var ctx = getContext("2d")
        ctx.fillStyle = "white"
        ctx.fillRect(0, 0, width, height)

        ctx.lineWidth = 2; ctx.strokeStyle = "black"
        ctx.beginPath(); ctx.moveTo(50, 50); ctx.lineTo(100, 100)
        ctx.closePath(); ctx.stroke()

        ctx.strokeStyle = "red"; ctx.fillStyle = "salmon"
        ctx.beginPath()
        ctx.moveTo(50, 150); ctx.lineTo(150, 150); ctx.lineTo(50, 250)
        ctx.closePath(); ctx.fill(); ctx.stroke()

        ctx.beginPath(); ctx.arc(220, 200, 60, 0, Math.PI, true)
        ctx.closePath(); ctx.fill(); ctx.stroke()

        ctx.drawImage("tux.png", 280, 10, 150, 174)
    }

    onImageLoaded: requestPaint()
}
```

| Primitiva | Descrição |
|---|---|
| `fillRect(x,y,w,h)` | Retângulo preenchido direto |
| `beginPath()` / `closePath()` | Inicia / fecha path |
| `moveTo()` / `lineTo()` | Segmento |
| `arc(cx,cy,r,start,end,acw)` | Arco/círculo |
| `stroke()` / `fill()` | Contorno / preenchimento |
| `drawImage(src,x,y,w,h)` | Imagem (pré-carregada) |

---

## Appendix A — Troubleshooting e FAQ

Problemas são inevitáveis, independentemente de quão bem estruturado está o código. Esta seção cobre os erros mais comuns em aplicações Qt/PySide6 e suas soluções práticas.

---

### 1. GUI congela durante tarefas longas

**Causa:** a operação está sendo executada na thread principal. O Qt usa a main thread para redesenhar a UI e processar eventos — bloqueá-la trava a interface.

**Solução:** mover a tarefa para uma thread separada com `QThread`, `QThreadPool` + `QRunnable`, ou `concurrent.futures` + `QFutureWatcher`.

```python
class Worker(QRunnable):
    def run(self):
        # operação longa aqui
        ...

pool = QThreadPool.globalInstance()
pool.start(Worker())
```

---

### 2. "Could not load the Qt platform plugin 'xcb'" no Linux

**Causa:** bibliotecas de sistema ausentes ou caminhos incorretos ao rodar uma aplicação empacotada.

**Solução:**
- Instalar: `libxcb-xinerama0 libxcb1 libxkbcommon-x11-0 libgl1`
- Ao empacotar com PyInstaller/cx_Freeze, garantir que o diretório `platforms/` (contendo `libqxcb.so`) esteja incluído e que `QT_QPA_PLATFORM_PLUGIN_PATH` aponte para ele em runtime.

---

### 3. Aplicação crasha silenciosamente no Windows

**Causa:** DLL ausente ou incompatível — geralmente mismatch de arquitetura (32 vs 64-bit).

**Solução:**
- Usar **Dependency Walker** ou **Dependencies** para inspecionar o EXE e identificar DLLs faltantes.
- Verificar que `PATH` inclui todos os runtime DLLs e bibliotecas Qt.
- Confirmar que Python interpreter e Qt libraries são ambos 64-bit.

---

### 4. Ícones ou stylesheets não carregam após empacotamento

**Causa:** caminhos relativos quebram quando a app é compilada em um único EXE.

**Solução:** embutir assets com `QResource` (`.qrc`) ou resolver caminhos dinamicamente:

```python
import sys, os

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

icon_path = os.path.join(base_path, "icons", "app.ico")
```

---

### 5. Aparência feia — como obter o visual nativo?

**Causa:** Qt usa seu próprio rendering por padrão.

**Solução:** aplicar o estilo do sistema via `QStyleFactory`:

```python
app.setStyle("Fusion")   # ou "Windows", "macOS", etc.
```

Use style sheets globais para controle total de temas. Evite over-customização sem um design system definido.

---

### 6. Eventos ou signals não são disparados

**Checklist:**
- O objeto emitindo o signal ainda existe (não foi coletado pelo GC).
- A assinatura do signal bate exatamente com o slot.
- O slot está decorado corretamente com `@Slot()` (opcional mas ajuda).
- Nenhum `time.sleep()` está bloqueando o event loop — substituir por `QTimer.singleShot()` ou métodos async.

---

### 7. Nada acontece ao clicar um botão

**Causa:** problema de binding ou ciclo de vida do objeto.

**Checklist:**
```python
# Verificar a conexão
self.button.clicked.connect(self.on_button_clicked)

# on_button_clicked deve estar definido e self deve ser o objeto correto
def on_button_clicked(self):
    ...
```

Ao criar botões dinamicamente, usar `functools.partial` em vez de lambdas para evitar captura de variável tardia:

```python
from functools import partial

for i in range(5):
    btn = QPushButton(f"Botão {i}")
    btn.clicked.connect(partial(self.handle_click, i))
```

---

## OpenGL em PySide6

### Setup

```bash
pip install PySide6 PyOpenGL PyOpenGL_accelerate
```

```python
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtOpenGL import (QOpenGLShaderProgram, QOpenGLShader,
                               QOpenGLBuffer, QOpenGLVertexArrayObject,
                               QOpenGLTexture)
import OpenGL.GL as gl
import numpy as np
```

**Regra**: usar `QOpenGLWidget` (embutido em janela QWidget) em Python — mais simples que `QOpenGLWindow`.

### Estrutura base — RenderWidget

```python
class RenderWidget(QOpenGLWidget):
    def initializeGL(self):
        gl.glClearColor(0.39, 0.58, 0.93, 1.0)

        vert_src = """
        #version 330 core
        layout(location = 0) in vec2 posAttr;
        void main() { gl_Position = vec4(posAttr, 0.0, 1.0); }
        """
        frag_src = """
        #version 330 core
        out vec4 col;
        void main() { col = vec4(1.0, 0.0, 0.0, 1.0); }
        """
        self.shader = QOpenGLShaderProgram()
        self.shader.addShaderFromSourceCode(QOpenGLShader.ShaderTypeBit.Vertex, vert_src)
        self.shader.addShaderFromSourceCode(QOpenGLShader.ShaderTypeBit.Fragment, frag_src)
        self.shader.link()

        vertices = np.array([-1.0,-1.0, 1.0,-1.0, 0.0,1.0], dtype=np.float32)

        self.vao = QOpenGLVertexArrayObject()
        self.vao.create()
        self.vao.bind()

        self.vbo = QOpenGLBuffer(QOpenGLBuffer.Type.VertexBuffer)
        self.vbo.create()
        self.vbo.setUsagePattern(QOpenGLBuffer.UsagePattern.StaticDraw)
        self.vbo.bind()
        self.vbo.allocate(vertices.tobytes(), vertices.nbytes)
        self.vao.release()

    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        self.vao.bind()
        self.shader.bind()
        self.shader.enableAttributeArray(0)
        self.shader.setAttributeBuffer(0, gl.GL_FLOAT, 0, 2)
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, 3)
        self.shader.release()
        self.vao.release()

    def resizeGL(self, w, h):
        gl.glViewport(0, 0, w, h)
```

**Diferença C++→Python**: usar `numpy` para arrays de vértices e `.tobytes()` para alocar no VBO.

### Animação com deltaTime

```python
from PySide6.QtCore import QElapsedTimer

class RenderWidget(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.elapsed = QElapsedTimer()
        self.elapsed.start()
        self.old_time = 0
        self.rotation = 0.0

    def paintGL(self):
        current = self.elapsed.elapsed()
        delta = (current - self.old_time) / 1000.0
        self.old_time = current
        self.rotation += delta * 50   # 50 graus/segundo
        # ... MVP + glDrawArrays ...
        self.update()   # força novo frame — cria game loop
```

### MVP Matrix

```python
from PySide6.QtGui import QMatrix4x4, QVector3D

model = QMatrix4x4()
view  = QMatrix4x4()
proj  = QMatrix4x4()

model.translate(0, 1, 0)
model.rotate(self.rotation, 0, 1, 0)
view.lookAt(QVector3D(4,4,0), QVector3D(0,0,0), QVector3D(0,1,0))
proj.perspective(60.0, self.width()/self.height(), 0.1, 100.0)

mvp = proj * view * model
self.shader.setUniformValue("matrix", mvp)
```

### Texturização

```python
texture = QOpenGLTexture(QImage("brick.jpg").mirrored())
texture.setMinificationFilter(QOpenGLTexture.Filter.Nearest)
texture.setMagnificationFilter(QOpenGLTexture.Filter.Linear)

# No paintGL:
texture.bind()
gl.glDrawArrays(gl.GL_TRIANGLES, 0, 36)
```

**Regra**: sempre `.mirrored()` ao criar textura de `QImage` — OpenGL tem eixo Y invertido.

### Movimento WASD

```python
class RenderWidget(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.move_x = 0.0
        self.move_z = 0.0
        self.movement = QVector3D(0, 0, 0)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_W: self.move_z = -10
        if event.key() == Qt.Key.Key_S: self.move_z =  10
        if event.key() == Qt.Key.Key_A: self.move_x = -10
        if event.key() == Qt.Key.Key_D: self.move_x =  10

    def keyReleaseEvent(self, event):
        if event.key() in (Qt.Key.Key_W, Qt.Key.Key_S): self.move_z = 0
        if event.key() in (Qt.Key.Key_A, Qt.Key.Key_D): self.move_x = 0

    def paintGL(self):
        # calcular delta_time ...
        self.movement.setX(self.movement.x() + self.move_x * delta_time)
        self.movement.setZ(self.movement.z() + self.move_z * delta_time)
        model = QMatrix4x4()
        model.translate(self.movement.x(), 1, self.movement.z())
        # ... MVP e glDrawArrays ...
        self.update()
```

**Regra**: setar velocidade no press/release; multiplicar `* delta_time` no loop de render — independente do key-repeat do OS.

### Qt Quick 3D em QML

```qml
import QtQuick
import QtQuick3D

View3D {
    anchors.fill: parent
    environment: SceneEnvironment {
        clearColor: "skyblue"
        backgroundMode: SceneEnvironment.Color
    }

    PerspectiveCamera { position: Qt.vector3d(0, 200, 300); eulerRotation.x: -30 }
    DirectionalLight  { eulerRotation.x: -10; eulerRotation.y: -20 }

    Model {
        position: Qt.vector3d(0, 0, 0)
        source: "#Cube"
        eulerRotation.y: -30
        materials: PrincipledMaterial {
            baseColorMap: Texture { source: "qrc:/brick.jpg" }
        }
        NumberAnimation on eulerRotation.y {
            duration: 3000; from: 0; to: 360
            easing.type: Easing.Linear; loops: Animation.Infinite
        }
    }
}
```

Primitivas nativas: `"#Cube"`, `"#Sphere"`, `"#Cone"`, `"#Cylinder"`. Use `PrincipledMaterial` para PBR; `DefaultMaterial` para renderização simples.

**Regra**: usar `addShaderFromSourceFile()` para shaders longos — mantém o GLSL separado e editável sem recompilar Python.

```python
self.shader.addShaderFromSourceFile(QOpenGLShader.ShaderTypeBit.Vertex,   "vertex.glsl")
self.shader.addShaderFromSourceFile(QOpenGLShader.ShaderTypeBit.Fragment, "fragment.glsl")
```

---

## Performance em PySide6

### Medir tempo de execução
```python
from PySide6.QtCore import QElapsedTimer
import time

# Qt
timer = QElapsedTimer()
timer.start()
# ... código ...
print(f"Elapsed: {timer.elapsed()} ms")

# Python puro (preferível fora do contexto Qt)
start = time.perf_counter()
# ... código ...
print(f"Elapsed: {(time.perf_counter() - start)*1000:.2f} ms")
```

### Profiling Python
```bash
# cProfile — profiler nativo
python -m cProfile -s cumulative my_app.py

# py-spy — profiler sem overhead (sampling), sem modificar o código
pip install py-spy
py-spy top -- python my_app.py
```

### Otimizações de widgets
- Criar widgets uma vez e reutilizá-los; nunca instanciar `QWidget()` em loops
- `setUpdatesEnabled(False)` / `setUpdatesEnabled(True)` ao popular tabelas grandes:
  ```python
  self.table.setUpdatesEnabled(False)
  for row_data in big_dataset:
      # popular tabela...
      pass
  self.table.setUpdatesEnabled(True)
  ```
- `QWidget` usa Raster Engine (software) — usar QML para aceleração de hardware
- Desabilitar `setMouseTracking(True)` em widgets que não precisam do evento
- Manter style sheets simples — QSS grande aumenta tempo de parse

### Otimização de imagens em QML
```qml
Image {
    source: "tux.png"
    sourceSize.width:  50   // redimensionar antes de carregar na GPU
    sourceSize.height: 60
    smooth:       false
    antialiasing: false
    asynchronous: true      // carrega em thread de baixa prioridade
}
```

### numpy vs loops Python
| Operação | Abordagem |
|---|---|
| Processamento numérico intenso | `numpy` — 10–100× mais rápido que loop Python |
| Arrays de vértices OpenGL | `numpy.array(..., dtype=np.float32).tobytes()` |
| Operações vetoriais | `numpy` nativo em vez de `QVector`-equivalente em list |

---

## Appendix B — Essential Qt 6 and Python Resources

After working through the examples in this book, you'll likely want to explore more advanced or domain-specific features of Qt or expand your Python skills to support larger applications. This appendix provides a curated set of practical, real-world resources and tools you'll find indispensable as a Qt/PySide developer.

### Qt 6 Official Documentation

The single most reliable and complete reference is the official Qt documentation. It offers class-level breakdowns, method signatures, and usage examples for every module—from QMainWindow to QGraphicsScene. While it's written primarily for C++, it maps closely to PyQt6 and PySide6, and understanding the C++ method signatures helps interpret Qt's object model more deeply.

Familiarize yourself with:

- Widget documentation (QWidget, QPushButton, etc.)
- Layout classes (QVBoxLayout, QGridLayout)
- Signal-slot mechanism
- The QtCore, QtGui, and QtWidgets module overview

### PySide6 and PyQt6 API Docs

PySide6 is the official Qt binding maintained by the Qt Company. PyQt6 is a third-party alternative but widely used. Both share near-identical APIs, though licensing and tooling may vary.

Keep bookmarked references for:

- PySide6 documentation site
- PyQt6 module index
- Class inheritance diagrams

These resources provide Python-native syntax, clear examples, and up-to-date notes on differences from earlier Qt versions (like Qt 5).

### Qt Designer and UIC Tools

For rapid interface prototyping, Qt Designer is invaluable. It lets you visually build GUIs, which you can later convert into Python code using tools like `pyuic6`. You'll get precise control over layout spacing, tab order, nested containers, and widget properties—without writing a line of code.

Knowing how to combine Qt Designer for layout and custom Python logic for behavior is a major productivity boost.

### Python Ecosystem Tools

Modern GUI applications often integrate with APIs, databases, file systems, or async I/O systems. Enhance your app with:

- `requests` or `httpx` for network APIs
- `asyncio` for non-blocking tasks
- `sqlite3` or `SQLAlchemy` for embedded databases
- `pytest` or `unittest` for GUI and logic testing

Many advanced apps eventually include modular architecture, plugin support, or a message bus—Python's ecosystem is robust enough to support all of this.

### Packaging and Distribution Resources

For packaging, the most mature tools are:

- **PyInstaller** — for one-click EXE creation
- **cx_Freeze** — alternative for Python 3.10+ support
- **virtualenv** or **venv** — for clean dependency separation
- **pipreqs**, **pip-tools**, or **poetry** — for managing requirements

Understanding how these tools interact with PyQt or PySide resources—such as `.ui` files, `.qrc` resource bundles, DLLs and plugin paths—is essential for professional distribution.

### Open Source Qt Apps and Code Examples

Studying open-source apps built with PyQt or PySide is a great way to understand patterns that scale. Some community-maintained projects mimic the complexity of real-world software, including media players, notepad replacements, calendar systems, and image editors.

Clone, read, run—and learn.

Troubleshooting and learning go hand-in-hand. The deeper you go into GUI application development, the more you'll appreciate how layers like event loops, threads, signals, layouts, and user expectations all intertwine. The resources here will guide you far beyond the scope of this book as you build professional, responsive, and reliable desktop apps.

If you ever feel stuck—go back to basics, isolate the problem, test iteratively, and trust your tools. Qt and Python are mature, battle-tested platforms. When you master their subtleties, you gain the power to craft truly excellent software.

---

## Qt6 C++ Cookbook — Referência

> Conteúdo extraído de *Qt 6 C++ GUI Programming Cookbook – Third Edition* (Packt).  
> Complementa a referência PySide6 com receitas práticas de Qt6 C++ e QML nativo.

| # | Seção C++ |
|---|---|
| C5 | [OpenGL em Qt6 C++](#opengl-em-qt6-c) |
| C6 | [Migração Qt 5 → Qt 6 (C++)](#migração-qt-5--qt-6-c) |
| C7 | [Networking em C++](#networking-em-c) |
| C8 | [Threading em C++](#threading-em-c) |
| C9 | [Touch Screen / Mobile Qt Quick (C++)](#touch-screen--mobile-qt-quick-c) |
| C10 | [JSON Parsing em C++](#json-parsing-em-c) |
| C11 | [Conversion Library (C++)](#conversion-library-c) |
| C12 | [Database SQL (C++)](#database-sql-c) |
| C13 | [Qt WebEngine (C++)](#qt-webengine-c) |
| C14 | [Performance Optimization (C++)](#performance-optimization-c) |
| CP | [Padrões Recorrentes Qt C++](#padrões-recorrentes-qt-c) |

---

## OpenGL em Qt6 C++

### Setup OpenGL em Qt
```ini
# .pro
QT += core gui opengl
LIBS += -lopengl32 -lglu32
```

### Janela OpenGL (QOpenGLWindow)
```cpp
// main.cpp
#include <QtOpenGL>
QOpenGLWindow window;
window.setTitle("Hello OpenGL");
window.resize(640, 480);
window.show();
```

**Regra**: Preferir `QOpenGLWindow` a `QOpenGLWidget` para melhor desempenho (sem dependência do módulo widgets).

### Classe RenderWindow — estrutura base
```cpp
// renderwindow.h
#include <QtOpenGL>
#include <QOpenGLFunctions>
#include <QOpenGLBuffer>
#include <QOpenGLVertexArrayObject>
#include <QOpenGLShaderProgram>

class RenderWindow : public QOpenGLWindow {
protected:
    void initializeGL();
    void paintGL();
    void paintEvent(QPaintEvent* event);
    void resizeEvent(QResizeEvent* event);
private:
    QOpenGLContext*       openGLContext;
    QOpenGLFunctions*     openGLFunctions;
    QOpenGLShaderProgram* shaderProgram;
    QOpenGLVertexArrayObject* vao;
    QOpenGLBuffer*        vbo_vertices;
};
```

### Inicialização com shaders GLSL e VBO
```cpp
void RenderWindow::initializeGL() {
    setSurfaceType(QWindow::OpenGLSurface);
    QSurfaceFormat fmt;
    fmt.setProfile(QSurfaceFormat::CoreProfile);
    fmt.setVersion(3, 2);
    setFormat(fmt);
    openGLContext = new QOpenGLContext();
    openGLContext->setFormat(fmt);
    openGLContext->create();
    openGLContext->makeCurrent(this);
    openGLFunctions = openGLContext->functions();

    static const char* vert =
        "#version 330 core\n"
        "layout(location = 0) in vec2 posAttr;\n"
        "void main() { gl_Position = vec4(posAttr, 0.0, 1.0); }";
    static const char* frag =
        "#version 330 core\n"
        "out vec4 col;\n"
        "void main() { col = vec4(1.0, 0.0, 0.0, 1.0); }";

    shaderProgram = new QOpenGLShaderProgram(this);
    shaderProgram->addShaderFromSourceCode(QOpenGLShader::Vertex, vert);
    shaderProgram->addShaderFromSourceCode(QOpenGLShader::Fragment, frag);
    shaderProgram->link();

    GLfloat vertices[] = { -1.0f,-1.0f, 1.0f,-1.0f, 0.0f,1.0f };
    vao = new QOpenGLVertexArrayObject();
    vao->create(); vao->bind();
    vbo_vertices = new QOpenGLBuffer(QOpenGLBuffer::VertexBuffer);
    vbo_vertices->create();
    vbo_vertices->setUsagePattern(QOpenGLBuffer::StaticDraw);
    vbo_vertices->bind();
    vbo_vertices->allocate(vertices, sizeof(vertices) * sizeof(GLfloat));
    vao->release();
}
```

### Renderização e resize
```cpp
void RenderWindow::paintEvent(QPaintEvent* event) {
    glViewport(0, 0, width(), height());
    glClearColor(0.39f, 0.58f, 0.93f, 1.f);
    glClear(GL_COLOR_BUFFER_BIT);
    vao->bind();
    shaderProgram->bind();
    shaderProgram->bindAttributeLocation("posAttr", 0);
    shaderProgram->enableAttributeArray(0);
    shaderProgram->setAttributeBuffer(0, GL_FLOAT, 0, 2);
    glDrawArrays(GL_TRIANGLES, 0, 3);
    shaderProgram->release();
    vao->release();
}

void RenderWindow::resizeEvent(QResizeEvent* event) {
    glViewport(0, 0, width(), height());
    update();
}
```

### Renderização 3D — MVP matrix
```cpp
glEnable(GL_DEPTH_TEST);
// format.setDepthBufferSize(16); no formato
// glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); no clear

QMatrix4x4 model, view, projection, mvp;
model.translate(0, 1, 0);
model.rotate(45, 0, 1, 0);
view.lookAt(QVector3D(4, 4, 0), QVector3D(0, 0, 0), QVector3D(0, 1, 0));
projection.perspective(60.0f, (float)width()/(float)height(), 0.1f, 100.0f);
mvp = projection * view * model;
shaderProgram->setUniformValue("matrix", mvp);
```

### Shader GLSL para 3D
```glsl
// vertex shader
#version 330 core
layout(location = 0) in vec3 posAttr;
uniform mat4 matrix;
out vec3 fragPos;
void main() { fragPos = posAttr; gl_Position = matrix * vec4(posAttr, 1.0); }

// fragment shader
#version 330 core
in vec3 fragPos;
out vec4 col;
void main() { col = vec4(fragPos, 1.0); }
```

### 2D com cores por vértice (multi-VBO)
```cpp
static const char *vertexShaderSource =
    "#version 330 core\n"
    "layout(location = 0) in vec2 posAttr;\n"
    "layout(location = 1) in vec3 colAttr;\n"
    "out vec3 fragCol;\n"
    "void main() { fragCol = colAttr; gl_Position = vec4(posAttr, 1.0, 1.0); }";
static const char *fragmentShaderSource =
    "#version 330 core\n"
    "in vec3 fragCol; out vec4 col;\n"
    "void main() { col = vec4(fragCol, 1.0); }";

GLfloat vertices[]  = { -0.3f,-0.5f, 0.8f,-0.4f,  0.2f, 0.6f };
GLfloat vertices2[] = {  0.5f, 0.3f, 0.4f,-0.8f, -0.6f,-0.2f };
GLfloat colors[]    = { 1.0f,0.0f,0.0f, 0.0f,1.0f,0.0f, 0.0f,0.0f,1.0f };

vbo_colors = new QOpenGLBuffer(QOpenGLBuffer::VertexBuffer);
vbo_colors->create();
vbo_colors->setUsagePattern(QOpenGLBuffer::StaticDraw);
vbo_colors->bind();
vbo_colors->allocate(colors, sizeof(colors) * sizeof(GLfloat));

// paintEvent — bind vbo_vertices + vbo_colors, depois repetir para vbo_vertices2
vbo_vertices->bind();
shaderProgram->bindAttributeLocation("posAttr", 0);
shaderProgram->enableAttributeArray(0);
shaderProgram->setAttributeBuffer(0, GL_FLOAT, 0, 2);
vbo_colors->bind();
shaderProgram->bindAttributeLocation("colAttr", 1);
shaderProgram->enableAttributeArray(1);
shaderProgram->setAttributeBuffer(1, GL_FLOAT, 0, 3);
glDrawArrays(GL_TRIANGLES, 0, 3);
vbo_vertices2->bind();
shaderProgram->setAttributeBuffer(0, GL_FLOAT, 0, 2);
glDrawArrays(GL_TRIANGLES, 0, 3);
```

> ⚠ Sempre chamar `bind()` no VBO correto antes de `setAttributeBuffer()` — OpenGL usa o VBO atualmente ativo como fonte do atributo.

### Animação contínua com QElapsedTimer e deltaTime
```cpp
// .h
QElapsedTimer* time;
int currentTime = 0, oldTime = 0;
float deltaTime = 0, rotation = 0;

// Construtor
time = new QElapsedTimer(); time->start();

// paintEvent
currentTime = time->elapsed();
deltaTime = (float)(currentTime - oldTime) / 1000.0f;
oldTime = currentTime;
rotation += deltaTime * 50;   // 50 graus/segundo
model.rotate(rotation, 0, 1, 0);
this->update();  // cria game loop
```

**Regra**: multiplicar toda velocidade por `deltaTime` (segundos do frame) para manter velocidade consistente independente do frame rate. Chamar `update()` ao final de `paintEvent()`.

### Texturização em OpenGL
```cpp
// initializeGL
glEnable(GL_DEPTH_TEST);
glEnable(GL_TEXTURE_2D);

texture = new QOpenGLTexture(
    QImage(qApp->applicationDirPath() + "/brick.jpg").mirrored());
texture->setMinificationFilter(QOpenGLTexture::Nearest);
texture->setMagnificationFilter(QOpenGLTexture::Linear);

GLfloat uvs[] = {
    0.0f,0.0f, 1.0f,0.0f, 0.0f,1.0f,  1.0f,0.0f, 1.0f,1.0f, 0.0f,1.0f,
    // ... (36 vértices para cubo)
};
vbo_uvs = new QOpenGLBuffer(QOpenGLBuffer::VertexBuffer);
vbo_uvs->create();
vbo_uvs->setUsagePattern(QOpenGLBuffer::StaticDraw);
vbo_uvs->bind();
vbo_uvs->allocate(uvs, sizeof(uvs) * sizeof(GLfloat));
```

```glsl
// vertex shader (acrescenta UV)
layout(location = 1) in vec2 uvAttr;
out vec2 fragUV;
void main() { fragUV = uvAttr; gl_Position = matrix * vec4(posAttr, 1.0); }

// fragment shader (sampler2D)
in vec2 fragUV;
uniform sampler2D tex;
out vec4 col;
void main() { col = texture(tex, fragUV); }
```

```cpp
// paintEvent — bind UV VBO e textura antes de glDrawArrays
vbo_uvs->bind();
shaderProgram->bindAttributeLocation("uvAttr", 1);
shaderProgram->enableAttributeArray(1);
shaderProgram->setAttributeBuffer(1, GL_FLOAT, 0, 2);
texture->bind();
glDrawArrays(GL_TRIANGLES, 0, 36);
```

> ⚠ Sempre chamar `.mirrored()` ao criar `QOpenGLTexture` a partir de `QImage` — OpenGL usa origem Y no canto inferior esquerdo.

**Regra**: `Nearest` para minificação; `Linear` para magnificação.

### Iluminação básica — Point Light em OpenGL

Em OpenGL 3+, `glEnable(GL_LIGHT0)` foi removido. Toda iluminação é calculada manualmente no fragment shader.

```cpp
// initializeGL — normais por face do cubo
GLfloat normals[] = {
    0.0f,-1.0f,0.0f, 0.0f,-1.0f,0.0f, 0.0f,-1.0f,0.0f,
    // ... (36 vértices)
};
vbo_normals = new QOpenGLBuffer(QOpenGLBuffer::VertexBuffer);
vbo_normals->create();
vbo_normals->setUsagePattern(QOpenGLBuffer::StaticDraw);
vbo_normals->bind();
vbo_normals->allocate(normals, sizeof(normals) * sizeof(GLfloat));

shaderProgram->addShaderFromSourceFile(
    QOpenGLShader::Vertex,   qApp->applicationDirPath() + "/vertex.txt");
shaderProgram->addShaderFromSourceFile(
    QOpenGLShader::Fragment, qApp->applicationDirPath() + "/fragment.txt");
shaderProgram->link();

// paintEvent
vbo_normals->bind();
shaderProgram->bindAttributeLocation("normalAttr", 2);
shaderProgram->enableAttributeArray(2);
shaderProgram->setAttributeBuffer(2, GL_FLOAT, 0, 3);
```

```glsl
// vertex.txt
layout(location = 2) in vec3 normalAttr;
out vec3 fragNormal;
void main() {
    fragPos = posAttr; fragUV = uvAttr; fragNormal = normalAttr;
    gl_Position = matrix * vec4(posAttr, 1.0);
}

// fragment.txt — point light com componente difusa
in vec3 fragNormal;
vec4 calcPointLight() {
    vec4  texCol   = texture(tex, fragUV);
    vec3  lightPos = vec3(1.0, 2.0, 1.5);
    vec3  lightDir = normalize(lightPos - fragPos);
    float diff     = clamp(dot(fragNormal, lightDir), 0.0, 1.0);
    return diff * texCol * vec4(1.0, 1.0, 1.0, 1.0);
}
void main() { col = calcPointLight(); }
```

**Regra**: usar `addShaderFromSourceFile()` para shaders longos — mantém GLSL separado e editável sem recompilar.

### Controle de movimento via teclado (WASD)
```cpp
float moveX = 0, moveZ = 0;
QVector3D movement = QVector3D(0, 0, 0);

void RenderWindow::keyPressEvent(QKeyEvent *event) {
    if (event->key() == Qt::Key_W) moveZ = -10;
    if (event->key() == Qt::Key_S) moveZ =  10;
    if (event->key() == Qt::Key_A) moveX = -10;
    if (event->key() == Qt::Key_D) moveX =  10;
}
void RenderWindow::keyReleaseEvent(QKeyEvent *event) {
    if (event->key() == Qt::Key_W || event->key() == Qt::Key_S) moveZ = 0;
    if (event->key() == Qt::Key_A || event->key() == Qt::Key_D) moveX = 0;
}

// paintEvent
movement.setX(movement.x() + moveX * deltaTime);
movement.setZ(movement.z() + moveZ * deltaTime);
model.translate(movement.x(), 1, movement.z());
```

**Regra**: setar `moveX`/`moveZ` no press/release, aplicar `* deltaTime` no loop de renderização.

### Qt Quick 3D em QML
Qt 6 substitui Qt Canvas 3D por Qt Quick 3D — renderização nativa sem three.js.

```qml
import QtQuick
import QtQuick3D

View3D {
    anchors.fill: parent
    environment: SceneEnvironment {
        clearColor: "skyblue"
        backgroundMode: SceneEnvironment.Color
    }

    PerspectiveCamera { position: Qt.vector3d(0, 200, 300); eulerRotation.x: -30 }
    DirectionalLight { eulerRotation.x: -10; eulerRotation.y: -20 }

    Model {
        position: Qt.vector3d(0, 0, 0)
        source: "#Cube"
        eulerRotation.y: -30
        materials: PrincipledMaterial {
            baseColorMap: Texture { source: "qrc:/brick.jpg" }
        }
        NumberAnimation on eulerRotation.y {
            duration: 3000; from: 0; to: 360
            easing.type: Easing.Linear; loops: Animation.Infinite
        }
    }
}
```

Primitivas nativas: `"#Cube"`, `"#Sphere"`, `"#Cone"`, `"#Cylinder"`. Usar `PrincipledMaterial` para PBR; `DefaultMaterial` para renderização simples.

---

## Migração Qt 5 → Qt 6 (C++)

### Mudanças em C++
- `QLinkedList` removido → usar `QList` ou `std::list`
- `QRegExp` substituído por `QRegularExpression`
- `QString::sprintf()` deprecado → usar `QString::arg()`
- Sintaxe de signals/slots MACRO removida → usar ponteiros de função
- `QTextCodec`, `QTextEncoder`, `QTextDecoder` — deprecados em Qt 6

```cpp
// QStringView — substring sem cópia (substituiu QStringRef)
QStringView x = QString("Good afternoon");
QStringView y = x.mid(5, 5);   // → "after"
QStringView z = x.mid(5);      // → "afternoon"
```

### QRegularExpression — substituição de QRegExp no Qt 6
```cpp
#include <QRegularExpression>

QRegularExpression rx("\\d+");
QString text = "Jacky has 3 carrots and 15 apples.";
QRegularExpressionMatchIterator it = rx.globalMatch(text);
QStringList numbers;
while (it.hasNext()) {
    QRegularExpressionMatch match = it.next();
    numbers << match.captured(0);  // grupo 0 = match completo
}
// → ["3", "15"]

QRegularExpressionMatch m = rx.match("abc123");
if (m.hasMatch())
    qDebug() << m.captured(0);  // "123"

QString result = text;
result.replace(rx, "N");  // "Jacky has N carrots and N apples."
```

**Diferenças-chave vs QRegExp:** `globalMatch()` retorna iterator; grupos via `captured(n)`; thread-safe.

### Módulo Core5Compat — compatibilidade temporária
```ini
# .pro
QT += core5compat
```
```cmake
find_package(Qt6 REQUIRED COMPONENTS Core5Compat)
target_link_libraries(myapp PRIVATE Qt6::Core5Compat)
```

> ⚠ `core5compat` não estará disponível no Qt 7 — use como medida temporária enquanto refatora.

```ini
# .pro — desativa APIs depreciadas antes do Qt 5.15
DEFINES += QT_DISABLE_DEPRECATED_UP_TO=0x050F00
```

### Mudanças em QML
- Caminhos relativos: `./images` → `/images` (sem ponto)
- `property variant` → `property var`
- Número de versão no import agora é opcional

**Carregar QML em main.cpp — Qt 5 vs Qt 6:**
```cpp
// Qt 5
const QUrl url(QStringLiteral("qrc:/main.qml"));

// Qt 6 — u"..."_qs: literal UTF-16 (C++17)
const QUrl url(u"qrc:/myproject/main.qml"_qs);
```

> ⚠ Qt Quick Controls 1 foi removido em Qt 6 — usar Qt Quick Controls (v2).

### Ferramenta Clazy — análise estática Qt
```bash
clazy-standalone --checks=level1 myfile.cpp
```

**Qt Creator IDE:** _Edit → Preferences → Analyzer → Diagnostic configuration → Copy → aba Clazy Checks_.  
Checks recomendados para migração Qt 5→6: `qt6-deprecated-api-fixes`, `qt6-header-fixes`, `qt6-qhash-signature`, `qt6-fwd-fixes`, `missing-qobject-macro`.

Executar via _Analyze → Clang-Tidy and Clazy_ — lista linhas depreciadas com sugestões de substituição.

---

## Networking em C++

### TCP Server
```cpp
// .pro: QT += network

class server : public QObject {
    Q_OBJECT
    QTcpServer* chatServer;
    QVector<QTcpSocket*>* allClients;
public slots:
    void newClientConnection();
    void socketDisconnected();
    void socketReadReady();
};

void server::startServer() {
    allClients = new QVector<QTcpSocket*>;
    chatServer = new QTcpServer();
    chatServer->setMaxPendingConnections(10);
    connect(chatServer, &QTcpServer::newConnection, this, &server::newClientConnection);
    chatServer->listen(QHostAddress::Any, 8001);
}

void server::newClientConnection() {
    QTcpSocket* client = chatServer->nextPendingConnection();
    connect(client, &QTcpSocket::readyRead,    this, &server::socketReadReady);
    connect(client, &QTcpSocket::disconnected, this, &server::socketDisconnected);
    allClients->push_back(client);
}

void server::socketReadReady() {
    QTcpSocket* client = qobject_cast<QTcpSocket*>(sender());
    QString data = QString(client->readAll());
    for (auto* c : *allClients)
        if (c->isOpen() && c->isWritable())
            c->write(data.toUtf8());
}
```

### TCP Client
```cpp
QTcpSocket* socket = new QTcpSocket();
connect(socket, &QTcpSocket::readyRead, this, &MainWindow::socketReadReady);
socket->connectToHost("127.0.0.1", 8001);
socket->write("Hello Server");
```

### Estado do socket (QAbstractSocket::SocketState)
| Estado | Significado |
|--------|-------------|
| `UnconnectedState` | Não conectado |
| `HostLookupState` | Resolvendo DNS |
| `ConnectingState` | Estabelecendo conexão |
| `ConnectedState` | Conectado |
| `ClosingState` | Encerrando (dados pendentes) |

### FTP em Qt 6

Qt 6 removeu FTP do `QNetworkAccessManager`. Implementar manualmente com `FtpControlChannel` e `FtpDataChannel` baseadas em `QTcpSocket`/`QTcpServer`.

Comandos FTP básicos: `USER/PASS` (auth), `PORT` (canal de dados), `MLSD` (listar), `STOR` (upload), `RETR` (download).

**FtpDataChannel** (canal de dados — porta dinâmica):
```cpp
class FtpDataChannel : public QObject {
    Q_OBJECT
public:
    void listen(const QHostAddress &address = QHostAddress::Any);
    void sendData(const QByteArray &data);
    void close();
    QString portspec() const;   // formato FTP: h1,h2,h3,h4,p1,p2
    QTcpServer m_server;
    std::unique_ptr<QTcpSocket> m_socket;
signals:
    void dataReceived(const QByteArray &data);
};

FtpDataChannel::FtpDataChannel(QObject *parent) : QObject(parent) {
    connect(&m_server, &QTcpServer::newConnection, this, [this]() {
        m_socket.reset(m_server.nextPendingConnection());
        connect(m_socket.get(), &QTcpSocket::readyRead, this, [this]() {
            emit dataReceived(m_socket->readAll());
        });
        connect(m_socket.get(), &QTcpSocket::bytesWritten, this, [this](qint64) {
            close();
        });
    });
}

void FtpDataChannel::listen(const QHostAddress &address) { m_server.listen(address); }
void FtpDataChannel::sendData(const QByteArray &data) {
    if (m_socket) m_socket->write(QByteArray(data).replace("\n", "\r\n"));
}
void FtpDataChannel::close() { if (m_socket) m_socket->disconnectFromHost(); }

// portspec(): converte IP+porta para formato FTP PORT (h1,h2,h3,h4,p1,p2)
QString FtpDataChannel::portspec() const {
    quint32 ipv4 = m_server.serverAddress().toIPv4Address();
    quint16 port = m_server.serverPort();
    return QString::number((ipv4 & 0xff000000) >> 24) + ',' +
           QString::number((ipv4 & 0x00ff0000) >> 16) + ',' +
           QString::number((ipv4 & 0x0000ff00) >>  8) + ',' +
           QString::number( ipv4 & 0x000000ff       ) + ',' +
           QString::number((port & 0xff00) >>  8) + ',' +
           QString::number( port & 0x00ff          );
}
```

**FtpControlChannel** (canal de controle — porta 21):
```cpp
class FtpControlChannel : public QObject {
    Q_OBJECT
public:
    void connectToServer(const QString &server);
    void command(const QByteArray &command, const QByteArray &params);
signals:
    void opened(const QHostAddress &localAddress, int localPort);
    void closed();
    void reply(int code, const QByteArray &parameters);
private:
    void onReadyRead();
    QTcpSocket m_socket;
    QByteArray m_buffer;
};

void FtpControlChannel::connectToServer(const QString &server) { m_socket.connectToHost(server, 21); }
void FtpControlChannel::command(const QByteArray &command, const QByteArray &params) {
    QByteArray data = command;
    if (!params.isEmpty()) data += " " + params;
    m_socket.write(data + "\r\n");
}
// onReadyRead: FTP responde "code message\r\n"
void FtpControlChannel::onReadyRead() {
    m_buffer.append(m_socket.readAll());
    int rn = -1;
    while ((rn = m_buffer.indexOf("\r\n")) != -1) {
        QByteArray received = m_buffer.mid(0, rn);
        m_buffer = m_buffer.mid(rn + 2);
        int space = received.indexOf(' ');
        if (space != -1) {
            int code = received.mid(0, space).toInt();
            if (code > 0) emit reply(code, received.mid(space + 1));
        }
    }
}
```

**Slots serverReply e dataReceived:**
```cpp
void MainWindow::serverConnected(const QHostAddress& addr, int port) {
    dataChannel->listen(addr);
    controlChannel->command("USER", username.toUtf8());
    controlChannel->command("PASS", password.toUtf8());
    // getFileList:
    controlChannel->command("PORT", dataChannel->portspec().toUtf8());
    controlChannel->command("MLSD", "");
}

void MainWindow::serverReply(int code, const QString &params) {
    if (code == 150 && uploadFileName != "") {
        QFile* file = new QFile(ui->uploadFileInput->text());
        if (file->open(QIODevice::ReadOnly)) {
            QThread::msleep(1000);
            dataChannel->sendData(file->readAll() + "\n\r");
        }
    }
    if (code == 226 && uploadFileName != "") {
        uploadFileName = "";
        QMessageBox::information(this, "Upload", "File uploaded successfully.");
    }
}

void MainWindow::dataReceived(const QByteArray &data) {
    if (data.startsWith("type=file")) {
        ui->fileList->clear();
        for (const QString& entry : QString(data).split("\r\n")) {
            if (entry.isEmpty()) continue;
            QStringList parts = entry.split(";");
            if (parts.size() > 4)
                ui->fileList->addItem(parts.at(4).simplified());
        }
    } else {
        QFile file(ui->downloadPath->text() + "/" + downloadFileName);
        file.open(QIODevice::WriteOnly);
        file.write(data);
        file.close();
        QMessageBox::information(this, "Download", "File downloaded successfully.");
    }
}
```

### HTTP GET com QNetworkAccessManager
```cpp
// .pro: QT += network
// Declarar em mainwindow.h
private:
    QNetworkAccessManager* manager;
private slots:
    void onReplyFinished(QNetworkReply* reply);

// Construtor
manager = new QNetworkAccessManager(this);
connect(manager, &QNetworkAccessManager::finished,
        this,    &MainWindow::onReplyFinished);

// Disparar GET
void MainWindow::doRequest() {
    QNetworkRequest req(QUrl("https://api.example.com/data"));
    req.setHeader(QNetworkRequest::ContentTypeHeader, "application/json");
    manager->get(req);
}

// Slot
void MainWindow::onReplyFinished(QNetworkReply* reply) {
    if (reply->error() == QNetworkReply::NoError) {
        QByteArray data = reply->readAll();
    } else {
        qDebug() << "Error:" << reply->errorString();
    }
    reply->deleteLater();  // SEMPRE deletar após processar
}
```

**POST com body JSON:**
```cpp
QNetworkRequest req(QUrl("https://api.example.com/submit"));
req.setHeader(QNetworkRequest::ContentTypeHeader, "application/json");
QByteArray body = QJsonDocument(QJsonObject{{"key", "value"}}).toJson();
manager->post(req, body);
```

**Regra**: sempre chamar `reply->deleteLater()` — sem isso a reply vaza memória. Um único `QNetworkAccessManager` gerencia múltiplas requisições simultâneas.

| Método | Função |
|--------|--------|
| `manager->get(req)` | HTTP GET |
| `manager->post(req, body)` | HTTP POST |
| `manager->put(req, body)` | HTTP PUT |
| `manager->deleteResource(req)` | HTTP DELETE |

| TCP | UDP |
|-----|-----|
| Confiável, ordenado | Não confiável, sem ordenação garantida |
| Chat, web, banco de dados | Video games, streaming, DNS |

---

## Threading em C++

### QtConcurrent (alto nível)
```cpp
#include <QFuture>
#include <QtConcurrent/QtConcurrent>

QFuture<void> f1 = QtConcurrent::run(myFunction, arg1, arg2);
f1.waitForFinished();
```

### QFutureWatcher (monitorar via signals)
```cpp
QFutureWatcher<void> watcher;
connect(&watcher, &QFutureWatcher<void>::finished, this, &MainWindow::onDone);
watcher.setFuture(QtConcurrent::run(myFunction));
```

### QThread + QObject (baixo nível)
```cpp
// Worker herda QObject (não QThread)
class MyWorker : public QObject {
    Q_OBJECT
signals:
    void doneProcess();
public slots:
    void process() { /* trabalho pesado */ emit doneProcess(); }
};

QThread* thread = new QThread;
MyWorker* worker = new MyWorker;
worker->moveToThread(thread);
connect(thread, &QThread::started,       worker,  &MyWorker::process);
connect(worker, &MyWorker::doneProcess,  thread,  &QThread::quit);
connect(worker, &MyWorker::doneProcess,  worker,  &MyWorker::deleteLater);
connect(thread, &QThread::finished,      thread,  &QThread::deleteLater);
thread->start();
```

### QMutex — proteção de dados compartilhados
```cpp
QMutex mutex;
mutex.lock();
sharedData++;
mutex.unlock();
// RAII:
QMutexLocker locker(&mutex);
```

### QRunnable e QThreadPool
```cpp
class MyTask : public QRunnable {
    void run() override { /* trabalho */ }
};
QThreadPool* pool = QThreadPool::globalInstance();
pool->start(new MyTask());
pool->activeThreadCount();
pool->setMaxThreadCount(4);
pool->setExpiryTimeout(60000);  // ms; padrão 30s

// Evitar deleção automática ao fim do run():
MyTask* t = new MyTask;
t->setAutoDelete(false);
pool->start(t);
```

### QReadWriteLock — leitura simultânea, escrita exclusiva
```cpp
QReadWriteLock rwLock;
QReadLocker  readLocker(&rwLock);   // múltiplos threads simultâneos OK
QWriteLocker writeLocker(&rwLock);  // exclusivo
```

**Regra**: use `QReadWriteLock` quando o dado é lido muito mais frequentemente do que escrito — permite paralelismo na leitura sem sacrificar consistência de escrita. `QMutex` bloqueia tanto leitura quanto escrita.

---

## Touch Screen / Mobile Qt Quick (C++)

### Setup para mobile
- Usar `Qt Quick Application` como template
- Arquivo principal: `main.qml` carregado por `QQmlApplicationEngine`
- Componentes UI: `.ui.qml` com Qt Design Studio

### MultiPointTouchArea — gestos multi-toque

**1 dedo → mover; 2 dedos → pinch-to-zoom:**
```qml
property int prevDistX: 0;  property int prevDistY: 0
property int curDistX:  0;  property int curDistY:  0
property int tuxWidth: tux.width; property int tuxHeight: tux.height

MultiPointTouchArea {
    id: touchArea
    anchors.fill: parent
    touchPoints: [
        TouchPoint { id: point1 },
        TouchPoint { id: point2 }
    ]

    onPressed: {
        if (touchArea.touchPoints[1].pressed) {
            prevDistX = Math.abs(touchArea.touchPoints[0].x - touchArea.touchPoints[1].x)
            prevDistY = Math.abs(touchArea.touchPoints[0].y - touchArea.touchPoints[1].y)
            tuxWidth  = tux.width
            tuxHeight = tux.height
        }
    }

    onUpdated: {
        if (!touchArea.touchPoints[1].pressed) {
            tux.x += touchArea.touchPoints[0].x - touchArea.touchPoints[0].previousX
            tux.y += touchArea.touchPoints[0].y - touchArea.touchPoints[0].previousY
        } else {
            curDistX = Math.abs(touchArea.touchPoints[0].x - touchArea.touchPoints[1].x)
            curDistY = Math.abs(touchArea.touchPoints[0].y - touchArea.touchPoints[1].y)
            tux.width  = tuxWidth  + (prevDistX - curDistX) * -1
            tux.height = tuxHeight + (prevDistY - curDistY) * -1
        }
    }
}
```

**Regra**: salvar `tuxWidth`/`tuxHeight` no `onPressed` (não no `onUpdated`) — o tamanho base deve ser fixo durante todo o gesto de pinch. Usar `Math.abs()` para evitar inversão de sinal quando os dedos cruzam.

| Evento | Quando ocorre |
|--------|--------------|
| `onPressed` | Dedo toca a tela |
| `onUpdated` | Dedo se move sem soltar |
| `onReleased` | Dedo sai da tela |

### Separação .ui.qml vs .qml (Qt Design Studio)
- **Screen01.ui.qml** — apenas definição visual (sem lógica). Widgets exportados como aliases acessíveis em App.qml
- **App.qml** — lógica e bindings; importa Screen01 como componente

```qml
// App.qml
Screen01 {
    anchors.fill: parent
    loginButton.onClicked: { messageDialog.visible = true }
}
```

### Propriedades Customizadas em QML
```qml
Item {
    id: myItem
    property int    count:   0
    property real   scale:   1.0
    property string label:   "default"
    property var    data:    null      // var aceita qualquer tipo
    property url    imgPath: ":/img.png"
    property color  accent:  "blue"
}
```

**property alias** — expõe propriedade de filho como se fosse do componente pai:
```qml
// Screen01.ui.qml
Rectangle {
    id: root
    property alias buttonText: btn.text
    property alias buttonColor: btn.color
    Button { id: btn; text: "Click me" }
}

// App.qml
Screen01 {
    buttonText:  "Submit"
    buttonColor: "green"
}
```

**Regra**: somente `property alias` re-exporta propriedades de filhos; `property int` cria cópia local, não binding.

**Tipos suportados:** `int`, `real`, `double`, `bool`, `string`, `url`, `color`, `var`, `date`, `point`, `size`, `rect`, `vector2d/3d/4d`.

### Model/View em QML — ListView com ListModel
```qml
ListView {
    id: listView1
    anchors.fill: parent
    orientation: ListView.Vertical
    boundsBehavior: Flickable.StopAtBounds

    model: ListModel {
        ListElement { title: "Home";     subtitle: "Dashboard"; icon: "images/home.png" }
        ListElement { title: "Map";      subtitle: "Navigation"; icon: "images/map.png" }
        ListElement { title: "Settings"; subtitle: "Preferences"; icon: "images/settings.png" }
    }

    delegate: Item {
        width: listView1.width; height: 55 * sizeMultiplier
        Row {
            Rectangle {
                width: listView1.width; height: 55 * sizeMultiplier
                MouseArea { anchors.fill: parent
                    onPressed:  parent.opacity = 0.5
                    onReleased: parent.opacity = 1.0
                }
                Image {
                    anchors.verticalCenter: parent.verticalCenter
                    x: 15 * sizeMultiplier; width: 30 * sizeMultiplier; height: 30 * sizeMultiplier
                    source: icon
                }
                Text { text: title;    font.pixelSize: 17 * sizeMultiplier; x: 55 * sizeMultiplier; y: 10 * sizeMultiplier }
                Text { text: subtitle; font.pixelSize:  9 * sizeMultiplier; x: 55 * sizeMultiplier; y: 30 * sizeMultiplier }
            }
        }
    }
}

// sizeMultiplier — scaling para mobile
Rectangle {
    property double sizeMultiplier: width / 480   // 480 = largura base de design
}
```

**Regra**: usar `font.pixelSize` (não `pointSize`) ao multiplicar por `sizeMultiplier` — `pointSize` já aplica DPI do sistema, causando duplo scaling.

### QML Image — modos de preenchimento
```qml
Image {
    source: "qrc:/tux.png"
    fillMode: Image.Stretch            // estica sem preservar proporção (default)
    fillMode: Image.PreserveAspectFit  // cabe dentro, mantendo proporção
    fillMode: Image.PreserveAspectCrop // preenche tudo, cortando se necessário
    fillMode: Image.Tile               // repete em tile
    smooth:       true
    antialiasing: false
    asynchronous: true     // carrega em thread de baixa prioridade
    sourceSize.width:  50  // redimensiona antes de carregar na GPU
    sourceSize.height: 60
}
```

| fillMode | Comportamento |
|----------|---------------|
| `Stretch` | Estica para `width × height` |
| `PreserveAspectFit` | Cabe dentro, pode sobrar espaço |
| `PreserveAspectCrop` | Preenche tudo cortando as bordas |
| `Tile` | Repete em ladrilho |
| `Pad` | Centraliza sem redimensionar |

### Integrar C++ com QML

**setContextProperty (acesso global ao objeto):**
```cpp
QQmlApplicationEngine engine;
MyClass myObj;
engine.rootContext()->setContextProperty("myObject", &myObj);
engine.load(QUrl("qrc:/main.qml"));
```
```qml
Button { onClicked: myObject.doSomething() }
```

**qmlRegisterType + findChild (manipular de main.cpp):**
```cpp
qmlRegisterType<MyClass>("MyClassLib", 1, 0, "MyClass");
QQmlApplicationEngine engine;
engine.load(QUrl(QStringLiteral("qrc:/content/App.qml")));

QObject* root = engine.rootObjects().value(0);
QObject* messageText = root->findChild<QObject*>("messageText");
messageText->setProperty("text", QVariant("C++ is now in control!"));
messageText->setProperty("color", QVariant("green"));
```
```qml
import MyClassLib
Window {
    MyClass { id: myclass }
    Screen01 {
        anchors.fill: parent
        Component.onCompleted: myclass.setMyObject(messageText)
    }
}
```

**Q_INVOKABLE e Q_PROPERTY:**
```cpp
class MyClass : public QObject {
    Q_OBJECT
public:
    Q_INVOKABLE void setMyObject(QObject* obj);
    Q_PROPERTY(QString text MEMBER m_text NOTIFY textChanged)
signals:
    void textChanged();
private:
    QString m_text;
};
```

**Regra**: `Q_INVOKABLE` é obrigatório para funções C++ chamadas do QML. Somente classes que herdam `QObject` podem ser integradas ao QML.

---

## JSON Parsing em C++

### Ler JSON de arquivo
```cpp
#include <QJsonDocument>
#include <QJsonObject>
#include <QJsonArray>

QFile file("data.json");
file.open(QIODevice::ReadOnly);
QJsonDocument doc = QJsonDocument::fromJson(file.readAll());
QJsonObject root = doc.object();
QString name = root["name"].toString();
int age = root["age"].toInt();
QJsonArray arr = root["items"].toArray();
for (const auto& item : arr)
    qDebug() << item.toObject()["key"].toString();
```

### JSON com root Array (início com `[`)
```cpp
QJsonDocument doc = QJsonDocument::fromJson(file.readAll());
if (doc.isArray()) {
    QJsonArray array = doc.array();
    for (int i = 0; i < array.size(); ++i) {
        QJsonObject obj = doc[i].toObject();
        QStringList keys = obj.keys();
        for (int j = 0; j < keys.size(); ++j)
            qDebug() << keys.at(j) << obj.value(keys.at(j));
    }
}
// doc.isObject() — root é {}
// doc.isArray()  — root é []
// doc.isEmpty()  — documento vazio ou inválido
```

### Escrever JSON para arquivo
```cpp
QJsonObject obj;
obj["name"] = "Alice";
obj["age"] = 30;
QJsonDocument doc(obj);
QFile out("output.json");
out.open(QIODevice::WriteOnly);
out.write(doc.toJson());
```

### Escrever JSON com array em arquivo
```cpp
QJsonObject contact1;
contact1["name"] = "John Doe"; contact1["age"] = 32; contact1["category"] = "Friend";
QJsonObject contact2;
contact2["name"] = "Jane Smith"; contact2["age"] = 24; contact2["category"] = "Family";

QJsonArray array;
array.append(contact1);
array.append(contact2);

QJsonDocument json;
json.setArray(array);

QString filename = QFileDialog::getSaveFileName(this, "Save JSON", ".", "JSON (*.json)");
QFile file(filename);
if (file.open(QFile::WriteOnly | QFile::Text))
    file.write(json.toJson());
file.close();
```

**Regra**: para salvar, usar `QFile::WriteOnly` e `json.toJson()` em vez de `QJsonDocument::fromJson()`.

---

## Conversion Library (C++)

### QVariant — conversão entre tipos
```cpp
QVariant v = 42;
QString s = v.toString();
int n = v.toInt();
double d = v.toDouble();
bool b = v.toBool();

// QVariant pode mudar de tipo em runtime
QVariant myData = QVariant(10);
myData = myData.toFloat() / 2.135;
myData = QDateTime::currentDateTime();
myData = "Good bye!";
```

### Conversões numéricas e de string
```cpp
#include <QtMath>
QString numberB = "5";
int n = numberB.toInt();
QString result = QString::number(10.25f * 2);

float f = qFloor(10.3f);   // → 10
float c = qCeil(10.3f);    // → 11

QString up = "hello world!".toUpper();  // → "HELLO WORLD!"
QString lo = "HELLO WORLD!".toLower();  // → "hello world!"
```

### Conversão de data/hora
```cpp
#include <QDateTime>
QDateTime dt = QDateTime::fromString("2024-05-21 14:30:00", "yyyy-MM-dd hh:mm:ss");
QString s = QDateTime::currentDateTime().toString("dd/MM/yy hh:mm");
```

### Conversão de imagem (QImage)
```cpp
QImage img("photo.jpg");
img.save("photo.png");
img.save("photo.jpg", 0, -1);  // qualidade máxima
QPixmap px = QPixmap::fromImage(img);
```

### Conversão de vídeo via QProcess + FFmpeg
```cpp
#include <QProcess>
process = new QProcess(this);
connect(process, &QProcess::started,                 this, &MainWindow::processStarted);
connect(process, &QProcess::readyReadStandardOutput, this, &MainWindow::readOutput);
connect(process, &QProcess::finished,                this, &MainWindow::processDone);

QStringList args;
args << "-i" << inputFile << outputFile;
process->setProcessChannelMode(QProcess::MergedChannels);
process->start("C:/FFmpeg/bin/ffmpeg", args);

void MainWindow::readOutput() {
    outputText += process->readAllStandardOutput();
    ui->outputLog->setPlainText(outputText);
}
```

**Regra**: desabilitar botões em `processStarted()` e reabilitar em `processFinished()`.

#### Python — QProcess + FFmpeg
```python
from PySide6.QtCore import QProcess

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.process = QProcess(self)
        self.process.started.connect(self.process_started)
        self.process.readyReadStandardOutput.connect(self.read_output)
        self.process.finished.connect(self.process_done)

    def convert_video(self, input_file, output_file):
        self.process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)
        self.process.start("ffmpeg", ["-i", input_file, output_file])

    def read_output(self):
        data = self.process.readAllStandardOutput().data().decode()
        self.output_log.appendPlainText(data)

    def process_started(self):
        self.btn_convert.setEnabled(False)

    def process_done(self):
        self.btn_convert.setEnabled(True)
```

### Validação de entrada numérica (QDoubleValidator / QIntValidator)
```cpp
#include <QDoubleValidator>

QValidator* inputRange = new QDoubleValidator(this);
ui->amountField->setValidator(inputRange);

QDoubleValidator* ranged = new QDoubleValidator(0.0, 999999.99, 2, this);
ui->priceField->setValidator(ranged);

QIntValidator* intVal = new QIntValidator(0, 100, this);
ui->quantityField->setValidator(intVal);
```

**Regra**: `setValidator()` não bloqueia colar texto inválido — cheque `ui->field->text() != ""` antes de converter.

---

## Database SQL (C++)

### Setup SQLite
```ini
# .pro
QT += sql
```
```cpp
// Colocar qsqlite.dll e sqlite3.dll no diretório do executável
QSqlDatabase db = QSqlDatabase::addDatabase("QSQLITE");
db.setDatabaseName("database.db3");
if (db.open()) { /* ok */ }
// Fechar no destructor:
db.close();
```

**Regra**: chamar `db.close()` no destructor — especialmente importante no SQLite (file-based).

### Queries CRUD com binding
```cpp
QSqlQuery query;

// SELECT
if (query.exec("SELECT emp_name, emp_age FROM employee")) {
    while (query.next()) {
        QString name = query.value(0).toString();
        int age = query.value(1).toInt();
    }
}

// INSERT com binding (previne SQL injection)
query.prepare("INSERT INTO employee (emp_name, emp_age) VALUES (:name, :age)");
query.bindValue(":name", "Alice");
query.bindValue(":age", 30);
query.exec();

// UPDATE
query.prepare("UPDATE employee SET emp_name=:name WHERE emp_id=:id");
query.bindValue(":name", "Bob");
query.bindValue(":id", currentID);
query.exec();

// DELETE
query.prepare("DELETE FROM employee WHERE emp_id=:id");
query.bindValue(":id", currentID);
query.exec();
```

### Drivers suportados no Qt 6
| Driver | Descrição |
|--------|-----------|
| `QSQLITE` | SQLite (arquivo local) |
| `QODBC` | ODBC |
| `QPSQL` | PostgreSQL |
| `QMYSQL` | MySQL (requer recompilação manual) |

> ⚠ SQLite: `QSqlQuery::size()` sempre retorna -1. Use contador manual no `while (query.next())`.

```cpp
if (!query.exec("SELECT ..."))
    qDebug() << query.lastError().text();
int newId = query.lastInsertId().toInt();
if (db.isOpen()) { ... }
```

### Login screen com QStackedWidget + SQL
```cpp
ui->stackedWidget->setCurrentIndex(0);  // 0=login, 1=conteúdo

void MainWindow::on_loginButton_clicked() {
    QSqlQuery query;
    if (query.exec("SELECT user_employeeID FROM user WHERE "
                   "user_username = '" + username + "' AND "
                   "user_password = '" + password + "'")) {
        int count = 0;
        while (query.next()) {
            ui->stackedWidget->setCurrentIndex(1);
            count++;
        }
        if (count == 0)
            QMessageBox::warning(this, "Login failed", "Invalid credentials.");
    }
}
```

**Regra**: definir `echoMode = Password` no QLineEdit de senha.

### QTableWidget com dados SQL
```cpp
ui->tableWidget->setColumnHidden(0, true);  // ocultar coluna ID

while (query.next()) {
    ui->tableWidget->setRowCount(ui->tableWidget->rowCount() + 1);
    int row = ui->tableWidget->rowCount() - 1;

    auto* nameItem = new QTableWidgetItem(query.value(1).toString());
    auto* ageItem  = new QTableWidgetItem(query.value(2).toString());

    // Para valores não-texto use setData(role=0, valor)
    auto* genderItem = new QTableWidgetItem();
    genderItem->setData(0, query.value(3).toInt() == 0 ? "Male" : "Female");

    ui->tableWidget->setItem(row, 1, nameItem);
    ui->tableWidget->setItem(row, 2, ageItem);
    ui->tableWidget->setItem(row, 3, genderItem);
}

// Slot de edição — ler valor via data(0)
void MainWindow::on_tableWidget_itemChanged(QTableWidgetItem* item) {
    if (!hasInit) return;
    QString id   = ui->tableWidget->item(item->row(), 0)->data(0).toString();
    QString name = ui->tableWidget->item(item->row(), 1)->data(0).toString();
}
```

**Regra**: use `setData(Qt::DisplayRole, valor)` (role=0) para células não criadas com texto direto.

### SQL avançado — INNER JOIN, COUNT, LIKE, DISTINCT, strftime
```cpp
// INNER JOIN
query.exec("SELECT emp_name, dep_name, brh_name "
           "FROM (SELECT emp_name, emp_departmentID FROM employee) AS e "
           "INNER JOIN department ON department.dep_id = e.emp_departmentID "
           "INNER JOIN branch ON branch.brh_id = department.dep_branchID");

// COUNT
query.exec("SELECT COUNT(emp_gender) FROM employee WHERE emp_gender = 1");

// LIKE
query.exec("SELECT emp_name FROM employee WHERE emp_name LIKE '%Ja%'");

// DISTINCT
query.exec("SELECT DISTINCT emp_name FROM ...");

// strftime — filtrar por mês no SQLite
query.exec("SELECT emp_name FROM employee "
           "WHERE strftime('%m', emp_birthday) = '08'");

// Formatar QDate para exibição
query.value(1).toDate().toString("d-MMMM-yyyy");  // ex.: 6-August-2024
```

---

## Qt WebEngine (C++)

**Requisito**: compilador **MSVC 2019 64-bit** (não funciona com MinGW).

### WebView simples
```cpp
// .pro
QT += webenginewidgets

#include <QWebEngineView>
QWebEngineView* view = new QWebEngineView(this);
view->load(QUrl("https://www.google.com"));
setCentralWidget(view);
```

### Sinais de loading e progressBar
```cpp
connect(webview, &QWebEngineView::loadStarted,  this, [this]{ ui->progressBar->show(); });
connect(webview, &QWebEngineView::loadProgress, this, [this](int v){ ui->progressBar->setValue(v); });
connect(webview, &QWebEngineView::loadFinished, this, [this](bool){ ui->progressBar->hide(); });
```

### Navegação e carregamento de conteúdo
```cpp
QUrl url = QUrl(ui->address->text());
url.setScheme("http");
webview->page()->load(url);

webview->back();
webview->forward();

webview->setHtml(ui->source->toPlainText());

// Carregar arquivo binário (ex.: imagem)
QFile file("://tux.png");
file.open(QFile::ReadOnly);
webview->page()->setContent(file.readAll(), "image/png");
```

### Configurações do WebEngine (QWebEngineSettings)
```cpp
auto* s = webview->page()->settings();
s->setAttribute(QWebEngineSettings::JavascriptEnabled, false);
s->setAttribute(QWebEngineSettings::AutoLoadImages,    false);
QString family = s->fontFamily(QWebEngineSettings::SansSerifFont);
int minSize    = s->fontSize(QWebEngineSettings::MinimumFontSize);
s->setFontFamily(QWebEngineSettings::StandardFont, family);
```

### Embutir Google Maps via QRC + HTML
```cpp
QWebEngineView* webview = new QWebEngineView;
webview->page()->load(QUrl("qrc:/map.html"));
ui->verticalLayout->addWidget(webview);
```

```html
<!-- map.html -->
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_KEY&libraries=drawing"></script>
<script>
function initialize() {
    var map = new google.maps.Map(document.getElementById("map-canvas"),
        { center: new google.maps.LatLng(40.7, -74.2), zoom: 6 });
    var marker = new google.maps.Marker({ position: map.getCenter(), map: map });
    google.maps.event.addListener(marker, 'click', function(){ map.panTo(marker.getPosition()); });
    new google.maps.drawing.DrawingManager().setMap(map);
}
google.maps.event.addDomListener(window, 'load', initialize);
</script>
```

### C++ → JavaScript
```cpp
view->page()->runJavaScript("document.title", [](const QVariant& result){
    qDebug() << result.toString();
});
view->page()->runJavaScript("changeHtmlText('Hello from C++');");
```

### JavaScript → C++ (Qt WebChannel)
```cpp
// .pro: QT += webchannel
QWebChannel* channel = new QWebChannel(this);
channel->registerObject("backend", myObject);
view->page()->setWebChannel(channel);
```

```javascript
// No lado JavaScript — incluir qwebchannel.js
new QWebChannel(qt.webChannelTransport, function(channel) {
    channel.objects.backend.mySlot("hello");
});
```

**Regra**: funções C++ chamáveis pelo JavaScript **devem** ser declaradas com `Q_INVOKABLE`:
```cpp
Q_INVOKABLE void changeQtText(QString newText);
Q_INVOKABLE void showLoginInfo(QString user, QString pass);
```

### Remote debugging do WebEngine
```cpp
// Habilitar antes de setupUi() — acessível em http://127.0.0.1:1234 (Chrome/Chromium)
qputenv("QTWEBENGINE_REMOTE_DEBUGGING", "1234");
```
Desabilitar antes de produção: aumenta tempo de inicialização.

---

## Performance Optimization (C++)

### Medir tempo de execução
```cpp
#include <QElapsedTimer>
QElapsedTimer timer;
timer.start();
// ... código ...
qDebug() << "Elapsed:" << timer.elapsed() << "ms";
```

### Profiler do Qt Creator
- Menu **Analyze → QML Profiler** para aplicações QML
- Abas: **Timeline**, **Flame Graph**, **Quick3D Frame**, **Statistics**
- Timeline: Scene Graph, Memory Usage, Input Events, Compiling, Creating, Binding
- Flame Graph: percentual de tempo total / memória / alocações

### Benchmarks de containers C++ (100 milhões de elementos)
| Container | Tempo aproximado |
|-----------|-----------------|
| `int[]` (array C nativo) | ~650 ms |
| `std::vector<int>` | ~3 830 ms |
| `QVector<int>` | ~5 400 ms |

**Regra**: use array C nativo quando velocidade é crítica. `std::vector` supera `QVector` na maioria dos casos.

### Dicas de otimização de formulários C++
- Preferir `QGridLayout` para organização eficiente
- Criar widgets uma vez e reutilizá-los (evitar `new` em loops)
- `QWidget` usa Raster Engine (software, sem GPU) — considere QML para aceleração de hardware
- Desabilitar `mouseTracking` e `tabletTracking` em widgets que não os usam
- Manter style sheets simples — style sheets grandes aumentam tempo de parse

> ⚠ Evite: `setStyleSheet()` individual em cada widget dentro de loop (ex.: 600 botões — 8× mais lento que sem style sheet)

### Otimização de QML

```qml
// Ruim — busca rect por id em cada iteração
for (var i = 0; i < 1000; ++i) { console.log(rect.color.r); }

// Bom — cache o objeto em variável local
var rectColor = rect.color;
for (var i = 0; i < 1000; ++i) { console.log(rectColor.r); }
```

```qml
// Ruim — re-evalua binding a cada iteração
for (var i = 0; i < 1000; ++i) { myValue += 1; }

// Bom — acumula em temp e assign uma vez
var temp = myValue;
for (var i = 0; i < 1000; ++i) { temp += 1; }
myValue = temp;
```

**Regra**: prefira anchors a bindings para posicionamento — bindings são mais flexíveis mas mais lentos.

### Padrão FPS counter em QML
```qml
Window {
    id: window
    property int frame: 0
    onAfterRendering: { frame++ }
    Timer {
        interval: 1000; running: true; repeat: true
        onTriggered: { frame = 0 }
    }
    Text {
        Timer {
            repeat: true; interval: 1000; running: true
            onTriggered: { parent.text = "FPS: " + window.frame + " fps" }
        }
    }
}
```

### Repeater + animação complexa — teste de stress
```qml
Repeater {
    model: 10  // aumentar para 10000 para stress test
    delegate: Image {
        id: tux
        source: "tux.png"
        sourceSize.width: 50; sourceSize.height: 60
        width: 50; height: 60
        smooth: false
        antialiasing: false
        asynchronous: true

        property double startX: Math.random() * 600
        property double startY: Math.random() * 600
        property double endX:   Math.random() * 600
        property double endY:   Math.random() * 600
        property double speed:  Math.random() * 3000 + 1000

        RotationAnimation on rotation {
            loops: Animation.Infinite; from: 0; to: 360
            duration: Math.random() * 3000 + 1000
        }

        SequentialAnimation {
            running: true; loops: Animation.Infinite
            ParallelAnimation {
                NumberAnimation { target: tux; property: "x"; from: startX; to: endX; duration: speed; easing.type: Easing.InOutQuad }
                NumberAnimation { target: tux; property: "y"; from: startY; to: endY; duration: speed; easing.type: Easing.InOutQuad }
            }
            ParallelAnimation {
                NumberAnimation { target: tux; property: "x"; from: endX; to: startX; duration: speed; easing.type: Easing.InOutQuad }
                NumberAnimation { target: tux; property: "y"; from: endY; to: startY; duration: speed; easing.type: Easing.InOutQuad }
            }
        }
    }
}
```

**Benchmarks (10.000 imagens em movimento):**
| Configuração | FPS |
|---|---|
| `sourceSize` + `smooth:false` + `asynchronous:true` | ~39 fps |
| Sem `sourceSize` + `smooth:true` + `asynchronous:false` | ~32 fps |

**Propriedades de Image que afetam performance:**
- `sourceSize`: redimensiona antes de carregar na memória GPU — crítico para imagens grandes
- `smooth`: filtro de suavização ao escalar
- `antialiasing`: remove artefatos de borda
- `asynchronous`: carrega em thread de baixa prioridade

---

## Padrões Recorrentes PySide6

### Qt módulo → PySide6 import
| Módulo Qt (`.pro`) | PySide6 import |
|---|---|
| `QT += network` | `from PySide6.QtNetwork import ...` |
| `QT += sql` | `from PySide6.QtSql import ...` |
| `QT += webenginewidgets` | `from PySide6.QtWebEngineWidgets import ...` |
| `QT += opengl` | `from PySide6.QtOpenGL import ...` |
| `QT += statemachine` | `from PySide6.QtStateMachine import ...` |
| `QT += svg` | `from PySide6.QtSvg import ...` |
| `QT += webchannel` | `from PySide6.QtWebChannel import ...` |
| `QT += qml` | `from PySide6.QtQml import ...` |

### Property com getter/setter/notify (forma explícita)
```python
from PySide6.QtCore import QObject, Signal, Property

class MyModel(QObject):
    name_changed = Signal(str)

    def __init__(self):
        super().__init__()
        self._name = ""

    def get_name(self):
        return self._name

    def set_name(self, value: str):
        if self._name != value:
            self._name = value
            self.name_changed.emit(value)

    # forma explícita: Property(type, fget, fset, notify=signal)
    name = Property(str, get_name, set_name, notify=name_changed)
```

Alternativa com decorador (`@Property(str, notify=...)`): ver seção [Qt Quick / QML](#qt-quick--qml).

---

## Padrões Recorrentes Qt C++

### Estrutura padrão de projeto Qt Widgets
```
projeto/
├── CMakeLists.txt (ou projeto.pro)
├── main.cpp
├── mainwindow.h / mainwindow.cpp / mainwindow.ui
└── resources.qrc
```

### Padrão Worker Thread seguro
1. Criar classe worker derivada de `QObject` (não `QThread`)
2. `moveToThread(thread)` para transferir ownership
3. Conectar `QThread::started` → `worker::process()`
4. Conectar `worker::done` → `QThread::quit` + `deleteLater`

### Adicionar módulo ao projeto
```ini
# qmake
QT += network sql webenginewidgets opengl concurrent
```
```cmake
find_package(Qt6 REQUIRED COMPONENTS Network Sql WebEngineWidgets OpenGL Concurrent)
target_link_libraries(myapp PRIVATE Qt6::Network Qt6::Sql ...)
```

### Debug
```cpp
#include <QDebug>
qDebug() << "Valor:" << myVar;
qWarning() << "Aviso!";
qCritical() << "Erro crítico";
```

### Executar processo externo (QProcess)
```cpp
QProcess* p = new QProcess(this);
connect(p, &QProcess::readyReadStandardOutput, this, [p, this](){
    ui->log->append(p->readAllStandardOutput());
});
p->setProcessChannelMode(QProcess::MergedChannels);
p->start("ffmpeg", {"-i", inputFile, outputFile});
```

### Seleção de arquivo (QFileDialog)
```cpp
QString file = QFileDialog::getOpenFileName(this, "Open", "", "Images (*.png *.jpg)");
QString path = QFileDialog::getSaveFileName(this, "Save SVG", "", "SVG (*.svg)");
QString dir  = QFileDialog::getExistingDirectory(this, "Select Folder",
               qApp->applicationDirPath(), QFileDialog::ShowDirsOnly);
```

### Conversão de objeto Qt (qobject_cast)
```cpp
// Identificar sender() dentro de um slot genérico
QTcpSocket* client = qobject_cast<QTcpSocket*>(sender());
```

### QMessageBox — métodos estáticos
```cpp
#include <QMessageBox>
QMessageBox::information(this, "Title", "Message text.");
QMessageBox::warning(this, "Warning", "Something went wrong.");
QMessageBox::critical(this, "Error", "Critical failure.");

int ret = QMessageBox::question(this, "Confirm", "Delete this item?",
                                QMessageBox::Yes | QMessageBox::No);
if (ret == QMessageBox::Yes) { /* confirmar */ }
```

**Regra**: desabilitar botões em `processStarted()` e reabilitar em `processFinished()` para evitar duplo clique.

### QFileInfo — metadados de caminho de arquivo
```cpp
#include <QFileInfo>
QFileInfo info("/home/user/photo.jpg");
info.path();              // "/home/user"
info.fileName();          // "photo.jpg"
info.baseName();          // "photo"
info.suffix();            // "jpg"
info.completeSuffix();    // "jpg" (todas extensões, ex.: "tar.gz")
info.exists();            // true/false

// Trocar extensão mantendo pasta e nome
QString newPath = info.path() + "/" + info.completeBaseName() + ".png";
```

### QComboBox — popular e ler itens
```cpp
ui->comboBox->addItem("Option A");
QStringList items = { "EUR", "USD", "CAD", "GBP" };
ui->comboBox->insertItems(0, items);

int  idx = ui->comboBox->currentIndex();
QString t = ui->comboBox->currentText();

// Definir seleção por índice (ex.: valor vindo de SQL)
ui->comboBox->setCurrentIndex(query.value(2).toInt());
```

### QTabWidget — reação à troca de página
```cpp
void MainWindow::on_tabWidget_currentChanged(int index) {
    for (auto* btn : { ui->btn0, ui->btn1, ui->btn2 })
        btn->setProperty("pagematches", false);
    if (index == 0)      ui->btn0->setProperty("pagematches", true);
    else if (index == 1) ui->btn1->setProperty("pagematches", true);
    else                 ui->btn2->setProperty("pagematches", true);
    for (auto* btn : { ui->btn0, ui->btn1, ui->btn2 })
        btn->style()->polish(btn);  // forçar re-aplicação do style sheet
}
```

**Regra**: chamar `style()->polish(widget)` após `setProperty()` — sem isso style sheets com seletor de propriedade dinâmica não são re-avaliados.

### QTimer — repetição e atraso
```cpp
QTimer* timer = new QTimer(this);
connect(timer, &QTimer::timeout, this, &MainWindow::onTimeout);
timer->start(1000);  // ms
timer->stop();

QTimer::singleShot(500, this, &MainWindow::onDelayed);
QTimer::singleShot(200, [this]{ ui->label->setText("Done"); });
```

### Auto-scroll de log widget (QScrollBar)
```cpp
#include <QScrollBar>
void MainWindow::appendLog(const QString& text) {
    ui->outputLog->append(text);
    ui->outputLog->verticalScrollBar()->setSliderPosition(
        ui->outputLog->verticalScrollBar()->maximum());
}
```

### QProgressBar — indicador de progresso
```cpp
ui->progressBar->setRange(0, 100);   // padrão
ui->progressBar->setRange(0, 0);     // modo indeterminado
ui->progressBar->setValue(50);
ui->progressBar->show(); ui->progressBar->hide();

// Com QFutureWatcher
QFutureWatcher<void> watcher;
connect(&watcher, &QFutureWatcher<void>::progressValueChanged,
        ui->progressBar, &QProgressBar::setValue);
watcher.setFuture(QtConcurrent::run(myHeavyTask));
```

### QLineEdit — configurações de entrada
```cpp
ui->passwordField->setEchoMode(QLineEdit::Password);
ui->resultField->setReadOnly(true);
ui->searchField->setPlaceholderText("Type to search...");
ui->lineEdit->selectAll();
QString text = ui->lineEdit->text().trimmed();
ui->lineEdit->clear();
ui->resultField->setCursor(Qt::ForbiddenCursor);
```

### QCheckBox / QRadioButton
```cpp
connect(ui->checkBox, &QCheckBox::toggled, this, [this](bool checked){
    ui->optionGroup->setEnabled(checked);
});

#include <QButtonGroup>
QButtonGroup* group = new QButtonGroup(this);
group->addButton(ui->radioA, 0);
group->addButton(ui->radioB, 1);
connect(group, &QButtonGroup::idClicked, this, [this](int id){
    qDebug() << "Selected:" << id;
});
int selectedId = group->checkedId();   // -1 se nenhum selecionado
```

### QListWidget — lista interativa
```cpp
#include <QListWidgetItem>
ui->fileList->addItem("arquivo.txt");
ui->fileList->addItems({ "Alpha", "Beta", "Gamma" });
ui->fileList->clear();

QListWidgetItem* current = ui->fileList->currentItem();
if (current) QString text = current->text();

// Slot de double-click
void MainWindow::on_fileList_itemDoubleClicked(QListWidgetItem* item) {
    QString selectedFile = item->text();
}

// Preencher a partir de MLSD (FTP)
void MainWindow::dataReceived(const QByteArray& data) {
    ui->fileList->clear();
    for (const QString& line : QString(data).split("\r\n")) {
        if (!line.isEmpty())
            ui->fileList->addItem(line.split(";").last().simplified());
    }
}
```

**Regra**: checar `current != nullptr` antes de `->text()`. Para listas grandes, preferir `QListView` + `QStringListModel`.

### Consumir API REST com JSON (ex.: Google Geocoding)
```cpp
addressRequest = new QNetworkAccessManager();
connect(addressRequest, &QNetworkAccessManager::finished,
        this, &MainWindow::getAddressFinished);

QNetworkRequest req;
req.setUrl(QUrl("https://maps.googleapis.com/maps/api/geocode/json?latlng="
                + lat + "," + lng + "&key=YOUR_KEY"));
addressRequest->get(req);

void MainWindow::getAddressFinished(QNetworkReply* reply) {
    QJsonDocument doc = QJsonDocument::fromJson(reply->readAll());
    QJsonArray results = doc.object()["results"].toArray();
    QString address = results.at(0).toObject()["formatted_address"].toString();
}
```
