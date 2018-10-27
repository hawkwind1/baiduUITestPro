#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/27 13:48
# @Author  : PanCheng
# @Site    : 
# @File    : newspage.py
# @Software: PyCharm

from page_obj.basepage import BasePage
from page_obj.searchresultpage import SearchResultPage


class NewsPage(BasePage):

    def __init__(self, driver):
        super(NewsPage, self).__init__(driver)

    @property
    def _hot_news_menu(self):
        return self._by_css("#headline-tabs > ul > li > a")

    @property
    def get_hot_news_menu_text(self):
        return self._hot_news_menu.text