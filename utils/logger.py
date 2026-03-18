import logging  # вграден Python модул за logging
import os  # за създаване на папки


def get_logger(name):  # name = __name__ от файла който го вика

    logger = logging.getLogger(name)  # създава logger с това име
    logger.setLevel(logging.DEBUG)  # показва ВСИЧКИ нива (DEBUG и нагоре)

    os.makedirs("reports/logs", exist_ok=True)  # създава папката ако не съществува

    file_handler = logging.FileHandler("reports/logs/test.log")  # записва във файл
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        #  дата/час  |  INFO/ERROR  | кой файл | съобщението
    )

    file_handler.setFormatter(formatter)  # слагаме формата на handler-а
    logger.addHandler(file_handler)  # слагаме handler-а на logger-а

    return logger