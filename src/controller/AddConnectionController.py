from cement.core.controller import CementBaseController, expose


class AddConnectionController(CementBaseController):
    class Meta:
        label = 'connection'
        description = 'Adds new connection to host'
        stacked_on = 'add'
        stacked_type = 'nested'
        arguments = [
            (['-n', '--name'], dict(help='The connection name/alias (Eg.: aws.producion.app.host)')),
            (['-t', '--host'], dict(help='The connection host (Eg.: 192.168.1.101 OR host.example.com)')),
            (['-u', '--user'], dict(help='The user to connect with (Eg.: root)')),
            (['-k', '--key'],  dict(help='The sshit key to use (Eg.: my-key)')),
        ]

    @expose(hide=True)
    def default(self):
        args = self.app.pargs

        if args.name is None or args.host is None or args.key is None or args.user is None:
            print('You must define --name, --host, --user and --key')
            self.app.close(1)
            return

        keys = self.app.config.keys('keys')

        if args.key not in keys:
            print('No key with name {} was found. You should call "sshit add key" first'.format(args.key))
            self.app.close(1)

        connections = self.app.config.get_section_dict('connections')

        connections[args.name] = dict(host=args.host, user=args.user, key=args.key)

        self.app.config.merge(connections)
