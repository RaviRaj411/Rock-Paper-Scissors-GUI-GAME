from tkinter import *
from PIL import Image, ImageTk
import random
import sqlite3
import pygame
import time
import os
import sys
from datetime import datetime


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


userscore = 0
pcscore = 0
id = -1


def save():
    mydb = sqlite3.connect(resource_path("database\\RPS.db"))
    cur = mydb.cursor()
    values = ()
    qu = ""
    if id == -1:
        qu = "insert into scores (user,win,loose,last_played) values ( ? , ? , ? , ? )"
        values = (nameinp.get(), userscore, pcscore, datetime.now())

    else:
        qu = "update scores set win= ? ,loose= ? ,last_played= ?  where id= ? "
        values = (userscore, pcscore, datetime.now(), id)

    cur.execute(qu, values)
    mydb.commit()

    cur.close()
    mydb.close()
    playclick()
    time.sleep(0.5)
    root.destroy()


def conti():
    mydb = sqlite3.connect(resource_path("database\\RPS.db"))

    cur = mydb.cursor()
    qu = "select * from scores order by last_played desc limit 1"

    cur.execute(qu)
    user = cur.fetchone()
    if user is not None:
        global id, userscore, pcscore
        id = user[0]
        nameinp.set(user[1])
        userscore = user[2]
        pcscore = user[3]

    cur.close()
    mydb.close()
    playclick()
    maingame()


def enter(event):
    rock.config(bg="black", fg="white")


def enter1(event):
    paper.config(bg="black", fg="white")


def enter2(event):
    scissor.config(bg="black", fg="white")


def leave(event):
    rock.config(bg="white", fg="black")


def leave1(event):
    paper.config(bg="white", fg="black")


def leave2(event):
    scissor.config(bg="white", fg="black")


def entergame(event):
    playclick()
    maingame()


def playclick():
    sound = pygame.mixer.Sound(resource_path("audio\\click1.wav"))
    sound.play()


def mainpath():
    playclick()
    maingame()


