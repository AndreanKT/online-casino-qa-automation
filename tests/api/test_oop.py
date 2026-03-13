from utils.auth_api import AuthAPI
from utils.booking_api import BookingAPI


class TestOOP:

    def test_login_and_get_booking(self, base_url, valid_credentials):

        auth = AuthAPI(base_url)
        booking = BookingAPI(base_url)

        token = auth.login(
            valid_credentials["username"],
            valid_credentials["password"]
        )

        # Validate token
        assert token is not None

        # Validate bookings
        response = booking.get_all_bookings()
        assert response.status_code == 200
        assert len(response.json()) > 0