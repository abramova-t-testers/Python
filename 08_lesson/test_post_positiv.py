import requests

base_url = "https://ru.yougile.com"
token = "ТОКЕН"
headers = {
    "Authorization": f"Bearer {token}",
}


def test_posit_create_project():
    project = {
        'title': 'задачи'
    }
    resp = requests.post(base_url+'/api-v2/projects',
                         json=project, headers=headers)
    assert resp.status_code == 201
    body = resp.json()
    assert body['id']
    print(body)