def maingame():
    global userscore, pcscore, id
    global nameinp
    global rock, paper, scissor
    root.geometry("650x450")
    name.destroy()
    f1.destroy()
    inpname.destroy()
    sub.destroy()
    sub1.destroy()

    img = Image.open(resource_path("images\\bg2.png"))
    img = img.resize((650, 450))
    pic = ImageTk.PhotoImage(img)
    Lab = Label(image=pic)
    Lab.image = pic
    Lab.place(x=0, y=0)

    L2 = Label(
        text=f"{nameinp.get()} Score: {userscore}",
        bg="#4834DF",
        fg="#ffffff",
        borderwidth=5,
        relief=RAISED,
        font="Rockwell 13 bold",
        padx=4,
        pady=2,
    )
    L2.grid(row=5, column=0, pady=15)
    L3 = Label(
        text=f"PC Score: {pcscore}",
        bg="#4834DF",
        fg="white",
        borderwidth=5,
        relief=RAISED,
        font="Rockwell 13 bold",
        padx=4,
        pady=2,
    )
    L3.grid(row=6, column=0, pady=15)

    def click(event):
        sound = pygame.mixer.Sound(resource_path("audio\\click2.wav"))
        sound.play()
        global userscore, pcscore
        global L1
        global pcchose
        L1.grid_forget()
        pcchose.destroy()
        val = event.widget.cget("text")

        x = random.randint(0, 2)
        l1 = ["Rock", "Paper", "Scissor"]
        pc_opt = l1[x]

        if pc_opt == "Rock":
            Computer_Rock = PhotoImage(file=resource_path("images\\rock_computer.png"))
            Computer_Rock_ado = Computer_Rock.subsample(x=1, y=2)
            rock = Label(image=Computer_Rock_ado)
            rock.image = Computer_Rock_ado
            rock.place(x=380, y=150)
        if pc_opt == "Paper":
            Computer_Paper = PhotoImage(
                file=resource_path("images\\paper_computer.png")
            )
            Computer_Paper_ado = Computer_Paper.subsample(1, 2)
            paper = Label(image=Computer_Paper_ado)
            paper.image = Computer_Paper_ado
            paper.place(x=380, y=150)
        if pc_opt == "Scissor":
            Computer_Scissor = PhotoImage(
                file=resource_path("images\\scissor_computer.png")
            )
            Computer_Scissor_ado = Computer_Scissor.subsample(1, 2)
            scissor = Label(image=Computer_Scissor_ado)
            scissor.image = Computer_Scissor_ado
            scissor.place(x=380, y=150)

        pcchose = Label(
            text=f"PC Opted: {pc_opt}", font="lucida 15 bold", bg="black", fg="red"
        )
        pcchose.grid(row=5, column=1, pady=15)

        if val == "Rock" and pc_opt == "Paper":
            L1 = Label(text="PC Won", font="lucida 15 bold", bg="black", fg="gold")
            L1.grid(row=6, column=1, pady=15)
            pcscore += 1

        elif val == "Rock" and pc_opt == "Scissor":
            L1 = Label(
                text=f"{nameinp.get()} Won",
                font="lucida 15 bold",
                bg="black",
                fg="gold",
            )
            L1.grid(row=6, column=1, pady=15)
            userscore += 1

        elif val == "Paper" and pc_opt == "Scissor":
            L1 = Label(text="PC Won", font="lucida 15 bold", bg="black", fg="gold")
            L1.grid(row=6, column=1, pady=15)
            pcscore += 1

        elif val == "Paper" and pc_opt == "Rock":
            L1 = Label(
                text=f"{nameinp.get()} Won",
                font="lucida 15 bold",
                bg="black",
                fg="gold",
            )
            L1.grid(row=6, column=1, pady=15)
            userscore += 1

        elif val == "Scissor" and pc_opt == "Rock":
            L1 = Label(text="PC Won", font="lucida 15 bold", bg="black", fg="gold")
            L1.grid(row=6, column=1, pady=15)
            pcscore += 1

        elif val == "Scissor" and pc_opt == "Paper":
            L1 = Label(
                text=f"{nameinp.get()} Won",
                font="lucida 15 bold",
                bg="black",
                fg="gold",
            )
            L1.grid(row=6, column=1, pady=15)
            userscore += 1

        elif val == pc_opt:
            L1 = Label(text=f"It's A Tie", font="lucida 15 bold", bg="black", fg="gold")
            L1.grid(row=6, column=1, pady=15)
            userscore += 1
            pcscore += 1
        maingame()

    head = Label(
        text="Rock Paper Scissor", font="arial 35 bold", bg="black", fg="white"
    )
    head.grid(columnspan=2, row=0, ipadx=70, padx=33, pady=10)
    playerone = Label(text=f"Player 1 : {nameinp.get()}", font="lucida 16")
    playerone.grid(row=1, column=0)
    playertwo = Label(text=f"Player 2 : Computer", font="lucida 16")
    playertwo.grid(row=1, column=1)

    Player_Rock = PhotoImage(file=resource_path("images\\rock_player.png"))
    Player_Rock_ado = Player_Rock.subsample(4, 5)
    rock = Button(text="Rock", image=Player_Rock_ado)
    rock.image = Player_Rock_ado
    rock.grid(row=2, column=0, pady=10)
    rock.bind("<Enter>", enter)
    rock.bind("<Leave>", leave)
    rock.bind("<Button-1>", click)

    Player_Paper = PhotoImage(file=resource_path("images\\paper_player.png"))
    Player_Paper_ado = Player_Paper.subsample(4, 5)
    paper = Button(text="Paper", image=Player_Paper_ado)
    paper.image = Player_Paper_ado
    paper.grid(row=3, column=0)
    paper.bind("<Enter>", enter1)
    paper.bind("<Leave>", leave1)
    paper.bind("<Button-1>", click)

    Player_Scissor = PhotoImage(file=resource_path("images\\scissor_player.png"))
    Player_Scissor_ado = Player_Scissor.subsample(4, 5)
    scissor = Button(text="Scissor", image=Player_Scissor_ado)
    scissor.image = Player_Scissor_ado
    scissor.grid(row=4, column=0, pady=10)
    scissor.bind("<Enter>", enter2)
    scissor.bind("<Leave>", leave2)
    scissor.bind("<Button-1>", click)

    btnclose = Button(text="Close Game", command=save, bg="green", font="arial 10 bold")
    btnclose.place(x=280, y=410)
    Lab.lower()


""" GUI Program Starting """

root = Tk()
root.title("Rock Paper Scissor")
root.iconbitmap(resource_path("images\\icon.ico"))

root.maxsize(650, 450)
root.minsize(650, 450)
pygame.mixer.init()
pygame.mixer.music.load(resource_path("audio\\audio.mp3"))
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.4)

rock = Button()
paper = Button()
scissor = Button()
rock = Label()
paper = Label()
scissor = Label()
L1 = Label()
pcchose = Label()


f1 = Frame(root)
img = Image.open(resource_path("images\\bg.jpg"))
img = img.resize((650, 450), Image.ANTIALIAS)
pic = ImageTk.PhotoImage(img)
Lab = Label(f1, image=pic)
Lab.pack()
f1.pack()


name = Label(root, text="Enter Your Name :", font="arial 15 bold")
name.place(x=262, y=20)
nameinp = StringVar()
inpname = Entry(root, textvar=nameinp, font="arial 10 bold")
inpname.bind("<Return>", entergame)
inpname.place(x=275, y=60)

sub = Button(
    root,
    text="Play",
    font="lucida 10 bold",
    bg="black",
    fg="white",
    command=mainpath,
)
sub.place(x=325, y=88)
sub1 = Button(
    root,
    text="continue",
    font="lucida 10 bold",
    bg="black",
    fg="white",
    command=conti,
)
sub1.place(x=312, y=120)

root.mainloop()
