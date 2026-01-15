class Deck:
    def __init__(self, row: int, column: int, is_alive: bool = True) -> None:
        self.row = row
        self.column = column
        self.is_alive = is_alive


class Ship:
    def __init__(self, start: tuple, end: tuple, is_drowned: bool = False) -> None:
        self.is_drowned = is_drowned
        self.decks = []
        start_row, start_col = start
        end_row, end_col = end
        for r in range(min(start_row, end_row), max(start_row, end_row) + 1):
            for c in range(min(start_col, end_col), max(start_col, end_col) + 1):
                self.decks.append(Deck(r, c))

    def get_deck(self, row: int, column: int) -> str | None:
        for deck in self.decks:
            if deck.row == row and deck.column == column:
                return deck
        return None

    def fire(self, row: int, column: int) -> str:
        deck = self.get_deck(row, column)
        if deck:
            deck.is_alive = False

        if all(not d.is_alive for d in self.decks):
            self.is_drowned = True
            return "Sunk!"
        return "Hit!"


class Battleship:
    def __init__(self, ships: list) -> None:
        self.field = {}
        for start, end in ships:
            new_ship = Ship(start, end)
            for deck in new_ship.decks:
                self.field[(deck.row, deck.column)] = new_ship

    def fire(self, location: tuple) -> str:
        if location in self.field:
            ship = self.field[location]
            return ship.fire(location[0], location[1])
        return "Miss!"
