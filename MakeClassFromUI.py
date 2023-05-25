import subprocess
import xml.etree.ElementTree as xml

def ClassFromUI(ui_file):
    uiPy = subprocess.check_output(['pyside6-uic', ui_file])
    parsed = xml.parse(ui_file)
    form_class = parsed.find('class').text
    pyc = compile(uiPy, '<string>', 'exec')
    frame = {}
    exec(pyc, frame)
    return frame['Ui_%s'%form_class]