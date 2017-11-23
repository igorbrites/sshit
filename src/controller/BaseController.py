from cement.core.controller import CementBaseController, expose


class BaseController(CementBaseController):
    class Meta:
        label = 'base'
        arguments = [
            (['-v', '--version'], dict(action='version', version='0.0.2'))
        ]
        description = "          	  _____ _____ _    _ _____ _______ _\n\
~“. ^ .”~	 / ____/ ____| |  | |_   _|__   __| |\n\
~“ ( ) ”~	| (___| (___ | |__| | | |    | |  | |\n\
~“(O O)”~	 \___ \\\\___ \|  __  | | |    | |  | |\n\
“(  ◡  )“	 ____) |___) | |  | |_| |_   | |  |_|\n\
(_______)	|_____/_____/|_|  |_|_____|  |_|  (_)\n\
\n\
            SSH Client made simple!"

    @expose(hide=True)
    def default(self):
        print('Run "sshit --help" to see the usage')

    @expose(help='Remove a server configuration')
    def remove(self):
        self.app.log.info('Add command, should call RemoveController')
