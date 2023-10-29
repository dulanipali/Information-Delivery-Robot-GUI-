from tkinter import *
import customtkinter
from PIL import ImageTk, Image 

from Directions import generateDirections

#Make a function for main page
#Make a function to destroy main menu and call other window
def mainMenu():

    root = customtkinter.CTk()

    root.configure(bg="black")
    
    def directions():
        root.destroy()
        generateDirections()

    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("dark-blue")


    #Getting the images
    weather_img = ImageTk.PhotoImage(Image.open("Weather.png").resize((300,300), Image.ANTIALIAS))
    dir_img = ImageTk.PhotoImage(Image.open("Directions.png").resize((300,300), Image.ANTIALIAS))
    news_img = ImageTk.PhotoImage(Image.open("News.png").resize((300,300), Image.ANTIALIAS))

    #Turning the images into buttons
    button_d = customtkinter.CTkButton(master=root, image=dir_img, text="Direction", width=190,height=48, compound="bottom", command=directions)
    button_d.pack(pady=20,padx=20, side=LEFT)

    button_w = customtkinter.CTkButton(master=root, image=weather_img, text="Weather", width=190,height=48, compound="bottom")
    button_w.pack(pady=20,padx=20, side=LEFT)

    button_n = customtkinter.CTkButton(master=root, image=news_img, text="News", width=190,height=48, compound="bottom")
    button_n.pack(pady=20,padx=20, side=LEFT)



    #This loop is how this keeps track of there the mouse is
    root.mainloop()

if __name__ == "__main__":
    mainMenu()