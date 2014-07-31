import daemon

from disp_news import news_displayer

with daemon.DeamonContext():
    news_displayer()