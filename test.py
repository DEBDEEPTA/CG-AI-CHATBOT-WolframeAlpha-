# importing the required modules
from tkinter import *  # importing all the widgets and modules from Tkinter
from tkinter import messagebox as mb  # importing the messagebox module from Tkinter
from PIL import Image, ImageTk  # importing the Image & ImageTk modules from PIL
import wolframalpha  # importing the wolframalpha module


# --------------------------------- Functions ---------------------------------
# defining a function to find answer
def find_answer(question):
    """This function will return the answer
    for the input query from the users"""

    # declaring a variable to store the APP ID
    app_id = '97U4GL-TYHG9YU349'

    # creating an object of the Client() class using the APP ID
    the_client = wolframalpha.Client(app_id)
    try:
        # storing the response from wolfram alpha
        response = the_client.query(question)

        # including only the text from the responses
        answer = next(response.results).text
    except:
        answer = ""
        # returning the answer
    return answer


# defining a function to compute the result
def compute_result():
    """This function checks if the user has raised
    any query and calls the find_answer() function
    and returns the appropriate answer"""

    # using the delete() method to delete any previous entry from the answer_field field
    answer_field.delete(0, END)

    # using the get() method to retrieve the entered query from the question_field field
    query = question_field.get()

    # if the field in not empty, call the find_answer() function and store the result
    if query != "":
        answer = find_answer(query)
        # if the result is not an empty string, insert the answer in the answer_field field using the insert() method
        if answer != "":
            answer_field.insert(0, answer)
            # if the result is an empty string, display the message box with the error message using the showerror() function of the messagebox module
        else:
            answer_field.insert(0, "No Results Found!")
            mb.showerror("No Results Found", "Oops! Unable to find the answer of the Query.")
            # if the question_field field is empty, display the message box with the error message using the showerror() function of the messagebox module
    else:
        mb.showerror("Empty Field", "Entry Field Cannot be Empty.")

    # defining a function to reset the entry fields


def reset_entries():
    """This function deletes all the
    entries from the entry fields"""

    # using the delete() method to delete the entries from the entry fields
    question_field.delete(0, END)
    answer_field.delete(0, END)

    # displaying the message box to display a SUCCESS statement using the showinfo() function of the messagebox module
    mb.showinfo("Fields Reset", "All Fields are reset.")


# defining a function to close the application
def exit_application():
    """This function closes the application"""

    # using the destroy() method to close the application
    main_win.destroy()


# main function
if __name__ == '__main__':
    # instanting the Tk() class
    main_win = Tk()

    # setting the title of the window
    main_win.title("MY BASIC ASSISTANT - 1RI21CS033")

    # defining the geometry of the window
    main_win.geometry("700x300+600+300")

    # disabling the resizable option
    main_win.resizable(0, 0)

    # configuring the background color of the window to #F0FFFF
    main_win.config(bg="#F0FFFF")

    # adding the icon to the application
    main_win.iconbitmap("BOT_ICON.png")

    # importing an image file, resizing it and making it compatible for the Tkinter use
    assist_img = ImageTk.PhotoImage(Image.open("BOT_ICON.png").resize((50, 50), Image.Resampling.LANCZOS))

    # adding frames using the Frame() widget
    title_frame = Frame(main_win,
                        bg="#F0FFFF")  # this frame will contain the labels to display the heading and subheading of the application
    input_frame = Frame(main_win,
                        bg="#F0FFFF")  # this frame will contain the labels and entry fields to enter the query and display the result
    button_frame = Frame(main_win,
                         bg="#F0FFFF")  # this frame will contain the buttons to manipute the entered data and call the function

    # using the pack() function to set the positioning of the frames on the main window screen
    title_frame.pack()
    input_frame.pack(fill="both", padx=30)
    button_frame.pack()

    # ----------------------------- the title_frame frame -----------------------------
    # adding the image as an label using the Label() widget
    image = Label(
        title_frame,
        image=assist_img,
        bg="#F0FFFF"
    )

    # adding the label to display the heading with the help of the Label() widget
    heading = Label(
        title_frame,
        text="My Assistant",
        font=("times new roman", "20", "bold"),
        bg="#F0FFFF",
        fg="#4169E1"
    )

    # using the grid() function to set the position of the above labels in the grid format on the main window
    image.grid(row=0, column=0, padx=10, pady=10)
    heading.grid(row=0, column=1, padx=10, pady=10)

    # ----------------------------- the input_frame frame -----------------------------
    # adding a label using the Label() widget to display some informative statement
    question_label = Label(
        input_frame,
        text="Enter the Query :",
        font=("times new roman", "12", "bold"),
        bg="#F0FFFF",
        fg="#191970"
    )

    # adding an entry field for the users to enter the query with the help of the Entry() widget
    question_field = Entry(
        input_frame,
        width=60,
        font=("times new roman", "12"),
        bg="#FFFFFF",
        fg="#000000",
        relief=GROOVE
    )

    # adding a label once again to display the another informative statement using the Label() widget
    answer_label = Label(
        input_frame,
        text="Answer :",
        font=("times new roman", "12", "bold"),
        bg="#F0FFFF",
        fg="#191970"
    )

    # adding an entry field to display the result of the entered query with the help of the Entry() widget
    answer_field = Entry(
        input_frame,
        width=60,
        font=("times new roman", "12"),
        bg="#FFFFFF",
        fg="#000000",
        relief=GROOVE
    )

    # using the grid() function to set the position of the above labels and entry fields in the grid format on the main window
    question_label.grid(row=0, column=0, padx=10, pady=0, sticky=W)
    question_field.grid(row=1, column=0, padx=10, pady=5, sticky=W)
    answer_label.grid(row=2, column=0, padx=10, pady=0, sticky=W)
    answer_field.grid(row=3, column=0, padx=10, pady=5, sticky=W)

    # ----------------------------- the button_frame frame -----------------------------
    # adding a button to compute the answer of the query with the help of the Button() widget
    compute_button = Button(
        button_frame,
        text="Go",
        font=("times new roman", "12"),
        bg="#00FF7F",
        fg="#000000",
        activebackground="#3CB371",
        activeforeground="#FFFFFF",
        relief=GROOVE,
        width=12,
        command=compute_result
    )

    # adding a button to reset the entries with the help of the Button() widget
    reset_button = Button(
        button_frame,
        text="Clear",
        font=("times new roman", "12"),
        bg="#DCDCDC",
        fg="#000000",
        activebackground="#696969",
        activeforeground="#FFFFFF",
        relief=GROOVE,
        width=12,
        command=reset_entries
    )

    # adding a button to close the application with the help of the Button() widget
    close_button = Button(
        button_frame,
        text="Cancel",
        font=("times new roman", "12"),
        bg="#FF0000",
        fg="#FFFFFF",
        activebackground="#8B0000",
        activeforeground="#FFFFFF",
        relief=GROOVE,
        width=12,
        command=exit_application
    )

    # using the grid() function to set the position of the above buttons in the grid format on the main window
    compute_button.grid(row=0, column=0, padx=10, pady=20)
    reset_button.grid(row=0, column=1, padx=10, pady=20)
    close_button.grid(row=0, column=2, padx=10, pady=20)

    # using the mainloop() method to run the application
    main_win.mainloop()