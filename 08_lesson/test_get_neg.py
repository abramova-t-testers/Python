import requests

base_url = "https://ru.yougile.com"
token = "ТОКЕН"
headers = {
    "Authorization": f"Bearer {token}",
}


def test_neg_get_id():
    resp = requests.get(base_url+'/api-v2/projects/430b0812-4aaa-407b-9eeb',
                        headers=headers)
    assert resp.status_code == 404
    body = resp.json()
    assert 'error' in body, (
        "В ответе ожидается 'error'")
