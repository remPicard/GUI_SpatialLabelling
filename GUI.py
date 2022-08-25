from tkinter import *
from tkinter.ttk import Progressbar
import pandas as pd
from os.path import exists
from tkinter import filedialog as fd
from PIL import Image, ImageTk
import numpy as np
import glob
from matplotlib import cm
from scipy import interpolate

##################################### Global variables ##################################


# Fonts #
# define the fonts for future use in the code
font_title = ('Helvetica', 25, 'bold')
font_corpus = ('Helvetica', 17)
font_case = ('Helvetica', 20, 'bold')


# Arrows #
# define the unicode arrows for future use in the code
DownLeft = "\u2199" 
Down = "\u2193"
DownRight = "\u2198" 
Right = "\u2192"
UpRight = "\u2197"
Up = "\u2191"
UpLeft = "\u2196"
Left = "\u2190"
Clockwise = "\u21BB"
AntiClockwise = "\u21BA"


##################################### CLASSES ##################################


""" ######################################### DATA BANK ######################################### """       


class DataBank () :
    """ This class create or manage everything acccording to the CSV files """

    def __init__ (self, title):
        """ 
        Constructor of the class DataBank. 
        
        title : is the path to the CSV file (created or modified)
        return : a DataBank oject containing a python dataframe as attribute
        """
        # save the pathname as an attribute of this class to be call later in the code
        self.CSVfile_name = title
        # Check the existance of the CSV file in the directory indicated by the title argument
        if exists (self.CSVfile_name):
            # if CSV, the dataframe is loaded thanks to the CSV file with the new skinny shape
            self.df = pd.read_csv(self.CSVfile_name)
        else :
            # count the number of Data.csv file already existing in the Downloads directory
            num_files = len(glob.glob('/Users/*/Downloads/Data*'))
            # first csv file in Downloads
            if num_files == 0:
                # if not exist, a blank preloaded (cases and pictures) dataframe is created with the function GenerateBlank_df
                self.df = self.GenerateBlank_df()
                # new data frame saved as th first CSV file in Downloads directory by default (name : Data.csv)
                self.df.to_csv('~/Downloads/Data.csv', mode='w', index =False, header=True)
            # csv file(s) already exist in Downloads
            else :
                # if not exist, a blank preloaded (cases and pictures) dataframe is created with the function GenerateBlank_df
                self.df = self.GenerateBlank_df()
                # new data frame saved as CSV file in Downloads directory by default and iterate the name according to the existing files 
                self.df.to_csv(f'~/Downloads/Data{int(num_files)+1}.csv', mode='w', index =False, header=True)


    def GenerateBlank_df (self):
        """ 
        GenerateBlank_df generates a DataFrame preloaded with the cases to be labelled. To preload the DataFrame, it uses the npy array containing the videos to label. 
        
        return : the Pandas DataFrame preloaded 
        """
        # load the array
        fnames = glob.glob('./numpyArrays8by8/*.npy')
        # create the header of the dataframe
        header = ['Case','Picture','Option 1', 'Option 2','Comment']
        # create the table where the data will be saved
        data = []
        # loop through each case 
        for f in fnames :
            case = f.split("/")[-1].split(".")[0]
            # load the np array corresponding to the case 
            array = np.load(f"./numpyArrays8by8/{case}.npy")
            # loop through each picture 
            for pic in range (0,len(array)) :
                picture = pic
                # add a row containing : the case number, the picture number, blank for Option 1, blank for Option 2, blank for Comments
                data.append([int(case), int(picture), " ", " ", " "])
        # arrange the dataframe with the preloaded rows and 5 columns : Case, Picture, Option 1, Option 2, Comments and ascending sort of cases then pictures
        df = pd.DataFrame(data, columns=header)
        df = df.sort_values(['Case', 'Picture'])
        return df  


    def unicode2str (self, uni):
        """ 
        unicode2str converts a direction from a unicode type to its meaning in string type.
        
        uni : code of the unicode arrow  
        return : the direction in string type 
        """
        if uni == "\u2199" :
            return 'DownLeft'
        if uni  == "\u2193":
            return 'Down'
        if uni ==  "\u2198" :
            return 'DownRight'
        if uni == "\u2192" :
            return 'Right'
        if uni  == "\u2197":
            return 'UpRight'
        if uni ==  "\u2191" :
            return 'Up'
        if uni ==  "\u2196" :
            return 'UpLeft'
        if uni == "\u2190" :
            return 'Left'
        if uni  == "\u21BB":
            return 'Clockwise'
        if uni ==  "\u21BA" :
            return 'AntiClockwise'
        if uni ==  '-' :
            return '-'
        if uni ==  " " :
            return " "


    def str2unicode (self, str):
        """ 
        str2unicode converts a direction expressed from a string type to a unicode type. 
        
        str : code of the unicode arrow  
        return : the direction in string type 
        """
        if str == 'DownLeft' :
            return DownLeft
        if str  == 'Down':
            return Down
        if str ==  'DownRight' :
            return DownRight
        if str == 'Right' :
            return Right
        if str  == 'UpRight':
            return UpRight
        if str ==  'Up' :
            return Up
        if str ==  'UpLeft' :
            return UpLeft
        if str == 'Left' :
            return Left
        if str  == 'AntiClockwise':
            return AntiClockwise
        if str ==  'Clockwise' :
            return Clockwise
        if str ==  '-' :
            return '-'
        if str ==  " " :
            return " "
    

    def SaveData (self, case, picture, option1, option2):
        """ 
        SaveData saves the Option 1, Option 2 chosen during the labelling work 
        into the df attribute of the DataBank object and then into the CSV file for a picture and a case given.
        
        case : the case where the data will be saved 
        picture : the picture where the data will be saved
        option1 : option1 chosen
        option2 : option2 chosen  
        return : save direclty the data into the CSV file
        """
        # add the option1 and the option2 in the good columns of the dataframe according to the arguments
        self.df.loc[(self.df["Case"]==int(case))&(self.df["Picture"]==int(picture)), "Option 1"] = self.unicode2str(option1)
        self.df.loc[(self.df["Case"]==int(case))&(self.df["Picture"]==int(picture)), "Option 2"] = option2 
        # save the data of the dataframe in the csv file 
        self.df.to_csv(self.CSVfile_name, mode='w', index =False, header=True)


    def SaveComment (self, case, picture, comment):
        """ 
        SaveData saves the possible Comments added during the labelling work 
        into the df attribute of the DataBank object and then into the CSV file for a picture and a case given.
        
        case : the case where the comment will be saved 
        picture : the picture where the comment will be saved
        comment : optional comments on this video
        return : save direclty the comment into the CSV file
        """
        # add the comment in the good column of the dataframe 
        self.df.loc[(self.df["Case"]==int(case))&(self.df["Picture"]==int(picture)), "Comment"] = comment
        # save the data of the dataframe in the csv file 
        self.df.to_csv(self.CSVfile_name, mode='w', index =False, header=True)


    def LoadData(self, case, picture):
        """ 
        LoadData returns the data saved in the CSV file for a case and a picture given 
        
        case : the case where the data will be extrated 
        picture : the picture where the data will be extrated 
        return : a list of 3 strings : option1, option2, comments in this order
        """
        # the df attribute (Pandas DataFrame) is filled with the data of the CSV file
        self.df = pd.read_csv(self.CSVfile_name)
        # pick up the option1 from the csv file
        option1 = self.df[(self.df["Case"]==int(case))&(self.df["Picture"]==int(picture))]["Option 1"].values[0]
        # pick up the option2 from the csv file
        option2 = self.df[(self.df["Case"]==int(case))&(self.df["Picture"]==int(picture))]["Option 2"].values[0]
        # pick up the optional comments from the csv file
        comment = self.df[(self.df["Case"]==int(case))&(self.df["Picture"]==int(picture))]["Comment"].values[0]
        # reurn the list of the 3 data of this picture in this case 
        return [self.str2unicode(option1), option2, comment]

 
