import random
from tkinter import *

window = Tk()
window.title("Snake")
window.geometry("700x700")
window.config(bg="#0a1628")
window.resizable(False,False)
window.iconbitmap("icon.ico")

speed = 5
square_length = 25
ball_present = False
snake_body = [[10, 11], [11, 11], [11, 12], [11, 13]]
ball_position = []
ball_placement_x = None
ball_placement_y = None
snake_pop = True
red_ball = None
gameover = False
right = False
left = False
up = False
down = True
restart_var =False

score = -1
try:
    file =  open("highscore.txt","r")
    highscore = int(file.read())
    file.close()
except:
    highscore = 0


def rounded_rect(canvas, x1, y1, x2, y2, r, **kwargs):
    points = [
        x1+r, y1,
        x2-r, y1,
        x2, y1,
        x2, y1+r,
        x2, y2-r,
        x2, y2,
        x2-r, y2,
        x1+r, y2,
        x1, y2,
        x1, y2-r,
        x1, y1+r,
        x1, y1,
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)

def up_button(event):
    global right, left,up, down
    if down == False:
        right = False
        left = False
        up = True
        down = False
def down_button(event):
    global right, left,up, down
    if up == False:
        right = False
        left = False
        up = False
        down = True
def left_button(event):
    global right, left,up, down
    if right == False:
        right = False
        left = True
        up = False
        down = False
def right_button(event):
    global right, left,up, down
    if left == False:
        right = True
        left = False
        up = False
        down = False
def controls():
    global right,left,up,down
    window.bind("<Up>",up_button)
    window.bind("<Down>",down_button)
    window.bind("<Left>",left_button)
    window.bind("<Right>",right_button)

main_board = Canvas(window,bg="#0f1b2d",relief="sunken",bd =1,height=600,width=600)

def render():
    global snake_body,snake_pop
    main_board.delete("all")
    for index,(x,y) in enumerate(snake_body):
        if x>23:
            snake_body.pop(index)
            snake_body.append([0,y])
        if y>23:
            snake_body.pop(index)
            snake_body.append([x,0])

        if x<0:
            snake_body.pop(index)
            snake_body.append([23, y])

        if y<0:
            snake_body.pop(index)
            snake_body.append([x, 23])

        rounded_rect(main_board,x*square_length,y*square_length,(x+1)*square_length,
                                    (y+1)*square_length,r=10,fill="#1a9e6e")
    if snake_pop == True:
        snake_body.pop(0)

def update():
    global snake_body
    if right:
        snake_body.append([snake_body[-1][0]+1,snake_body[-1][1]])
    elif left:
        snake_body.append([snake_body[-1][0]-1,snake_body[-1][1]])
    elif up:
        snake_body.append([snake_body[-1][0],snake_body[-1][1]-1])
    elif down:
        snake_body.append([snake_body[-1][0],snake_body[-1][1]+1])

def ball():
    global ball_present,snake_body,ball_position,ball_placement_y,ball_placement_x,red_ball,snake_pop,score

    if ball_present == False:
        ball_placement_x = random.randint(0,23)
        ball_placement_y = random.randint(0,23)
        ball_position = [ball_placement_x,ball_placement_y]
        score += 1
        snake_pop = True
        ball_present = True

    if ball_present == True:
        for x,y in snake_body:
            if x == ball_position[0] and y == ball_position[1]:
                ball_position.pop()
                ball_present = False
                snake_pop = False

    main_board.create_oval(
        ball_placement_x * 25, ball_placement_y * 25,
        (ball_placement_x + 1) * 25, (ball_placement_y + 1) * 25,
        fill="#ff6b6b")

def restart_command():
    global snake_body,ball_position,ball_placement_x,ball_placement_y,snake_pop,red_ball
    global right,left,up,down,score,ball_present,quit_button,restart_button,gameover


    snake_body = [[10, 11], [11, 11], [11, 12], [11, 13]]
    ball_position = []
    ball_placement_x = None
    ball_placement_y = None
    snake_pop = True
    red_ball = None
    gameover = False
    right = False
    left = False
    up = False
    down = True
    ball_present = False
    score = -1



def game_over():
    global snake_body,gameover,restart_button,quit_button,highscore
    snake_body_set = set(tuple(i) for i in snake_body)
    if len(snake_body) != len(snake_body_set):
        gameover = True
        main_board.delete("all")
        if highscore < score:
            print("this worked")
            highscore = score
            highscore_file = open("highscore.txt","w")
            highscore_file.write(str(highscore))
            highscore_file.close()
        main_board.create_text(277,200,text="Game Over",font=('Arial',20,'bold'),fill="white",anchor="center")
        main_board.create_text(190, 232, text="You scored", font=("Consolas", 14), fill="#4a7fa5", anchor="w")
        main_board.create_text(300, 232, text=str(score), font=("Consolas", 14, "bold"), fill="#56b8ff", anchor="w")
        main_board.create_text(321, 232, text="points", font=("Consolas", 14), fill="#4a7fa5", anchor="w")
        snake_body=[[10,11],[11,11],[11,12],[11,13]]
        for x,y in snake_body:
            rounded_rect(main_board, x * square_length, y * square_length, (x + 1) * square_length,
                         (y + 1) * square_length, r=10, fill="#1a9e6e")
        restart_button = Button(main_board,command=lambda: [restart_button.destroy()
                                , quit_button.destroy(),restart_command()]
                                ,text="Restart",font=("Consolas", 14, "bold")
                                ,fg="#1a3a5c",bd=2,highlightbackground="#2d6a9f")

        quit_button = Button(main_board,command=lambda :window.destroy(),text="Quit",font=("Consolas", 14, "bold"),
                      fg="#1a3a5c",bd=2,highlightbackground="#2d6a9f")
        restart_button.place(x=190, y=400)
        quit_button.place(x=320, y=400)



def all_scores():
    main_board.create_text(30,15,text=f"Score : {score}",fill = "#56b8ff")
    main_board.create_text(560,15,text= f"Best : {highscore}",fill= "#56b8ff")

def gameloop():
    global game_over,snake_body
    if gameover == False:
        render()
        update()
        controls()
        ball()
    game_over()
    all_scores()
    window.after(100,gameloop)

window.after(100,gameloop)
main_board.place(x=40,y=40)
window.mainloop()