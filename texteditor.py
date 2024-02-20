import tkinter as tk # import Tkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename # dialogs to save and open

def open(window, txt_edit):
# function to open a file and print its contents
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")]) # look for any .txt file
    
    if not filepath: 
        return
    
    txt_edit.delete(1.0, tk.END) # delete everything in the text editor so far
    # txt_edit = ""
    with open(filepath, "r") as file: # open file to read
        text = file.read() # content of the file
        txt_edit.insert(tk.END, text) # insert content of the text file
    window.title(f"Open File: {filepath}") # set title
    


def save(window, edit):
# function to save a file
    print("save")

def main():
    window = tk.Tk()
    window.title("Text Editor App")
    # initializing tkinter window
    
    # [Save = row:0, column 0]   [Text Editor = row:    0, column:1]
    # [Column = row:1, column:0]
    
    window.rowconfigure(0, minsize = 400, weight = 1)
    window.columnconfigure(1, minsize = 1000, weight = 1)
    # edit the row and columns of the tkinter
    # seperate to 0 rows and 1 column
    
    txt_edit = tk.Text(window, font = "Helvetica 18") # set grid for text editor
    txt_edit.grid(row = 0, column = 1, sticky = "nsew") # at row 0, column 1, expand north, south, east, west
    
    frame = tk.Frame(window, relief = tk.RAISED, bd = 2) # set frame ofor buttons
    saveBtn = tk.Button(frame, text = "Save As...") # call save function when clicked
    openBtn = tk.Button(frame, text = "Open...", command = lambda: open(window, txt_edit)) # call open function when clicked
    
    saveBtn.grid(row = 0, column = 0, padx = 5, pady = 5, sticky="ew")
    openBtn.grid(row = 1, column = 0, padx = 5, sticky = "ew") 
    # expand east and west, save 1st row, open 2nd row, both column 0
    frame.grid(row = 0, column = 0, sticky = "ns") # set grid for
    
    window.mainloop() 

if __name__ == "__main__":
    main()