""" ######################################### HEADER ######################################### """


class Header ():

    def __init__(self, master):
        """ 
        Constructor of the class Header. This class will manage the different pages of the GUI via the drop down menu at the top right of the window.
        
        matser : master window which will be the parent of the Header object 
        return : nothing but display the header of the app 
        """
        # create a frame for the title at the top of the window
        self.frame_title = Frame(master, height=50, bg="#15AFDA")
        # fix the size of the frame (independantly of the widgets)
        self.frame_title.pack_propagate(0)
        # display the frame
        self.frame_title.pack(side="top", fill="x", expand=False)

        # open the logo image png
        self.logo = PhotoImage(file = r"./GUI_images/logo.png")
        # add the logo in a label
        self.label_title = Label(self.frame_title, image=self.logo, bg="#15AFDA")
        # display the logo with y padding
        self.label_title.pack(ipady=5)

        # create the drop down menu with the method createDropDownMenu
        self.drop_down_menu = self.createDropDownMenu('Menu')

        # create the frame where the different pages will be displayed    
        self.main_container = Frame(master, bg='black')
        # fix the size of the frame (independantly of the widgets)
        self.main_container.pack_propagate(0)
        # display the frame 
        self.main_container.pack(side="top", fill="both", expand=True)

        # create and display a welcome message in a label
        self.welcome_label = Label(self.main_container, text="Welcome", font=font_title, bg="black", fg="#15AFDA", anchor=CENTER)
        self.welcome_label.pack(fill="both", expand=True)

        # create and display an instruction in a label
        self.help_label = Label(self.main_container, text="Please read the instructions before you begin labelling videos", font=font_case, bg="black", fg="white", anchor=N)
        self.help_label.pack(fill="both", expand=True)

        # left click shortcut on the logo to come back to the welcome page
        self.label_title.bind("<1>", self.welcomePage)
        

    def createDropDownMenu (self, title):
        """ 
        createDropDownMenu returns the drop down menu of the header with the correct name 
        
        title : string giving the title of the drop down menu when first displayed 
        return : drop down menu of the header
        """
        # list of the options available in the header drop down menu
        MENU_OPTIONS = ['GUI instructions', 'Labelling instructions', 'Start new labelling', 'Resume labelling']
        # set up the option selected when first displayed
        self.menu_selected = StringVar(self.frame_title, value=title)
        # create the drop down menu widget
        self.drop_down_menu = OptionMenu(self.frame_title, self.menu_selected, *MENU_OPTIONS)
        # configure the font of the options 
        self.frame_title.nametowidget(self.drop_down_menu.menuname).config(font=font_corpus)
        # configure the preview of the drop down widget
        self.drop_down_menu.config(font=font_corpus, bg="#15AFDA")
        # display the drop down menu at a given position
        self.drop_down_menu.place(x=20, y=11)
        # if option selected changes, it executes the change page method
        self.menu_selected.trace("w", self.changePage)
        # return the drop down menu
        return self.drop_down_menu


    def welcomePage (self, event = None):
        """ 
        welcomePage delete the current page and display the welcome page instead  
        
        event : means the method can be used for shortcuts with bind function 
        return : nothing but display the welcome page
        """
        # destroy all the widgets on the page
        for widgets in self.main_container.winfo_children():
            widgets.destroy()
        # detroy the drop down menu of the header 
        A.drop_down_menu.destroy()
        # recreate the dropdown menu with the name of the good section you are in 
        self.drop_down_menu = self.createDropDownMenu('Menu')
        # create and display a welcome message in a label
        self.welcome_label = Label(self.main_container, text="Welcome", font=font_title, bg="black", fg="#15AFDA", anchor=CENTER)
        self.welcome_label.pack(fill="both", expand=True)
        # create and display an instruction in a label
        self.help_label = Label(self.main_container, text="Please read the instructions before you begin labelling videos", font=font_case, bg="black", fg="white", anchor=N)
        self.help_label.pack(fill="both", expand=True)
        # set the focus on the welcome page 
        self.main_container.focus()

    def selectFile (self):
        """ 
        selectFile open file explorer and allow to chose a file with a given format 
        
        return : nothing but save the path of the file selected in the attribute 
        """
        # open a file explorer window
        self.path = fd.askopenfilename(initialdir="~/Documents",
            title = "Select a labelling file",
            # define the file formats allowed to be selected
            filetypes = (("CSV files","*.csv"), ("Excel files","*.xlsx"), ("All files","*.*")))


    def changePage (self, *args):
        """ 
        changePage switch between pages of teh GUI by creating object of the other classes in the main_container frame
        
        return : nothing but display the page selected in the drop down menu  
        """
        # get the option selected in the drop down menu
        info = self.menu_selected.get()
        # check if selected option matches the options available in the drop down menu  
        if info == 'Labelling instructions' :
            # destroy the current page displayed
            for widgets in self.main_container.winfo_children():
                widgets.destroy()
            # display the new page corresponding the option selected
            Labelling_instructions(self.main_container)
        elif info == 'GUI instructions' :
            # destroy the current page displayed
            for widgets in self.main_container.winfo_children():
                widgets.destroy()
            # display the new page corresponding the option selected
            GUI_instructions(self.main_container)
        elif info == 'Start new labelling' :
            # destroy the current page displayed
            for widgets in self.main_container.winfo_children():
                widgets.destroy()
            # display the new page corresponding the option selected
            MainPage(self.main_container, "~/Downloads/Data.csv")
        elif info == 'Resume labelling' :
            # pick up the path of the file you want to continue editing
            self.selectFile()
            # destroy the current page displayed
            for widgets in self.main_container.winfo_children():
                widgets.destroy()
            # display the new page corresponding the option selected
            MainPage(self.main_container, self.path)      


""" ######################################### GUI INSTRUCTIONS ######################################### """       


