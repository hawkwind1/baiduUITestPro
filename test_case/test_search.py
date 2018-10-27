#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/27 13:58
# @Author  : PanCheng
# @Site    : 
# @File    : test_search.py
# @Software: PyCharm

import pytest
from selenium import webdriver
from page_obj.searchpage import SearchPage
from page_obj.newspage import NewsPage
from page_obj.searchresultpage import SearchResultPage


def test_search_page_search_success(dr):
    my_searchpage = SearchPage(dr)
    my_searchresultpage = my_searchpage.search_content("pytest")
    assert "百度为您找到相关结果约" in my_searchresultpage.get_results_number_text
    assert "pytest_百度搜索" in my_searchresultpage.get_title()


def test_search_page_navigate_news_page(dr):
    my_serachpage = SearchPage(dr)
    my_news_page = my_serachpage.navigate_2_news_page()
    assert "热点y要闻" in my_news_page.get_hot_news_menu_text


