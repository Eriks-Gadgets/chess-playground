#import PySimpleGUI as sg

#sg.Popup("CHESS PLAYGROUND")

print("chess playground log")   

#Class "Chess Piece" defines a list of black rooks and a list of white rooks, as well as a dictionary {ALL PIECES}

class Chess_Piece:
  	
    all_pieces = {} #{Piece Name:Piece Position}
    
    black_rook_list = ["1","2","3","4","5","6","7","8","9","10"] #A list of the maximum number of black rooks
    
    white_rook_list = ["1","2","3","4","5","6","7","8","9","10"] #A list of the maximum number of white rooks
    

#Used for configuring how the rook piece works  

class Rook(Chess_Piece): #Class ROOK
  	
    def __init__(self, col_x, col_y, color): #The Constructor for the Rook Class
      	
        self.color = color #Will either be White or Black
        
        self.pos = str(col_x) + str(col_y) #The Position of the Rook
        
        self.col_x = col_x #col_x and col_y are used for positioning
        
        self.col_y = col_y #These are now attributes of the Rook Object / Rook Class
        
        legal_moves = [] #The Creation of a List '[]' that would be filled of all of the legal moves of the Rook
        
        columns = 8 #The Columns on the Board
        
        columns2 = ["A","B","C","D","E","F","G","H"] #What they are referred to
        
        rows2 = [1,2,3,4,5,6,7,8] #What the Rows on the board are referred to
        
        rows = 8 #No. of Rows
        
        if col_x in columns2: #If the variable col_x is in the list of column references
          	
            for i in columns2: #For each item in columns2
              	
                if i == col_x: #If the item is the same as col_x
                  	
                    legal_column = i #My Legal Column is I
        
        #This Code does the exact thing shown above
        if col_y in rows2:
            for i in rows2:
                if i == col_y: #col_y is ROWS, while col_x is COLUMNS
                    legal_row = i
                    
        #initializing the piece, globally
        
        if self.color == "Black": #If the Color is Black
          	
            self.all_pieces[self.color + "Rook" + self.black_rook_list[0]] = self.pos #BlackRook[N], Where N refers to the first value in the Black_Rook_List.
            
            self.global_name = self.color + "Rook" + self.black_rook_list[0] #Sets the attribute 'Global_Name' to BlackRook[N], Where N refers to the first value in the Black_Rook_List.
            
            del self.black_rook_list[0] #Deletes the first item in black_rook_list, because it has been used.
            
        elif self.color == "White": #Otherwise, if the color is White (ignores special cases [e.g. Red, Orange, Green, Purple, Yellow])
          	#Does the exact same thing as shown above, only using replacing references of 'BLACK' with 'WHITE'.
            self.all_pieces[self.color + "Rook" + self.white_rook_list[0]] = self.pos #WhiteRook[N], Where N refers to the first value in the White_Rook_List.
            self.global_name = self.color + "Rook" + self.white_rook_list[0] #Sets the attribute 'Global_Name' to WhiteRook[N], Where N refers to the first value in the White_Rook_List.
            del self.white_rook_list[0] #Deletes the first item in white_rook_list, because it has been used.
            
        #legalizing all columns + rows
        pos_x = -1 #Set to Negative One, because the first thing it will do is add one (0)
        
        pos_y = -1 #Same reason as shown above.
        
        for i in rows2: #For each item in Rows (what it is referred to),
          	
            pos_x += 1 #Adds one to pos_x [you'll see why]
            
            legal_moves.append(str(legal_column) + str(rows2[pos_x])) #e.g. if pos is B8, this would append 'B', which is the legal column- and rows2(0), which is 1. B1.
            
        for i in columns2: #Does a similar thing as shown above.
            pos_y += 1
            legal_moves.append(str(columns2[pos_y]) + str(legal_row)) #Columns2[POS_Y] is basically Columns2[0] (for instance), which can be A, and str(legal_row), which can be 8. A8.
        
        pos = 0 #Sets the position variable to 0.
        
        for i in legal_moves: #For each item in the legal moves list,
          	
            if i in self.all_pieces.values() and i != self.pos: #If the item is the position of a different chess piece AND isn't theh position of the object,
              	
                legal_moves[pos] = str(legal_moves[pos][0]) + "x" + str(legal_moves[pos][1]) #Sets the move (B4), for example, to Bx4 [Takes on B4]
                
            else: #Otherwise
              	
                pos += 1 #Add one to the position variable
                
        self.legal_moves = legal_moves #Sets the object's attribute to legal_moves
        
        pos = 0 #ONCE AGAIN, resets the position
        
        for i in self.legal_moves: #for each item in the legal moves attribute
          	
            if i == self.pos: #If the ITEM is equal to self.pos
              	
                del self.legal_moves[pos] #deletes that position
                pos += 1 #adds one
                continue #moves on
                
            else:
                pos += 1 #adds one
                
    #Updating Legal Moves [Refer to lines 32 through line 113]          
    def legal_move_update(self):
        col_x, col_y = self.col_x, self.col_y #Refreshed COL_X and COL_Y
        legal_moves = [] #Reset Legal Moves
        columns = 8 
        columns2 = ["A","B","C","D","E","F","G","H"]
        rows2 = [1,2,3,4,5,6,7,8]
        rows = 8
        
        #determining if a column or row is legal?
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
                for j in self.all_pieces:
                    if self.all_pieces[j] == i:
                        if self.color in j:
                            pass
                          	#adds an X to moves that can take a piece
                        else:
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
       #allows a chess peice to move by changing its location    
    def move(self, x, y):
      	
        pos = str(x) + str(y) #The new position is made.
        
        previous_x = self.col_x #Backups of col_x and col_y
        previous_y = self.col_y
        
        self.col_x = x #Replaces them with x and y
        self.col_y = y
        
        #check if move is possible
        if pos in self.legal_moves: #If the new pos is in legal moves
          
            del previous_x #Deletes the backups
            del previous_y
            
            self.all_pieces[self.global_name] = pos #Updates the global position
            
            self.pos = pos #Updates self.pos
            
            self.legal_move_update() #Updates legal mvoes
            
        else: #Else
          	
            self.col_x = previous_x #Restores the backups of X and Y
            self.col_y = previous_y
            
            print("Illegal Move") #Reminds you that you commited a crime
            

#Create scenarios down here!            
rook1 = Rook("B", 3, "White")
rook2 = Rook("C", 3, "White")
rook3 = Rook("F", 3, "White")
rook1.legal_move_update()
rook2.legal_move_update()
rook3.legal_move_update()
print(rook1.all_pieces)
print(rook1.global_name, rook1.pos, rook1.legal_moves)
rook1.move("B",7)
print(rook1.global_name, rook1.pos, rook1.legal_moves)