class GUI_instructions (Frame) : 
    """ This class heritates the Tkinter Frame class, GUI_Instructions is a frame widget"""

    def __init__(self, master):
        """ 
        Constructor of the class GUI_instructions. 

        master :  master frame (main_container) which will be the parent of the GUI_instructions object
        return : nothing but display the GUI instructions  
        """
        # all the objects of the GUI_instructions class get the methods of the Frame tkinter class
        Frame.__init__(self, master)

    # LABEL WITH THE INSTRUCTIONS #
        # define the bullet 
        bullet = "•"
        # create the text widget 
        t = Text(master)
        # create the scrollbar widget 
        scroll = Scrollbar(master, command= t.yview)
        # effectiveness of the scrollbar in the text widget   
        t.configure(yscrollcommand=scroll.set, wrap=WORD, bd=50)

        # configure the different fonts which will be used in the text widget
        t.tag_configure('image', justify='center')
        t.tag_configure('title', font=font_title, justify='center')
        t.tag_configure('corpus', foreground='black', font=font_corpus)
        t.tag_configure('special', foreground='#15AFDA', font=('Helvetica', 20, 'bold'))
        t.tag_configure('italic', foreground='black', font=('Helvetica', 17, 'italic', 'bold'))

        # display the text widget 
        t.pack(fill="both", side=LEFT, expand=True)
        # display the scrollbar 
        scroll.pack(fill=Y, side=LEFT)

        # Title #
        # insert the string at the end of the text widget with the title font
        t.insert(END,'GUI User manual (V1)\n\n', 'title')

        # Intro #
        corps1  = """
        These instructions are for the GUI, the GUI is a standalone app running on your computer which allow you to label the spatial metrics videos.\nUsing the drop down menu, you can start a new work. This will create a new .csv file in your Downloads directory under the name 'Data.csv'. Or you can simply resume labelling the videos from an older .csv.\nOnce you are done labelling please rename your labelled files.\n """
        t.insert(END, corps1, 'corpus')
    

        # SHORTCUTS #
        
        t.insert(END, "\nKeyboard shortcuts\n", 'special')
        corps2="""
        The GUI is entirely clickable with the mouse or you can use keyboard shortcuts to modify the widgets.\n\n"""
        t.insert(END, corps2, 'corpus')
        # windows section
        t.insert(END, "Switching windows\n", 'italic')
        t.insert(END, """To navigate between the windows of a case, you can use the Next and Previous buttons at the bottoms of the window or use keys :\n""", 'corpus')
        t.insert(END, bullet+" Space ", 'special') 
        t.insert(END, ": Next window\n", 'corpus')
        t.insert(END, bullet+" Shift+Space ", 'special') 
        t.insert(END, ": Previous window\n\n", 'corpus')

        # option1 section
        t.insert(END, "Option 1\n", 'italic')
        corps4="""To select a direction use the arrows of the keyboard : \n"""
        t.insert(END, corps4, 'corpus')
        t.insert(END, bullet+" Up arrow       ", 'special') 
        t.insert(END, ": Direction is Up\n", 'corpus')
        t.insert(END, bullet+" Right arrow   ", 'special') 
        t.insert(END, ": Direction is Right\n", 'corpus')
        t.insert(END, bullet+" Down arrow  ", 'special') 
        t.insert(END, ": Direction is Down\n", 'corpus')
        t.insert(END, bullet+" Left arrow     ", 'special') 
        t.insert(END, ": Direction is Left\n\n", 'corpus')
        corps5="""To select a diagonal direction use the arrows of the keyboard while pressing the Option key :\n"""
        t.insert(END, corps5, 'corpus')
        t.insert(END, bullet+" Option+Up arrow       ", 'special') 
        t.insert(END, ": Direction is UpRight\n", 'corpus')
        t.insert(END, bullet+" Option+Right arrow   ", 'special') 
        t.insert(END, ": Direction is DownRight\n", 'corpus')
        t.insert(END, bullet+" Option+Down arrow  ", 'special') 
        t.insert(END, ": Direction is DownLeft\n", 'corpus')
        t.insert(END, bullet+" Option+Left arrow     ", 'special') 
        t.insert(END, ": Direction is UpLeft\n\n", 'corpus')
        corps6="""To select a Clockwise or Anticlockwise direction use the triangle of the keyboard: \n"""
        t.insert(END, corps6, 'corpus')
        t.insert(END, bullet+" > ", 'special') 
        t.insert(END, ": Direction is Clockwise\n", 'corpus')
        t.insert(END, bullet+" < ", 'special') 
        t.insert(END, ": Direction is Anticlockwise\n\n", 'corpus')
        corps7="""If you are unsure about the direction and do not want to inform it, please do not leave blank otherwise the case will not be considered finished :\n"""
        t.insert(END, corps7, 'corpus')
        t.insert(END, bullet+" ? ", 'special') 
        t.insert(END, ": No direction\n\n", 'corpus')


        # option2 section
        t.insert(END, "Option 2\n", 'italic')
        corps3="""To select a criteria for this option, press a number between 1 and 5 on the keyboard. If you are unsure about the stabilty and do not want to inform it, please do not leave blank otherwise the case will not be considered finished :\n"""
        t.insert(END, corps3, 'corpus')
        t.insert(END, bullet+" 1 ", 'special') 
        t.insert(END, ": Option 2 is 1\n", 'corpus')
        t.insert(END, bullet+" 2 ", 'special') 
        t.insert(END, ": Option 2 is 2\n", 'corpus')
        t.insert(END, bullet+" 3 ", 'special') 
        t.insert(END, ": Option 2 is 3\n", 'corpus')
        t.insert(END, bullet+" 4 ", 'special') 
        t.insert(END, ": Option 2 is 4\n", 'corpus')
        t.insert(END, bullet+" 5 ", 'special') 
        t.insert(END, ": Option 2 is 5\n", 'corpus')
        t.insert(END, bullet+" ~ ", 'special') 
        t.insert(END, ": Nothing happened\n\n", 'corpus')

        # Speed section 
        t.insert(END, "Speed selector\n", 'italic')
        t.insert(END, """To modify the speed of the frame rate, you can use the drop-down menu or the following keys :\n""", 'corpus')
        t.insert(END, bullet+" ] ", 'special') 
        t.insert(END, ": Increase speed\n", 'corpus')
        t.insert(END, bullet+" [ ", 'special') 
        t.insert(END, ": Decrease speed\n\n", 'corpus')

        ##### Button ######
        # define back to the line + alinea
        space = """\n
        """
        # insert space
        t.insert(END, space, 'corpus')
        # create a button 'start new labelling'
        b1=Button(master, text="Start new labelling", font=font_corpus, command= lambda : self.newLabelling(master))
        # display the button
        t.window_create(END, window=b1)
        
        # insert space
        t.insert(END, space, 'corpus')
        # create a button 'resume labelling'
        b2=Button(master, text="Resume labelling", font=font_corpus, command= lambda : self.resumeLabelling(master))
        # display the button
        t.window_create(END, window=b2)

        # set the text widget to not modifiable by the user 
        t.configure(state=DISABLED)

    def newLabelling (self, *args) :
        # detroy the drop down menu of the header 
        A.drop_down_menu.destroy()
        # recreate the dropdown menu with the name of the good section you are in 
        A.createDropDownMenu('Start new labelling')
        # destroy all the widget in the white space of the window (under the header)
        for widgets in A.main_container.winfo_children():
            widgets.destroy()
        # create a MainPage object in the white space instead 
        MainPage(A.main_container, '~/Downloads/Data.csv')

    def resumeLabelling (self, *args) :
        # execute the selectFile function to obtain the path of the file you want to resume labelling 
        A.selectFile()                
        # detroy the drop down menu of the header 
        A.drop_down_menu.destroy()
        # recreate the dropdown menu with the name of the good section you are in 
        A.createDropDownMenu('Resume labelling')
        # destroy all the widget in the white space of the window (under the header)
        for widgets in A.main_container.winfo_children():
            widgets.destroy()
        # create a MainPage object in the white space instead with the path as an argument
        MainPage(A.main_container, A.path) 
            

""" ######################################### LABELLING INSTRUCTIONS ######################################### """


