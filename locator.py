# from tkinter import *
# import logging
#
# win = Tk ()
# win.geometry ("700x300")
#
#
# def get_input():
#     try:
#         logging.basicConfig (filename="file_locator.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s:%('
#                                                                                       'message)s')
#
#         # Creating a text box widget
#         Directory_Label = Label (text="Directory: ", width=20)
#         Directory_Label.pack (side=TOP)
#
#         my_text_box = Entry (width=100)
#         my_text_box.pack (side=TOP)
#
#         # Create a button for text box
#         search = Button (win, height=5, width=10, text="Search", command=lambda: get_input ())
#
#         search.pack()
#
#         win.mainloop ()
#         logging.info ("Going through the files in the mentioned directory!!")
#         # print (get_input ())
#
#     except Exception as e:
#         logging.error ("Please enter a valid path!")
#         logging.debug ("Please check the entered path")
#         logging.exception ("Exception has occurred: " + str (e))
#
#
import os
import logging

path = input("Please enter the directory path: ")


def get_input():
    try:
        logging.basicConfig (filename="file_locator.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s:%('
                                                                                           'message)s')

        os.chdir(path)
        logging.info ("Going through the files in the mentioned directory!!")

    except Exception as e:
        logging.error ("Please enter a valid path!")
        logging.debug ("Please check the entered path")
        logging.exception ("Exception has occurred: " + str (e))
