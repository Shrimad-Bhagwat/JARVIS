import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random
import sys
import time
import tkinter
import modules.camera as opencv
import src.faces as face
# import mysql.connector as sqltor



greetings=["hello","hi","hey"]
wish={"morning":"Good Morning",
        "night":"Good Night",
        "care":"You too",
        "bye":"Please don't go"
        }
silly={
        "marry":"No I have a boyfriend",
        "love":"I love myself",
        "hate": "lmao, look at your face",
        }
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

'''def tk(Text):
    
   
    root=tkinter.Tk()
    widgt1=tkinter.Label(root,text=Text)
    widgt1.pack()
    widgt2=tkinter.Button(root,text="Quit",command=root.destroy)
    
    widgt2.pack()
    root.mainloop()

'''
def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

def pri_spk(ps):
    print(ps)
    speak(ps)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        pri_spk('Good Morning!')
    

    elif hour>=12 and hour<18:
        pri_spk("Good Afternoon!")
    
        

    else:
        pri_spk("Good Evening!")
    
          
      
    #tk('Hello Sir, I am your digital assistant JARVIS!') 
    pri_spk('Hello Sir, I am your digital assistant JARVIS!')

    


    y=query.split(" ")
    for word in y:
        if word in greetings:
            pri_spk(greetings[random.randint(0,3)])
        elif word in wish:
            pri_spk(wish[word])
        elif word in silly:
            pri_spk(silly[word])
        

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        r.phrase_threshold = 0.1
         
        
        audio = r.listen(source)
        


    try:
        print("Recognizing...")
        
         
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        print("\n"*100)
        

    except Exception :
         
        print("Say that again please...")  
        #speak("Say that again please...")
        
        return " "
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('<your-email>', '<password>')
    server.sendmail('<your-email>', to, content) 
    server.close()

    


if __name__ == "__main__":
   
    speak("Verifying Identity..")
    x=face.faceRecognition()
    if x=='<the-name-of-the-person-you-want-to-allow-to-access>':
        speak("Access Granted...")
        wishMe()
        

    
    
    #while True:  #temporary
        while True:    
            
        
            query = takeCommand().lower()

            # Logic for executing tasks based on query
            


            
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                pri_spk(results)
                
            elif 'open youtube' in query:
                try:
                    speak('What should I Search for?')
                    query1=takeCommand()               
                    webbrowser.open("https://www.youtube.com/results?search_query="+query1)
                    
                except:
                    speak('Not Working')
                    webbrowser.open('www.youtube.com')

            elif 'google' in query:
                speak('Search in Google for?')
                

                query1 =takeCommand()
                
                speak('opening Google and searching for'+query1)
                webbrowser.open("https://www.google.com/search?source=hp&ei=yo0AXZD6I92PwgPcyrCQCA&q="+query1)
            
            elif 'open gmail' in query:
                speak('opening Gmail')
                webbrowser.open('www.gmail.com')

            elif 'play music' in query:
                music_dir = '<music-directory-path>'
                songs = os.listdir(music_dir)
                
                a=random.randint(0,31)   
                os.startfile(os.path.join(music_dir, songs[a]))
                x=songs[a]
                print('Playing :',x)
                speak('Playing :'   )
                      
            elif 'play video' in query:
                video_dir='<video-directory-path>'
                video= os.listdir(video_dir)
                print(video)
                a=random.randint(0,4)   
                os.startfile(os.path.join(video_dir, video[a]))
                x=video[a]
                print('Playing :',x)
                speak('Playing :')
                continue
                
            elif 'time' in query: 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'hey' in query or 'hello' in query or 'jarvis' in query:
                i=random.randint(0,3)
                greet=greetings[i]
                pri_spk(greet)
             
            elif 'open python' in query:
                codePath =  "<path-to-python>\\idle.pyw"
                os.startfile(codePath)

            elif 'open game' in query:
                speak('opening Gamee')
                webbrowser.open("")
                
            elif 'pay fees' in query:
                speak('opening Fees portal')
                webbrowser.open("")
                
            elif 'send mail' in query:
                pri_spk('Send mail to ?')
                
                if 'Name1' in query:
                    try:
                        speak("What should I say?")
                        content = takeCommand()
                        to = "name1@email.com"    
                        sendEmail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("I am not able to send this email")    
                elif 'Name2' in query:
                    try:
                        speak("What should I say?")
                        content = takeCommand()
                        to = "name2@emaill.com"    
                        sendEmail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak(" I am not able to send this email") 
                
                elif 'name3' in query:
                    try:
            
                        speak("What should I say?")
                        content = takeCommand()
                        to = "name3@email.com"    
                        sendEmail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak(" I am not able to send this email")    
            
            elif 'nothing' in query or 'abort' in query or 'stop' in query or 'bye' in query:
                speak('Bye Sir, have a good day.')
                sys.exit()

            elif "binary" in query:
                speak("Encode or decode")
                query2=takeCommand().lower()
                if query2=='encode':
                    speak("Enter data :")
                    query1=takeCommand()
                    x=b.encode(query1)
                    print(x)
                    speak(x)
                elif query2=='decode':
                    speak("Enter data :")
                    query1=takeCommand()
                    x=b.decode(query1)
                    print(x)
                    speak(x)
                else:
                    speak("Say again!")
 
            elif "today's weather" in query:
                webbrowser.open("https://www.google.com/search?source=hp&ei=yo0AXZD6I92PwgPcyrCQCA&q="+"today's weather")

            
            else:
                speak("Access Denied...")    


  







        
            # elif 'file' in query:

            #     speak("File name : ")
            #     query1=takeCommand()
            #     filename="f:\\jarvis\\file\\"+query1+".txt"
            #     speak("Read , Append or Write")
            #     choice=takeCommand().lower()
            #     if choice =="read":
            #         myfile=open(filename,'r')
                    
            #         try:
            #             data=myfile.readlines()
                        
            #             print(data)
            #             speak(data)

                    
            #             myfile.close()
            #             speak("Done")
            #         except:
            #             continue

            #     elif choice=="append":
            #         myfile=open(filename,'a')
            #         speak("Input : ")
            #         try:
            #             query2=takeCommand()
            #             myfile.writelines(query2+"\n")
            #             myfile.close()
            #             speak("Done")
            #         except:
            #             continue


            #     elif choice=="write":
            #         myfile=open(filename,'w')
            #         speak("Input : ")
            #         try:
            #             query2=takeCommand()
            #             myfile.writelines(query2+"\n")
            #             myfile.close()
            #             speak("Done")
            #         except:
            #             continue


            # elif 'database' in query:
            #     db=sqltor.connect(host="localhost",user="root",passwd="mysql",database="shrimad01")
            #     cur=db.cursor()
            #     speak("Try speaking the command or write it.")
            #     try:
            #         query1=takeCommand()
            #         if 'star' in query1:
            #             query1 = query1.replace("star", "*")
            #         cur.execute(query1)
            #     except:
            #         speak("I didn't get that try typing the command .")

            #         query1=input("Enter command : ")
            #         cur.execute(query1)
            
            #     result=cur.fetchall()
                
            #     print(result) 
            #     speak(result)
            #     db.close()
