# base class for all implementations of aircraft
# notice: has no initializer
# not useful on its own. you would never instantiate an Aircraft


class Aircraft:
    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


# this is how you inherit from a base class
class Boeing777(Aircraft):
    def __init__(self, registration):
        pass

