#!/usr/bin/env python3.7

##
#Import Section
import random
import json
import pickle
import numpy as np 
import re
import nltk 
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model 
##

##
#Initialises needed objects to process the input and opens the intents/model
lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pk1', 'rb'))
classes = pickle.load(open('classes.pk1', 'rb'))
model = load_model('cyberbotmodel.h5')
##

####
#DNN processing and initialisation

#Cleans up the input and lemmatizes the sentence 
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

#Creates a bag of words ( An array with a 1 if the word is found and a 0 if not ) in place of the words in the sentence
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1 
                
    return np.array(bag)

#Uses the model and takes the highest probable result from the different results of the neuralnet based on the probability
def predict_class(sentence):
    #create bag of words
    bow = bag_of_words(sentence)
    #predicting the results
    res = model.predict(np.array([bow]))[0]
    #threshold of the probability capped at 25%
    ERROR_THRESHOLD = 0.25
    #remove the uncenrtanty by cappping with the threshold 
    results = [[i, r] for i,r in enumerate(res) if r > ERROR_THRESHOLD]
    #sort by probability in order ( highest probability first) 
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probablility': str(r[1])})
    return return_list

##Mock chatbot testing part
def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result 
##

####



####
#Processing section / Results formatting

print("~~~~~CyberBot is Running!~~~~~")
print("What would you like me to process?")

##
#Opens the nmap scan file and reads it's content ( The scan results ) 
scantext = open("NmapScan.txt", "r") 
content = scantext.read()
scantext.close()
##

##
#removes characters like { } [ ] to be able to split and process the string 
replaced_content = content.replace('[', '')
replaced_content = replaced_content.replace(']','')
replaced_content = replaced_content.replace('{','')
replaced_content = replaced_content.replace('}','')
scan_content = re.split(',',replaced_content)
##

##
#initialising variables needed
message = " "
i = 0
linuxcpe = ""
apachecpe = ""
generalcpe = ""
nginxcpe = ""
mswindowscpe = ""
oraclecpe = ""
ftpcpe = ""
report_str = ""
##

##
#Two classes that formats the response for the final Report
def cpe_check(botres, cpe):
    ##
    #calling global variables
    global linuxcpe
    global apachecpe
    global generalcpe
    global nginxcpe
    global mswindowscpe
    global oraclecpe
    global ftpcpe
    ##

    ##Linux
    if botres == "This environment runs on Linux, here are the cpe's found:":
        if linuxcpe == "": 
            linuxcpe = botres + "\n" + cpe + "\n"
        else:
            linuxcpe = linuxcpe + cpe + "\n"
    ##General
    elif botres == "A general CPE has been found, check the details below":
        if generalcpe == "": 
            generalcpe = botres + "\n" + cpe + "\n"
        else:
            generalcpe = generalcpe + cpe + "\n"
    ##Apache
    elif botres == "A version of apache has been detected! Here are the cpe's found:":
        if apachecpe == "": 
           apachecpe = botres + "\n" + cpe + "\n"
        else:
            apachecpe = apachecpe + cpe + "\n"
    ##Nginx
    elif botres == "Nginx has been found! Here are the cpe's found:":
        if nginxcpe == "": 
            nginxcpe = botres + "\n" + cpe + "\n"
        else:
            nginxcpe = nginxcpe + cpe + "\n"
    ##Windows
    elif botres == "A Microsoft based product has been found, most probably a Windows Operating System. Check below for more details":
        if mswindowscpe == "": 
            mswindowscpe = botres + "\n" + cpe + "\n"
        else:
            mswindowscpe = mswindowscpe + cpe + "\n"
    ##Oracle
    elif botres == "An oracle product has been found. Check the Product and version below":
        if oraclecpe == "": 
            oraclecpe = botres + "\n" + cpe + "\n"
        else:
            oraclecpe = oraclecpe + cpe + "\n"
    ##ftp
    elif botres == "An FTP product has been discovered. Check below for more details":
        if ftpcpe == "": 
            ftpcpe = botres + "\n" + cpe + "\n"
        else:
            ftpcpe = ftpcpe + cpe + "\n"
##

##
#Creates the final string that will be displayed to the user
def final_str():
    report_str = generalcpe +"\n"+ linuxcpe +"\n" + apachecpe +"\n"+ nginxcpe +"\n" + mswindowscpe +"\n" + oraclecpe +"\n"+ ftpcpe
    cyber_report = open("cyberbotreport.txt", "w")
    cyber_report.write(report_str)
    cyber_report.close()
##

##Creating a while loop that iterates and feeds the deep learning algorithm the results in cut strings    
for x in scan_content:
    if 'cpe' in x: 
        message = x
        ints = predict_class(message)
        res = get_response(ints,intents)
        cpe_check(res, message)
        message = " "
##

#calls the function that takes the global variables and concatenates the strings(Results) into a Report acceptable format
final_str()

