##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600)
drawpad.grid(row=0, column=1)


#roof outline

line1 = drawpad.create_line(50,150,710,150)
line2 = drawpad.create_line(50,150,90,50)
line3 = drawpad.create_line(90,50,670,50)
line4 = drawpad.create_line(670,50,710,150)
#house outline

house1 = drawpad.create_rectangle(80,150,670,510, fill = 'red')






root.mainloop()