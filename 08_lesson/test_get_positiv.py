import requests

base_url = "https://ru.yougile.com"
token = "ТОКЕН"
headers = {
    "Authorization": f"Bearer {token}",
}


def test_posit_get_id():
    resp = requests.get(base_url+'/api-v2/projects/430b0812-4aaa-407b-9eeb-5bb340d70388',
                        headers=headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body['id']
