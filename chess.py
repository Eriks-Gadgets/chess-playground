import PySimpleGUI as sg

#sg.Popup("CHESS PLAYGROUND")

print("chess playground log")   

class Chess_Piece:
    all_pieces = {} #{Piece Name:Piece Position}
    black_rook_list = ["1","2","3","4","5","6","7","8","9","10"]
    white_rook_list = ["1","2","3","4","5","6","7","8","9","10"]
class Rook(Chess_Piece):
    def __init__(self, col_x, col_y, color):
        self.color = color
        self.pos = str(col_x) + str(col_y)
        self.col_x = col_x
        self.col_y = col_y
        legal_moves = []
        columns = 8
        columns2 = ["A","B","C","D","E","F","G","H"]
        rows2 = [1,2,3,4,5,6,7,8]
        rows = 8
        if col_x in columns2:
            for i in columns2:
                if i == col_x:
                    legal_column = i
        if col_y in rows2:
            for i in rows2:
                if i == col_y:
                    legal_row = i
        #initializing the piece, globally
        if self.color + "Rook" + self.black_rook_list[0] in self.all_pieces:
            pass
        else:
            if self.color == "Black":
                self.all_pieces[self.color + "Rook" + self.black_rook_list[0]] = self.pos
                self.global_name = self.color + "Rook" + self.black_rook_list[0]
                del self.black_rook_list[0]
            elif self.color == "White":
                self.all_pieces[self.color + "Rook" + self.white_rook_list[0]] = self.pos
                self.global_name = self.color + "Rook" + self.white_rook_list[0]
                del self.white_rook_list[0]
            
        #legalizing all columns + rows
        pos_x = -1
        pos_y = -1
        for i in rows2:
            pos_x += 1
            legal_moves.append(str(legal_column) + str(rows2[pos_x]))
        for i in columns2:
            pos_y += 1
            legal_moves.append(str(columns2[pos_y]) + str(legal_row))
        pos = 0
        for i in legal_moves:
            if i in self.all_pieces.values() and i != self.pos:
                legal_moves[pos] = str(legal_moves[pos][0]) + "x" + str(legal_moves[pos][1])
            else:
                pos += 1
        self.legal_moves = legal_moves
        pos = 0
        for i in self.legal_moves:
            if i == self.pos:
                del self.legal_moves[pos]
                pos += 1
                continue
            else:
                pos += 1
    def legal_move_update(self):
        col_x, col_y = self.col_x, self.col_y #Refreshed COL_X and COL_Y
        legal_moves = [] #Reset Legal Moves
        columns = 8
        columns2 = ["A","B","C","D","E","F","G","H"]
        rows2 = [1,2,3,4,5,6,7,8]
        rows = 8
        if col_x in columns2:
            for i in columns2:
                if i == col_x:
                    legal_column = i
        if col_y in rows2:
            for i in rows2:
                if i == col_y:
                    legal_row = i
        #legalizing all columns + rows
        pos_x = -1
        pos_y = -1
        for i in rows2:
            pos_x += 1
            legal_moves.append(str(legal_column) + str(rows2[pos_x]))
        for i in columns2:
            pos_y += 1
            legal_moves.append(str(columns2[pos_y]) + str(legal_row))
        pos = 0
        for i in legal_moves:
            if i in self.all_pieces.values() and i != self.pos:
                legal_moves[pos] = str(legal_moves[pos][0]) + "x" + str(legal_moves[pos][1])
            else:
                pos += 1
        self.legal_moves = legal_moves
        pos = 0
        for i in self.legal_moves:
            if i == self.pos:
                del self.legal_moves[pos]
                pos += 1
                continue
            else:
                pos += 1
            #This works well! :D
    def move(self, x, y):
        pos = str(x) + str(y)
        previous_x = self.col_x
        previous_y = self.col_y
        self.col_x = x
        self.col_y = y
        self.legal_move_update()
        if pos in self.legal_moves:
            del previous_x
            del previous_y
            self.all_pieces[self.global_name] = pos
            self.pos = pos
            self.legal_move_update()
        else:
            self.col_x = previous_x
            self.col_y = previous_y
            print("Illegal Move")
rook_test_mark = Rook("B", 3, "Black")
rook_test_mark2 = Rook("C", 3, "White")
rook_test_mark.legal_move_update()
rook_test_mark.legal_move_update()
print(rook_test_mark.global_name, rook_test_mark.pos, rook_test_mark.legal_moves)
rook_test_mark.move("D",4)
rook_test_mark.move("B",6)
print(rook_test_mark.all_pieces)
print(rook_test_mark.global_name, rook_test_mark.pos, rook_test_mark.legal_moves)
