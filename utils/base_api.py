# utils/base_api.py

from utils.logger import get_logger
import requests                                    # Кой модул?

class BaseAPI:                                    # Как се казва класа?

    def __init__(self, base_url):                       # Как се казва конструктора и какво приема?
        self.base_url = base_url                   # Как запазваме base_url?
        self.session = requests.Session()             # Как се казва сесията и какъв клас?
        self.session.headers.update({"Content-Type": "application/json"})
        self.logger = get_logger(__name__)# Какъв Content-Type за JSON?

    def post(self, endpoint, payload):
        self.logger.info(f"POST {endpoint} | payload: {payload}")# Какви параметри приема post?
        return self.session.post(                  # session + HTTP метод?
            url=f"{self.base_url}{endpoint}",           # Как строим URL?
            json=payload                       # Как подаваме JSON?
        )

    def get(self, endpoint):
        self.logger.info(f"GET {endpoint}")# Какъв параметър приема get?
        return self.session.get(                  # session + HTTP метод?
            url=f"{self.base_url}{endpoint}"            # Как строим URL?
        )

    def delete(self, endpoint, token):
        self.logger.info(f"DELETE {endpoint} | token: {token}")# Какви параметри приема delete?
        return self.session.delete(                  # session + HTTP метод?
            url=f"{self.base_url}{endpoint}",           # Как строим URL?
            headers={"Cookie": f"token={token}"}   # Какъв header за token?
        )

    def put(self, endpoint, payload, token):
        self.logger.info(f"PUT {endpoint}| payload: {payload} | token: {token}")# Какви параметри приема put?
        return self.session.put(                  # session + HTTP метод?
            url=f"{self.base_url}{endpoint}",           # Как строим URL?
            json=payload,                      # Как подаваме JSON?
            headers={"Cookie": f"token={token}"}     # Какъв header за token?
        )
    def get_with_token(self, endpoint, token):
        self.logger.info(f"get_with_token {endpoint} | token: {token}")# ← нов метод!
        return self.session.get(
            url=f"{self.base_url}{endpoint}",
            headers={"Authorization": token}
        )