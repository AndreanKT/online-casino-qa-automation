# utils/schemas/auth_schemas.py

LOGIN_SCHEMA = {
    "type": "object",                              # Response е обект или списък?
    "required": ["token", "userId", "message"],          # Кои три полета са задължителни?
    "properties": {
        "token": {
            "type": "string",                      # Какъв тип е token?
            "minLength": 10                    # Минимална дължина?
        },
        "userId": {
            "type": "string",                      # Какъв тип е userId?
            "minLength": 24,                   # MongoDB ID е точно колко символа?
            "maxLength": 24                    # Същото
        },
        "message": {
            "type": "string",                      # Какъв тип е message?
            "enum": ["Login Successfully"]                     # Точното съобщение?
        }
    }
}

REGISTER_SCHEMA = {
    "type": "object",
    "required": ["message"],                 # Пусни теста и виж полетата!
    "properties": {
        "message": {
            "type": "string",
            "enum": ["Registered Successfully"]
        }
    }
}