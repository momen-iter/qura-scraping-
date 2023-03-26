import requests
from bs4 import BeautifulSoup
import csv 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import mysql.connector
import tkinter as tk

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(f'https://ar.quora.com/profile/%D8%B9%D9%85%D8%B1-%D8%A3%D8%A8%D9%88%D9%87%D8%A7%D8%B4%D9%85')

qustions=driver.find_elements(By.CSS_SELECTOR,'.qu-flexDirection--row .qu-flexWrap--wrap .qu-truncateLines--5 .qu-userSelect--text span')
answers=driver.find_elements(By.CSS_SELECTOR,'.qu-display--block .spacing_log_answer_content .qu-cursor--pointer .qu-truncateLines--3 span')

qustionlist=[]
answerslist=[]


for i in qustions:
    qustionlist.append(i.get_attribute('innerHTML'))
    
print(qustionlist)
for i in answers:
    answerslist.append(i.get_attribute('innerHTML'))

#print(answerslist)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="momen"
)
"""mycursor = mydb.cursor()


qustionssql = "INSERT INTO datascraping (qustion) VALUES (%s)"

for i in range(len(qustionlist)):
    mycursor.executemany(qustionssql, [(qustionlist[i],)])

answersql = "INSERT INTO datascraping (ans) VALUES (%s)"
for i in range(len(answerslist)):
    mycursor.executemany(answersql, [(answerslist[i],)])    


mydb.commit()
"""

root = tk.Tk()
root.title(" Questions and Answers")


frame1 = tk.Frame(root)
frame2 = tk.Frame(root)


tk.Label(frame1, text="Questions:", font=("Arial", 14)).pack(side="top")
question_listbox = tk.Listbox(frame1, width=150, height=100)
question_listbox.pack(side="left", fill="y")
scrollbar1 = tk.Scrollbar(frame1, orient="vertical", command=question_listbox.yview)
scrollbar1.pack(side="right", fill="y")
question_listbox.config(yscrollcommand=scrollbar1.set)

hscrollbar1 = tk.Scrollbar(frame1, orient="horizontal", command=question_listbox.xview)
hscrollbar1.pack(side="bottom", fill="x")
question_listbox.config(xscrollcommand=hscrollbar1.set)

tk.Label(frame2, text="Answers:", font=("Arial", 14)).pack(side="top")
answer_listbox = tk.Listbox(frame2, width=150, height=100)
answer_listbox.pack(side="left", fill="y")
scrollbar2 = tk.Scrollbar(frame2, orient="vertical", command=answer_listbox.yview)
scrollbar2.pack(side="right", fill="y")
answer_listbox.config(yscrollcommand=scrollbar2.set)

hscrollbar2 = tk.Scrollbar(frame2, orient="horizontal", command=answer_listbox.xview)
hscrollbar2.pack(side="bottom", fill="x")
answer_listbox.config(xscrollcommand=hscrollbar2.set)


mycursor = mydb.cursor()
mycursor.execute("SELECT qustion FROM datascraping")
for row in mycursor.fetchall():
    question_listbox.insert(tk.END, row[0])
    
mycursor.execute("SELECT ans FROM datascraping")
for row in mycursor.fetchall():
    answer_listbox.insert(tk.END, row[0])


frame1.pack(side="left", padx=20, pady=20)
frame2.pack(side="right", padx=20, pady=20)

root.mainloop()
mydb.commit()
