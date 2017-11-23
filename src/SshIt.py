from cement.core.foundation import CementApp
from src.controller.BaseController import BaseController
from src.controller.AddController import AddController
from src.controller.AddConnectionController import AddConnectionController
# from src.controller.AddKeyController import AddKeyController


class SshIt(CementApp):
    class Meta:
        label = 'sshit'
        base_controller = 'base'
        extensions = ['yaml']
        config_handler = 'yaml'
        handlers = [BaseController, AddController, AddConnectionController]
