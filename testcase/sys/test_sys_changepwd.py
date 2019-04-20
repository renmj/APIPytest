from commen.commenDB import CommenDB
from conftest import http
import allure
@allure.feature('修改密码模块')
class Test_changePwd():
    @allure.story('修改密码成功')
    def test_changepwdnew(self):
        data = {'userId':198,
                "userName":CommenDB.mobile,
                'oldPwd':CommenDB.password,
                'password':"123321"}
        res = http.post('/sys/changePwd', data)
        assert res['code'] == 200
        assert res['msg'] == '操作成功'
        print(res)

    @allure.story('恢复密码成功')
    def test_changepwdold(self):
        data = {'userId':198,
                "userName":CommenDB.mobile,
                'oldPwd':"123321",
                'password':CommenDB.password}
        res = http.post('/sys/changePwd', data)
        assert res['code'] == 200
        assert res['msg'] == '操作成功'
        print(res)