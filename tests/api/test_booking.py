import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com"


class TestBookingAPI:

    def test_get_all_bookings(self):
        """Вземи всички резервации"""
        response = requests.get(f"{BASE_URL}/booking")

        assert response.status_code == 200
        assert len(response.json()) > 0

    def test_get_booking_by_id(self):
        """Вземи конкретна резервация"""
        response = requests.get(f"{BASE_URL}/booking/1")

        assert response.status_code == 200
        assert "firstname" in response.json()
        assert "lastname" in response.json()

    def test_create_booking(self):
        """Създай нова резервация"""
        payload = {
            "firstname": "Andrean",
            "lastname": "Test",
            "totalprice": 100,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2025-01-01",
                "checkout": "2025-01-10"
            }
        }
        response = requests.post(
            f"{BASE_URL}/booking",
            json=payload
        )

        assert response.status_code == 200
        assert response.json()["booking"]["firstname"] == "Andrean"