class XiangqiGame():

    """
    Represents a xiangqi game with the ability to move players and win, lose or draw the game
    """

    def __init__(self):
        """
        constuctor method that initializeS data member
        """
        self._board_1 = Board(self)
        self._move_1 = Move(self)
        self._player_1 = Player(self)
        self._game_state = "UNFINISHED"
        self._move_legal = None
        self._mf_board_row = 0
        self._mf_board_column = 0
        self._mt_board_row = 0
        self._mt_board_column = 0
        self._move_from = None
        self._move_to = None

    def set_game_state(self, state):
        """
        sets game state
        """
        self._game_state = state

    def get_game_state(self):
        """
        returns game state
        """

        return self._game_state

    def is_in_check(self, player_color):
        """
        returns if a player is in check
        """

        if player_color == "red":
            if self._player_1._red_in_check is False:
                return False
            if self._player_1._red_in_check is True:
                return True

        if player_color == "black":
            if self._player_1._black_in_check is False:
                return False
            if self._player_1._black_in_check is True:
                return True

    def player_turn(self):
        """returns players turn"""

        if self._player_1._turn == "red":
            return "red"
        if self._player_1._turn == "black":
            return "black"

    def make_move(self, moved_from, moved_to):
        """
        moves players in the game on the board
        """

        if self._move_1.move(moved_from, moved_to) == True:
            self._move_1.in_check()

            self.show_board()






        if self._move_legal is None:
            return False

        return self._move_legal





    def show_board(self):
        """
        helper function to print out game board for debugging
        """
        return self._board_1.board_visual()




class Board:
    """
    represents the board for the game
    """

    def __init__(self, XiangqiGame, board = None, temp_board = None):
        """
        constructor method that initializes data members, including data member that holds
        game board
        """
        self._XiangqiGame_board = XiangqiGame
        self._board = board
        self._temp_board = temp_board
        if self._board is None:
            self._board = [
            ["rx1", "rh1", "re1", "ra1", "rg1", "ra2", "re2", "rh2", "rx2" ],
            [" ",    " ",   " ",   " ",   " ",   " ",   " ",   " ",   " "  ],
            [" ",   "rc1",  " ",   " ",   " ",   " ",   " ",  "rc2",  " "  ],
            ["rs1",  " ",  "rs2",  " ",   "rs3", " ",  "rs4",  " ",  "rs5" ],
            [" ",    " ",   " ",   " ",   " ",   " ",   " ",   " ",   " "  ],
            [" ",    " ",   " ",   " ",   " ",   " ",   " ",   " ",   " "  ],
            ["bs1",  " ",  "bs2",  " ",  "bs3",  " ",  "bs4",  " ",  "bs5" ],
            [" ",   "bc1",  " ",   " ",   " ",   " ",   " ",  "bc2",  " "  ],
            [" ",    " ",   " ",   " ",   " ",   " ",   " ",   " ",   " "  ],
            ["bx1", "bh1", "be1", "ba1", "bg1", "ba2", "be2", "bh2", "bx2"]]

        if self._temp_board is None:
            self._temp_board = [
            ["rx1", "rh1", "re1", "ra1", "rg1", "ra2", "re2", "rh2", "rx2" ],
            [" ",    " ",   " ",   " ",   " ",   " ",   " ",   " ",   " "  ],
            [" ",   "rc1",  " ",   " ",   " ",   " ",   " ",  "rc2",  " "  ],
            ["rs1",  " ",  "rs2",  " ",   "rs3", " ",  "rs4",  " ",  "rs5" ],
            [" ",    " ",   " ",   " ",   " ",   " ",   " ",   " ",   " "  ],
            [" ",    " ",   " ",   " ",   " ",   " ",   " ",   " ",   " "  ],
            ["bs1",  " ",  "bs2",  " ",  "bs3",  " ",  "bs4",  " ",  "bs5" ],
            [" ",   "bc1",  " ",   " ",   " ",   " ",   " ",  "bc2",  " "  ],
            [" ",    " ",   " ",   " ",   " ",   " ",   " ",   " ",   " "  ],
            ["bx1", "bh1", "be1", "ba1", "bg1", "ba2", "be2", "bh2", "bx2"]]



    def board_visual(self):
        """
        helper function to print out game board for debugging
        """

        for row in self._board:
            print(row)
        print()


    def update(self, mf_row, mf_column, mt_row, mt_column):
        """
        updates the board data member to reflect a move on the board
        """


        self._board[mt_row][mt_column] = self._board[mf_row][mf_column]
        self._board[mf_row][mf_column] = " "


    def temp_update(self, mf_row, mf_column, mt_row, mt_column):
        """
        updates the board data member to reflect a move on the board
        """


        self._temp_board[mt_row][mt_column] = self._temp_board[mf_row][mf_column]
        self._temp_board[mf_row][mf_column] = " "




    def empty(self, mf_row, mf_column):
        """
        determines if spot on board is empty is empty
        """

        if self._board[mf_row][mf_column] == " ":
            return True

        else:
            return None

