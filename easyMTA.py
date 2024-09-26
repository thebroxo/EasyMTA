import customtkinter as ctk
import os
import webbrowser

fontNormal = ("Inria Sans", 18)
fontbold = ("Inria Sans", 35, "bold")
fontboldic = ("Inria Sans", 17, "bold")

def makeScript(scriptNameEntry, scriptTypeVar, featureVar, scriptDescriptionEntry, scriptAuthorEntry, status, consoleDebug):
    scriptName = scriptNameEntry.get()
    scriptType = scriptTypeVar.get()
    feature = featureVar.get()
    description = scriptDescriptionEntry.get()
    author = scriptAuthorEntry.get()

    if scriptName and scriptType:
        consoleDebug.configure(text="Proccessing :", text_color="#9c9791")
        status.configure(text="Buidling it wait...", text_color="#9c9791")
        MUSIC_FOLDER = os.path.join(os.getcwd(), scriptName)
        
        if not os.path.exists(MUSIC_FOLDER):
            os.makedirs(MUSIC_FOLDER)
            if not description:
                description = "EasyMTA"
            if not author:
                author = "EasyMTA"

            meta_content = '<meta> \n<info author="{}" description="{}" />\n'.format(author, description)

            if scriptType == "client" or scriptType == "both":
                client_file = os.path.join(MUSIC_FOLDER, f"{scriptName}_client.lua")
                with open(client_file, "w") as file:
                    file.write("-- Client script content here\n")

                    if feature == "guiwindow":
                        file.write('''
function createMyGui()
    local window = guiCreateWindow(0.5, 0.5, 0.2, 0.2, "EasyMTA", true)
    guiWindowSetSizable(window, false)
end
addCommandHandler("showgui", createMyGui)
                        ''')
                    elif feature == "dxwindow":
                        file.write('''
function drawMyDx()
    dxDrawRectangle(0.4, 0.4, 0.2, 0.2, tocolor(255, 0, 0, 150))
    dxDrawText("EasyMTA", 0.45, 0.45)
end
addEventHandler("onClientRender", root, drawMyDx)
                        ''')
                    
                meta_content += '<script src="{}_client.lua" type="client" />\n'.format(scriptName)
            
            if scriptType == "server" or scriptType == "both":
                server_file = os.path.join(MUSIC_FOLDER, f"{scriptName}_server.lua")
                with open(server_file, "w") as file:
                    file.write(
                        '''-- Server script content here
function server(thePlayer)
    outputChatBox("EasyMTA is working !", thePlayer)
end
addCommandHandler("test", server)
                        '''
                    )
                meta_content += '<script src="{}_server.lua" type="server" />\n'.format(scriptName)
            
            meta_content += '</meta>'
            
            meta_file = os.path.join(MUSIC_FOLDER, "meta.xml")
            with open(meta_file, "w") as file:
                file.write(meta_content)

            consoleDebug.configure(text="Success :", text_color="#02cc45")
            status.configure(text="Done !! Enjoy !!", text_color="#02cc45")
        else:
            consoleDebug.configure(text="Error :", text_color="#d10f2f")
            status.configure(text="Change Folder Name", text_color="#d10f2f")
    else:
        status.configure(text="Make sure of:\n- Folder Name \n- Select Option", text_color="#d10f2f")
        consoleDebug.configure(text="Error", text_color="#d10f2f")

def mtaWiki():
    mta_wikiLink = "https://wiki.multitheftauto.com/wiki/Main_Page"
    webbrowser.open(mta_wikiLink)

def gotoDiscord():
    discordlink = "https://github.com/thebroxo"
    webbrowser.open(discordlink)

