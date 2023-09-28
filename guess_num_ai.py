from tkinter import *
from tkinter import messagebox as msb


def game_call():
    game_logic()


def game_call_1(a):
    game_logic()


def prep_screen():
    global guess
    high_entry.destroy()
    low_entry.destroy()
    high_label.destroy()
    low_label.destroy()
    guess = Label(Window, text='My Guess Is\n', font='Poppins 15 bold',
                  bg='#3c67de', fg='#e3e3e3')
    guess.place(anchor=CENTER, relx=0.3, rely=0.3)
    range_accept['text'] = 'You Guessed It'
    range_accept['command'] = VBS.end_game
    range_accept.place(anchor=CENTER, relx=0.3, rely=0.5)
    higher = Button(Window, text='Higher', font='Poppins 15 bold',
                    fg='#e3e3e3', bg='#3c67de', command=VBS.make_guess_higher)
    higher.place(anchor=CENTER, relx=0.18, rely=0.3)
    lower = Button(Window, text='Lower', font='Poppins 15 bold',
                   fg='#e3e3e3', bg='#3c67de', command=VBS.make_guess_lower)
    lower.place(anchor=CENTER, relx=0.42, rely=0.3)


class Human_Binary_Search():
    def __init__(self, high_bound: int, low_bound: int):
        self.h_or_l = ''
        self.high = high_bound
        self.low = low_bound
        self.counter = 0

    def make_guess_higher(self):
        self.low = self.guess
        self.logic()

    def make_guess_lower(self):
        self.high = self.guess
        self.logic()

    def end_game(self):
        cancel = msb.showinfo(
            'I Got It!', f'I guessed the number {str(self.guess)} in {str(self.counter)} tries')
        if cancel:
            Window.destroy()

    def logic(self):
        self.guess = (self.high + self.low) // 2
        guess['text'] = 'My Guess Is\n' + str(self.guess)
        self.counter += 1


def game_logic():
    global VBS
    high_bound = int(high_entry.get())
    low_bound = int(low_entry.get())
    VBS = Human_Binary_Search(high_bound=high_bound, low_bound=low_bound)
    prep_screen()
    VBS.logic()


def main():

    global Instructions, high_entry, high_label, low_entry, low_label, range_accept, Window

    Window = Tk()

    Window.title('The computer Guesses the Number')
    Window.config(bg='#3c67de')

    screen_width = Window.winfo_screenwidth()
    screen_length = Window.winfo_screenheight()

    app_width = 960
    app_length = 540

    x = (screen_width/2) - (app_width / 2)
    y = (screen_length/2) - (app_length / 2)

    Window.geometry(f'{app_width}x{app_length}+{int(x)}+{int(y)}')

    Instructions = Label(Window, text='''Think of a number. Specify the range. \nI will make a guess and you tell me if i should guess higher or lower. \nIf I get it right press the button.''',
                         fg='#e3e3e3', bg='#3c67de', font='Poppins 15 bold')
    Instructions.pack()

    high_label = Label(Window, text='High Bound',
                       font='Poppins 15 bold', bg='#3c67de', fg='#e3e3e3')
    high_label.place(anchor=NW, relx=0.1, rely=0.2)

    high_entry = Entry(Window, font='Poppins 15 bold', bg='#e3e3e3', fg='#3c67de')
    high_entry.place(anchor=NW, relx=0.1, rely=0.25)

    low_label = Label(Window, text='Low Bound', font='Poppins 15 bold',
                      bg='#3c67de', fg='#e3e3e3')
    low_label.place(anchor=NW, relx=0.6, rely=0.2)

    low_entry = Entry(Window, font='Poppins 15 bold', bg='#e3e3e3', fg='#3c67de')
    low_entry.place(anchor=NW, relx=0.6, rely=0.25)

    range_accept = Button(Window, 
        text='Enter', font='Poppins 15 bold', bg='#3c67de', fg='#e3e3e3', command=game_call)
    range_accept.place(anchor=NW, relx=0.45, rely=0.35)

    Window.bind('<Return>', game_call_1)
    Window.mainloop()


if __name__ == '__main__':
    main()
