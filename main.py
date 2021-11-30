from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def read (filePath):
    try:
        fo = open (filePath, 'r')
        res = fo.read()
        fo.close()
        return res
    except:
        return []

games = eval(read("Akinator\gamesLoads.txt")) #GAMES FILE

class Main:
    def __init__(self, master):
        self.master = master
        master.title("Guesser")
        master.geometry("550x550")
        master.iconbitmap('Akinator\icon.ico')#ICON
        
        self.img = ImageTk.PhotoImage(Image.open('Akinator\genieBackground.png'))#BACKGROUND
        self.background = Label(master, image=self.img)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        self.playButtom = Button(master, text="PLAY",bg = "royal blue",
                                    font=("8-BIT WONDER.TFF",20),command=self.openGameMenu)#PLAY BUTTOM
        self.playButtom.place(x=250,y=170)

        self.helpButtom = Button(master, text="HELP", bg="dodger blue",
                                    font=("8-BIT WONDER.TFF",20))#HELP BUTTOM
        self.helpButtom.place(x=250,y=240)

        self.quitButtom = Button(master, text="QUIT", bg="dodger blue",
                                    font=("8-BIT WONDER.TFF",20),command=self.master.destroy)#HELP BUTTOM
        self.quitButtom.place(x=250,y=310)

    def openGameMenu(classCall): #Open Game Menu
        gameMenu = Toplevel(menu)
        classCall = GameMenu(master=gameMenu)
        gameMenu.mainloop()

class GameMenu():
    def __init__(self,master):
        self.master = master
        master.title("Game Menu")
        master.geometry("550x550")
        master.iconbitmap('Akinator\icon.ico')#ICON

        self.img = ImageTk.PhotoImage(Image.open('Akinator\goldPit.jpg'))#BACKGROUND
        self.background = Label(master, image=self.img)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        self.newGameButtom = Button(master, text="NEW GAME",bg = "goldenrod",
                                    font=("8-BIT WONDER.TFF",20),command=self.openNewGame)#NEW GAME BUTTOM
        self.newGameButtom.place(x=190,y=170)
        
        self.loadGameButtom = Button(master, text="LOAD GAME",bg = "light goldenrod",
                                    font=("8-BIT WONDER.TFF",20),command=self.openSavedGames)#NEW GAME BUTTOM
        self.loadGameButtom.place(x=185,y=240)

    def openSavedGames(self): #Open saves menu
        gameMenu = Toplevel(menu)
        classCall = SavedMenu(master=gameMenu)
        gameMenu.mainloop()
    
    def openNewGame(self):
        gameMenu = Toplevel(menu)
        classCall = NewGame(master=gameMenu)
        gameMenu.mainloop()

class NewGame():
    global games
    def __init__(self,master):
        self.master = master
        master.title("New Game")
        master.geometry("550x550")
        master.iconbitmap('Akinator\icon.ico')#ICON

        self.img = ImageTk.PhotoImage(Image.open('Akinator\jas.jpg'))#BACKGROUND
        self.background = Label(master, image=self.img)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        self.scrollbar = Scrollbar(orient="horizontal")

        self.gameTheme = Entry(master,bg="yellow green",font=("8-BIT WONDER.TFF",20),xscrollcommand=self.scrollbar.set)
        self.gameTheme.insert(0,"Theme")
        self.gameTheme.place(x=130,y=20)

        self.newTreeLeaf_1 = Entry(master,bg="sea green",font=("8-BIT WONDER.TFF",20),xscrollcommand=self.scrollbar.set)
        self.newTreeLeaf_1.insert(0,"First Thing")
        self.newTreeLeaf_1.place(x=130,y=80)

        self.newTreeLeaf_2 = Entry(master,bg="medium sea green",font=("8-BIT WONDER.TFF",20),xscrollcommand=self.scrollbar.set)
        self.newTreeLeaf_2.insert(0,"Second Thing")
        self.newTreeLeaf_2.place(x=130,y=120)

        self.newTreeRoot = Entry(master,bg="dark sea green",font=("8-BIT WONDER.TFF",20),xscrollcommand=self.scrollbar.set)
        self.newTreeRoot.insert(0,"Question")
        self.newTreeRoot.place(x=130,y=160)

        self.valid = Button(master,text="SAVE",bg = "pale green",
                                    font=("8-BIT WONDER.TFF",15),command=self.answerValid)
        self.valid.place(x=235,y=200)

    def answerValid(self):    #Ask the user which answer is correct
        self.parameter = self.newTreeLeaf_1.get()
        self.validador = Label(self.master,text="If the parameter was: "+ self.parameter + ", the answer will be? (Y/N)",
                                        bg='light sea green',font=("8-BIT WONDER.TFF",15))
        self.validador.place(x=10,y=240)
        self.entryValid = Entry(self.master,bg="lime green",font=("8-BIT WONDER.TFF",15))
        self.entryValid.insert(0,"Y/N")
        self.entryValid.place(x=160,y=280)
        self.done = Button(self.master,text="DONE",bg = "forest green",
                                    font=("8-BIT WONDER.TFF",15),command=self.createGame)
        self.done.place(x=230,y=320)

    def createGame(self):
        newTree = []
        newRoot = self.newTreeRoot.get()
        if self.entryValid.get().strip().lower() == 'y':            
                newTree = [self.gameTheme.get(),[newRoot,self.newTreeLeaf_1.get(),self.newTreeLeaf_2.get()]]
        elif self.entryValid.get().strip().lower() == 'n':
                newTree = [self.gameTheme.get(),[newRoot,self.newTreeLeaf_2.get(),self.newTreeLeaf_1.get()]]
        else:
            messagebox.showinfo(title="Incorrect Entry", message="Ups something went wrong! \n Try again with (Y/N)")
            quit()
        games.append(newTree)
        fo = open("Akinator\gamesLoads.txt", "w")   #crea el file si no existe
        fo.write (str(games))
        fo.close()
        messagebox.showinfo(title="Games saved", message="Your game is saved!")

