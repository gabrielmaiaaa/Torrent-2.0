from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QWidget, QSizePolicy, QLineEdit,
    QScrollArea, QGridLayout, QSpacerItem
)
from PySide6.QtGui import QPixmap, QIcon, QFont
from PySide6.QtCore import Qt, Signal

class ClickableImageLabel(QLabel):
    clicked = Signal()

    def __init__(self, pixmap, width, height):
        super().__init__()
        self.setPixmap(pixmap.scaled(width, height))
        self.setFixedSize(width, height)
        self.setAlignment(Qt.AlignCenter)
        self.setScaledContents(True)
        self.setCursor(Qt.PointingHandCursor)

    def mousePressEvent(self, event):
        self.clicked.emit()

def initUI4(self,tipo):
   
    # Área da pesquisa
    content_pesquisa_layout = QVBoxLayout() 

    pesquisa_widget = QWidget()
    pesquisa_widget.setStyleSheet("background-color: #242121; border-bottom: 2px solid white;")
    pesquisa_widget.setFixedHeight(80)
    pesquisa_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    pesquisa_layout = QHBoxLayout(pesquisa_widget)
    pesquisa_layout.setAlignment(Qt.AlignCenter)

    label_seta = ClickableImageLabel(QPixmap("Imagens/voltar.png"),512,512)
    label_seta.setStyleSheet("border:none; padding: 0px;")
    label_seta.clicked.connect(self.tipo_clicked)
    label_seta.setStyleSheet("border-bottom: none; padding: 0px;")
    label_seta.setFixedSize(50,30)
    pesquisa_layout.addWidget(label_seta, alignment=Qt.AlignCenter)

    label_inicio = QLabel(tipo)
    label_inicio.setFont(QFont("Abril Fatface", 30))
    label_inicio.setStyleSheet("border: none;  padding: 0px;")
    pesquisa_layout.addWidget(label_inicio, alignment=Qt.AlignCenter)

    pesquisa_layout.addStretch()

    self.line_edit_busca = QLineEdit()
    self.line_edit_busca.setStyleSheet("color: white; padding: 5px;")
    self.line_edit_busca.textChanged.connect(self.filtrar_conteudo1)
    self.line_edit_busca.setPlaceholderText("Buscar")
    self.line_edit_busca.setFont(QFont("Lato", 11, QFont.Bold))
    self.line_edit_busca.setFixedWidth(200)
    pesquisa_layout.addWidget(self.line_edit_busca, alignment=Qt.AlignCenter)

    content_pesquisa_layout.addWidget(pesquisa_widget)

    # Conteúdo principal
    # Layout principal
    content_pri_layout = QVBoxLayout()

    # Criar a área de rolagem
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)

    content_widget = QWidget()
    content_layout = QVBoxLayout(content_widget)

    self.data_list = self.ListaAtualizada()

    self.itens_filtrados = []
    for item in self.data_list:
        if item['tipo_midia'] == tipo:
            self.itens_filtrados.append(item)

    if self.itens_filtrados != []:
        self.destaques_widget = QLabel("Destaque")
        self.destaques_widget.setFont(QFont("Lato", 20, QFont.Bold))
        self.destaques_widget.setStyleSheet("border: none; padding: 0px;")
        content_layout.addWidget(self.destaques_widget)

        primeiro_item = self.itens_filtrados[0]  # Seleciona o primeiro item da lista filtrada
        nome_selecionado = primeiro_item['nome']
    
        self.destaque_widget = ClickableImageLabel(QPixmap('Imagens/cinza.png'), 600, 120)
        self.destaque_widget.clicked.connect(lambda nome_selecionado=nome_selecionado, tipo=tipo: self.titulo_clicked(nome_selecionado,tipo))
        self.destaque_widget.setStyleSheet("border:2px solid white; padding: 0px;")

        label_nome = QLabel(nome_selecionado)  
        label_nome.setAlignment(Qt.AlignCenter)  
        label_nome.setStyleSheet("color: white; border: 1px solid white; padding: 0px; background-color: transparent; border-radius: 10px;")
        label_nome.setFont(QFont("Lato", 22, QFont.Bold))
        label_nome.setFixedSize(label_nome.sizeHint())

        self.destaque_widget.setLayout(QVBoxLayout())  
        self.destaque_widget.layout().addWidget(label_nome, alignment= Qt.AlignBottom) 

        content_layout.addWidget(self.destaque_widget, alignment=Qt.AlignCenter)
        content_layout.addSpacing(10)

        self.populares_widget = QLabel("Populares")
        self.populares_widget.setFont(QFont("Lato", 20, QFont.Bold))
        self.populares_widget.setStyleSheet("border: none; padding: 0px;")
        content_layout.addWidget(self.populares_widget)
    # Widget para conter os itens
    self.content_layout1 = QGridLayout()

    self.content_layout1.setHorizontalSpacing(50)
    self.content_layout1.setVerticalSpacing(20)    
    self.content_layout1.setContentsMargins(40,15,0,0)

    if self.data_list != []:
        self.home_layout(self.itens_filtrados)
    else:
        self.populares_widget = QLabel("Sem Dados De " + tipo)
        self.populares_widget.setFont(QFont("Lato", 12, QFont.Bold))
        self.populares_widget.setStyleSheet("border: none; padding: 0px;")
        content_layout.addWidget(self.populares_widget)


    content_layout.addLayout(self.content_layout1)
    
    # Adicionar content_widget ao scroll_area
    scroll_area.setWidget(content_widget)

    # Adicionar scroll_area ao content_pri_layout
    content_pri_layout.addWidget(scroll_area)
    # Adicionando o layout de conteúdo ao layout principal
    content_pesquisa_layout.addLayout(content_pri_layout)

    return content_pesquisa_layout
