import requests

base_url = "https://ru.yougile.com"
token = "ТОКЕН_2"
headers = {
    "Authorization": f"Bearer {token}",
}


def test_neg_create_project():
    project = {
        'title': 'задачи'
    }
    resp = requests.post(base_url+'/api-v2/projects',
                         json=project, headers=headers)
    assert resp.status_code == 401
    body = resp.json()
    assert 'error' in body, (
        "В ответе ожидается 'error'")
