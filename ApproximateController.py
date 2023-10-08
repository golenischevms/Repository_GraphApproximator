
from ApproximateView import ApproximateView
import numpy as np


class ApproximateController:
    """
        Класс ApproximateController представляет реализацию контроллера.
        Согласовывает работу представления с моделью.
    """
    def __init__(self, inModel):
        """
        Конструктор принимает ссылку на модель.
        Конструктор создаёт и отображает представление.
        """
        self.mModel = inModel
        self.mView = ApproximateView(self, self.mModel)
        self.mView.show()

    # Загрузка данных
    def load_data_set(self, response):

        skiprows = 2 #число игнорируемых строк сверху
        dataTitle = np.dtype('f8')
        data = np.loadtxt(response, dtype= dataTitle, skiprows=skiprows, usecols=(0,1)) # Параметры чтения файла

        with open(response, 'r') as fp:
            lines = len(fp.readlines()) - skiprows

        X = np.zeros(lines)
        Y = np.zeros(lines)
        Fapproxim = np.zeros(lines)
        for i in range(lines):
            X[i] = data[i][0]
            Y[i] = data[i][1]

        # Аппроксимация
        t = np.polyfit(X,Y,9)
        F = np.poly1d(t)

        return X, Y, F

    def dot_replace(self, response):
        data = ""
        with open(response, 'r') as file:
            data = file.read().replace(',', '.')
        print("Данные подготовлены.")

        with open(response, "w") as out_file:
            out_file.write(data)