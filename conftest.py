import pytest
import requests
import json
from util.httpUtil import HttpUtil
from commen.commenDB import CommenDB
http =HttpUtil()
#module/session/class/function
@pytest.fixture(scope='session',autouse=True)
def session_fixture():
    path="/sys/login"
    data={'userName':CommenDB.mobile,
          'password':CommenDB.password}
    resq_login=http.post(path,data)
    CommenDB.token=resq_login['object']['token']
    print("登陆成功")
    # print(resq_login)
    # yield
     # json转python dict

    # headers['token'] = token  # 加到header里
    # resq = http.post(url="http://192.168.1.203:8083/sys/logout",
    #                  data=None,
    #                  proxies=proxies,
    #                  headers=headers)
    # assert resq.status_code == 200
    # print("退出成功")
    # print(resq.text)