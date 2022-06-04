
class Board:
    def __init__(self):
        board_lst = []
        for y in range(8):
            temp_row = []
            for x in range(8):
                temp_row.append('o')
            board_lst.append(temp_row)
        self.board = board_lst    
        self.board[3][3] = 'B'
        self.board[3][4] = 'W'
        self.board[4][3] = 'W'
        self.board[4][4] = 'B'             
        
    def __repr__(self):
        '''
        Returns a string representation of self
        
        __repr__: Board -> Str
        '''  
        s = "    0    1    2    3    4    5    6    7\n"
        s += "0 {0.board[0]}\n1 {0.board[1]}\n2 {0.board[2]}\n3 {0.board[3]}\n4 {0.board[4]}\n5 {0.board[5]}\n6 {0.board[6]}\n7 {0.board[7]}\n"
        return s.format(self) 
    
    def get_score(self):
        score = [0,0]
        for row in self.board:
            for item in row:
                if item == "B":
                    score[0] += 1
                elif item == "W":
                    score[1] += 1
        return score
    
    ############################################################################
      
    def get_left_ind(self, cur_player, row_num, col_num):
        row_list = self.board[row_num]
        if (col_num > 0) and \
           ((row_list[col_num - 1] == cur_player) or (row_list[col_num - 1] == "o")):
            return None
        for ind in range(1, col_num + 1):
            cur_pos = col_num - ind
            if row_list[cur_pos] == "o":
                return None            
            elif row_list[cur_pos] == cur_player:
                return cur_pos
    
    def insert_hor_ind_left(self, cur_player, row_num, col_num, ind):
        row_list = self.board[row_num]
        for x in range(col_num - ind):
            row_list[col_num - x] = cur_player
        return self.board
    
    
    #######
    
    def get_right_ind(self, cur_player, row_num, col_num):
        row_list = self.board[row_num]
        if (col_num < 7) and \
           ((row_list[col_num + 1] == cur_player) or (row_list[col_num + 1] == "o")):
            return None
        for ind in range(1, 8 - col_num):
            cur_pos = col_num + ind
            if row_list[cur_pos] == "o":
                return None            
            elif row_list[cur_pos] == cur_player:
                return cur_pos
        
    def insert_hor_ind_right(self, cur_player, row_num, col_num, ind):
        row_list = self.board[row_num]
        for x in range(ind - col_num):
            row_list[col_num + x] = cur_player
        return self.board
    
    #######
    
    def get_down_ind(self, cur_player, row_num, col_num):
        if (row_num < 7) and \
           ((self.board[row_num + 1][col_num] == cur_player) or (self.board[row_num + 1][col_num] == "o")):
            return None
        for x in range(1, 8-row_num):
            ind = row_num + x
            if self.board[ind][col_num] == "o":
                return None            
            elif self.board[ind][col_num] == cur_player:
                return ind
    
    def insert_ver_ind_down(self, cur_player, row_num, col_num, ind):
        for x in range(ind-row_num):
            self.board[row_num + x][col_num] = cur_player
        return self.board  
    
    #######
    
    def get_up_ind(self, cur_player, row_num, col_num):
        if (row_num > 0) and \
           ((self.board[row_num - 1][col_num] == cur_player) or (self.board[row_num - 1][col_num] == "o")):
            return None
        for x in range(1, row_num + 1):
            ind = row_num - x
            if self.board[ind][col_num] == "o":
                return None            
            elif self.board[ind][col_num] == cur_player:
                return ind
    
    def insert_ver_ind_up(self, cur_player, row_num, col_num, ind):
        for x in range(row_num-ind):
            self.board[row_num - x][col_num] = cur_player
        return self.board  
    
    #######
    
    def get_diag1_ind(self, cur_player, row_num, col_num):
        if (col_num < 7) and (row_num > 0) and \
           ((self.board[row_num - 1][col_num + 1] == cur_player) or (self.board[row_num - 1][col_num + 1] == "o")):
            return None
        counter = 1
        while (row_num > 0) and (col_num < 7):
            if self.board[row_num - counter][col_num + counter] == "o":
                return None
            elif self.board[row_num - counter][col_num + counter] == cur_player:
                return [row_num - counter, col_num + counter]
            row_num -= 1
            col_num += 1
    
    def insert_diag_ind_1(self, cur_player, row_num, col_num, col_ind):
        for x in range(col_ind - col_num):
            self.board[row_num - x][col_num + x] = cur_player
        return self.board
     
    #######
    
    def get_diag2_ind(self, cur_player, row_num, col_num):
        if (row_num < 7) and (col_num < 7) and \
           ((self.board[row_num + 1][col_num + 1] == cur_player) or (self.board[row_num + 1][col_num + 1] == "o")):
            return None
        counter = 1
        while (row_num < 7) and (col_num < 7):
            if self.board[row_num + counter][col_num + counter] == "o":
                return None
            elif self.board[row_num + counter][col_num + counter] == cur_player:
                return [row_num + counter, col_num + counter]
            row_num += 1
            col_num += 1
    
    def insert_diag_ind_2(self, cur_player, row_num, col_num, col_ind):
        for x in range(col_ind - col_num):
            self.board[row_num + x][col_num + x] = cur_player
        return self.board   
    
    #######
    
    def get_diag3_ind(self, cur_player, row_num, col_num):
        if (row_num < 7) and (col_num > 0) and \
           ((self.board[row_num + 1][col_num - 1] == cur_player) or (self.board[row_num + 1][col_num - 1] == "o")):
            return None
        counter = 1
        while (row_num < 7) and (col_num > 0):
            if self.board[row_num + counter][col_num - counter] == "o":
                return None
            elif self.board[row_num + counter][col_num - counter] == cur_player:
                return [row_num + counter, col_num - counter]
            row_num += 1
            col_num -= 1
    
    def insert_diag_ind_3(self, cur_player, row_num, col_num, col_ind):
        for x in range(col_num - col_ind):
            self.board[row_num + x][col_num - x] = cur_player
        return self.board  
    
    #######
    
    def get_diag4_ind(self, cur_player, row_num, col_num):
        if (row_num > 0) and (col_num > 0) and \
           ((self.board[row_num - 1][col_num - 1] == cur_player) or (self.board[row_num - 1][col_num - 1] == "o")):
            return None
        counter = 1
        while (row_num > 0) and (col_num > 0):
            if self.board[row_num - counter][col_num - counter] == "o":
                return None
            elif self.board[row_num - counter][col_num - counter] == cur_player:
                return [row_num - counter, col_num - counter]
            row_num -= 1
            col_num -= 1
    
    def insert_diag_ind_4(self, cur_player, row_num, col_num, col_ind):
        for x in range(col_num - col_ind):
            self.board[row_num - x][col_num - x] = cur_player
        return self.board
    
    #######
      
    def check_val_move(self, cur_player, row_num, col_num):
        if (self.get_left_ind(cur_player, row_num, col_num) == None) and \
           (self.get_right_ind(cur_player, row_num, col_num) == None) and \
           (self.get_down_ind(cur_player, row_num, col_num) == None) and \
           (self.get_up_ind(cur_player, row_num, col_num) == None) and \
           (self.get_diag1_ind(cur_player, row_num, col_num) == None) and \
           (self.get_diag2_ind(cur_player, row_num, col_num) == None) and \
           (self.get_diag3_ind(cur_player, row_num, col_num) == None) and \
           (self.get_diag4_ind(cur_player, row_num, col_num) == None):
            return False
        else:
            return True   
    
    ############################################################################
    
    def val_list(self, cur_player):
        ans = []
        for row_num in range(7):
            for col_num in range(7):
                if (self.board[row_num][col_num] != "B") and (self.board[row_num][col_num] != "W"):
                    if self.check_val_move(cur_player, row_num, col_num):
                        ans.append([row_num,col_num])
        return ans  
    
    def update_board(self, cur_player, row_num, col_num):
        ind_left = self.get_left_ind(cur_player, row_num, col_num)
        if ind_left != None:
            self.insert_hor_ind_left(cur_player, row_num, col_num, ind_left)
        
        ind_right = self.get_right_ind(cur_player, row_num, col_num)    
        if ind_right != None:
            self.insert_hor_ind_right(cur_player, row_num, col_num, ind_right)
        
        ind_down = self.get_down_ind(cur_player, row_num, col_num)    
        if ind_down != None:
            self.insert_ver_ind_down(cur_player, row_num, col_num, ind_down)
            
        ind_up = self.get_up_ind(cur_player, row_num, col_num)    
        if ind_up != None:
            self.insert_ver_ind_up(cur_player, row_num, col_num, ind_up)  
            
        ind_diag1 = self.get_diag1_ind(cur_player, row_num, col_num)
        if ind_diag1 != None:
            self.insert_diag_ind_1(cur_player, row_num, col_num, ind_diag1[1])
        
        ind_diag2 = self.get_diag2_ind(cur_player, row_num, col_num)
        if ind_diag2 != None:
            self.insert_diag_ind_2(cur_player, row_num, col_num, ind_diag2[1])
        
        ind_diag3 = self.get_diag3_ind(cur_player, row_num, col_num)
        if ind_diag3 != None:
            self.insert_diag_ind_3(cur_player, row_num, col_num, ind_diag3[1])
            
        ind_diag4 = self.get_diag4_ind(cur_player, row_num, col_num)
        if ind_diag4 != None:
            self.insert_diag_ind_4(cur_player, row_num, col_num, ind_diag4[1])  
                
        
      
            
