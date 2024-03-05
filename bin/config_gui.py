import tkinter as tk 
import requests
import json

# launchable config utility, make an .exe, then store the preferences somewhere where it makes sense.
# choose your preferred sounds, notifications, visuals (can have different styles), bins to check
# pass these preferences as a dict

class BinPrefsGUI():
    def __init__(self):
        
        description_frame = tk.Frame()
        description_frame.pack()
        postcode_address_frame = tk.Frame()
        postcode_address_frame.pack()
        utility_preferences_frame = tk.Frame()
        utility_preferences_frame.pack()
        
        self.populate_Description_Frame(description_frame)
        self.populate_Postcode_Address_Frame(postcode_address_frame)  # Call function to populate postcode and address
        self.populate_Utility_Preferences_Frame(utility_preferences_frame)
    
    def populate_Description_Frame(self,description_frame):
        description_label = tk.Label(description_frame,text="This is the bin date checker configuration utility...")
        description_label.pack()
        # short description of utility
    
    def populate_Postcode_Address_Frame(self,postcode_address_frame):
        address_label = tk.Label(postcode_address_frame,text="Select your address data...")
        address_label.pack()
    # dropdown menus reading options from some database
    # request this data each time config is run
    # have 2-3 backups in case first one fails to GET
        self.postcode = "AAA AAA"
        self.address = "10 Downing Street"


    def populate_Utility_Preferences_Frame(self,utility_preferences_frame):
        pass
        prefs_label = tk.Label(utility_preferences_frame,text="Specify your preferences for the application...")
        prefs_label.pack()
        # all kinds of options, the more the merrier! provide previews, sound bits, animations and so on.
        # choose notifications, email? text? as many options as possible. 
        # set all of these as self.email and self.sound_2, will bundle these up in a dict
        self.send_desktop_notifications = True
        self.send_email_notifications = False 
        
    # write all user preferences to the json file
    def get_prefs(self):
        prefs = {
            "postcode" : self.postcode,
            "address" : self.address,
            "send_desktop_notifications" : self.send_desktop_notifications,
            "send_email_notifications" : self.send_email_notifications 
        }
    
        
        with open('user_preferences.json', 'w') as file:
            json.dump(prefs, file,indent=4)



def set_user_configuration():
    
    print("getting user configuration...")
    
    root = tk.Tk() # launch from executable.
    root.geometry("300x400")
    app = BinPrefsGUI()
    
    root.mainloop()
    
    app.get_prefs() # after GUI is closed by "OK", write preferences to .json and pass into rest of the script

set_user_configuration()


    
    


        
        

