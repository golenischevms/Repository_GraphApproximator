import os, sys


try:
    if os.environ["XDG_SESSION_TYPE"] == "wayland":
        os.environ["QT_QPA_PLATFORM"] = "wayland"
except Exception as e:
    print(str(e))
import sys


from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication

from ApproximateController import ApproximateController
from ApproximateModel import ApproximateModel

sys.path.append('.')

is_with_figure = True

ORGANIZATION_NAME = 'Federal State Autonomous Educational Institution of Higher Education “South Ural State University (national research university)”'
ORGANIZATION_DOMAIN = 'https://www.susu.ru/'
APPLICATION_NAME = 'Approximate Model'

QCoreApplication.setApplicationName(ORGANIZATION_NAME)
QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
QCoreApplication.setApplicationName(APPLICATION_NAME)

QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)


def main():
    app = QApplication(sys.argv)
    # создаём модель
    model = ApproximateModel()
    # создаём контроллер и передаём ему ссылку на модель
    controller = ApproximateController(model)
    with open("SUSU.qss", "r") as file:
        app.setStyleSheet(file.read())
    sys.exit(app.exec_())
    app.exec()

if __name__ == "__main__":
    sys.exit(main())
