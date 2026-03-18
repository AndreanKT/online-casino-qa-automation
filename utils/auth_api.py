from utils.logger import get_logger
from utils.base_api import BaseAPI              # Кой клас импортираме от кой файл?


class AuthAPI(BaseAPI):                        # Как се казва класа и кой е parent?

    def __init__(self, base_url):                # Конструктора и какво приема?
        super().__init__(base_url)                   # Как викаме parent конструктора?

    def login(self, username, password):         # Какви параметри приема login?
        return self.post(               # Кой метод от BaseAPI ползваме?
            "/api/ecom/auth/login",                     # Кой endpoint?
            {
                "userEmail": username,       # Ключ за username в payload?
                "userPassword": password        # Ключ за password в payload?
            }
        )

    def register(self, confirmPassword, firstName, lastName, userEmail, userMobile, userPassword ):   # Какви параметри приема?
        return self.post(               # Кой метод от BaseAPI?
            "/api/ecom/auth/register",
            {
                "confirmPassword": confirmPassword,
                "firstName": firstName,
                "lastName": lastName,
                "userEmail": userEmail,
                "userMobile":  userMobile,
                "userPassword": userPassword
            }
        )