# pylint: disable=missing-module-docstring, missing-class-docstring
# pylint: disable=missing-function-docstring

from PyQt5 import QtWidgets as QW
from PyQt5.QtCore import pyqtSlot  # pylint: disable=no-name-in-module


class TMStatusBar(QW.QStatusBar):
    def __init__(self, parent: QW.QWidget = None):
        super().__init__(parent)

        self.state_label = QW.QLabel()
        self.path_label = QW.QLabel()

        if parent is not None:
            self.setFont(parent.font())

        self.insertWidget(0, self.state_label)
        self.insertWidget(1, self.path_label)

    @pyqtSlot(str)
    def set_state_label(self, state_name: str):
        if state_name != "":
            self.state_label.setVisible(True)
            self.state_label.setText(state_name)
        else:
            self.state_label.setVisible(False)

    @pyqtSlot(str)
    def set_path_label(self, path: str):
        if path and path != "":
            self.path_label.setVisible(True)
            self.path_label.setText(path)
        else:
            self.path_label.setVisible(False)
