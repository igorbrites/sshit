from cement.core.controller import CementBaseController, expose


class AddController(CementBaseController):
    class Meta:
        label = 'add'
        description = 'Add keys or connections'
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(hide=True)
    def default(self):
        print('Run "sshit add --help" to see the usage')