class Player:
    """
    represents player of the game
    """
    def __init__(self, XiangqiGame):
        """
        constructor method that inherits parent class and initializes data members
        """
        self._XiangqiGame_player = XiangqiGame
        self._red_in_check = False
        self._black_in_check = False
        self._turn = "red"



class Move:
    """
    class that facilitates the movement of pieces on game board
    """

    def __init__(self, XiangqiGame):
        """
        constructor method that inherits parent class and initializes a helper data function
        """
        self._XiangqiGame = XiangqiGame
        self._helper_board = [["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1", "i1"],
                              ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2", "i2"],
                              ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "i3"],
                              ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4", "i4"],
                              ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5", "i5"],
                              ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6", "i6"],
                              ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7", "i7"],
                              ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8", "i8"],
                              ["a9", "b9", "c9", "d9", "e9", "f9", "g9", "h9", "i9"],
                              ["a10","b10","c10","d10","e10","f10","g10","h10","i10"]]

        self._turn_holder = "black"
        self._legal_move = True
        self._mf_board_row_m = 0
        self._mf_board_column_m = 0
        self._mt_board_row_m = 0
        self._mt_board_column_m = 0
        self._red_general_row = 0
        self._red_general_column = 4
        self._black_general_row = 9
        self._black_general_column = 4
        self._moves_left = False







    def move(self, move_from, move_to):
        """
        iterates through helper board and shows the respective position of passed values in the game board
        in accordance with the alegraic labeling of the board
        """

        # variables that hold position values
        move_legal = None
        red_move_out_of_check = 0
        black_move_out_of_check = 0

        try:

            self._XiangqiGame._player_1._red_in_check = False
            self._XiangqiGame._player_1._black_in_check = False





            #iterates through helper board and finds the position of the piece
            #to be moved. updates variables with position when found.
            for row in range(0, 10):
                for column in range(0, 9):
                    if self._helper_board[row][column] == move_from:
                        self._mf_board_row_m = row
                        self._mf_board_column_m = column

            #iterates through helper board and finds the position the piece
            #will move to. updates variables with position when found.
            for row in range(0, 10):
                for column in range(0, 9):
                    if self._helper_board[row][column] == move_to:
                        self._mt_board_row_m = row
                        self._mt_board_column_m = column



            self._XiangqiGame._mf_board_row = self._mf_board_row_m
            self._XiangqiGame._mf_board_column = self._mf_board_column_m
            self._XiangqiGame._mt_board_row = self._mt_board_row_m
            self._XiangqiGame._mt_board_column = self._mt_board_column_m


            if self.legal(self._mf_board_row_m, self._mf_board_column_m, self._mt_board_row_m, self._mt_board_column_m) == True:

                #updates temp board for general facing general check
                #
                self._XiangqiGame._board_1.temp_update(self._mf_board_row_m, self._mf_board_column_m,
                                                       self._mt_board_row_m,
                                                       self._mt_board_column_m)


                #checks if general will face general
                if self._red_general_column == self._black_general_column:

                    # will check if there are pieces between the intended travel
                    piece_counter = 0
                    for space in range(self._red_general_row + 1, self._black_general_row):

                        if self._XiangqiGame._board_1._temp_board[space][self._black_general_column] != " ":
                            piece_counter += 1

                    # condition if there are no pieces
                    if piece_counter == 0:
                        return False

                    if piece_counter > 0:
                        pass

                # condition for trying to move horizontally
                if self._XiangqiGame._player_1._turn[0] == "b":

                    if self._red_general_column == self._mt_board_column_m:

                        # will check if there are pieces between the intended travel
                        piece_counter = 0
                        for space in range(self._red_general_row + 1, self._black_general_row):

                            if self._XiangqiGame._board_1._board[space][self._mt_board_column_m] != " ":
                                piece_counter += 1

                        # condition if there are no pieces
                        if piece_counter == 0:

                            return False

                        if piece_counter > 0:
                            pass

                # condition for trying to move horizontally
                if self._XiangqiGame._player_1._turn[0] == "r":

                    if self._black_general_column == self._mt_board_column_m:

                        # will check if there are pieces between the intended travel
                        piece_counter = 0
                        for space in range(self._red_general_row + 1, self._black_general_row):

                            if self._XiangqiGame._board_1._board[space][self._mt_board_column_m] != " ":
                                piece_counter += 1

                        # condition if there are no pieces
                        if piece_counter == 0:

                            return False

                        if piece_counter > 0:
                            pass

                self.in_check()
                self._XiangqiGame._board_1.update(self._mf_board_row_m, self._mf_board_column_m, self._mt_board_row_m,
                                                  self._mt_board_column_m)
                self.in_check()





                #updates player turn by setting conditionals to compare game class
                #data member to methd variable
                


                if self._turn_holder == "black":
                    self._XiangqiGame._player_1._turn = "black"
                    self._turn_holder = "red"


                elif self._turn_holder == "red":
                    self._XiangqiGame._player_1._turn = "red"
                    self._turn_holder = "black"




                if self._XiangqiGame._player_1._red_in_check == True:

                    for row in range(0, 10):
                        for column in range(0, 9):

                            if self.general(self._red_general_row, self._red_general_column, row, column) == False:
                                pass



                            if self.general(self._red_general_row, self._red_general_column, row, column) == True:

                                self.moves_left(row, column)
                                if self._moves_left == True:
                                    continue
                                red_move_out_of_check += 1


                    if red_move_out_of_check == 0:
                        self._XiangqiGame._game_state == "BLACK_WON"

                if self._XiangqiGame._player_1._black_in_check == True:

                    for row in range(0, 10):
                        for column in range(0, 9):

                            if self.general(self._black_general_row, self._black_general_column, row, column) == False:

                                pass

                            if self.general(self._black_general_row, self._black_general_column, row, column) == True:

                                self.moves_left(row, column)
                                if self._moves_left == True:
                                    continue
                                black_move_out_of_check += 1

                    if red_move_out_of_check == 0:
                        self._XiangqiGame._game_state == "RED_WON"






                #all condions met and return
                self._XiangqiGame._move_legal = True
                return True


            elif self.legal(self._mf_board_row_m, self._mf_board_column_m, self._mt_board_row_m, self._mt_board_column_m) == False:

                self._XiangqiGame._move_legal = False

                return False

        # program continues to run if invalid position is attempted on board
        # prints error message
        except TypeError:
            print("Invalid space!")


    def legal(self, mf_board_row, mf_board_column, mt_board_row, mt_board_column):

        """
        determines if move is legal
        """

        # iterates through board  and finds the position of the black and red general
        for row in range(0, 10):
            for column in range(0, 9):
                if self._XiangqiGame._board_1._board[row][column] != " ":
                    if self._XiangqiGame._board_1._board[row][column][1] == "g":

                        if self._XiangqiGame._board_1._board[row][column][0] == "r":
                            self._red_general_row = row
                            self._red_general_column = column


                        if self._XiangqiGame._board_1._board[row][column][0] == "b":
                            self._black_general_row = row
                            self._black_general_column = column


        if self._XiangqiGame._game_state == "UNFINISHED" and self._XiangqiGame._player_1._turn[0] == \
                self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][0]:

            if self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][1] == "s":
                return self.soldier(mf_board_row, mf_board_column, mt_board_row, mt_board_column)

            if self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][1] == "c":
                return self.cannon(mf_board_row, mf_board_column, mt_board_row, mt_board_column)

            if self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][1] == "x":
                return self.chariot(mf_board_row, mf_board_column, mt_board_row, mt_board_column)

            if self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][1] == "h":
                return self.horse(mf_board_row, mf_board_column, mt_board_row, mt_board_column)

            if self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][1] == "e":
                return self.elephant(mf_board_row, mf_board_column, mt_board_row, mt_board_column)

            if self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][1] == "a":
                return self.advisor(mf_board_row, mf_board_column, mt_board_row, mt_board_column)

            if self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][1] == "g":
                return self.general(mf_board_row, mf_board_column, mt_board_row, mt_board_column)


    def soldier(self, mf_board_row, mf_board_column, mt_board_row, mt_board_column):
        """
        function that sets the rules for a soldier to move on the board
        """

        #ensures piece to be moved is a soldier & sets the moved to
        #piece owner info to a variable
        if self._XiangqiGame._game_state == "UNFINISHED" and self._XiangqiGame._player_1._turn[0] == \
                self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][0] and \
                self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][1] == "s":

            current_space_player = self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][0]
            next_space_player = self._XiangqiGame._board_1._board[mt_board_row][mt_board_column][0]

            #ensures the soldier will either go into an empty space or the other opponents piece
            if (self._XiangqiGame._player_1._turn[0] != next_space_player)\
                    or (self._XiangqiGame._board_1._board[mt_board_row][mt_board_column] == " "):


                #sets movement rules for red peices
                if current_space_player == "r":

                    if mf_board_row < 5:

                        #ensures the move will only go one space
                        if mt_board_row == (mf_board_row + 1) and mf_board_column == mt_board_column:

                            #all conditions met, move will return true which is legal
                            return True

                    if mf_board_row > 4:

                        #ensures the move will only go one space
                        if (mt_board_row == mf_board_row + 1) or \
                                (mt_board_row == mf_board_row):


                            if (mt_board_column == mf_board_column) or \
                                    (mt_board_column == mf_board_column + 1) or \
                                    (mt_board_column == mf_board_column - 1):


                                #all conditions met, move will return true which is legal
                                return True



                #sets movement rules for black pieces
                if current_space_player == "b":

                    if mf_board_row > 4:

                        # ensures the move will only go one space
                        if mt_board_row == (mf_board_row - 1) and mf_board_column == mt_board_column:
                            # all conditions met, move will return true which is legal
                            return True

                    if mf_board_row < 5:


                        # ensures the move will only go one space
                        if (mt_board_row == mf_board_row - 1) or \
                                (mt_board_row == mf_board_row):


                            if (mt_board_column == mf_board_column) or \
                                    (mt_board_column == mf_board_column + 1) or \
                                    (mt_board_column == mf_board_column - 1):


                                # all conditions met, move will return true which is legal
                                return True



    def cannon(self, mf_board_row, mf_board_column, mt_board_row, mt_board_column):
        """
        function that sets the rules for a cannon to move on the board
        """

        # ensures piece to be moved is a cannon & sets piece owner info to variables
        if self._XiangqiGame._game_state == "UNFINISHED" and self._XiangqiGame._player_1._turn[0] == \
                self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][0] and \
                self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][1] == "c":
            current_space_player = self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][0]
            next_space_player = self._XiangqiGame._board_1._board[mt_board_row][mt_board_column][0]

            # ensures the cannon will either go into an empty space or the other opponents piece
            if (self._XiangqiGame._player_1._turn[0] != next_space_player) \
                    or (self._XiangqiGame._board_1._board[mt_board_row][mt_board_column] == " "):


                # sets movement rules for red pieces and black pieces
                if current_space_player == "r" or current_space_player == "b":

                    #condition for trying to move vertically
                    if mt_board_row == mf_board_row:

                        #if moving vertically down
                        if mt_board_column < mf_board_column:

                            # will check if there are pieces between the intended travel
                            piece_counter = 0
                            for space in range(mt_board_column + 1, mf_board_column):

                                if self._XiangqiGame._board_1._board[mf_board_row][space] != " ":
                                    piece_counter += 1

                        # if moving vertically up
                        if mt_board_column >= mf_board_column:

                            # will check if there are pieces between the intended travel
                            piece_counter = 0
                            for space in range(mf_board_column + 1, mt_board_column):

                                if self._XiangqiGame._board_1._board[mf_board_row][space] != " ":
                                    piece_counter += 1


                        # condition if there are no pieces
                        if piece_counter == 0:

                            # if no piece, allowed to move to empty spot
                            if self._XiangqiGame._board_1._board[mt_board_row][mt_board_column] == " ":
                                return True

                            # if piece exist at destination not allowed to move b/c no pieces between
                            if self._XiangqiGame._board_1._board[mt_board_row][mt_board_column] != " ":
                                return False

                        # condition that allows piece to take another piece b/c piece between
                        if piece_counter == 1:

                            # if piece at destination, allowed to move to capture piece
                            if self._XiangqiGame._board_1._board[mt_board_row][mt_board_column] != " ":
                                    return True

                            # if piece between exists, not allowed to move to empty spot
                            if self._XiangqiGame._board_1._board[mt_board_row][mt_board_column] == " ":
                                    return False

                        # can't move beyond one piece
                        if piece_counter > 1:
                            return False

                    # condition for trying to move horizontally
                    if mt_board_column == mf_board_column:

                        # if the piece is trying to move horizontally to left
                        if mt_board_row < mf_board_row:

                            # will check if there are pieces between the intended travel
                            piece_counter = 0
                            for space in range(mt_board_row+1, mf_board_row):

                                if self._XiangqiGame._board_1._board[space][mt_board_column] != " ":
                                    piece_counter += 1


                        #if the piece is trying to move horizonatally to right
                        if mt_board_row >= mf_board_row:

                            #will check if there are pieces between the intended travel
                            piece_counter = 0
                            for space in range(mf_board_row + 1, mt_board_row):

                                if self._XiangqiGame._board_1._board[space][mt_board_column] != " ":
                                    piece_counter += 1


                        #condition if there are no pieces
                        if piece_counter == 0:

                            #if no piece, allowed to move to empty spot
                            if self._XiangqiGame._board_1._board[mt_board_row][mt_board_column] == " ":
                                return True

                            #if piece exist at destination not allowed to move b/c no pieces between
                            if self._XiangqiGame._board_1._board[mt_board_row][mt_board_column] != " ":
                                return False

                        #condition that allows piece to take another piece b/c piece between
                        if piece_counter == 1:

                            # if piece at destination, allowed to move to capture piece
                            if self._XiangqiGame._board_1._board[mt_board_row][mt_board_column] != " ":
                                return True

                            # if piece between exists, not allowed to move to empty spot
                            if self._XiangqiGame._board_1._board[mt_board_row][mt_board_column] == " ":
                                return False

                        #can't move beyond one piece
                        if piece_counter > 1:
                            return False



    def chariot(self, mf_board_row, mf_board_column, mt_board_row, mt_board_column):
        """
        function that sets rules for chariot to move
        """

        # ensures piece to be moved is a chariot & sets piece owner info to variables
        if self._XiangqiGame._game_state == "UNFINISHED" and self._XiangqiGame._player_1._turn[0] == \
                self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][0] and \
                self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][1] == "x":
            current_space_player = self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][0]
            next_space_player = self._XiangqiGame._board_1._board[mt_board_row][mt_board_column][0]

            # ensures the chariot will either go into an empty space or the other opponents piece
            if (self._XiangqiGame._player_1._turn[0] != next_space_player) \
                    or (self._XiangqiGame._board_1._board[mt_board_row][mt_board_column] == " "):

                # sets movement rules for red pieces and black pieces
                if current_space_player == "r" or current_space_player == "b":

                    # condition for trying to move vertically
                    if mt_board_row == mf_board_row:

                        # if moving vertically down
                        if mt_board_column < mf_board_column:

                            # will check if there are pieces between the intended travel
                            piece_counter = 0
                            for space in range(mt_board_column + 1, mf_board_column):

                                if self._XiangqiGame._board_1._board[mf_board_row][space] != " ":
                                    piece_counter += 1

                        # if moving vertically up
                        if mt_board_column >= mf_board_column:

                            # will check if there are pieces between the intended travel
                            piece_counter = 0
                            for space in range(mf_board_column + 1, mt_board_column):

                                if self._XiangqiGame._board_1._board[mf_board_row][space] != " ":
                                    piece_counter += 1

                        # condition if there are no pieces
                        if piece_counter == 0:

                            # if no piece, allowed to move to empty spot
                            if self._XiangqiGame._board_1._board[mt_board_row][mt_board_column] == " ":
                                return True

                            # if piece exist at destination not allowed to move b/c no pieces between
                            if self._XiangqiGame._board_1._board[mt_board_row][mt_board_column] != " ":
                                return True

                            else:
                                return False

                        # condition that allows piece to take another piece b/c piece between
                        if piece_counter >= 1:

                            return False


                    # condition for trying to move horizontally
                    if mt_board_column == mf_board_column:

                        # if the piece is trying to move horizontally to left
                        if mt_board_row < mf_board_row:

                            # will check if there are pieces between the intended travel
                            piece_counter = 0
                            for space in range(mt_board_row + 1, mf_board_row):

                                if self._XiangqiGame._board_1._board[space][mt_board_column] != " ":
                                    piece_counter += 1

                        # if the piece is trying to move horizonatally to right
                        if mt_board_row >= mf_board_row:

                            # will check if there are pieces between the intended travel
                            piece_counter = 0
                            for space in range(mf_board_row + 1, mt_board_row):

                                if self._XiangqiGame._board_1._board[space][mt_board_column] != " ":
                                    piece_counter += 1

                        # condition if there are no pieces
                        if piece_counter == 0:

                            # if no piece, allowed to move to empty spot
                            if self._XiangqiGame._board_1._board[mt_board_row][mt_board_column] == " ":
                                return True

                            # if piece exist at destination not allowed to move b/c no pieces between
                            if self._XiangqiGame._board_1._board[mt_board_row][mt_board_column] != " ":
                                return True

                        # condition that allows piece to take another piece b/c piece between
                        if piece_counter >= 1:

                            return False



    def horse(self, mf_board_row, mf_board_column, mt_board_row, mt_board_column):
        """
        function that sets rules for horse to move
        """


        # ensures piece to be moved is a horse & sets piece owner info to variables
        if self._XiangqiGame._game_state == "UNFINISHED" and self._XiangqiGame._player_1._turn[0] == \
                self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][0] and \
                self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][1] == "h":
            current_space_player = self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][0]
            next_space_player = self._XiangqiGame._board_1._board[mt_board_row][mt_board_column][0]


            # ensures the chariot will either go into an empty space or the other opponents piece
            if (self._XiangqiGame._player_1._turn[0] != next_space_player) \
                    or (self._XiangqiGame._board_1._board[mt_board_row][mt_board_column] == " "):


                # sets movement rules for red pieces and black pieces
                if current_space_player == "r" or current_space_player == "b":


                    #up left
                    if (mt_board_row == mf_board_row - 2) and (mt_board_column == mf_board_column - 1):


                        if self._XiangqiGame._board_1._board[mf_board_row - 1][mf_board_column] != " ":
                            return False

                        else:
                            return True

                    #up right
                    if (mt_board_row == mf_board_row - 2) and (mt_board_column == mf_board_column + 1):

                        if self._XiangqiGame._board_1._board[mf_board_row - 1][mf_board_column] != " ":
                            return False

                        else:
                            return True

                    #left up

                    if (mt_board_row == mf_board_row - 1) and (mt_board_column == mf_board_column - 2):



                        if self._XiangqiGame._board_1._board[mf_board_row][mf_board_column - 1] != " ":
                            return False

                        else:
                            return True

                    #left down

                    if (mt_board_row == mf_board_row + 1) and (mt_board_column == mf_board_column - 2):

                        if self._XiangqiGame._board_1._board[mf_board_row][mf_board_column - 1] != " ":
                            return False

                        else:
                            return True

                    #down left
                    if (mt_board_row == mf_board_row + 2) and (mt_board_column == mf_board_column - 1):

                        if self._XiangqiGame._board_1._board[mf_board_row+1][mf_board_column] != " ":
                            return False

                        else:
                            return True

                    #down right
                    if (mt_board_row == mf_board_row + 2) and (mt_board_column == mf_board_column + 1):

                        if self._XiangqiGame._board_1._board[mf_board_row + 1][mf_board_column] != " ":
                            return False

                        else:
                            return True

                    #right up
                    if (mt_board_row == mf_board_row - 1) and (mt_board_column == mf_board_column + 2):


                        if self._XiangqiGame._board_1._board[mf_board_row][mf_board_column + 1] != " ":
                            return False

                        else:
                            return True

                    #right down
                    if (mt_board_row == mf_board_row + 1) and (mt_board_column == mf_board_column + 2):

                        if self._XiangqiGame._board_1._board[mf_board_row][mf_board_column + 1] != " ":
                            return False

                        else:
                            return True




    def elephant(self, mf_board_row, mf_board_column, mt_board_row, mt_board_column):
        """
        function that sets rules for elephant to move
        """


        #ensures piece to be moved is a elephant & sets piece owner info to variables
        if self._XiangqiGame._game_state == "UNFINISHED" and self._XiangqiGame._player_1._turn[0] == \
                self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][0] and \
                self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][1] == "e":

            current_space_player = self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][0]
            next_space_player = self._XiangqiGame._board_1._board[mt_board_row][mt_board_column][0]


            #ensures the elephant will either go into an empty space or the other opponents piece
            if (self._XiangqiGame._player_1._turn[0] != next_space_player) \
                    or (self._XiangqiGame._board_1._board[mt_board_row][mt_board_column] == " "):


                #stops elephant from being on wrong sid of board for red piece
                if current_space_player == "r" and mt_board_row > 4:

                    return False

                # stops elephant from being on wrong sid of board for black piece
                if current_space_player == "b" and mt_board_row < 5:

                    return False

                # up diagonal left
                if (mt_board_row == mf_board_row - 2) and (mt_board_column == mf_board_column - 2):


                    if self._XiangqiGame._board_1._board[mf_board_row - 1][mf_board_column - 1] != " ":
                        return False

                    else:
                        return True

                # up diagonal right
                if (mt_board_row == mf_board_row - 2) and (mt_board_column == mf_board_column + 2):


                    if self._XiangqiGame._board_1._board[mf_board_row - 1][mf_board_column + 1] != " ":
                        return False

                    else:
                        return True

                # down diagonal left
                if (mt_board_row == mf_board_row + 2) and (mt_board_column == mf_board_column - 2):


                    if self._XiangqiGame._board_1._board[mf_board_row + 1][mf_board_column - 1] != " ":
                        return False

                    else:
                        return True

                # down diagonal right
                if (mt_board_row == mf_board_row + 2) and (mt_board_column == mf_board_column + 2):

                    if self._XiangqiGame._board_1._board[mf_board_row + 1][mf_board_column + 1] != " ":
                        return False

                    else:
                        return True






    def advisor(self, mf_board_row, mf_board_column, mt_board_row, mt_board_column):
        """
        function that sets rules for advisor to move
        """

        # ensures piece to be moved is a advisor & sets piece owner info to variables
        if self._XiangqiGame._game_state == "UNFINISHED" and self._XiangqiGame._player_1._turn[0] == \
                self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][0] and \
                self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][1] == "a":
            current_space_player = self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][0]
            next_space_player = self._XiangqiGame._board_1._board[mt_board_row][mt_board_column][0]


            # ensures the advisor will either go into an empty space or the other opponents piece
            if (self._XiangqiGame._player_1._turn[0] != next_space_player) \
                    or (self._XiangqiGame._board_1._board[mt_board_row][mt_board_column] == " "):

                # stops advisor from moving outside specified area
                if current_space_player == "r":


                    if mt_board_column < 3 or mt_board_column > 6 or mt_board_row > 2:


                            return False

                    # ensures the move will only go one space
                    if mt_board_row == (mf_board_row + 1) and mt_board_column == (mf_board_column + 1):
                        return True

                    if mt_board_row == (mf_board_row + 1) and mt_board_column == (mf_board_column - 1):
                        return True

                    if mt_board_row == (mf_board_row - 1) and mt_board_column == (mf_board_column + 1):
                        return True

                    if mt_board_row == (mf_board_row - 1) and mt_board_column == (mf_board_column - 1):
                        return True



                # stops advisor from moving outside specified area
                if current_space_player == "b":


                    if mt_board_column < 3 or mt_board_column > 6 or mt_board_row < 7:

                        return False

                            # ensures the move will only go one space
                    if mt_board_row == (mf_board_row + 1) and mt_board_column == (mf_board_column + 1):
                        return True

                    if mt_board_row == (mf_board_row + 1) and mt_board_column == (mf_board_column - 1):
                        return True

                    if mt_board_row == (mf_board_row - 1) and mt_board_column == (mf_board_column + 1):
                        return True

                    if mt_board_row == (mf_board_row - 1) and mt_board_column == (mf_board_column - 1):
                        return True


    def general(self, mf_board_row, mf_board_column, mt_board_row, mt_board_column):
        """
        function that sets rules for general to move
        """

        # ensures piece to be moved is a general & sets piece owner info to variables
        if self._XiangqiGame._game_state == "UNFINISHED" and self._XiangqiGame._player_1._turn[0] == \
                self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][0] and \
                self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][1] == "g":


            current_space_player = self._XiangqiGame._board_1._board[mf_board_row][mf_board_column][0]
            next_space_player = self._XiangqiGame._board_1._board[mt_board_row][mt_board_column][0]

            # ensures the general will either go into an empty space or the other opponents piece
            if (self._XiangqiGame._player_1._turn[0] != next_space_player) \
                    or (self._XiangqiGame._board_1._board[mt_board_row][mt_board_column] == " "):


                # stops general from moving outside specified area
                if current_space_player == "r":

                    if mt_board_column < 3 or mt_board_column > 6 or mt_board_row > 2:
                        return False

                    # ensures the move will only go one space
                    if mt_board_row == (mf_board_row + 1) and mt_board_column == mf_board_column:
                        return True

                    if mt_board_row == mf_board_row  and mt_board_column == (mf_board_column + 1):
                        return True

                    if mt_board_row == (mf_board_row - 1) and mt_board_column == mf_board_column:
                        return True

                    if mt_board_row == mf_board_row and mt_board_column == (mf_board_column - 1):
                        return True


                # stops advisor from moving outside specified area
                if current_space_player == "b":



                    if mt_board_column < 3 or mt_board_column > 6 or mt_board_row < 7:
                        return False

                    # ensures the move will only go one space
                    if mt_board_row == (mf_board_row + 1) and mt_board_column == mf_board_column:
                        return True

                    if mt_board_row == mf_board_row and mt_board_column == (mf_board_column + 1):
                        return True

                    if mt_board_row == (mf_board_row - 1) and mt_board_column == mf_board_column:
                        return True

                    if mt_board_row == mf_board_row and mt_board_column == (mf_board_column - 1):
                        return True



    def in_check(self):

        for row in range(0, 10):
            for column in range(0, 9):


                if self._XiangqiGame._board_1._board[row][column] != " ":

                    if self._XiangqiGame._board_1._board[row][column][0] == "r":

                        if self._XiangqiGame._board_1._board[row][column][1] == "s":

                            if self.soldier(row, column, self._XiangqiGame._move_1._black_general_row,
                                          self._XiangqiGame._move_1._black_general_column) == True:

                                self._black_soldier_check_row = row
                                self._black_soldier_check_column = column
                                self._XiangqiGame._player_1._black_in_check = True

                        if self._XiangqiGame._board_1._board[row][column][1] == "c":

                            if self.cannon(row, column, self._XiangqiGame._move_1._black_general_row,
                                          self._XiangqiGame._move_1._black_general_column) == True:

                                self._black_cannon_check_row = row
                                self._black_cannon_check_column = column
                                self._XiangqiGame._player_1._black_in_check = True

                        if self._XiangqiGame._board_1._board[row][column][1] == "x":


                            if self.chariot(row, column, self._XiangqiGame._move_1._black_general_row,
                                          self._XiangqiGame._move_1._black_general_column) == True:


                                self._XiangqiGame._player_1._black_in_check = True

                        if self._XiangqiGame._board_1._board[row][column][1] == "h":

                            if self.horse(row, column, self._XiangqiGame._move_1._black_general_row,
                                          self._XiangqiGame._move_1._black_general_column) == True:


                                self._XiangqiGame._player_1._black_in_check = True

                        if self._XiangqiGame._board_1._board[row][column][1] == "e":

                            if self.elephant(row, column, self._XiangqiGame._move_1._black_general_row,
                                          self._XiangqiGame._move_1._black_general_column) == True:

                                self._XiangqiGame._player_1._black_in_check = True


                if self._XiangqiGame._board_1._board[row][column] != " ":
                    if self._XiangqiGame._board_1._board[row][column][0] == "b":

                        if self._XiangqiGame._board_1._board[row][column][1] == "s":

                            if self.soldier(row, column, self._XiangqiGame._move_1._red_general_row,
                                          self._XiangqiGame._move_1._red_general_column) == True:


                                self._XiangqiGame._player_1._red_in_check = True

                        if self._XiangqiGame._board_1._board[row][column][1] == "c":

                            if self.cannon(row, column, self._XiangqiGame._move_1._red_general_row,
                                          self._XiangqiGame._move_1._red_general_column) == True:


                                self._XiangqiGame._player_1._red_in_check = True

                        if self._XiangqiGame._board_1._board[row][column][1] == "x":

                            if self.chariot(row, column, self._XiangqiGame._move_1._red_general_row,
                                          self._XiangqiGame._move_1._red_general_column) == True:


                                self._XiangqiGame._player_1._red_in_check = True

                        if self._XiangqiGame._board_1._board[row][column][1] == "h":

                            if self.horse(row, column, self._XiangqiGame._move_1._red_general_row,
                                          self._XiangqiGame._move_1._red_general_column) == True:


                                self._XiangqiGame._player_1._red_in_check = True

                        if self._XiangqiGame._board_1._board[row][column][1] == "e":

                            if self.elephant(row, column, self._XiangqiGame._move_1._red_general_row,
                                          self._XiangqiGame._move_1._red_general_column) == True:


                                self._XiangqiGame._player_1._red_in_check = True

    def moves_left(self, row, column):

        self._XiangqiGame._move_1._moves_left = False

        for sub_row in range(0, 10):
            for sub_column in range(0, 9):


                if self._XiangqiGame._board_1._board[sub_row][sub_column] != " ":

                    if self._XiangqiGame._board_1._board[sub_row][sub_column][0] == "r":

                        if self._XiangqiGame._board_1._board[sub_row][sub_column][1] == "s":

                            if self.soldier(sub_row, sub_column, row, column) == True:

                                self._XiangqiGame._move_1._moves_left = True

                        if self._XiangqiGame._board_1._board[sub_row][sub_column][1] == "c":

                            if self.cannon(sub_row, sub_column, row, column) == True:

                                self._XiangqiGame._move_1._moves_left = True

                        if self._XiangqiGame._board_1._board[sub_row][sub_column][1] == "x":

                            if self.chariot(sub_row, sub_column, row, column) == True:

                                self._XiangqiGame._move_1._moves_left = True

                        if self._XiangqiGame._board_1._board[sub_row][sub_column][1] == "h":

                            if self.horse(sub_row, sub_column, row, column) == True:

                                self._XiangqiGame._move_1._moves_left = True

                        if self._XiangqiGame._board_1._board[sub_row][sub_column][1] == "e":

                            if self.elephant(sub_row, sub_column, row, column) == True:

                                self._XiangqiGame._move_1._moves_left = True



                if self._XiangqiGame._board_1._board[sub_row][sub_column] != " ":
                    if self._XiangqiGame._board_1._board[sub_row][sub_column][0] == "b":

                        if self._XiangqiGame._board_1._board[sub_row][sub_column][1] == "s":

                            if self.soldier(sub_row, sub_column, row, column) == True:

                                self._XiangqiGame._move_1._moves_left = True

                        if self._XiangqiGame._board_1._board[sub_row][sub_column][1] == "c":

                            if self.cannon(sub_row, sub_column, row, column) == True:

                                self._XiangqiGame._move_1._moves_left = True

                        if self._XiangqiGame._board_1._board[sub_row][sub_column][1] == "x":

                            if self.chariot(sub_row, sub_column, row, column) == True:

                                self._XiangqiGame._move_1._moves_left = True

                        if self._XiangqiGame._board_1._board[sub_row][sub_column][1] == "h":

                            if self.horse(sub_row, sub_column, row, column) == True:

                                self._XiangqiGame._move_1._moves_left = True

                        if self._XiangqiGame._board_1._board[sub_row][sub_column][1] == "e":

                            if self.elephant(sub_row, sub_column, row, column) == True:

                                self._XiangqiGame._move_1._moves_left = True

game = XiangqiGame()
game.make_move("a4","a5")

game.make_move("c7","c6")

game.make_move("a5", "a6")

game.make_move("c6", "c5")

game.make_move("a6", "a7")

game.make_move("c5", "c4")

game.make_move("a7", "a8")

game.make_move("c4", "c3")

game.make_move("a8", "a9")

game.make_move("c3", "c2")

game.make_move("a9", "a10")

game.make_move("c2", "c1")

game.make_move("a10", "b10")

game.make_move("c1", "d1")
