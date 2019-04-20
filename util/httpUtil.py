import requests
import  json
from commen.commenDB import CommenDB
class HttpUtil:
    def __init__(self):
        self.http=requests.session()
        self.headers={'Content-Type': 'application/json;charset=UTF-8'}

    def post(self,path,data):
        proxies = CommenDB.proxies
        host=CommenDB.host
        data_json=json.dumps(data)
        if CommenDB.token is not None:
            self.headers['token']=CommenDB.token
        resq_login = self.http.post(url=host+path,
                         data=data_json,
                         proxies=proxies,
                         headers=self.headers)
        assert resq_login.status_code == 200
        resq_json=resq_login.text
        resq_dic=json.loads(resq_json)
        return resq_dic