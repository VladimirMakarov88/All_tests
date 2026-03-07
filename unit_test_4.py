import requests
import pytest


token = '' # вставить сюда свой токен

class Creation:
    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': f'OAuth {token}'}

    def create_directory(self, path=None):
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': path}
        response = requests.put(URL, headers=self.headers, params=params)
        status_response = response.status_code
        return status_response
    
def delete_directory(path):
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Authorization': f'OAuth {token}'}
    params = {'path': path, 'permanently': 'true'}
    response = requests.delete(URL, headers=headers, params=params)
    return response.status_code

@pytest.fixture(autouse=True)
def clean():
    yield
    try:
        delete_directory('test_data')
    except:
        pass

@pytest.mark.parametrize('path, expected',
    [('test_data', 201),
     ('', 400)]
)

def test_creation(path, expected):
    create = Creation(token)
    status_code = create.create_directory(path)
    assert status_code == expected


if __name__ == '__main__':
    pytest.main([__file__, '-v'])