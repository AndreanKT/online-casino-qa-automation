# utils/performance.py

THRESHOLDS = {
    "login": 2000,      # ms — логинът трябва да е под 1 сек
    "register": 3000,   # ms — регистрацията под 2 сек
}

def assert_response_time(response, endpoint):
    actual_ms = response.elapsed.total_seconds() * 1000
    threshold = THRESHOLDS.get(endpoint, 2000)

    assert actual_ms < threshold, \
        f"{endpoint} too slow: {actual_ms:.0f}ms     (threshold: {threshold}ms)"