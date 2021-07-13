# coding: utf-8
""" This is MainWindow module """

import sys
import os
import subprocess
from functools import partial

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '\\Commands')
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '\\UI')

from qt import *

import MainWindow_UI
from SingletonInstance import SingletonInstane
from AppDocData import *


class MainWindow(QMainWindow, MainWindow_UI.Ui_MainWindow, SingletonInstane):
    """ This is MainWindow class """
    addMessage = Signal(Enum, str)

    def __init__(self):
        """ initialize """
        from App import App

        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.addMessage.connect(self.add_message)

        try:
            self.progressBar = QProgressBar()
            self.statusbar.addPermanentWidget(self.progressBar, 1)

            self.actionExit.triggered.connect(self.on_exit)

            app_doc_data = AppDocData.instance()
            _translate = QCoreApplication.translate
            version = QCoreApplication.applicationVersion()
            self.setWindowTitle(f"{App.NAME}({version})")

            # load stylesheet file list
            stylesheet_name = App.instance().stylesheet_name
            files = [os.path.splitext(file)[0] for file in os.listdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'stylesheets'))
                     if os.path.splitext(file)[1] == '.qss']
            for file in files:
                action = self.menuTheme.addAction(file)
                action.setCheckable(True)
                action.setChecked(True) if stylesheet_name == file else action.setChecked(False)
                action.triggered.connect(partial(self.load_stylesheet, file))
            # up to here

            # load language files
            language_name = App.instance().language_name
            files = ['en_us']  # english is default language
            files.extend([os.path.splitext(file)[0] for file in
                          os.listdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'translates')) if
                          os.path.splitext(file)[1] == '.qm'])
            for file in files:
                action = self.menuLanguage.addAction(file)
                action.setCheckable(True)
                action.setChecked(True) if language_name.lower() == file.lower() else action.setChecked(False)
                action.triggered.connect(partial(self.load_language, file))
            # up to here
        except Exception as ex:
            message = f"error occurred({repr(ex)}) in {sys.exc_info()[-1].tb_frame.f_code.co_filename}:" \
                      f"{sys.exc_info()[-1].tb_lineno}"
            print(message)

    def load_stylesheet(self, file: str):
        """load stylesheets"""
        from App import App

        App.instance().loadStyleSheet(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'stylesheets', file))

        app_doc_data = AppDocData.instance()
        configs = [Config('app', 'stylesheet', file)]
        app_doc_data.save_app_configs(configs)

    def load_language(self, file: str):
        """ load language file and then apply selected language """
        from App import App

        try:
            qm_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'translate', '{0}.qm'.format(file))
            App.instance().load_language(qm_file)

            app_doc_data = AppDocData.instance()
            configs = [Config('app', 'language', file)]
            app_doc_data.save_app_configs(configs)
        finally:
            self.retranslateUi(self)

    def add_message(self, messageType, message):
        """add message to listwidget"""
        from AppDocData import MessageType

        try:
            current = QDateTime.currentDateTime()

            item = QListWidgetItem('{}: {}'.format(current.toString('hh:mm:ss'), message))
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            if messageType == MessageType.Error:
                item.setBackground(Qt.red)

            self.listWidgetLog.insertItem(0, item)
        except Exception as ex:
            print(f'error occurred({repr(ex)}) in {sys.exc_info()[-1].tb_frame.f_code.co_filename}:'
                  f'{sys.exc_info()[-1].tb_lineno}')

    def on_exit(self):
        """exit application"""
        QCoreApplication.quit()

    def on_help(self):
        """show help document"""
        pass

    def show_message(self, title, text):
        """pop-up message box"""

        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)

        msg.setWindowTitle(title)
        msg.setText(text)

        return msg.exec_()


if __name__ == '__main__':
    import locale
    from App import App

    app = App(sys.argv)
    try:
        app._mainWnd = MainWindow.instance()
        app._mainWnd.show()
        sys.exit(app.exec_())
    except Exception as ex:
        print(f'error occurred({repr(ex)}) in {sys.exc_info()[-1].tb_frame.f_code.co_filename}:'
              f'{sys.exc_info()[-1].tb_lineno}')
    finally:
        pass
