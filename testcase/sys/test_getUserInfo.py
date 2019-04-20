from conftest import *
from conftest import http
from commen.commenDB import CommenDB
import allure
@allure.feature('获取用户信息模块')
class Test_userInfo():
    @allure.story('获取用户信息成功')
    def test_userInfo(self):
        proxies=CommenDB.proxies
        path="/sys/getUserInfo"
        headers=http.headers
        headers["token"]=CommenDB.token
        data=None
        resq=http.post(path,data)
        print(resq)