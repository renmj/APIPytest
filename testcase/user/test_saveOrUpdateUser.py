from commen.commenDB import CommenDB
from conftest import http
import random
import allure
@allure.feature('注册登录校验模块')
class Test_saveOrUpdateUser():
    @allure.story('注册登录校验成功')
    def test_regiter_success(self):
        nickname=str(random.randint(10000000,100000000))
        data = {"nickName": nickname,
	            "userName": '135'+nickname,
	            "telNo": "",
	            "email": "",
                "address": "",
                "roleIds": "1",
                "regionId": 1,
                "regionLevel": 1}
        res_register= http.post('/user/saveOrUpdateUser', data)
        # assert res['code']==200
        # assert res['msg'] == '操作成功'
        print("注册成功")
        print(res_register)
        name=data["userName"]
        data = {'userName':name,
                'password': CommenDB.password}
        res_login = http.post('/sys/login', data)
        assert res_login['code'] == 200
        assert res_login['msg'] == '操作成功'
        print("新窗口登录")
        print(res_login)
        login_id=res_login['object']['userId']
        print(login_id)
        data={"pageCurrent": 1, "pageSize": 10, "nickName": "", "userName": "", "regionId": 1}
        res_look= http.post('/user/loadUserList', data)
        # assert res['code'] == 200
        # assert res['msg'] == '操作成功'
        print("查看列表第一条")
        print(res_look)
        look_id = res_look['object']['list'][0]['id']
        print(id)
        assert  login_id==look_id
        print("校验成功")