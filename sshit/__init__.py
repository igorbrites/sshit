from src.SshIt import SshIt


def main():
    with SshIt() as app:
        app.run()
        app.close(0)
