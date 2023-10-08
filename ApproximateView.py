from PyQt5.QtWidgets import QMainWindow, QFileDialog
from mainwindow import *
from aboutprog import *
import os


class ApproximateView(QMainWindow):
    """
       Класс отвечающий за визуальное представление ApproximateModel.
    """

    def __init__(self, inController, inModel, parent=None):
        super(ApproximateView, self).__init__(parent)
        """
            Конструктор принимает ссылку на модель.
            Конструктор создаёт и отображает представление.
        """
        self.mController = inController
        self.mModel = inModel
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setup_graphics_settings()
        self.options = ('Get File Name', 'Get File Names', 'Get Folder Dir', 'Save File Name')
        self.ui.AboutProg.triggered.connect(self.prog_information)
        self.ui.LoadDataSet.triggered.connect(self.load_data)
        self.ui.PrepareData.triggered.connect(self.prepare_data)

    # НАСТРОЙКА ПОЛЯ ГРАФИКОВ
    def setup_graphics_settings(self):
        self.ui.graphics.setBackground('w') # Цвет фона
        self.ui.graphics.setTitle("График зависимости F(x)", color="black", size="14pt") # Название графика
        self.ui.graphics.setLabel("left", "y, усл. ед.") # Подпись сбоку
        self.ui.graphics.setLabel("bottom", "x, усл. ед.") # Подпись внизу
        self.ui.graphics.addLegend() # Добавление легенды, её можно двигать на графике

    def prog_information(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    def load_csv(self):
        option = self.options.index('Get File Name')
        if option == 0:
            response = self.getFileName()
        elif option == 1:
            response = self.getFileNames()
        elif option == 2:
            response = self.getDirectory()
        elif option == 3:
            response = self.getSaveFileName()
        else:
            print('Got Nothing')
        return response

    def getFileName(self):
        file_filter = 'Файлы данных (*.txt)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Выберите файл',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Файлы данных (*.txt)'
        )
        print(response)
        return response[0]

    def getFileNames(self):
        file_filter = 'Data File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls)'
        response = QFileDialog.getOpenFileNames(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Excel File (*.xlsx *.xls)'
        )
        return response[0]

    def getDirectory(self):
        response = QFileDialog.getExistingDirectory(
            self,
            caption='Select a folder'
        )
        return response

    def getSaveFileName(self):
        file_filter = 'Data File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls)'
        response = QFileDialog.getSaveFileName(
            parent=self,
            caption='Select a data file',
            directory='Data File.dat',
            filter=file_filter,
            initialFilter='Excel File (*.xlsx *.xls)'
        )
        print(response)
        return response[0]

    # ПОСТРОЕНИЕ ГРАФИКОВ
    def draw_graphics(self, X, Y, F):
        self.ui.graphics.plot(X, Y, pen='b', symbol='o', symbolPen='b', symbolSize=1)
        self.ui.graphics.plot(X, F(X), pen='r', symbol='o', symbolPen='r', symbolSize=1)


    def load_data(self):
        response = self.load_csv()
        X, Y, F = self.mController.load_data_set(response)
        self.draw_graphics(X, Y, F)

    def prepare_data(self):
        response = self.load_csv()
        self.mController.dot_replace(response)


