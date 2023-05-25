import subprocess
import xml.etree.ElementTree as xml
class ClassFromUI:
    def __init__(self, ui_file):
        self.__ui_file = ui_file

    def __getUi(self):
        return subprocess.check_output(['pyside6-uic', self.__ui_file])

    def load(self):
        uipy = self.__getUi()
        parsed = xml.parse(self.__ui_file)
        form_class = parsed.find('class').text
        pyc = compile(uipy, '<string>', 'exec')
        frame = {}
        exec(pyc, frame)
        return frame['Ui_%s'%form_class]