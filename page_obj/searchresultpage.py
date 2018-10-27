#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/27 12:49
# @Author  : PanCheng
# @Site    : 
# @File    : searchresultpage.py
# @Software: PyCharm
from page_obj.basepage import BasePage


class SearchResultPage(BasePage):

    def __init__(self, driver):
        super(SearchResultPage, self).__init__(driver) # path 为空，不用跳转，只用来传递driver

    @property
    def _results_number_text(self):
        return self._by_css("#container > div.head_nums_cont_outer.OP_LOG > div > div.nums")

    @property
    def get_results_number_text(self):
        return self._results_number_text.text