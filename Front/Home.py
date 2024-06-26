from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QWidget, QSizePolicy, QLineEdit,
    QScrollArea, QGridLayout, QSpacerItem
)
from PySide6.QtGui import QPixmap, QIcon, QFont
from PySide6.QtCore import Qt, Signal
import random

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

def initUI(self):
   
    # Área da pesquisa
    content_pesquisa_layout = QVBoxLayout() 

    pesquisa_widget = QWidget()
    pesquisa_widget.setStyleSheet("background-color: #242121; border-bottom: 2px solid white;")
    pesquisa_widget.setFixedHeight(80)
    pesquisa_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    pesquisa_layout = QHBoxLayout(pesquisa_widget)
    pesquisa_layout.setAlignment(Qt.AlignCenter)

    label_inicio = QLabel("Início")
    label_inicio.setFont(QFont("Abril Fatface", 30))
    label_inicio.setStyleSheet("border: none;  padding: 0px;")
    pesquisa_layout.addWidget(label_inicio, alignment=Qt.AlignCenter)

    pesquisa_layout.addStretch()

    self.line_edit_busca = QLineEdit()
    self.line_edit_busca.setStyleSheet("color: white; padding: 5px;")
    self.line_edit_busca.setPlaceholderText("Buscar")
    self.line_edit_busca.setFont(QFont("Lato", 11, QFont.Bold))
    self.line_edit_busca.setFixedWidth(200)
    self.line_edit_busca.textChanged.connect(self.filtrar_conteudo1)
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

    if self.data_list != []:
        primeiro_torrent = self.data_list[0]
        nome_do_primeiro_torrent = primeiro_torrent['nome']
        tipo_do_primeiro_torrent = primeiro_torrent['tipo_midia']

        self.destaques_widget = QLabel("Destaque")
        self.destaques_widget.setFont(QFont("Lato", 20, QFont.Bold))
        self.destaques_widget.setStyleSheet("border: none; padding: 0px;")
        content_layout.addWidget(self.destaques_widget)

        self.destaque_widget = ClickableImageLabel(QPixmap("Imagens/cinza.png"), 600, 120)
        self.destaque_widget.clicked.connect(lambda: self.titulo_clicked(nome_do_primeiro_torrent, tipo_do_primeiro_torrent))
        self.destaque_widget.setStyleSheet("border:2px solid white; padding: 0px;")

        label_nome = QLabel(nome_do_primeiro_torrent)  
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
        self.home_layout(self.data_list)
    else:
        self.populares_widget = QLabel("Sem dados")
        self.populares_widget.setFont(QFont("Lato", 12, QFont.Bold))
        self.populares_widget.setStyleSheet("border: none; padding: 0px;")
        content_layout.addWidget(self.populares_widget)
    
   
    # Definir o layout interno de content_widget como content_layout
    content_layout.addLayout(self.content_layout1)
    
    # Adicionar content_widget ao scroll_area
    scroll_area.setWidget(content_widget)

    # Adicionar scroll_area ao content_pri_layout
    content_pri_layout.addWidget(scroll_area)
    # Adicionando o layout de conteúdo ao layout principal
    content_pesquisa_layout.addLayout(content_pri_layout)

    return content_pesquisa_layout
