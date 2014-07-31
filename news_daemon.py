from disp_news import news_displayer

from daemon import runner

app = news_displayer()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()