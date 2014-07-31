from disp_news import news_daemon

from daemon import runner

app = news_daemon()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
