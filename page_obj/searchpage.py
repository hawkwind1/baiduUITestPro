#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/27 12:49
# @Author  : PanCheng
# @Site    : 
# @File    : searchpage.py
# @Software: PyCharm
import pytest
from page_obj.basepage import BasePage
from page_obj.searchresultpage import SearchResultPage
from page_obj.newspage import NewsPage
from conftest import *


class SearchPage(BasePage):

    def __init__(self, driver):
        path = INIPAGE  # www.baidu.com
        super(SearchPage, self).__init__(driver, path)

    @property
    def _input_editbox(self):
        return self._by_css('#kw')

    @property
    def _search_button(self):
        return self._by_css('#su')

    @property
    def _news_link(self):
        return self._by_css('#u1 > a:nth-child(1)')

    @property
    def _map_link(self):
        return self._by_css('#u1 > a:nth-child(3)')

    def search_content(self, keys):
        self._input_editbox.clear()
        self._input_editbox.send_keys(keys)
        self._search_button.click()
        # 返回结果页面
        return SearchResultPage(self.driver)

    def navigate_2_news_page(self):
        self._news_link.click()
        #返回新闻页面
        return NewsPage(self.driver)