class Labelling_instructions (Frame) : 
    """ This class heritates the Tkinter Frame class, Labelling_instructions is also a tkinter Frame widget"""

    def __init__(self, master):
        """ 
        Constructor of the class GUI_instructions. 
        
        master :  master frame (main_container) which will be the parent of the Labelling_instructions object
        return : nothing but display the GUI instructions  
        """
        # all the objects of the Labelling_instructions class get the methods of the Frame tkinter class
        Frame.__init__(self, master)

    # LABEL WITH THE INSTRUCTIONS #
        # define the bullet 
        bullet = "•"
        # create the text widget 
        t = Text(master)
        # create the scrollbar widget 
        scroll = Scrollbar(master, command= t.yview)
        # effectiveness of the scrollbar in the text widget   
        t.configure(yscrollcommand=scroll.set, wrap=WORD, bd=50)

        # configure the different fonts which will be used in the text widget
        t.tag_configure('image', justify='center')
        t.tag_configure('title', font=font_title, justify='center')
        t.tag_configure('corpus', foreground='black', font=font_corpus)
        t.tag_configure('special', foreground='#15AFDA', font=('Helvetica', 20, 'bold'))
        t.tag_configure('italic', foreground='black', font=('Helvetica', 17, 'italic', 'bold'))

        # display the text widget 
        t.pack(fill="both", side=LEFT, expand=True)
        # display the scrollbar on the right of the text widget
        scroll.pack(fill=Y, side=LEFT)

        # Title #
        # insert the string in the text widget with the title font
        t.insert(END,'Spatial Labelling Instructions (V1)\n\n', 'title')

        # Intro #
        corps1  = """
        These instructions are here to explain to the users how to label properly the videos according to the possible options.\n\n"""

        t.insert(END, corps1, 'corpus')

        # Instructions #
        t.insert(END, bullet+" Image for the instructions\n", 'special')
        

        ###### Image 1 #####
        global im_instructions1
        im_instructions1 = PhotoImage(file = "./GUI_images/instructions.png").subsample(3,3)
        t.insert(END, """
                                                                    """, 'corpus')
        t.image_create(END, image = im_instructions1)


      
        ##### Button ######
        # define back to the line + alinea
        space = """\n
        """
        # insert space
        t.insert(END, space, 'corpus')
        # create a button 'start new labelling'
        b1=Button(master, text="Start new labelling", font=font_corpus, command= lambda : self.newLabelling(master))
        # display the button
        t.window_create(END, window=b1)
        
        # insert space
        t.insert(END, space, 'corpus')
        # create a button 'resume labelling'
        b2=Button(master, text="Resume labelling", font=font_corpus, command= lambda : self.resumeLabelling(master))
        # display the button
        t.window_create(END, window=b2)

        # set the text widget to not modifiable by the user 
        t.configure(state=DISABLED)

    def newLabelling (self, *args) :
        # detroy the drop down menu of the header 
        A.drop_down_menu.destroy()
        # recreate the dropdown menu with the name of the good section you are in 
        A.createDropDownMenu('Start new labelling')
        # destroy all the widget in the white space of the window (under the header)
        for widgets in A.main_container.winfo_children():
            widgets.destroy()
        # create a MainPage object in the white space instead 
        MainPage(A.main_container, '~/Downloads/Data.csv')

    def resumeLabelling (self, *args) :
        # execute the selectFile function to obtain the path of the file you want to resume labelling 
        A.selectFile()                
        # detroy the drop down menu of the header 
        A.drop_down_menu.destroy()
        # recreate the dropdown menu with the name of the good section you are in 
        A.createDropDownMenu('Resume labelling')
        # destroy all the widget in the white space of the window (under the header)
        for widgets in A.main_container.winfo_children():
            widgets.destroy()
        # create a MainPage object in the white space instead with the path as an argument
        MainPage(A.main_container, A.path) 
    

""" ######################################### MAIN PAGE ######################################### """


