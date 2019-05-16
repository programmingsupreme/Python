import easygui as eg

filetoedit=''

def checkuse():
    useprogram = eg.ynbox('Welcome to the text editor made with Python3. Would you like to continue?','Welcome',('Yes','No'))
    if useprogram==True:
        startwriting()
    else:
        print('Have a good day!')
        exit()

def starteditor(fil=''):
    print('Editor started')
    if fil=='':
        texttowrite=eg.textbox('The file is automatically saved once the ok button is pressed','Editing')
        savlocation=eg.filesavebox()
        with open(savlocation,'w+') as f:
            f.write(texttowrite)

        if f.closed:
            del f
    else:
        with open(filetoedit,'r+') as f:
            texttowrite=eg.textbox(f'Editing {filetoedit}\nThis file will automatically save once you click the ok button','Editing',f.read())
        
        if f.closed:
            del f

        with open(filetoedit,'w') as f:
            f.write(texttowrite)

        if f.closed:
            del f

def startwriting():
    makenew = eg.ynbox('Do you want to create a new file?',('Yes','No'))
    if makenew:
        makenewfile()
    else:
        openfile()

def makenewfile():
    starteditor()

def openfile():
    global filetoedit
    filetoedit=eg.fileopenbox('Pick a file to open')
    starteditor(filetoedit)

if __name__=='__main__':
    while True:
        checkuse()
