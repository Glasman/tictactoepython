import tkinter


def set_tile(row, column):
    global curr_player
    
    board[row][column]["text"] = curr_player
    
    if curr_player == playerO:
        curr_player = playerX
    else:
        curr_player = playerO

def new_game():
    pass

playerX = "X"
playerO = "O"

curr_player = playerX
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(
    frame,
    text=curr_player + "'s turn",
    font=("Consolas", 20),
    background=color_gray,
    foreground="white",
)

label.grid(row=0, column=0, columnspan=3)

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(
            frame,
            text="",
            font=("Consolas", 50, "bold"),
            bg=color_gray,
            foreground=color_blue,
            width=3,
            height=1,
            highlightthickness=0,
            highlightbackground=color_gray,
            relief="flat",
            command=lambda row=row, column=column: set_tile(row, column),
        )
        board[row][column].grid(row=row + 1, column=column, sticky="nsew")
        
button = tkinter.Button(frame, text="Restart", font=("Consolas", 20), bg=color_gray, fg=color_blue,
                        command=new_game)

button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()


#centers the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
