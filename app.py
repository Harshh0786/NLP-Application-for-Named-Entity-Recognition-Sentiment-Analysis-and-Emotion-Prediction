import json
from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API
class NLPApp:

    def __init__(self):

        # Create db obect

        self.dbo = Database()

        # create apio object

        self.apio = API()
        # login ka gui load karna hai

        self.root = Tk()
        self.root.title('NLPApp')          # for title changing
        self.root.iconbitmap('resources/favicon.ico')   # to change app icon img
        self.root.geometry('350x600')      # set width and height
        self.root.configure(background='#5779B8')   # to configure your gui

        self.login_gui()

        self.root.mainloop()      # it holds the gui

    def login_gui(self):

        self.clear()

        heading = Label(self.root,text='NLPApp',bg='#5779B8',fg='#374E78')    # define gui object and tell the text
        heading.pack(pady=(30,30))        # pady for pading at y axis
        heading.configure(font=('verdana',27,'bold'))    # to configure the label

        label1 = Label(self.root,text='Enter Email',bg='#5779B8',fg='white')
        label1.pack(pady=(10,10))
        label1.configure(font=('verdana',14,'bold'))

        self.email_input = Entry(self.root,width=30)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root, text='Enter Password',bg='#5779B8',fg='white')
        label2.pack(pady=(10, 10))
        label2.configure(font=('verdana', 14, 'bold'))

        self.password_input = Entry(self.root, width=30,show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root,text='Login',width=15,height=1,bg='#5779B8',command=self.perform_login)
        login_btn.pack(pady=(20,10))

        label3 = Label(self.root, text='Not a Member?',bg='#5779B8',fg='white')
        label3.pack(pady=(20, 10))
        label3.configure(font=('verdana', 10, 'bold'))

        redirect_btn = Button(self.root, text='Register now',command=self.register_gui,bg='#5779B8')
        redirect_btn.pack(pady=(10, 10))

    def register_gui(self):

        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#5779B8', fg='#374E78')  # define gui object and tell the text
        heading.pack(pady=(30, 30))  # pady for pading at y axis
        heading.configure(font=('verdana', 27, 'bold'))  # to configure the label

        label0 = Label(self.root, text='Enter Name', bg='#5779B8', fg='white')
        label0.pack(pady=(10, 10))
        label0.configure(font=('verdana', 14, 'bold'))

        self.name_input = Entry(self.root, width=30)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='Enter Email', bg='#5779B8', fg='white')
        label1.pack(pady=(10, 10))
        label1.configure(font=('verdana', 14, 'bold'))

        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter Password', bg='#5779B8', fg='white')
        label2.pack(pady=(10, 10))
        label2.configure(font=('verdana', 14, 'bold'))

        self.password_input = Entry(self.root, width=30, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root, text='Register', width=15, height=1, bg='#5779B8',command=self.perform_registration)
        login_btn.pack(pady=(20, 10))

        label3 = Label(self.root, text='Already a Member?', bg='#5779B8', fg='white')
        label3.pack(pady=(20, 10))
        label3.configure(font=('verdana', 10, 'bold'))

        redirect_btn = Button(self.root, text='Login now', command=self.login_gui, bg='#5779B8')
        redirect_btn.pack(pady=(10, 10))

    def clear(self):
        # clear the existing gui
        for i in self.root.pack_slaves():        # pack_slaves gui ke elements ko utha ke le aata hai
            i.destroy()                   # destroy the elements

    def perform_registration(self):

        # fetch the data from the gui
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success','Registration successful. you can join now')
        else:
            messagebox.showerror('error','email already exists')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email,password)

        if response:
            messagebox.showinfo('Success', 'Login successful.')
            self.home_gui()
        else:
            messagebox.showerror('error', 'Incorrect email / password ')

    def home_gui(self):

        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#5779B8', fg='#374E78')  # define gui object and tell the text
        heading.pack(pady=(30, 30))  # pady for pading at y axis
        heading.configure(font=('verdana', 27, 'bold'))  # to configure the label

        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=3, bg='#5779B8',command=self.sentiment_analysis)
        sentiment_btn.pack(pady=(20, 10))

        ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=3, bg='#5779B8',command=self.named_entity_recognition)
        ner_btn.pack(pady=(20, 10))

        emotion_btn = Button(self.root, text='Emotion Prediction', width=30, height=3, bg='#5779B8',command=self.emotion_prediction)
        emotion_btn.pack(pady=(20, 10))

        logout_btn = Button(self.root, text='Logout', width=10, height=1, bg='#5779B8',command=self.login_gui)
        logout_btn.pack(pady=(20, 10))

    def sentiment_analysis(self):

        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#5779B8', fg='#374E78')  # define gui object and tell the text
        heading.pack(pady=(30, 30))  # pady for pading at y axis
        heading.configure(font=('verdana', 27, 'bold'))  # to configure the label

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#5779B8', fg='white')  # define gui object and tell the text
        heading2.pack(pady=(10,20))  # pady for pading at y axis
        heading2.configure(font=('verdana', 19, 'bold'))  # to configure the label

        label1 = Label(self.root, text='Enter the text', bg='#5779B8', fg='white')
        label1.pack(pady=(5, 10))
        label1.configure(font=('verdana', 10, 'bold'))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        sentiment_btn = Button(self.root, text='Analyze Sentiment', width=20, height=2, bg='#5779B8',
                               command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root,text='', bg='#5779B8', fg='white')
        self.sentiment_result.pack(pady=(5, 5))
        self.sentiment_result.configure(font=('verdana', 15))

        goback_btn = Button(self.root, text='Go Back', width=20, height=2, bg='#5779B8',command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):

        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        txt = ''
        for i in result['sentiment']:
            txt = txt + i + ' -> ' + str(result['sentiment'][i]) + '\n'

        self.sentiment_result['text'] = txt

    def named_entity_recognition(self):

        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#5779B8', fg='#374E78')  # define gui object and tell the text
        heading.pack(pady=(30, 30))  # pady for pading at y axis
        heading.configure(font=('verdana', 27, 'bold'))  # to configure the label

        heading2 = Label(self.root, text='Named Entity Recognition', bg='#5779B8', fg='white')  # define gui object and tell the text
        heading2.pack(pady=(10,20))  # pady for pading at y axis
        heading2.configure(font=('verdana', 15, 'bold'))  # to configure the label

        label1 = Label(self.root, text='Enter the text', bg='#5779B8', fg='white')
        label1.pack(pady=(5, 10))
        label1.configure(font=('verdana', 10, 'bold'))

        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(5, 10), ipady=4)

        ner_btn = Button(self.root, text='Click here', width=20, height=2, bg='#5779B8',
                               command=self.do_named_entity_recognition)
        ner_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root,text='', bg='#5779B8', fg='white')
        self.ner_result.pack(pady=(2, 2))
        self.ner_result.configure(font=('verdana', 10))

        goback_btn = Button(self.root, text='Go Back', width=20, height=2, bg='#5779B8',command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_named_entity_recognition(self):

        text = self.ner_input.get()
        result = self.apio.ner(text)

        output = ''
        output_str = ''

        for entity in result['entities']:
            output_str += 'name :{}'.format(entity['name'] + '\n')
            output_str += 'Category :{}'.format(entity['category'] + '\n')
            output_str += 'Confidence Score :{}'.format(str(entity['confidence_score']) + '\n')
            output_str += '\n'

        output = str(output_str)

        self.ner_result['text'] = output



    def emotion_prediction(self):

        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#5779B8', fg='#374E78')  # define gui object and tell the text
        heading.pack(pady=(30, 30))  # pady for pading at y axis
        heading.configure(font=('verdana', 27, 'bold'))  # to configure the label

        heading2 = Label(self.root, text='Emotion Prediction', bg='#5779B8', fg='white')  # define gui object and tell the text
        heading2.pack(pady=(10,20))  # pady for pading at y axis
        heading2.configure(font=('verdana', 19, 'bold'))  # to configure the label

        label1 = Label(self.root, text='Enter the text', bg='#5779B8', fg='white')
        label1.pack(pady=(5, 10))
        label1.configure(font=('verdana', 10, 'bold'))

        self.ep_input = Entry(self.root, width=50)
        self.ep_input.pack(pady=(5, 10), ipady=4)

        emotionp_btn = Button(self.root, text='Click here', width=20, height=2, bg='#5779B8',
                               command=self.do_emotion_prediction)
        emotionp_btn.pack(pady=(10, 10))

        self.ep_result = Label(self.root,text='', bg='#5779B8', fg='white')
        self.ep_result.pack(pady=(5, 5))
        self.ep_result.configure(font=('verdana', 15))

        goback_btn = Button(self.root, text='Go Back', width=20, height=2, bg='#5779B8',command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_emotion_prediction(self):

        text = self.ep_input.get()
        result = self.apio.emotion_prediction(text)

        txt = ''
        for i in result['emotion']:
            txt = txt + i + ' -> ' + str(result['emotion'][i]) + '\n'

        self.ep_result['text'] = txt

nlp = NLPApp()