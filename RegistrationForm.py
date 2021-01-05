# Q : Create a registration form which will accept data from user and save it into file
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from validate_email import validate_email
# the package 'validate_email" is used to check validation of email
class Form:
    def name(self):
        name_Label=Label(root,text="Full Name :",font=("Arial Bold",9)).grid(row=1,column=0,sticky=W)
        name_entry=Entry(root,width=20,textvariable=nameVar,justify=CENTER).grid(row=1,column=1,pady=20,sticky=W)
        # 'justify' argument will start input from middle of entry box
    def email(self):
        email_label=Label(root,text="Email :",font=("Arial Bold",9)).grid(row=2,column=0,sticky=W)
        email_entry=Entry(root,width=35,textvariable=emailVar,justify=CENTER).grid(row=2,column=1,sticky=W)
    def mobile_no(self):
        mobile_label=Label(root,text="Mobile Number :",font=("Arial Bold",9)).grid(row=3,column=0,sticky=W)
        mobile_entry=Entry(root,width=20,textvariable=mobileVar,justify=CENTER).grid(row=3,column=1,pady=20,sticky=W)
    def country(self):
        country_label=Label(root,text="Select your Country :",font=("Arial bold",9)).grid(row=4,column=0,sticky=W)
        country_combo=ttk.Combobox(root,width=10,state='readonly',textvariable=countryVar)
        country_combo['values']=("Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Bangladesh","Belgium","Brazil","Canada","China","Egypt","France","Germany","India","Indonesia","Japan","Mexico")
        country_combo.current(14)
        country_combo.grid(row=4,column=1,sticky=W)
        #countryVar=country_combo.get()
    def degree(self):
        degree_label=Label(root,text="Select your Degree Course :",font=("Arial Bold",9),justify=LEFT).grid(row=5,column=0,pady=20,sticky=W)
        degree_combo=ttk.Combobox(root,width=10,textvariable=degreeVar,state='readonly')
        degree_combo['values']=("BBA","B.Sc(Physics)","BA","BE/B.Tech","BCA","B.Sc(IT)","B.Sc(Nursing)","B.Sc(Math)","B.Sc(Chem)","B.Sc(Stat)")
        degree_combo.current(3)
        degree_combo.grid(row=5,column=1,sticky=W)
       # degreeVar=degree_combo.get()
    def result(self):
        result_label=Label(root,text="Select percentge here :",font=("Arial Bold",9),justify=LEFT).grid(row=6,column=0,sticky=W)
        result_entry=Scale(root,from_=0,to=100,orient=HORIZONTAL,variable=marks).grid(row=6,column=1,sticky=W)


    def get(self):

        if not validate_email(emailVar.get()):
            # validate_email() check that given email is valid or not and returns Boolean vale
            msg.showerror('Error','Invalid Email Address...!')
       # if validate_email(emailVar.get(),verify=True):
          #  msg.showerror('Error','This Email address is already exist...!')
        elif (len(mobileVar.get()))!=10:
            msg.showerror('Error','Invalid Mobile Number...!')
        elif nameVar.get()=='':
            msg.showwarning('Warning','Fill valid name...!')
        elif marks.get()==0:
            msg.showwarning('Warning','Fill the Marks...!')
        else:
            with open("Records.txt",'a') as rs:
                rs.write("Name :")
                rs.write(str(nameVar.get()))   # to write class variable in file we must use get method otherwise we got data in the form of 'PY_VAR0',PY_VAR"
                rs.write("\nEmail :")
                rs.write(str(emailVar.get()))
                rs.write("\nMobile :")
                rs.write(str(mobileVar.get()))
                rs.write("\nCountry :")
                rs.write(str(countryVar.get()))
                rs.write("\nDegree Course :")
                rs.write(str(degreeVar.get()))
                rs.write("\nMarks Obtained :")
                rs.write(str(marks.get()))
                rs.write("\n\n")
                sys.exit()

    def submit(self):
        Button(root,text="Submit Details",fg='white',bg='black',command=self.get).grid(row=20,column=1,pady=40)

root=Tk().minsize(500,500)
frm=Frame(root,bg="grey",borderwidth=6)
frm.grid(row=0,column=1,pady=20)
Label(frm,text=" Entrance Exam Form").grid(row=0,column=1)
nameVar = StringVar()
countryVar = StringVar()
emailVar=StringVar()
mobileVar=StringVar()
degreeVar = StringVar()
marks=StringVar()

'''for callable in Form.__dict__.values():
    callable()'''
f=Form()
f.name()
f.email()
f.mobile_no()
f.country()
f.degree()
f.result()
f.submit()
mainloop()