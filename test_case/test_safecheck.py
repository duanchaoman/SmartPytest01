import os
import sys

import pytest

path=os.path.abspath(os.path.dirname('E:\pypro\SmartPytest\SmartApi'))
sys.path.append(path)
import allure
from SmartApi import Safecheck


@allure.feature('安全复核')
class Test_Safecheck():
    @allure.title('外来车辆')
    def test_foreigncar(self):
        res=Safecheck.foreigncar()
        assert res.get('msg') == 'OK'

    @allure.title('外来人员')
    def test_foreignpeople(self):
        res=Safecheck.foreignpeople()
        assert res.get('msg') == 'OK'

    @allure.title('罪犯流动')
    def test_criminalInOut(self):
        res=Safecheck.criminalInOut()
        assert res.get('msg') == 'OK'

    @allure.title('外来物资')
    def test_materials(self):
        res=Safecheck.materials()
        assert res.get('msg') == 'OK'