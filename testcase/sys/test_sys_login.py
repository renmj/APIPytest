from commen.commenDB import CommenDB
from conftest import http
import allure
@allure.feature('用户登录模块模块')
class Test_Login():
    # 成功
    @allure.story('用户登录成功')
    def test_login_success(self):
        data = {'userName': CommenDB.mobile,
                'password': CommenDB.password}
        res= http.post('/sys/login', data)
        assert res['code']==200
        assert res['msg'] == '操作成功'
        assert res['object'] ['userId']== 2
        print(res)
    # 失败：用户名或密码错误
    # def test_login_failone(self):
    #     data = {'userName':CommenDB.mobile,
    #             'password':"123"}
    #     res= http.post('/sys/login', data)
    #     assert res['code']==410
    #     assert res['msg'] == '用户名或密码错误'
    #     print(res)
    # def test_login_failtwo(self):
    #     data={"userName": "", "password": " "}
    #     res= http.post('/sys/login', data)
    #     assert res['code']==3010
    #     assert res['msg'] == '此账户禁止登录'
    #     print(res)
    # # 失败：用户名不存在
    # def test_login_failthree(self):
    #     data = {'userName': "182325",
    #             'password': CommenDB.password}
    #     res= http.post('/sys/login', data)
    #     assert res['code']==301
    #     assert res['msg'] == "用户不存在"
    #     print(res)
