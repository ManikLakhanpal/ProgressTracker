import tkinter as tk
from tkinter import messagebox
import requests
import pyperclip
import datetime as dt


class Start():
    def __init__(self):
        self.main_window()

    def main_window(self):
        self.window = tk.Tk()
        self.window.title("Pixela Progress Tracker")
        self.window.config(padx=20, pady=20)

        self.canvas_1 = tk.Canvas(width=300, height=70, bg="#333333")
        self.canvas_1.create_text(150, 35, text="PROGRESS TRACKER", fill="white", font=("Arial", 20, "italic"))
        self.canvas_1.grid(row=0, column=1)

        self.create = tk.Button(text="Create Account", width=12, command=self.create, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        self.create.grid(column=0, row=1, ipady=3, pady=10)

        self.add_data = tk.Button(text="Add Data", width=12, command=self.add, bg="#FF9800", fg="white", font=("Arial", 12, "bold"))
        self.add_data.grid(column=0, row=2, ipady=3, pady=10)

        self.update_data = tk.Button(text="Update", width=12, command=self.update, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
        self.update_data.grid(column=2, row=1, ipady=3, pady=10)

        self.delete_data = tk.Button(text="Delete", width=12, command=self.delete, bg="#F44336", fg="white", font=("Arial", 12, "bold"))
        self.delete_data.grid(column=2, row=2, ipady=3, pady=10)

        self.create_g = tk.Button(text="Make Graph", width=12, command=self.create_graph, bg="#F44336", fg="white", font=("Arial", 12, "bold"))
        self.create_g.grid(column=1, row=3, ipady=3, pady=10)

        self.window.mainloop()

    def create(self):
        self.window.destroy()
        self.window = tk.Tk()
        self.window.title("New Account")
        self.window.config(padx=20, pady=20)

        self.canvas_2 = tk.Canvas(self.window, width=300, height=70, bg="#333333")
        self.canvas_2.create_text(150, 35, text="CREATE ACCOUNT", fill="white", font=("Arial", 20, "italic"))
        self.canvas_2.grid(column=1, row=0)

        self.token_label = tk.Label(self.window, text="Token:", font=("Arial", 12))
        self.token_label.grid(column=0, row=1, sticky="e", ipady=10)

        self.username_label = tk.Label(self.window, text="Username:", font=("Arial", 12))
        self.username_label.grid(column=0, row=2, sticky="e", ipady=10)

        self.agree_label = tk.Label(self.window, text="AgreeTermsOfService:", font=("Arial", 12))
        self.agree_label.grid(column=0, row=3, sticky="e", ipady=10)

        self.NotMinor_label = tk.Label(self.window, text="Not Minor(yes/no):", font=("Arial", 12))
        self.NotMinor_label.grid(column=0, row=4, sticky="e", ipady=10)

        self.token_entry = tk.Entry(self.window, font=("Arial", 12))
        self.token_entry.grid(column=1, row=1)

        self.username_entry = tk.Entry(self.window, font=("Arial", 12))
        self.username_entry.grid(column=1, row=2)

        self.agree_entry = tk.Entry(self.window, font=("Arial", 12))
        self.agree_entry.grid(column=1, row=3)

        self.NotMinor_entry = tk.Entry(self.window, font=("Arial", 12))
        self.NotMinor_entry.grid(column=1, row=4)

        self.create_button = tk.Button(self.window, text="Create", command=self.create_account, font=("Arial", 12), width= 12, bg="#4CAF50")
        self.create_button.grid(column=0, row=5, ipady=3)

        self.cancel_button = tk.Button(self.window,command=self.cancel, text="Back", font=("Arial", 12), width=12, bg="#F44336")
        self.cancel_button.grid(column=2, row=5, ipady=3)

        self.window.mainloop()

    def create_graph(self):
        self.window.destroy()
        self.window = tk.Tk()
        self.window.title("Create Graph")
        self.window.config(padx=20, pady=20)

        self.canvas_a = tk.Canvas(self.window, width=300, height=70, bg="#333333")
        self.canvas_a.create_text(150, 35, text="CREATE GRAPH", fill="white", font=("Arial", 20, "italic"))
        self.canvas_a.grid(column=1, row=0)

        self.graph_name_label_a = tk.Label(self.window, text="Name:", font=("Arial", 12))
        self.graph_name_label_a.grid(column=0, row=1, sticky="e", ipady=10)

        self.graph_name_entry_a = tk.Entry(self.window, font=("Arial", 12))
        self.graph_name_entry_a.grid(column=1, row=1)

        self.graph_id_label_a = tk.Label(self.window, text="Graph ID:", font=("Arial", 12))
        self.graph_id_label_a.grid(column=0, row=2, sticky="e", ipady=10)

        self.graph_id_entry_a = tk.Entry(self.window, font=("Arial", 12))
        self.graph_id_entry_a.grid(column=1 ,row=2)

        self.username_label_a = tk.Label(self.window, text="Username:", font=("Arial", 12))
        self.username_label_a.grid(column=0, row=3, sticky="e", ipady=10)

        self.username_entry_a = tk.Entry(self.window, font=("Arial",12))
        self.username_entry_a.grid(column=1, row=3)

        self.unit_label_a = tk.Label(self.window,text="Unit:", font=("Arial", 12))
        self.unit_label_a.grid(column=0, row=4, sticky="e", ipady=10)

        self.unit_entry_a = tk.Entry(self.window, font=("Arial", 12))
        self.unit_entry_a.grid(column=1, row=4)

        self.color_label_a = tk.Label(self.window, text="Color:", font=("Arial", 12))
        self.color_label_a.grid(column=0, row=5, sticky="e", ipady=10)

        self.color_entry_a = tk.Entry(self.window, font=("Arial", 12))
        self.color_entry_a.grid(column=1, row=5)

        self.timezone_label_a = tk.Label(self.window, text="Timezone:", font=("Arial", 12))
        self.timezone_label_a.grid(column=0, row=6, sticky="e", ipady=10)

        self.timezone_entry_a = tk.Entry(self.window, font=("Arial", 12))
        self.timezone_entry_a.grid(column=1, row=6)

        self.token_label_a = tk.Label(self.window, text="Token:", font=("Arial", 12))
        self.token_label_a.grid(column=0, row=7, sticky="e", ipady=10)

        self.token_entry_a = tk.Entry(self.window, font=("Arial", 12))
        self.token_entry_a.grid(column=1, row=7)

        self.create_button_a = tk.Button(self.window, text="Create", command=self.create_graph_b, font=("Arial", 12), width= 12, bg="#4CAF50")
        self.create_button_a.grid(column=0, row=9, ipady=3)

        self.cancel_button_a = tk.Button(self.window,command=self.cancel, text="Back", font=("Arial", 12), width=12, bg="#F44336")
        self.cancel_button_a.grid(column=2, row=9, ipady=3)

    def create_graph_b(self):
        HEADER = {
            "X-USER-TOKEN": self.token_entry_a.get()
        }

        GRAPH_NAME = self.graph_name_entry_a.get()
        GRAPH_ID = self.graph_id_entry_a.get()
        USERNAME = self.username_entry_a.get()
        UNIT = self.unit_entry_a.get()
        COLOR = self.color_entry_a.get()
        TIMEZONE = self.timezone_entry_a.get()

        PARAMS = {
            "id": GRAPH_ID,
            "name": GRAPH_NAME,
            "unit": UNIT,
            "type": "float",
            "color": COLOR,
            "timezone": TIMEZONE
        }
        
        GRAPH_CREATION_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs" 

        if len(GRAPH_NAME) == 0 or len(GRAPH_ID) == 0 or len(UNIT) == 0 or len(COLOR) == 0 or len(TIMEZONE) == 0:
            messagebox.showerror(title="Incomplete", message="Please fill everything.")

        else:
            with requests.post(url= GRAPH_CREATION_ENDPOINT, json=PARAMS, headers=HEADER) as response:
                self.msg = response.text
                messagebox.showinfo(title="Response",message=f"{self.msg}\n\n Click Ok, link has been copied to you clip board")
                profile = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html"
                pyperclip.copy(profile)

         

    def create_account(self):
        TOKEN = self.token_entry.get()
        USERNAME = self.username_entry.get()
        AGREE = self.agree_entry.get()
        MINOR = self.NotMinor_entry.get()

        user_params = {
                "token": TOKEN,
                "username": USERNAME,
                "agreeTermsOfService": AGREE,
                "notMinor": MINOR
        }

        CREATE_ACCOUNT_ENDPOINT = "https://pixe.la/v1/users"

        if len(TOKEN)==0 or len(USERNAME)==0 or len(AGREE) == 0 or len(MINOR)==0:
                messagebox.showerror(title="Incomplete", message="Please fill everything.")

        else:
            with requests.post(url=CREATE_ACCOUNT_ENDPOINT, json=user_params) as response:
                self.msg = response.text
                messagebox.showinfo(message=f"{self.msg}\n\n Click Ok, link has been copied to you clip board")
                profile = f"https://pixe.la/@{USERNAME}"
                pyperclip.copy(profile)

    def add(self):
        self.window.destroy()
        self.window = tk.Tk()
        self.window.title("Add Data")
        self.window.config(padx=20, pady=20)

        self.canvas_3 = tk.Canvas(self.window, width=300, height=70, bg="#333333")
        self.canvas_3.create_text(150, 35, text="ADD PROGRESS", fill="white", font=("Arial", 20, "italic"))
        self.canvas_3.grid(column=1, row=0)

        self.username_label_2 = tk.Label(self.window, text="Username:", font=("Arial", 12))
        self.username_label_2.grid(column=0, row=2, sticky="e", ipady=10)

        self.token_label_2 = tk.Label(self.window, text="Token:", font=("Arial", 12))
        self.token_label_2.grid(column=0, row=3, sticky="e", ipady=10)

        self.graph_id = tk.Label(self.window, text="Graph ID:", font=("Arial", 12))
        self.graph_id.grid(column=0, row=4, sticky="e", ipady=10)

        self.quantity = tk.Label(self.window, text="Quantity:", font=("Arial", 12))
        self.quantity.grid(column=0, row=5, sticky="e", ipady=10)

        self.username_entry = tk.Entry(self.window, font=("Arial", 12))
        self.username_entry.grid(column=1, row=2)

        self.token_entry_2 = tk.Entry(self.window, font=("Arial", 12))
        self.token_entry_2.grid(column=1, row=3)

        self.graph_id_entry = tk.Entry(self.window, font=("Arial", 12))
        self.graph_id_entry.grid(column=1, row=4)

        self.quantity_entry = tk.Entry(self.window, font=("Arial", 12))
        self.quantity_entry.grid(column=1, row=5)

        self.create_button_2 = tk.Button(self.window,command=self.add_pixel, text="Add", font=("Arial", 12), width= 12, bg="#4CAF50")
        self.create_button_2.grid(column=0, row=7, ipady=3)

        self.cancel_button = tk.Button(self.window, text="Back",command=self.cancel, font=("Arial", 12), width=12, bg="#F44336")
        self.cancel_button.grid(column=2, row=7, ipady=3)

        self.window.mainloop()



    def add_pixel(self):
        TOKEN = self.token_entry_2.get()
        USERNAME = self.username_entry.get()
        GRAPH_ID = self.graph_id_entry.get()
        QUANTITY = self.quantity_entry.get()

        pixel_params = {
                "date": dt.datetime.now().strftime('%Y%m%d'),
                "quantity": QUANTITY,
        }

        HEADER = {
            "X-USER-TOKEN": TOKEN
        }

        ADD_PIXEL_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

        if len(TOKEN)==0 or len(USERNAME)==0 or len(GRAPH_ID) == 0 or len(QUANTITY)==0:
                messagebox.showerror(title="Incomplete", message="Please fill everything.")

        else:
            with requests.post(url=ADD_PIXEL_ENDPOINT, json=pixel_params, headers=HEADER) as response:
                    self.msg = response.text
                    messagebox.showinfo(title="Response",message=f"{self.msg}\n\n Click Ok, link has been copied to you clip board")
                    profile = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html"
                    pyperclip.copy(profile)


    def update(self):
        self.window.destroy()
        self.window = tk.Tk()
        self.window.title("Update A Pixel")
        self.window.config(padx=20, pady=20)

        self.canvas_4 = tk.Canvas(self.window, width=300, height=70, bg="#333333")
        self.canvas_4.create_text(150, 35, text="UPDATE PIXEL", fill="white", font=("Arial", 20, "italic"))
        self.canvas_4.grid(column=1, row=0)

        self.username_label_3 = tk.Label(self.window, text="Username:", font=("Arial", 12))
        self.username_label_3.grid(column=0, row=1, sticky="e", ipady=10)

        self.token_label_4 = tk.Label(self.window, text="Token:", font=("Arial", 12))
        self.token_label_4.grid(column=0, row=2, sticky="e", ipady=10)

        self.graph_id_2 = tk.Label(self.window, text="Graph ID:", font=("Arial", 12))
        self.graph_id_2.grid(column=0, row=3, sticky="e", ipady=10)

        self.date_2 = tk.Label(self.window, text="Date:", font=("Arial", 12))
        self.date_2.grid(column=0, row=4, sticky="e", ipady=10)

        self.quantity_2 = tk.Label(self.window, text="Quantity:", font=("Arial", 12))
        self.quantity_2.grid(column=0, row=5, sticky="e", ipady=10)

        self.username_entry_1 = tk.Entry(self.window, font=("Arial", 12))
        self.username_entry_1.grid(column=1, row=1)

        self.token_entry_3 = tk.Entry(self.window, font=("Arial", 12))
        self.token_entry_3.grid(column=1, row=2)

        self.graph_id_entry_2 = tk.Entry(self.window, font=("Arial", 12))
        self.graph_id_entry_2.grid(column=1, row=3)

        self.date_entry = tk.Entry(self.window, font=("Arial", 12))
        self.date_entry.grid(column=1, row=4)

        self.quantity_entry_2 = tk.Entry(self.window, font=("Arial", 12))
        self.quantity_entry_2.grid(column=1, row=5)

        self.create_button_3 = tk.Button(self.window, command=self.update_pixel, text="Update", font=("Arial", 12), width= 12, bg="#4CAF50")
        self.create_button_3.grid(column=0, row=7, ipady=3)

        self.cancel_button_2 = tk.Button(self.window, text="Back",command=self.cancel, font=("Arial", 12), width=12, bg="#F44336")
        self.cancel_button_2.grid(column=2, row=7, ipady=3)

        self.window.mainloop()

    def update_pixel(self):
        TOKEN = self.token_entry_3.get()
        USERNAME = self.username_entry_1.get()
        GRAPH_ID = self.graph_id_entry_2.get()
        QUANTITY = self.quantity_entry_2.get()
        DATE = f"{self.date_entry.get()}"

        day = int(DATE[:2])
        month = int(DATE[3:5])
        year = int(DATE[6:])
        GIVE_DATE = dt.datetime(year=year, month=month, day=day).strftime("%Y%m%d")

        pixel_params = {
                "date": GIVE_DATE,
                "quantity": QUANTITY,
        }

        HEADER = {
            "X-USER-TOKEN": TOKEN
        }

        ADD_PIXEL_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

        if len(TOKEN)==0 or len(USERNAME)==0 or len(GRAPH_ID) == 0 or len(QUANTITY)==0 or len(DATE)==0:
                messagebox.showerror(title="Incomplete", message="Please fill everything.")

        else:
            with requests.post(url=ADD_PIXEL_ENDPOINT, json=pixel_params, headers=HEADER) as response:
                    self.msg = response.text
                    messagebox.showinfo(message=f"{self.msg}\n\n Click Ok, link has been copied to you clip board")
                    profile = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html"
                    pyperclip.copy(profile)

    def delete(self):
        self.window.destroy()
        self.window = tk.Tk()
        self.window.title("Delete A Pixel")
        self.window.config(padx=20, pady=20)

        self.canvas_5 = tk.Canvas(self.window, width=300, height=70, bg="#333333")
        self.canvas_5.create_text(150, 35, text="DELETE PIXEL", fill="white", font=("Arial", 20, "italic"))
        self.canvas_5.grid(column=1, row=0)

        self.username_label_4 = tk.Label(self.window, text="Username:", font=("Arial", 12))
        self.username_label_4.grid(column=0, row=1, sticky="e", ipady=10)

        self.username_entry_2 = tk.Entry(self.window, font=("Arial", 12))
        self.username_entry_2.grid(column=1, row=1)

        self.token_label_5 = tk.Label(self.window, text="Token:", font=("Arial", 12))
        self.token_label_5.grid(column=0, row=2, sticky="e", ipady=10)

        self.token_entry_4 = tk.Entry(self.window, font=("Arial", 12))
        self.token_entry_4.grid(column=1, row=2)

        self.graph_id_3 = tk.Label(self.window, text="Graph ID:", font=("Arial", 12))
        self.graph_id_3.grid(column=0, row=3, sticky="e", ipady=10)

        self.graph_id_entry_3 = tk.Entry(self.window, font=("Arial", 12))
        self.graph_id_entry_3.grid(column=1, row=3)

        self.date_3 = tk.Label(self.window, text="Date:", font=("Arial", 12))
        self.date_3.grid(column=0, row=4, sticky="e", ipady=10)

        self.date_entry_2 = tk.Entry(self.window, font=("Arial", 12))
        self.date_entry_2.grid(column=1, row=4)

        self.create_button_4 = tk.Button(self.window,command=self.delete_pixel, text="Delete", font=("Arial", 12), width= 12, bg="#4CAF50")
        self.create_button_4.grid(column=0, row=6, ipady=3)

        self.cancel_button_3 = tk.Button(self.window, text="Back",command=self.cancel, font=("Arial", 12), width=12, bg="#F44336")
        self.cancel_button_3.grid(column=2, row=6, ipady=3)

    def delete_pixel(self):

        TOKEN = self.token_entry_4.get()
        USERNAME = self.username_entry_2.get()
        GRAPH_ID = self.graph_id_entry_3.get()
        DATE = self.date_entry_2.get()

        day = int(DATE[:2])
        month = int(DATE[3:5])
        year = int(DATE[6:])
        GIVE_DATE = dt.datetime(year=year, month=month, day=day).strftime("%Y%m%d")

        DELETE_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{GIVE_DATE}"

        HEADER = {
            "X-USER-TOKEN": TOKEN
        }

        with requests.delete(url=DELETE_ENDPOINT, headers=HEADER) as response:
                    self.msg = response.text
                    messagebox.showinfo(message=f"{self.msg}\n\n Click Ok, link has been copied to you clip board")
                    profile = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html"
                    pyperclip.copy(profile)   


    def cancel(self):
        self.window.destroy()
        self.main_window()



