'''Model for aircraft flights'''


class Flight:
    """A flight with a particular passenger aircraft."""
    # this is an initializer, not a constructor. The object exists already.
    def __init__(self, number, aircraft):
        # this assignment is enough to bring an object into existence
        if not number[:2].isalpha():
            raise ValueError("no airline code in '{}'".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))
        if not (number[:2].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("invalid route number '{}'".format(number))

        self._number = number
        self._aircraft = aircraft

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()


class Aircraft:

    def__init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

def console_card_printer(passenger, seat, flight_number, aircraft):
    output = 