class SavedMenu():
    global games
    def __init__(self,master):
        self.master = master
        self.loads = games
        master.title("Saves")
        master.geometry("550x550")
        master.iconbitmap('Akinator\icon.ico')#ICON

        self.img = ImageTk.PhotoImage(Image.open('Akinator\city.jpg'))#BACKGROUND
        self.background = Label(master, image=self.img)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.ycoord = 20
        for self.gameSaved in self.loads:   #Creates a buttom for each save game
            self.text = self.gameSaved[0]
            self.save = Button(self.master, text=self.text,bg ="coral2",
                            font=("8-BIT WONDER.TFF",20),command=lambda i=self.text: self.openAnswerGame(i))
            self.save.place(x=200,y=self.ycoord)
            self.ycoord += 70
    
    def openAnswerGame(self,themeGame):
        for self.gameSearch in self.loads:
            if self.gameSearch[0] == themeGame:
                gameMenu = Toplevel(menu)
                classCall = AnswerWindow(master=gameMenu,list=self.gameSearch[1],theme=themeGame)
                gameMenu.mainloop()
            else:
                continue

class AnswerWindow():
    def __init__(self,master,list,theme):
        self.master = master
        self.list = list
        self.theme = theme
        master.title("Game Menu")
        master.geometry("550x550")
        master.iconbitmap('Akinator\icon.ico')#ICON

        self.img = ImageTk.PhotoImage(Image.open('Akinator\cave.jpg'))#BACKGROUND
        self.background = Label(master, image=self.img)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        self.gameOn(self.list,"",theme)

    #CHECK IF TREE IS ATOM (NO LEAFS):
    #Input: A tree
    def atom(self,tree):
        return not isinstance(tree,list)

    #RETURNS LEFT LEAF  
    #Input: A tree
    def leftSon(self,tree):
        if self.atom(tree):
            return []
        else:
            return tree[1]
    #RETURNS RIGHT LEAF  
    #Input: A tree
    def rightSon(self,tree):
        if self.atom(tree):
            return []
        else:
            return tree[2]
    
    def gameWorking(self):
        messagebox.showinfo(title="Thanks for playing", message="That's Great! \n It deserves a 100 right Diego?")
    
    #SAVE THE FILE TRUNCATING IT
    #IF THE FILE DOESN'T EXIST IT CREATES IT
    #Input: The file path, the string to save in the file
    #Output: The amount of character written
    def saveFile(self,filePath, stringToWrite):
        fo = open(filePath, "w")   #crea el file si no existe
        fo.write (str(stringToWrite))
        fo.close()

    def finalSave(self,question,additon,old,parameter ,fullGame,theme):
        global games
        if old in fullGame:
            if parameter.strip().lower() == 'y':
                            fullGame[fullGame.index(old)] = [question,additon,old] 
                            for game in games:
                                if game[0] == theme:
                                    game[1] = fullGame
                                    self.saveFile("Akinator\gamesLoads.txt",games)
                                    messagebox.showinfo(title="Thanks for my learning", message="Wow I didn't know that")
                                else:
                                    continue
            else:
                fullGame[fullGame.index(old)] = [question,old,additon] 
                for game in games:
                    if game[0] == theme:
                        game[1] = fullGame
                        self.saveFile("Akinator\out.txt",games)
                        messagebox.showinfo(title="Thanks for my learning", message="Wow I didn't know that")
                    else:
                        continue
        else:
            for answer in fullGame:
                if isinstance(answer, list):
                    if old in answer:
                        if parameter.strip().lower() == 'y':
                            answer[answer.index(old)] = [question,additon,old] 
                            for game in games:
                                if game[0] == theme:
                                    game[1] = fullGame
                                    self.saveFile("Akinator\gamesLoads.txt",games)
                                    messagebox.showinfo(title="Thanks for my learning", message="Wow I didn't know that")
                                else:
                                    continue
                        elif parameter.strip().lower() == 'n':
                            answer[answer.index(old)] = [question,old,additon] 
                            for game in games:
                                if game[0] == theme:
                                    game[1] = fullGame
                                    self.saveFile("Akinator\out.txt",games)
                                    messagebox.showinfo(title="Thanks for my learning", message="Wow I didn't know that")
                                else:
                                    continue
                        else:
                            messagebox.showinfo(title="Incorrect Entry", message="Ups something went wrong! \n Try again with (Y/N)")
                    else:
                        self.finalSave(question,additon,old,parameter,answer,theme)
                else:
                    continue

    def gameNeedsUpdate_Aux(self,newQuestion,newThing,oldThing,fullGame,theme):
        self.scrollbar = Scrollbar(orient="horizontal")
        self.parameter = Label(self.master,text="If the parameter was "+newThing+" the answer will be(Y/N)",
                                        font=("8-BIT WONDER.TFF",12))
        self.parameter.pack()
        self.valid = Entry(self.master,fg="white",bg="blue",font=8,xscrollcommand=self.scrollbar.set)
        self.valid.pack()
        self.toSave = Button(self.master,text="SAVE",command=lambda: self.finalSave(newQuestion,newThing,oldThing,self.valid.get(),fullGame,theme))
        self.toSave.pack()

    def gameNeedsUpdate(self,wrongAswer,fullGame,theme):
        self.scrollbar = Scrollbar(orient="horizontal")
        newThingEntry = Entry(self.master,fg="white",bg="blue",font=8,xscrollcommand=self.scrollbar.set)
        newThingEntry.insert(0,"What were you thinking?")
        newThingEntry.pack()
        newQuestionEntry = Entry(self.master,fg="white",bg="blue",font=8,xscrollcommand=self.scrollbar.set)
        newQuestionEntry.insert(0,"Difference with "+wrongAswer+"?")
        newQuestionEntry.pack()
        saveNewInfo = Button(self.master,text="DONE",command=lambda: self.gameNeedsUpdate_Aux(newQuestionEntry.get(),newThingEntry.get(),wrongAswer,fullGame,theme))
        saveNewInfo.pack()
        

    def gameOn_Aux(self,list,answer,fullGame,theme):
        self.actualGame = list
        if self.atom(list):
            self.finalAnswer = Label(self.master,text="Your answer is "+self.actualGame,
                                        font=("8-BIT WONDER.TFF",15))
            self.finalAnswer.pack()
            self.valid = Label(self.master,text="Is it correct?",
                                        font=("8-BIT WONDER.TFF",15))
            self.valid.pack()
            self.yesButtom = Button(self.master,text="YES",command=self.gameWorking)
            self.yesButtom.pack()
            self.noButtom = Button(self.master,text="NO",command=lambda: self.gameNeedsUpdate(list,fullGame,theme))
            self.noButtom.pack()
            print("Your answer is",list)
        else:
            self.rootQuestion = Label(self.master,text="Question: "+self.actualGame[0],font=("8-BIT WONDER.TFF",15))
            self.rootQuestion.pack()
            self.yesButtom = Button(self.master,text="YES",command=lambda: self.gameOn_Aux(self.leftSon(list),"",fullGame,theme))
            self.yesButtom.pack()
            self.noButtom = Button(self.master,text="NO",command=lambda: self.gameOn_Aux(self.rightSon(list),"",fullGame,theme))
            self.noButtom.pack()

    def gameOn(self,list,answer,theme):
        self.actualGame = list
        self.rootQuestion = Label(self.master,text="Question: "+self.actualGame[0],font=("8-BIT WONDER.TFF",15))
        self.rootQuestion.pack()
        self.yesButtom = Button(self.master,text="YES",command=lambda: self.gameOn_Aux(self.leftSon(list),"",self.actualGame,theme))
        self.yesButtom.pack()
        self.noButtom = Button(self.master,text="NO",command=lambda: self.gameOn_Aux(self.rightSon(list),"",self.actualGame,theme))
        self.noButtom.pack()
        self.print = Button(self.master,text="PRINT",command= lambda: self.printer(list))
        self.print.pack(side = BOTTOM)

    def printer(self,list):
        gameMenu = Toplevel(menu)
        classCall = PrinterWindow(master=gameMenu,listToPrint=list)
        gameMenu.mainloop()

class PrinterWindow():
    def __init__(self,master,listToPrint):
        self.master = master
        self.listToPrint = listToPrint
        master.title("Game Menu")
        master.geometry("550x550")
        master.iconbitmap('Akinator\icon.ico')#ICON

        self.img = ImageTk.PhotoImage(Image.open('Akinator\monkey.jpg'))#BACKGROUND
        self.background = Label(master, image=self.img)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        self.printer(self.listToPrint)

    def printer(self,listToPrint, level=0):
        for l in listToPrint:
            if type(l) is list:
                self.printer(l, level + 1)
            else:
                toPrint = ('     ' * level + '+---' + l)
                print(toPrint)
                printing = Label(self.master, text=toPrint)
                printing.pack()

menu = Tk()
classCall = Main(master=menu)
menu.mainloop()