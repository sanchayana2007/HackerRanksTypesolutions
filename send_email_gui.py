import os.path
import getpass
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import COMMASPACE, formatdate
from tkinter import *
from tkinter.filedialog import *

class gmail_utility:
 def __init__(self):
  self.server = smtplib.SMTP('smtp.gmail.com:587')
  self.server.starttls()
  self.msg = MIMEMultipart()
 
 def send_email(self, username, passwd, toaddrs,fromaddr,email_subject, email_body, attach_file=None):
  #print(username,passwd,toaddrs,fromaddr,email_subject, email_body,attach_file)
  self.msg['Date'] = formatdate(localtime = True)
  self.msg['Subject'] = email_subject
  self.msg.attach(MIMEText(email_body))
  if(attach_file is not None):
   attachment = MIMEApplication(open(attach_file,"rb").read(), Name = os.path.basename(attach_file))
   attachment['Content-Disposition'] = 'attachment; filename = "%s"' %os.path.basename(attach_file)
   self.msg.attach(attachment)
  self.server.login(username,passwd)
  self.server.send_message(self.msg, fromaddr, toaddrs)
  self.server.quit()
				
  
class gmail_gui:
 def __init__(self):
   self.root = Tk()
   self.root.title("Gmail Utility")
   Label(self.root, text="From: ").grid(row =0, column=0, rowspan = 1, columnspan=1)
   self.from_email_id = Text(self.root, height=1)
   self.from_email_id.grid(row=0, column=1,rowspan = 1, columnspan=1)
   self.from_email_id.insert(END, "")
   Label(self.root, text="To List:").grid(row =1, column=0, rowspan = 1, columnspan=1)
   self.to_email_ids = Text(self.root, height=1)
   self.to_email_ids.grid(row=1, column=1,rowspan = 1, columnspan=1)
   self.to_email_ids.insert(END, "")
   Label(self.root, text="Subject:").grid(row =2, column=0, rowspan = 1, columnspan=1)
   self.subject = Text(self.root, height=1)
   self.subject.grid(row=2, column=1,rowspan = 1, columnspan=1)
   self.subject.insert(END, "")
   Label(self.root, text="email content:").grid(row =3, column=0, rowspan = 1, columnspan=1)
   self.email_content = Text(self.root, height=15)
   self.email_content.grid(row=3, column=1,rowspan = 1, columnspan=1)
   self.email_content.insert(END, "")
   self.mail_attachment = Button(self.root, text = "Attachment", command=self.attach_file)
   self.mail_attachment.grid(row=4,column=0,rowspan=1,columnspan=1)
   self.B = Button(self.root, text = "send email", command=self.send_email)
   self.B.grid(row=4, column=1, rowspan = 2, columnspan=2)
   self.root.resizable(width=False, height=False)
   self.email_vendor = gmail_utility()
   self.sender_email_id = ""
   self.receiver_email_list = []
   self.email_subject = ""
   self.email_body = ""
   self.attachment = None
   
 def create_auth_window(self):
   self.auth_window = Toplevel()
   self.auth_window.wm_title("Enter Gmail credential")
   Label(self.auth_window, text="username: ").grid(row =0, column=0, rowspan = 1, columnspan=1)
   self.user_name = Text(self.auth_window, height=1,width=30)
   self.user_name.grid(row=0, column=1,rowspan = 1, columnspan=1)
   #self.user_name.grid(row=0, column=1,width=10)
   self.user_name.insert(END, "")
   Label(self.auth_window, text="password: ").grid(row =1, column=0, rowspan = 1, columnspan=1)
   self.passwd = Entry(self.auth_window, width=40, show="*")
   self.passwd.grid(row=1, column=1,rowspan = 1, columnspan=1)
   self.passwd.insert(END, "")
   #self.passwd.bind("<KeyPress>", lambda e: "break")
   submit = Button(self.auth_window, text = "submit", command=self.get_username_passwd)
   submit.grid(row=3, column=1, rowspan = 2, columnspan=2)
   self.auth_window.resizable(width=False, height=False)

 def send_email(self):
   self.sender_email_id = self.from_email_id.get("1.0", END).strip()
   receivers = self.to_email_ids.get("1.0", END)
   receivers = receivers.split(';')
   self.receiver_email_list = ''
   for i in receivers:
    self.receiver_email_list += (i + ';')
   self.email_subject = self.subject.get("1.0", END).strip()
   self.email_payload = self.email_content.get("1.0", END).strip()
   #print("Sender: ", self.sender_email_id)
   #print("Receivers: ", self.receiver_email_list)
   #print("Email Subject: ", self.email_subject)
   #print("Email Payload: ", self.email_payload)
   self.create_auth_window()

 def get_username_passwd(self):
   uname = self.user_name.get("1.0", END).strip()
   pwd = self.passwd.get().strip()
   #print(uname, pwd)
   self.auth_window.destroy()
   try:
    self.email_vendor.send_email(uname, pwd, self.sender_email_id,self.receiver_email_list, self.email_subject,self.email_payload, self.attachment)
   except:
    text_msg = "Email Delivery Failed"
   else:
    text_msg = "Email Delivered Successfully"
   finally:
    print(text_msg)
    self.root.destroy()

 def attach_file(self):
   self.attachment = askopenfilename(filetypes=[("all files", "*")])

#main code
gmail_gui()
mainloop()