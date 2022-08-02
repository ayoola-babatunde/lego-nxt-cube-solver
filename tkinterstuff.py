#%%

# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry( "200x200" )

# Change the label text
def show():
	label.config( text = clicked.get() )

# Dropdown menu options
options = [
    "🟨"
    "🟦"
	"🟥",
    "🟩"
	"🟧",
	"⬜"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set( "⬜" )

# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()


# Execute tkinter
root.mainloop()

# %%
