#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/27 12:02
# @Author  : PanCheng
# @Site    : 
# @File    : basepage.py
# @Software: PyCharm

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from conftest import *


class BasePage(object):

    # 所有页面的初始化方法, 一是driver; 二是 path,即要访问页面的路径
    def __init__(self, driver, path=None):
        self.driver = driver
        self.driver.maximize_window()

        # 如果输入的url不为空，且navigate为True时，将访问新的url
        if path:
            self.url = path
            self._navigate()

    # 用浏览器打开网页
    def _navigate(self):
        self.driver.get(self.url)

    # 封装获取网页title的方法,方便外部直接用page对象调用获取title信息
    def get_title(self):
        return self.driver.title

    # 封装获取网页url的方法,方便外部直接用page对象调用获取url信息
    def get_url(self):
        return self.driver.current_url

    # 封装部分find elements的方法,方便子pages使用
    def _by_css(self, css_string):
        element = WebDriverWait(self.driver,TIMEOUT).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_string)))
        return element

    def _check_element_not_exist_by_css(self, css_string):
        return EC.invisibility_of_element_located((By.CSS_SELECTOR, css_string))

    def _by_id(self, id_string):
        return self.driver.find_element_by_id(id_string)