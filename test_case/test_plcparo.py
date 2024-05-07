import allure
import pytest
import os
import sys
path=os.path.abspath(os.path.dirname('E:\pypro\SmartPytest\SmartApi'))
sys.path.append(path)
from SmartApi import PlcparoApi

@allure.feature('日常巡更')
class Test_Plcparo():
    @allure.title('新增巡更路线')
    def test_addPlcparo(self):
        res=PlcparoApi.addPlcparo()
        print(res)
        assert res.get('msg')=='OK'

    @allure.title('新增巡更路线')
    def test_addPlcdata(self):
        res=PlcparoApi.addPlcdata()
        print(res)
        assert res.get('msg')=='OK'

    @allure.title('执行巡更任务')
    def test_plcimp(self):
        res =PlcparoApi.plcimp()
        print(res)
        assert res.get('msg')=='OK'

    @allure.title('添加定时巡更任务')
    def test_addtask(self):
        res = PlcparoApi.addtask()
        print(res)
        assert res.get('msg') == 'OK'

    @allure.title('执行定时巡更任务')
    def test_dotimetask(self):
        res = PlcparoApi.dotimetask()
        print(res)
        assert res.get('msg') == 'OK'

    @allure.title('巡更日志')
    def test_plclog(self):
        res = PlcparoApi.plclog()
        print(res)
        assert res.get('msg') == 'OK'

    @allure.title('统计分析')
    def test_plcstaana(self):
        res = PlcparoApi.plcstaana()
        print(res)
        assert res.get('msg') == 'OK'


if __name__ == '__main__':
    pytest.main(['-s', '-r', './test_case/test_plcparo'])