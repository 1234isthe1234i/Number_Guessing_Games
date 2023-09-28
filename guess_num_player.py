from random import randint
import tkinter as tk
from tkinter import messagebox as msb


def game_logic_call_1(a):
    try:
        game_logic()
    except:
        return

def prep_screen():
    global h_or_l, counter
    h_or_l = tk.Label(Win, text='', font='Poppins 30 bold',
                      fg='#e3e3e3', bg='#3c67de')
    h_or_l.place(anchor=tk.NW, relx=0.5, rely=0.3)
    counter = 0
    Instruction['text'] = 'Guess A Number: '
    Enter['command'] = game_logic
    Win.bind('<Return>', game_logic_call_1)
    Tries['text'] = 'Guess No: ' + str(counter)


def game_logic():
    global counter
    guess = max_limit.get()
    if guess == '':
        msb.showerror('Invalid Number',
                      'You have entered nothing. \nPlease Try again')
    else:
        counter = counter + 1
        guess = int(guess)
        if guess > rand_num:
            h_or_l['text'] = 'Your Guess Is Too Large'
        elif guess < rand_num:
            h_or_l['text'] = 'Your Guess Is Too Small'
        elif guess == rand_num:
            msg = msb.showinfo('You Found the Number',
                               f'The number was {str(rand_num)} \nYou took {str(counter)} tries')
            if msg:
                Win.destroy()
                game_over = True
                main()

        Tries['text'] = 'Guess No: ' + str(counter)

    try:
        max_limit.delete(0, tk.END)
    except:
        pass


def run_game():
    global rand_num, max_num
    try:
        max_num = int(max_limit.get())
        if max_num < 2:
            msb.showerror(title='Number Too Low',
                        message='Number can\'t be lower than 100')
        else:
            rand_num = randint(1, int(max_num))
            max_limit.delete(0, tk.END)
            prep_screen()
    except ValueError:
        msb.showerror(title='No Number',
                      message='You didn\'t enter a number. \nPlease try again.')
    


def call_game_1(a):
    run_game()


def main():
    global max_limit, Instruction, Enter, Win, Tries

    Win = tk.Tk()

    Win.title('Guess the Number')
    Win.configure(bg='#3c67de')

    screen_width = Win.winfo_screenwidth()
    screen_length = Win.winfo_screenheight()

    app_width = 960
    app_length = 540

    x = (screen_width/2) - (app_width / 2)
    y = (screen_length/2) - (app_length / 2)

    Win.geometry(f'{app_width}x{app_length}+{int(x)}+{int(y)}')

    Instruction = tk.Label(Win, text='Enter the Max Number: ',
                           font='Poppins 15 bold', bg='#3c67de', fg='#e3e3e3')
    Instruction.place(anchor=tk.NW, relx=0.05, rely=0.2)

    Tries = tk.Label(Win, text='', font='Poppins 15 bold',
                     bg='#3c67de', fg='#e3e3e3')
    Tries.place(anchor=tk.NW, relx=0.3, rely=0.05)

    max_limit = tk.Entry(Win)
    max_limit.place(anchor=tk.NW, relx=0.3, rely=0.215)

    Enter = tk.Button(Win, text='Enter', fg='#3c67de',
                      bg='#e3e3e3', font='Poppins 15 bold', command=run_game)
    Enter.place(anchor=tk.NW, relx=0.2, rely=0.3)

    Win.bind('<Return>', call_game_1)
    Win.mainloop()
    print(1)

if __name__ == '__main__':
    global game_over
    game_over = False
    main()