def startHandling():
    root = ctk.CTk()
    root.title("EasyMTA")
    root.geometry("770x380")
    root.resizable(False, False)

    root.columnconfigure((0, 1, 2), weight=1, uniform="a")
    root.rowconfigure((0, 1, 2, 3), weight=1)

    ctk.CTkLabel(root, text="Enter your folder name:", font=fontboldic).grid(row=0, column=0, padx=20, pady=10, sticky="w")
    scriptNameEntry = ctk.CTkEntry(root, width=200, height=35, justify="left", placeholder_text="Script Folder Name...")
    scriptNameEntry.grid(row=1, column=0, padx=20, pady=10, sticky="we")

    ctk.CTkLabel(root, text="Enter your name:", font=fontboldic).grid(row=0, column=1, padx=20, pady=10, sticky="w")
    scriptAuthorEntry = ctk.CTkEntry(root, width=200, height=35, justify="left", placeholder_text="Script Author Name...")
    scriptAuthorEntry.grid(row=1, column=1, padx=20, pady=10, sticky="we")

    ctk.CTkLabel(root, text="Enter script description:", font=fontboldic).grid(row=0, column=2, padx=20, pady=10, sticky="w")
    scriptDescriptionEntry = ctk.CTkEntry(root, width=200, height=35, justify="left", placeholder_text="Script Description...")
    scriptDescriptionEntry.grid(row=1, column=2, padx=20, pady=10, sticky="we")

    scriptTypeVar = ctk.StringVar(value="")
    featureVar = ctk.StringVar(value="")

    clientOnly = ctk.CTkRadioButton(root, text="Client Only", variable=scriptTypeVar, value="client")
    clientOnly.grid(row=2, column=0, padx=20, pady=10, sticky="w")

    serverOnly = ctk.CTkRadioButton(root, text="Server Only", variable=scriptTypeVar, value="server")
    serverOnly.grid(row=3, column=0, padx=20, pady=10, sticky="w")

    bothElements = ctk.CTkRadioButton(root, text="Both", variable=scriptTypeVar, value="both")
    bothElements.grid(row=4, column=0, padx=20, pady=10, sticky="w")

    guiWindow = ctk.CTkRadioButton(root, text="Simple Gui Window", variable=featureVar, value="guiwindow")
    guiWindow.grid(row=2, column=1, padx=20, pady=10, sticky="w")

    dxWindow = ctk.CTkRadioButton(root, text="Simple Dx Window", variable=featureVar, value="dxwindow")
    dxWindow.grid(row=3, column=1, padx=20, pady=10, sticky="w")

    consoleDebug = ctk.CTkLabel(
        root, 
        text="Status :", 
        font=fontboldic, 
        text_color="#9c9791"
    )
    consoleDebug.grid(row=2, column=2, padx=20, pady=(10, 5), sticky="w")

    status = ctk.CTkLabel(
        root, 
        text="Ready to use", 
        font=fontboldic, 
        text_color="#9c9791"
    )
    status.grid(row=3, column=2, padx=20, pady=(10, 20), sticky="w")




    MakeButton = ctk.CTkButton(
        root, 
        text="Make my script!", 
        font=fontboldic,
        fg_color="#057a2e",
        hover_color="#077010",
        height=40, 
        width=250,
        command=lambda: makeScript(scriptNameEntry, scriptTypeVar, featureVar, scriptDescriptionEntry, scriptAuthorEntry, status, consoleDebug)
    )
    
    MakeButton.grid(row=4, column=1, padx=20,pady=10, sticky="w")


    gotoWiki = ctk.CTkButton(root, text="MTA WIKI", font=fontboldic, height=40, fg_color="#a15d0a", hover_color="#422501", command=mtaWiki)
    gotoWiki.grid(row=5, column=0, padx=20, pady=10, sticky="we")

    aboutBrox = ctk.CTkButton(root, text="About EASYMTA", font=fontboldic, height=40, command=gotoDiscord)
    aboutBrox.grid(row=5, column=1, padx=20, pady=10, sticky="we")

    exitEasyMta = ctk.CTkButton(root, text="EXIT", font=fontboldic, height=40, fg_color="#c93061", hover_color="#59021e", command=root.destroy)
    exitEasyMta.grid(row=5, column=2, padx=20, pady=10, sticky="we")

    root.mainloop()

startHandling()