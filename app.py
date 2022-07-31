import tkinter
import customtkinter
import os
import webbrowser
import time
LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
TUTORIAL = "https://google.com"
TUTORIAL2 = "https://google.nl"
roblox_defalt_location = os.path.isdir(LOCAL + '\Roblox\Versions')
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
app = customtkinter.CTk()
app.geometry("520x250")
app.title("oof")
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)
def openurl(url):
    webbrowser.open_new(url)
def button_callback():
    print("Tutorial ", openurl(TUTORIAL))
def button_callback2():
    print("Tutorial ", openurl(TUTORIAL2))

def app_run():
    if roblox_defalt_location == True:
        print('location = OK')
        entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="oof.ogg")
        entry_1.pack(pady=12, padx=10)
        def button_callback3():
            #os.remove(roblox_defalt_location + "/version-9045f70ea522489c/content/sounds/ouch.ogg")
            if os.path.isfile(os.getcwd() + "/assets/" + entry_1.get()):
                list = []
                for file in os.listdir(LOCAL + '\Roblox\Versions'):
                    if file.endswith("exe"):
                        continue
                    f = os.path.join(LOCAL + '\Roblox\Versions', file)
                    list.append(file)
                    print(f)
                for li in list:
                    os.system("powershell Remove-Item '" + LOCAL + '\Roblox\Versions/' + li.split("Versions").pop() + "/content/sounds/ouch.ogg" + "'")
                    os.system("powershell copy '" + os.getcwd() + "/assets/" + entry_1.get() + "' '" + LOCAL + '\Roblox\Versions/' + li.split("Versions").pop() + "/content/sounds/ouch.ogg'")
                    # os.replace(os.getcwd() + "/assets/" + entry_1.get(), LOCAL + '\Roblox\Versions/' + li.split("Versions").pop() + "/content/sounds/ouch.ogg")
                    print("copy " + os.getcwd() + "/assets/" + entry_1.get() + " " + LOCAL + '\Roblox\Versions/' + li.split("Versions").pop() + "/content/sounds/ouch.ogg")
                # os.replace(os.getcwd() + "/assets/" + entry_1.get(), LOCAL + '\Roblox\Versions' + "/version-9045f70ea522489c/content/sounds/ouch.ogg")
                print('done')
                label_Done = customtkinter.CTkLabel(master=frame_1, text="Done", text_font=("Roboto Medium", -16))  # font name and size in px
                label_Done.pack(pady=12, padx=10)
                time.sleep(1)
                exit()
        done = customtkinter.CTkButton(master=frame_1, text="done", command=button_callback3)
        done.pack(pady=12, padx=10)
        ##tutorial_2 = customtkinter.CTkButton(master=frame_1, text="tutorial", command=button_callback2)
        ##tutorial_2.pack(pady=12, padx=10)
    else:
        print('location = NULL')
        label_1 = customtkinter.CTkLabel(master=frame_1, text="ROBLOX not installed on default location", text_font=("Roboto Medium", -16))  # font name and size in px
        label_1.pack(pady=12, padx=10)
        ##tutorial_1 = customtkinter.CTkButton(master=frame_1, text="help", command=button_callback)
        ##tutorial_1.pack(pady=12, padx=10)
        #entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="roblox path")
        #entry_2.pack(pady=12, padx=10)
        #def button_callback3():
        #    print(entry_2.get())
        #    print(os.path.isdir(entry_2.get()))
        #    roblox_defalt_location = os.path.isdir(entry_2.get())
        #    if roblox_defalt_location == True:
        #        app_run()
        #    else:
        #        label_2 = customtkinter.CTkLabel(master=frame_1, text="Location invaled", text_font=("Roboto Medium", -16))  # font name and size in px
        #        label_2.pack(pady=12, padx=10)
        #location = customtkinter.CTkButton(master=frame_1, text="done", command=button_callback3)
        #location.pack(pady=12, padx=10)
app_run()
app.mainloop()