"""
Utils
"""
import re
import pandas as pd
import os, sys
import threading
import numpy as np
from openpyxl import load_workbook
from collections import defaultdict
import decimal
from PyQt5.QtWidgets import QFileDialog

def choose_one_file(title):
    file_path, file_type = QFileDialog.getOpenFileName(title, './',
                                                       "All Files (*);;")
    return file_path

#生成资源文件目录访问路径
def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
	