class MainPage(Frame):
    """ This class heritates the Tkinter Frame class, MainPage is also a tkinter Frame widget """

    def __init__ (self, master, title):
        """ 
        Constructor of the class MainPage. This class generates a page on which it will be possible to label the videos 
        
        master :  master frame (main_container) which will be the parent of the MainPage object
        title : String; give the path to the directory of the CSV file
        return : nothing but display the labelling page   
        """
        # all the objects of the MainPage class get the methods of the Frame tkinter class
        Frame.__init__(self, master)

    # Atrrributes definition 
        # save the dataframe in the data attribute to be called at anytime 
        # each time you create a Main Page, it refers to a different DataBank object
        self.data = DataBank(title)
        # set up the case and picture attributes which will contain respectively the number of the current case and  window 
        self.case = 0
        self.picture= 0
        # collect all the cases available in a list according to the dataframe created by the DataBank object 
        self.CASE_OPTIONS = self.data.df["Case"].unique()
        # set up the 2 options and comment attributes which will contain the data selected  
        self.option1 = str
        self.option2 = str
        self.comment = str
        # create the list of the speed options for the videos frame rate (in ms between 2 frames)
        self.SPEED_OPTIONS = [120, 60, 30, 10]
        # indice of the speed options list set up for normal speed (30ms between 2 frames)
        self.speedInd = 2

    # FRAME OF THE CASE #
        # create a frame widget to manage the cases
        self.case_frame = Frame(master,height=50)
        # fix the size of the frame independantly of the widgets inside
        self.case_frame.pack_propagate(0)
        # display the frame
        self.case_frame.pack(side = "top", fill="x")

        # create 2 columns in the case_frame (equal size) to place easily the widgets insisde and not to move according tot their size
        self.case_frame.columnconfigure(0, weight=1)
        self.case_frame.columnconfigure(1, weight=1)

        # create and display a frame widget in the first column 
        self.frame1 = Frame(self.case_frame,height=50)
        self.frame1.pack_propagate(0)
        self.frame1.grid(column=0, row=0, sticky=NSEW)

        # create and display a frame in the second column 
        self.frame2 = Frame(self.case_frame,height=50)
        self.frame2.pack_propagate(0)
        self.frame2.grid(column=1, row=0, sticky=NSEW)
        
        # Case selection #
        # Check which cases is entirely filled in and also save in an attribute these cases filled in not to check this for all case in the future
        self.checkAllCases()
        # create a drop down menu to chose the case, need to be an attribute to be called anytime
        self.drop_down_case = self.createDropDownCase('Number')

        # Speed selection #
        # create a drop down menu to chose the frame rate, need to be an attribute to be called anytime
        self.drop_down_speed = self.createDropDownSpeed()

    # FRAME OF THE PROGRESS #
        # create and display a frame where the advancement in the case will be updated
        self.progress_frame = Frame(master)
        self.progress_frame.pack(side = "top", fill="x")

    # FRAME OF THE WIDGETS #
        # create and display a frame for the labelling widgets
        self.widget_frame = Frame(master, background="white")
        # fix the size of the frame independantly of the widgets inside
        self.widget_frame.pack_propagate(0)
        # display the frame
        self.widget_frame.pack(side="top", fill="both", expand=True)

        # create 6 columns in the widget_frame (inequal size) to arrange widgets in the widget_frame 
        self.widget_frame.columnconfigure(0, weight=2)
        self.widget_frame.columnconfigure(1, weight=2) 
        self.widget_frame.columnconfigure(2, weight=3) 
        self.widget_frame.columnconfigure(3, weight=3)
        self.widget_frame.columnconfigure(4, weight=2) 
        self.widget_frame.columnconfigure(5, weight=2)

        # create 5 rows in the widget_frame (inequal size) to arrange widgets in the widget_frame 
        self.widget_frame.rowconfigure(0, weight=1)
        self.widget_frame.rowconfigure(1, weight=4)
        self.widget_frame.rowconfigure(2, weight=1)
        self.widget_frame.rowconfigure(3, weight=1)
        self.widget_frame.rowconfigure(4, weight=1)

    # FRAME OF THE BUTTONS #
        # create a frame for the switching (next and previou) buttons 
        self.buttons_frame = Frame(master, height=50)
        # fix the size of the frame independantly of the widgets inside
        self.buttons_frame.pack_propagate(0)
        # display the frame at the bottom of the page 
        self.buttons_frame.pack(side="bottom", fill="x")
        
        # create 2 columns in the buttons_frame (equal size)
        self.buttons_frame.columnconfigure(0, weight=1)
        self.buttons_frame.columnconfigure(1, weight=1)

        # create the previous button with all the features
        self.button_previous = Button(self.buttons_frame, 
            text="Previous", 
            height=2,
            width=20, 
            font=font_case,
            fg = "black",
            relief=GROOVE,
            command=self.previousPicture,
            takefocus=1
            )
        # display the previous buttons in the left column
        self.button_previous.grid(column=0, row=0)

         # create the previous button with all the features
        self.button_next = Button(self.buttons_frame,
            text="Next", 
            height=2,
            width=20,
            font=font_case,
            fg = "black",
            relief=GROOVE,
            command=self.nextPicture, 
            takefocus=1
            )
        # display the previous buttons in the right column
        self.button_next.grid(column=1, row=0)


    ######################################### METHODS OF THE MAIN PAGE #########################################       

    def createDropDownOption1 (self, title):
        """ 
        createDropDownOption1 returns the drop down menu of the option1 with the correct selected option.
        
        title : string, give the title of the drop down menu when first displayed 
        return : drop down menu of the option1
        """
        # list of the options available 
        OPTIONS1 = [Up, UpRight, Right, DownRight, Down, DownLeft, Left, UpLeft, Clockwise, AntiClockwise, "-", " "]
        # set up the option selected
        self.option1_selected = StringVar(self.widget_frame, value=title)
        # create the drop down menu
        self.drop_down_option1 = OptionMenu(self.widget_frame, self.option1_selected, *OPTIONS1)
        # configure the font of the options 
        self.case_frame.nametowidget(self.drop_down_option1.menuname).config(font=font_corpus)
        # configure the font of the option selected
        self.drop_down_option1.config(font=font_corpus, background="white", width=5, fg = "black")
        # display the drop down menu at a given position
        self.drop_down_option1.grid(column=3, row=1, sticky=SW, padx=20)
        # if option selected changes, it executes the changeCSV method
        self.option1_selected.trace("w", self.changeCSV)
        # return the drop down menu
        return self.drop_down_option1


    def createDropDownOption2 (self, title):
        """ 
        createDropDownOption2 returns the drop down menu of the option2 with the correct selected option.
        
        title : string, give the title of the drop down menu when first displayed 
        return : drop down menu of the option2
        """
        # list of the options available 
        OPTIONS2 = ["1", "2", "3", "4", "5", "-", " "]
        # set up the option selected
        self.option2_selected = StringVar(self.widget_frame, value=title)
        # create the drop down menu
        self.drop_down_option2 = OptionMenu(self.widget_frame, self.option2_selected, *OPTIONS2)
        # configure the font of the options 
        self.case_frame.nametowidget(self.drop_down_option2.menuname).config(font=font_corpus)
        # configure the font of the option selected
        self.drop_down_option2.config(font=font_corpus, background="white", width=5, fg = "black")
        # display the drop down menu at a given position
        self.drop_down_option2.grid(column=3, row=2, sticky=W, padx=20)
        # if option selected changes, it executes the changeCSV method
        self.option2_selected.trace("w", self.changeCSV)
        # return the drop down menu
        return self.drop_down_option2


    def createDropDownCase (self, title):
        """ 
        createDropDownCase returns the drop down menu of the cases with the currently case selected.
        
        title : string, give the title of the drop down menu when first displayed 
        return : drop down menu of the cases
        """
        # create and display a label indicating the case
        self.case_label = Label(self.frame1, text="Case", font=font_case)
        self.case_label.pack(side=RIGHT, padx=5)
        # set up the option selected
        self.case_selected = StringVar(self.frame2, value=title)
        # create the drop down menu
        self.drop_down_case = OptionMenu(self.frame2, 
            self.case_selected, 
            *self.CASE_DONE)
        # configure the font of the options 
        self.frame2.nametowidget(self.drop_down_case.menuname).config(font=font_case)
        # configure the font of the option selected
        self.drop_down_case.config(font=font_case)
        # display the drop down menu at a given position
        self.drop_down_case.pack(side=LEFT, padx=5)
        # if option selected changes, it executes the changeCase method
        self.case_selected.trace("w", self.changeCase)
        # return the drop down menu
        return self.drop_down_case  


    def createDropDownSpeed (self):
        """ 
        createDropDownSpeed returns the drop down menu of the speed with the correct speed currently selected.
        
        title : string, give the title of the drop down menu when first displayed 
        return : drop down menu of the speed
        """
        # list of the options available 
        SPEED_OPTIONS = ['x0.25', 'x0.5','x1.0', 'x2.0']
        # set up the option selected
        self.speed_selected = StringVar(self.frame2, value=SPEED_OPTIONS[self.speedInd])
        # create the drop down menu
        self.drop_down_speed = OptionMenu(self.frame2,
            self.speed_selected, 
            *SPEED_OPTIONS
            )
        # configure the font of the options 
        self.frame2.nametowidget(self.drop_down_speed.menuname).config(font=font_corpus)
        # configure the font of the option selected
        self.drop_down_speed.config(font=font_corpus)
        # display the drop down menu at a given position
        self.drop_down_speed.pack(side=RIGHT, padx=10)
        # if option selected changes, it executes the changeSpeed method
        self.speed_selected.trace("w", self.changeSpeed)
        
        # create  a label indicating the speeed 
        self.speed_label = Label(self.frame2, text="Speed", font=font_corpus)
        # display the label on the right of the frame but after the previous widget display (dd menu of speed)
        self.speed_label.pack(side=RIGHT)

        # return the drop down menu 
        return self.drop_down_speed
        

    def changeSpeed (self, *args):
        """ 
        changeSpeed modify the speed indice and also the frame rate of the video  
        
        return : nothing but modify the frame rate of the video 
        """
        # get the option selected in the drop down menu of the speed
        info = self.speed_selected.get()
        # check which one of the potion selected matches 
        if info == "x0.25" :
            # modify the indice in the speed list 
            self.speedInd = 0
        elif info == "x0.5" :
            # modify the indice in the speed list 
            self.speedInd = 1
        elif info == "x1.0" :
            # modify the indice in the speed list 
            self.speedInd = 2
        elif info == "x2.0" :
            # modify the indice in the speed list 
            self.speedInd = 3


    def buttonsBar (self, list):
        """ 
        buttonsBar create the list of buttons. Each one correponds to a time slot of the case 
        
        list : list of all the pictures in this case
        return : nothing but display the list of buttons in the progresss_frame 
        """
        # set up the hour anf the minutes to 0
        h=0
        min=0
        # for each picture of the case 
        for i in list :
            # create as many columns as pictures in the case
            self.progress_frame.columnconfigure(i, weight=1)
            # check if data for option1 AND option2 have been registered for this picture 
            if self.data.LoadData(self.case, i)[0] == " " and self.data.LoadData(self.case, i)[1] == " " :
                # create a red button with the time slot written on it
                Button(self.progress_frame, text=f"{h}:{min:02d}", fg='red',command=lambda i=i: self.update(i)).grid(column=i, row=0,sticky=NSEW, ipadx=20)
            # check if data for option1 OR option2 have been registered for this picture 
            elif self.data.LoadData(self.case, i)[0] == " " or self.data.LoadData(self.case, i)[1] == " " :
                # create an orange button with the time slot written on it
                Button(self.progress_frame, text=f"{h}:{min:02d}", fg='orange',command=lambda i=i: self.update(i)).grid(column=i, row=0,sticky=NSEW, ipadx=20)

            else :
                # create a green button with the time slot written on it
                Button(self.progress_frame, text=f"{h}:{min:02d}", fg='green',command=lambda i=i: self.update(i)).grid(column=i, row=0,sticky=NSEW, ipadx=20)
            # update the minutes according to the picture number 
            if min <45 :
                min+=15
            # update the hours according to the picture number 
            else :
                h+=1
                min=0
    

    def generateTimeSlot (self, picture):
        """ 
        generateTimeSlot gives the time slot of the picture given in argument of the method
        
        picture : picture number (int)
        return : time slot of the number (str) 
        """
        # there are 4 pictures per hour, calculate the minutes of the time slot
        if picture%4 == 0:
            min = '00'
        elif picture%4 == 1:
            min = '15'
        elif picture%4 == 2:
            min = '30'
        elif picture%4 == 3:
            min = '45'
        # concatenate the hour indicator with the minute indicator 
        timeSlot = str(picture//4)+':'+min
        return timeSlot


    def loadFrames (self):
        """ 
        loadFrames saves all the frames of the case from the numpy array to a list which is an attribute of the class 
        this is required otherwise the call of a frame in the numpy array can't be used to display the array
        
        return : nothing but update the argument with the frames of the current case 
        """
        # scan all the pictures of the case
        for elt in self.PICTURE_OPTIONS :   
            # add the colored and resized frames from the numpy array to the list, need to be an attribute to be called to be displayed
            self.frames.append([ImageTk.PhotoImage(image = Image.fromarray(np.uint8(cm.Reds(self.array64[elt][i])*255)).resize((250, 250))) for i in range (87)])


    def changeCase (self, *args):
        """ 
        changeCase changes the case number and also modify everything according to the case (picture number, videos, data, ... ) 
        
        return : nothing but update the current case 
        """
        # case number different of 0, avoid to search the first time when case=='0' because any case have been previously modified
        if self.case != 0:
            # loop through the pictures in the previously treated case 
            for j in self.data.df[self.data.df["Case"] == int(self.case)]["Picture"] :
                # check if data for option1 or option2 exist in the CSV file
                if self.data.LoadData(self.case, j)[0] == " " or self.data.LoadData(self.case, j)[1] == " " :
                    # leave the number of the case as is in the attribute containing the cases already filled in
                    self.CASE_DONE[int(self.case)-1] = str(self.CASE_OPTIONS[int(self.case)-1])
                    break
                else :
                    # else, update the attribute containing the cases already filled in with a star next to the case number
                    self.CASE_DONE[int(self.case)-1] = str(self.CASE_OPTIONS[int(self.case)-1])+' *'

        # create  and display a loading label the time the frames are saved in the list as attribute to be displayed later
        self.loading = Label(self.widget_frame, text='Loading...', bg='white', fg='black', font=font_title)
        self.loading.grid(column=0, columnspan=6, row=0, rowspan=5, sticky=NSEW)
        # get the number of the case in the drop down menu of the case 
        test = self.case_selected.get()
        # simplify the case number if the case was entirely completed (* added after the number)
        self.case = test.split(" *")[0]
        # pick up all the pictures among the current case 
        self.PICTURE_OPTIONS = self.data.df[self.data.df["Case"] == int(self.case)]["Picture"]
        # create empty frame ready to get all the frames of the case
        self.frames = []
        
        # destroy the label and the drop down menu of the case 
        self.drop_down_case.destroy()
        self.case_label.destroy()
        # recreate the drop down menu with the right case number display on it 
        self.drop_down_case = self.createDropDownCase(self.case)
        # wait 2ms for the loading label to display, otherwise the loading label don't have the time be displayed 
        self.loading.after(2)
        # load the numpy array of raw data corresponding to the current case in the array8 attribute of the class
        self.array8=np.load(f"./numpyArrays8by8/{self.case}.npy", allow_pickle=True)
        # interpolate with the avgIntrep method the array8by8 to get a 64by64 array (increase the quality of the frame)
        self.array64=self.avgInterp(self.array8)
        # set the range to be between 1st percentile and zero (select negative and avoid outlier in negative)
        self.array64 = np.clip(self.array64, a_min=np.percentile(self.array64, 1), a_max=0)
        # set the minimum to zero
        self.array64 = -self.array64
        # set the max to one, 
        self.array64 = self.array64/np.max(self.array64)
        # load frames in the list attribute 
        self.loadFrames()
        # destroy the loading label once everything is loaded
        self.loading.destroy()
        # update everything on the page according to the change of the case number and setup the picture number to the first (0)
        self.update(0)


    def update (self, index_picture):
        """ 
        update modifies all the widgets of the MainFrame according to the change of case or picyure number.
        
        index_picture : (int) new picture number 
        return : nothing but update the widgets  
        """
        # update of the picture attribute with the current picture number selected 
        self.picture=index_picture
        # destroy all the widgets in the progress_frame
        for widgets in self.progress_frame.winfo_children():
            widgets.destroy()
        # recreate all the buttons for each picture of the case using buttonBar method 
        self.buttonsBar(self.PICTURE_OPTIONS)
        # destroy all the labelling widgets in the widget_frame
        for widgets in self.widget_frame.winfo_children():
            widgets.destroy()
        # Recreate the progress bar 
        self.achieved = Progressbar(self.progress_frame, orient=HORIZONTAL, mode="determinate")
        # display the progress bar
        self.achieved.grid(columnspan=len(self.PICTURE_OPTIONS) ,row=1, sticky=NSEW)
        # update the value of this progress bar according to the picture number
        self.achieved['value'] = self.picture*100/len(self.PICTURE_OPTIONS)+50/len(self.PICTURE_OPTIONS)

        # create and display an empty label in which the video of the previous picture will be display
        self.labelPrev = Label(self.widget_frame, bg='white')
        self.labelPrev.grid(column=0, columnspan=2, row=1, sticky=NSEW)
        # create and display an empty label in which the video of the current picture will be display
        self.label = Label(self.widget_frame, bg='white')
        self.label.grid(column=2, columnspan=2, row=0, rowspan=2, sticky=NSEW)
        # create and display an empty label in which the video of the next picture will be display
        self.labelNext = Label(self.widget_frame, bg='white')
        self.labelNext.grid(column=4, columnspan=2, row=1, sticky=NSEW)
        
        # create 3 labels indicating the corresponding the widget
        Label(self.widget_frame, text="Comments", background="white", font = font_case, fg = "black").grid(column=2, columnspan=2, row=3)
        Label(self.widget_frame, text="Option 2", background="white", font = font_case, fg = "black").grid(column=2, row=2, sticky=E)
        Label(self.widget_frame, text="Option 1", background="white", font = font_case, fg = "black").grid(column=2, row=1, sticky=SE)
        # create and display an empty entry bar for the comments
        self.comment_entry = Entry(self.widget_frame)
        self.comment_entry.grid(column=2, columnspan=2, row=4, sticky=N)
        
        # create the drop down menus for the option1 and the option2 with methods of the class
        self.option1MenuPrev = self.createDropDownOption1(self.data.LoadData(self.case, self.picture)[0])
        self.option2MenuPrev = self.createDropDownOption2(self.data.LoadData(self.case, self.picture)[1])
        # update the comment slot with previously filled in comments of this picture (if exist)
        self.comment_entry.insert(0, str(self.data.LoadData(self.case, self.picture)[2]))

        # create a Previous and Next label a the top the previous and next label where the videos will be displayed
        self.previous_label = Label(self.widget_frame, text='                                                  ', font=font_case, bg='white', fg = "black")
        self.previous_label.grid(column=0, columnspan=2, row=0, pady=10)
        self.next_label = Label(self.widget_frame, text='                                                  ', font=font_case, bg='white', fg = "black")
        self.next_label.grid(column=4, columnspan=2, row=0, pady=10)

        # create and display a label indicating the time slot of the current picture 
        self.timeslot = Label(self.widget_frame, text=self.generateTimeSlot(self.picture), font=font_case, bg='white', fg = "black")
        self.timeslot.grid(column=2, columnspan=2, row=0, sticky=N, pady=50)
        # create and display a label indicating the seconds running in the video of the current picture 
        self.counter = Label(self.widget_frame, text='', font=font_corpus, bg='white', fg = "black")
        self.counter.grid(column=2, columnspan=2, row=1, sticky=S, pady=70)

        # check if picture number strictly above 0 not to display an unexisting previous video
        if self.picture > 0 : 
            # display previous in the label above the previous video
            self.previous_label.configure(text='Previous', font=font_case)
            # display labels indicating the option2 data of the previous picture of this case 
            Label(self.widget_frame, text="Option 2 : ", background="white", font = font_corpus, fg = "black", width=10).grid(column=0, row=3, sticky=E)
            Label(self.widget_frame, text=self.data.LoadData(self.case, self.picture-1)[1], background="white", font = font_corpus, fg = "black", width=10).grid(column=1, row=3, sticky=W)
            # display labels indicating the option1 data of the previous picture of this case 
            Label(self.widget_frame, text="Option 1 : ", background="white", font = font_corpus, fg = "black", width=10).grid(column=0, row=2, sticky=SE)
            Label(self.widget_frame, text=self.data.LoadData(self.case, self.picture-1)[0], background="white", font = font_corpus, fg = "black", width=10).grid(column=1, row=2, sticky=SW)
            # create and display a label indicating the time slot of the previous picture 
            self.timeslot = Label(self.widget_frame, text=self.generateTimeSlot(self.picture-1), font=font_corpus, bg='white', fg = "black")
            self.timeslot.grid(column=0, columnspan=2, row=1, sticky=N)
            # create and display a label indicating the seconds running in the video of the previous picture
            self.counterPrev = Label(self.widget_frame, text='', font=font_corpus, bg='white', fg = "black")
            self.counterPrev.grid(column=0, columnspan=2, row=1, sticky=S)

        # check if picture number strictly below the last picture number not to display an unexisting next video
        if self.picture < self.PICTURE_OPTIONS.max(): 
            # display next in the label above the next video
            self.next_label.configure(text='Next', font=font_case)
            # display labels indicating the option2 data of the next picture of this case
            Label(self.widget_frame, text="Option 2 : ", background="white", font = font_corpus, fg = "black", width=10).grid(column=4, row=3, sticky=E)
            Label(self.widget_frame, text=self.data.LoadData(self.case, self.picture+1)[1], background="white", font = font_corpus, fg = "black", width=10).grid(column=5, row=3, sticky=W)
            # display labels indicating the option1 data of the next picture of this case 
            Label(self.widget_frame, text="Option 1 : ", background="white", font = font_corpus, fg = "black", width=10).grid(column=4, row=2, sticky=SE)
            Label(self.widget_frame, text=self.data.LoadData(self.case, self.picture+1)[0], background="white", font = font_corpus, fg = "black", width=10).grid(column=5, row=2, sticky=SW)            
            # create and display a label indicating the time slot of the next picture 
            self.timeslot = Label(self.widget_frame, text=self.generateTimeSlot(self.picture+1), font=font_corpus, bg='white', fg = "black")
            self.timeslot.grid(column=4, columnspan=2, row=1, sticky=N)
            # create and display a label indicating the seconds running in the video of the next picture
            self.counterNext = Label(self.widget_frame, text='', font=font_corpus, bg='white', fg = "black")
            self.counterNext.grid(column=4, columnspan=2, row=1, sticky=S)
        # display the 3 videos at the same time in the corresponding labels previously created as attribute to be called at anytime
        self.show()

        # give focus for the shortcut to all the widget on the main page
        self.widget_frame.focus_set()

        # all the line bellow work the same way : 
            # self.widget_frame.bind("*", ~) -> means execute the ~ method if * key is pressed and widget_frame is focus
        self.widget_frame.bind("<space>", self.nextPicture)
        self.widget_frame.bind("<Shift-space>", self.previousPicture)
        self.widget_frame.bind("1", self.shortcut1)
        self.widget_frame.bind("2", self.shortcut2)
        self.widget_frame.bind("3", self.shortcut3)
        self.widget_frame.bind("4", self.shortcut4)
        self.widget_frame.bind("5", self.shortcut5)
        self.widget_frame.bind("<`>", self.shortcutNoStab)

        self.widget_frame.bind("<Up>", self.shortcutUp)
        self.widget_frame.bind("<Down>", self.shortcutDown)
        self.widget_frame.bind("<Right>", self.shortcutRight)
        self.widget_frame.bind("<Left>", self.shortcutLeft)

        self.widget_frame.bind("<Option-Up>", self.shortcutUpRight)
        self.widget_frame.bind("<Option-Right>", self.shortcutDownRight)
        self.widget_frame.bind("<Option-Left>", self.shortcutUpLeft)
        self.widget_frame.bind("<Option-Down>", self.shortcutDownLeft)

        self.widget_frame.bind("<,>", self.shortcutAntiClockwise)
        self.widget_frame.bind("<.>", self.shortcutClockwise)
        self.widget_frame.bind("</>", self.shortcutNoDir)

        self.widget_frame.bind("<]>", self.shortcutSpeedUp)
        self.widget_frame.bind("<[>", self.shortcutSpeedDown)

        self.widget_frame.bind("<1>", self.focus)
        self.label.bind("<1>", self.focus)
        self.labelNext.bind("<1>", self.focus)
        self.labelPrev.bind("<1>", self.focus)        


    def focus (self, event=None) :  
        """ 
        focus gives focus to the frame_widget and save the comments from the Entry widget to the CSV file.
        
        event : means the method can be used for shortcuts with bind function
        return : nothing but save the comment  
        """
        # save the comments in the CSV file using SaveComment method
        self.data.SaveComment(self.case, self.picture, self.comment_entry.get())
        # set focus on the widget_frame for keyboard shortcuts to be use
        self.widget_frame.focus()


    def previousPicture (self, event=None):
        """ 
        previousPicture modifies the picture number to the previous one if possible.
        
        event : means the method can be used for shortcuts with bind function
        return : nothing but decrease the picture number and update the widgets
        """
        # save the comments in the CSV file using SaveComment method
        self.data.SaveComment(self.case, self.picture, self.comment_entry.get())
        # if picture number above the minimum 
        if self.picture > self.PICTURE_OPTIONS.min() : 
            # update everything on the page with picture number -= 1
            self.update (self.picture - 1)


    def nextPicture (self, event=None):
        """ 
        nextPicture modifies the picture number to the next one if possible.
        
        event : means the method can be used for shortcuts with bind function
        return : nothing but increase the picture number and update the widgets 
        """
        # save the comments in the CSV file using SaveComment method
        self.data.SaveComment(self.case, self.picture, self.comment_entry.get())
        # if picture number below the maximum 
        if self.picture < self.PICTURE_OPTIONS.max() : 
            # update everything on the page with picture number += 1
            self.update (self.picture + 1)
        # if picture number equals the maximum to update to progress bar to 100% otherwise it will never be reached 
        elif self.picture == self.PICTURE_OPTIONS.max() : 
            # update everything on the page with picture number == maximum picture number
            self.update (self.picture)
            # update the progress bar to 100% 
            self.achieved['value'] = 100
        

    def changeCSV (self, *args):
        """ 
        changeCSV update the data of the 2 options of labelling in the CSV file.
        
        return : nothing but update the CSV file 
        """
        # update options attributes to the selected one
        self.option1 = self.option1_selected.get()
        self.option2 = self.option2_selected.get()
        # save in the dataframe then in the CSV file using the SaveData method
        self.data.SaveData (self.case, self.picture, self.option1, self.option2)

    def display(self, list, ind, master, counter):
        """ 
        recursive display function displays the video frames by frames of the numpy array according to the case and picture number.
        
        list : list of all the frames 
        ind : the number of the currently display frame 
        master : widget in which the frames will be displayed
        counter : widget displaying the second running of the video
        return : nothing but display the video of the picture 
        """
        # extraction of a frame among the list of frames, not possible to call directly from the np array 
        frame = list[ind]
        # update the counter for the second (4 frames per second)
        counter.configure(text = str(ind//4)+' s')
        # next frame 
        ind += 1
        # if maximal frame number reach
        if ind == len(list):
            # back to first frame
            ind = 0
            # wait 100ms between each loop 
            master.after(100)
        # display the extracted frame in the corresponding master widget (label)
        master.configure(image=frame)
        # wait the time given by the speed selection before repeat the method (loop)
        master.after(self.SPEED_OPTIONS[self.speedInd], self.display, list, ind, master, counter)


    def show(self):
        """ 
        show displays the 3 videos simultaneously of the previous, current and next picture thank to the display method.
        
        return : nothing but display the videos
        """
        # picture number above the minimum not to display unexisting video
        if self.picture > 0 : 
            # execute the display method in the previous label for curernt picture-1
            self.labelPrev.after(0, self.display, self.frames[self.picture-1], 0, self.labelPrev, self.counterPrev)
        # execute the display method in the label for current picture
        self.label.after(0, self.display, self.frames[self.picture], 0, self.label, self.counter)
        # picture number below the maximum  not to display unexisting video
        if self.picture < self.PICTURE_OPTIONS.max():
            # execute the display method in the next label for current picture+1
            self.labelNext.after(0, self.display, self.frames[self.picture+1], 0, self.labelNext, self.counterNext)


    def checkAllCases(self):
        """ 
        checkAllCases checks which cases are completely done (every video labelled).
        
        return : list of the cases done
        """
        # create an empty list which will contain to cases completely fille in (marked by a symbol)
        self.CASE_DONE =[]     
        # loop through the cases  
        for i in self.CASE_OPTIONS :
            # pick up all the pictures available in the case
            PICTURE_OPTIONS = self.data.df[self.data.df["Case"] == i]["Picture"]
            # loop through the pictures in the case 
            for j in PICTURE_OPTIONS :
                # check if data for the 2 options exist
                if self.data.LoadData(i, j)[0] == " " or self.data.LoadData(i, j)[1] == " " :
                    # leave the number of the case as is in the attribute containing the cases already filled in
                    number = str(i)
                    break
                else :
                    # else, update the attribute containing the cases already filled in with a star next to the case number
                    number = str(i)+' *'
            # add the case number in the list which is an attribute of the class to be called at anytime 
            self.CASE_DONE.append(number)
            

    def avgInterp(self, inwaves, res=64):
        """ 
        avgInterp interpolate a numpy array to increase the size of the 2D arrays it contains.
        
        inwaves : numpy array in input of the method containing all the frames of a case 
        res : final size of the 2D arays wanted, default size is 64
        return : the interpolated array with a bigger size
        """
        # number of windows in the case
        nwin = inwaves.shape[0]
        # number of frames in the window
        nframe = inwaves.shape[1]
        # set the size of the uotput array 
        outwave = np.zeros((nwin, nframe, res, res))
        xi, yi = np.linspace(0, 8, res), np.linspace(0, 8, res)
        # loop through windows
        for win in range(0, nwin):
            # loop through frames 
            for t in range(0, nframe):
                # create a function f which interpolate the inwave acoording to the frames and window number 
                f = interpolate.interp2d(
                    x=np.arange(8),
                    y=np.arange(8),
                    z=inwaves[win, t, :, :],
                    # linear intrepolation
                    kind='linear'
                )
                # save the interpolation in the output array
                outwave[win, t, :, :] = f(xi, yi)

        return outwave
        


#################### Shortcuts : option2 ####################

        # all the methods bellow work the same way : 

    def shortcut1(self, event=None):
        """ 
        shortcut1 modifies the option2 drop down menu to 1.
        
        event : means the method can be used for shortcuts with bind function
        return : nothing but modify the drop down menu and update the CSV file 
        """
        # destroy the option2 drop down menu
        self.drop_down_option2.destroy()
        # recreate the option2 drop down menu with 1 for option2
        self.createDropDownOption2('1')
        # update the CSV file with the new option2
        self.changeCSV()

    def shortcut2(self, event=None):
        self.drop_down_option2.destroy()
        self.createDropDownOption2('2')
        self.changeCSV()

    def shortcut3(self, event=None):
        self.drop_down_option2.destroy()
        self.createDropDownOption2('3')
        self.changeCSV()

    def shortcut4(self, event=None):
        self.drop_down_option2.destroy()
        self.createDropDownOption2('4')
        self.changeCSV()

    def shortcut5(self, event=None):
        self.drop_down_option2.destroy()
        self.createDropDownOption2('5')
        self.changeCSV()

    def shortcutNoStab(self, event=None):
        self.drop_down_option2.destroy()
        self.createDropDownOption2('-')
        self.changeCSV()

#################### Shortcuts : option1 ####################

    def shortcutUp(self, event=None):
        self.drop_down_option1.destroy()
        self.createDropDownOption1(Up)
        self.changeCSV()

    def shortcutDown(self, event=None):
        self.drop_down_option1.destroy()
        self.createDropDownOption1(Down)
        self.changeCSV()
        
    def shortcutLeft(self, event=None):
        self.drop_down_option1.destroy()
        self.createDropDownOption1(Left)
        self.changeCSV()

    def shortcutRight(self, event=None):
        self.drop_down_option1.destroy()
        self.createDropDownOption1(Right)
        self.changeCSV()

    def shortcutUpRight(self, event=None):
        self.drop_down_option1.destroy()
        self.createDropDownOption1(UpRight)
        self.changeCSV()

    def shortcutDownRight(self, event=None):
        self.drop_down_option1.destroy()
        self.createDropDownOption1(DownRight)
        self.changeCSV()

    def shortcutDownLeft(self, event=None):
        self.drop_down_option1.destroy()
        self.createDropDownOption1(DownLeft)
        self.changeCSV()

    def shortcutUpLeft(self, event=None):
        self.drop_down_option1.destroy()
        self.createDropDownOption1(UpLeft)
        self.changeCSV()

    def shortcutClockwise(self, event=None):
        self.drop_down_option1.destroy()
        self.createDropDownOption1(Clockwise)
        self.changeCSV()

    def shortcutAntiClockwise(self, event=None):
        self.drop_down_option1.destroy()
        self.createDropDownOption1(AntiClockwise)
        self.changeCSV()

    def shortcutNoDir(self, event=None):
        self.drop_down_option1.destroy()
        self.createDropDownOption1('-')
        self.changeCSV()

#################### Shortcuts : speed ####################

    def shortcutSpeedUp(self, event=None):
        """ 
        shortcut1 modifies the option2 drop down menu to 1.
        
        event : means the method can be used for shortcuts with bind function
        return : nothing but increase the speed of the frame rate  
        """
        # destroy the speed drop down menu
        self.drop_down_speed.destroy()
        # destroy the speed label
        self.speed_label.destroy()
        # not maximum speed
        if self.speedInd < 3 :
            # increase speed indice (modify the speeed with spee list)
            self.speedInd+=1 
        # maximum speed 
        else :
            # speed stays the same
            self.speedInd= 3
        # update the speed drop down menu with the new one 
        self.drop_down_speed = self.createDropDownSpeed()

    def shortcutSpeedDown(self, event=None):
        """ 
        shortcut1 modifies the option2 drop down menu to 1.
        
        event : means the method can be used for shortcuts with bind function
        return : nothing but decrease the speed of the frame rate  
        """
        # destroy the speed drop down menu
        self.drop_down_speed.destroy()
        # destroy the speed label
        self.speed_label.destroy()
        # not minimu speed
        if self.speedInd > 0 :
            # decrease speed indice (modify the speeed with spee list)
            self.speedInd=self.speedInd-1 
        # minimum speed 
        else :
            # speed stays the same
            self.speedInd=0
        # update the speed drop down menu with the new one
        self.drop_down_speed = self.createDropDownSpeed()


""" ######################################### WINDOW ######################################### """


class Window(Tk):
    """ This class create the main Tkinter window for the GUI, This class heritates the Tkinter Tk class, Window is also a tkinter window """
    def __init__(self):
        """ 
        Constructor of the class Window. Setting the size, icon, tilte
        """
        super().__init__()
        # define the title of the GUI window
        self.title("GUI - Space labelling")
        # set up the GUI windows' size when you execute the code
        self.geometry('1400x800') 
        # set up the icon
        self.iconbitmap('./GUI_images/application.icns')
        # define the minimum size of the window 
        self.minsize(850,700)


""" ################################################################################################# """


############################################ MAIN #####################################################


# execute the code 
if __name__ == "__main__":    
    # create a new window for the GUI
    win = Window()
    # add a header in the Tkinter window which will manage all the page of the GUI displayed in its main_container attribute.
    A = Header(win)
    # run the code continously and keep the window operable
    win.mainloop()




