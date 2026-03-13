from utils.base_api import BaseAPI


class BookingAPI(BaseAPI):

    def __init__(self, base_url):
        super().__init__(base_url)

    def get_all_bookings(self):
        return self.get("/booking")

    def get_booking(self, booking_id):
        return self.get(f"/booking/{booking_id}")

    def create_booking(self, data):
        return self.post("/booking", data)