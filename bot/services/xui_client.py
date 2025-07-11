import requests

class XUIClient:
    def __init__(self, base_url, username, password):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.authenticated = False
        self.username = username
        self.password = password

    def login(self):
        login_url = f"{self.base_url}/api/v1/login"
        payload = {"username": self.username, "password": self.password}
        response = self.session.post(login_url, json=payload)
        self.authenticated = response.status_code == 200
        return self.authenticated

    def get_users(self):
        if not self.authenticated:
            if not self.login():
                return None
        users_url = f"{self.base_url}/api/v1/users"
        response = self.session.get(users_url)
        if response.status_code == 200:
            return response.json()
        return None

    def create_user(self, user_data):
        if not self.authenticated:
            if not self.login():
                return False
        create_url = f"{self.base_url}/api/v1/users"
        response = self.session.post(create_url, json=user_data)
        return response.status_code == 201

    def delete_user(self, user_id):
        if not self.authenticated:
            if not self.login():
                return False
        delete_url = f"{self.base_url}/api/v1/users/{user_id}"
        response = self.session.delete(delete_url)
        return response.status_code == 204