def main():
    s = input("press s then enter to start the game: ")
    while s != 's':
        print("your input is: " + s)
        s = input("press s then enter to start the game: ")
    
    print("\nHere is the board:")
    new_board = Board()
    print(new_board)
    print("\nPlayer 1 goes first.  Player 1 is B and Player 2 is W\n")
    player_lst = ['B', 'W']
    player_num = 0
    cur_player = player_lst[player_num]
    
    score = new_board.get_score()    
    while (score[0] + score[1]) < 64:
        if new_board.val_list(cur_player) == []:
            old_player = cur_player
            player_num = (player_num + 1) % 2
            cur_player = player_lst[player_num]
            print(old_player + " has no valid moves.  It is now "+ cur_player + "'s turn.\n")
            
        in_row = input("enter row: ")
        in_col = input("enter col: ")
    
        while not(isinstance(in_row, int)) or not(0<=in_row<=7) or \
              not(isinstance(in_col, int)) or not(0<=in_col<=7) or \
              new_board.check_val_move(cur_player, int(in_row), int(in_col)) == False:
            print("invalid move\n")
            in_row = input("enter row: ")
            in_col = input("enter col: ")        
        
        new_board.update_board(cur_player, int(in_row), int(in_col))
        player_num = (player_num + 1) % 2
        cur_player = player_lst[player_num]
        print("\n")
        print(new_board)
        score = new_board.get_score() 
        if (score[0] + score[1]) < 64:
            print("Board updated.  It is now " + cur_player + "'s turn.\n")
        
    
    
    #board is full
    if score[0] > score[1]:
        print(player_lst[0] + " wins!")
    elif score[0] < score[1]:
        print(player_lst[1] + " wins!")
    else:
        print("It is a tie.")
    print("Thanks for playing! :)")
    
main()