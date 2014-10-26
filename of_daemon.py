from of import of_daemon

from daemon import runner

app = of_daemon()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
