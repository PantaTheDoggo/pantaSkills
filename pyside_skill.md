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

---

## Instalação

PySide6 é o binding oficial Python para o Qt6, mantido pela The Qt Company. Diferente do PyQt6 (licença GPL/comercial), o PySide6 usa a licença LGPL, o que permite uso em aplicações comerciais sem royalties. O pacote `PySide6` no PyPI instala automaticamente tudo que é necessário para começar.

```bash
pip install PySide6
python -c "import PySide6; print(PySide6.__version__)"
```

Instala automaticamente: `PySide6-Essentials` + `PySide6-Addons` + `shiboken6`.

Para ambientes de produção, fixe a versão no `requirements.txt`:
```
PySide6>=6.7,<7
```

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

    def wheelEvent(self, event):
        delta = event.angleDelta().y()
        print(f"Scroll: {delta}")
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

### Regras de Thread Safety

- **Nunca** acesse ou modifique widgets fora da thread principal.
- Use sinais para enviar resultados de volta para a UI.
- `QObject.moveToThread()` transfere a afinidade de thread do objeto.
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
        # desenhar ponteiros com save()/rotate()/drawConvexPolygon()/restore()
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
```

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

### Checklist de deploy
- [ ] `resources_rc.py` incluído e importado em `main.py`
- [ ] Caminhos de arquivo via `QStandardPaths` ou recursos embutidos — nunca hardcoded
- [ ] `app.setApplicationName` + `setOrganizationName` configurados (QSettings)
- [ ] `--windowed` / `--noconsole` para app GUI (sem janela de terminal)
- [ ] Testar o executável em máquina limpa (sem Python instalado)
- [ ] Assinar o executável (Windows: `signtool`; macOS: `codesign`) para evitar alertas de antivírus

---

## Migração PySide legado → PySide6

O Qt6 unificou enumerações em namespaces fortemente tipados (e.g., `Qt.AlignmentFlag.AlignCenter` em vez de `Qt.AlignCenter`) e removeu o sufixo `_()` dos métodos `exec`, `open` e similares. A ferramenta `pyside6-codemods` automatiza parte da migração, mas os usos de enums e a reorganização de módulos (ex.: `QAction` saiu de `QtWidgets` para `QtGui`) precisam ser revisados manualmente.

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
