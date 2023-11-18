from datetime import datetime
from enums import *
class Table:
    def __init__(self, id, max_capacity, location_identifier, status=TableStatus.FREE):
        self.__table_id = id
        self.__max_capacity = max_capacity
        self.__location_identifier = location_identifier
        self.__status = status
        self.__seats = []
    def get_number(self):
        return self.__table_id
    def show_location(self):
        return self.__location_identifier
    def show_status(self):
        return self.__status
    def is_table_free(self):
        return self.__status == TableStatus.FREE
    def get_capacity(self):
        return self.__max_capacity
    def update_status(self, new_status):
        self.__status = new_status
    def add_reservation(self, reservation):
        self.__status = TableStatus.RESERVED
        self.__seats.extend(reservation.get_table_seats())

    def search(self, capacity, start_time):
        # Return all tables with the given capacity and availability
        available_tables = []
        for table in self.__tables:
            if table.__status == TableStatus.FREE and table.__max_capacity >= capacity:
                available_tables.append(table)
        return available_tables


class TableSeat:
    def __init__(self, seat_number, seat_type=SeatType.REGULAR):
        self.__table_seat_number = seat_number
        self.__type = seat_type

    def update_seat_type(self, seat_type):
        self.__type = seat_type

    def get_seat_number(self):
        return self.__table_seat_number

    def get_seat_type(self):
        return self.__type


# class Reservation:
#     def __init__(self, id, people_count, notes, customer):
#         self.__reservation_id = id
#         self.__time_of_reservation = datetime.now()
#         self.__people_count = people_count
#         self.__status = ReservationStatus.REQUESTED
#         self.__notes = notes
#         self.__checkin_time = None
#         self.__customer = customer
#         self.__tables = []
#         self.__notifications = []
#     def create_reservation(self, people_count):
#         self.__people_count = people_count

#     def update_people_count(self, count):
#         self.__people_count = count

#     def add_table(self, table):
#         self.__tables.append(table)

#     def get_table_seats(self):
#         seats = []
#         for table in self.__tables:
#             for seat_number in range(1, table.__max_capacity + 1):
#                 seat = TableSeat(seat_number)
#                 seats.append(seat)
#         return seats

#     def check_in(self):
#         self.__status = ReservationStatus.CHECKED_IN
#         self.__checkin_time = datetime.now()

#     def cancel_reservation(self):
#         self.__status = ReservationStatus.CANCELED

class Reservation:
    def __init__(self, reservation_id, people_count, notes, customer):
        self.__reservation_id = reservation_id
        self.__time_of_reservation = datetime.now()
        self.__people_count = people_count
        self.__status = ReservationStatus.REQUESTED
        self.__notes = notes
        self.__checkin_time = None
        self.__customer = customer
        self.__tables = []
        self.__notifications = []
    def get_reservation_id(self):
        return self.__reservation_id

    def update_people_count(self, count):
        self.__people_count = count

    def add_table(self, table):
        self.__tables.append(table)
    def get_tables(self):
        return self.__tables
    def get_table_seats(self):
        seats = []
        for table in self.__tables:
            for seat_number in range(1, table.get_capacity() + 1):
                seat = TableSeat(seat_number)
                seats.append(seat)
        return seats

    def check_in(self):
        self.__status = ReservationStatus.CHECKED_IN
        self.__checkin_time = datetime.now()

    def cancel_reservation(self):
        self.__status = ReservationStatus.CANCELED
