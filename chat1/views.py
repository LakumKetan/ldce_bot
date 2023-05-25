from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from nltk.tokenize import word_tokenize

def find_list():
    f = open("D:/ChatBot/Untitled Folder/Ketan_lakum_final3.txt",'r')
    lines = f.readlines()
    urls_list = []
    urls_keyword = []
    i=1
    for line in lines:
        print(line,i)
        i += 1
        line = line.replace('\n','')
        line = line.split(',')
        urls_list.append(line[0])
        urls_keyword.append(line[1])
    f.close()
    f = open("D:/ChatBot/Untitled Folder/mix_url_sentences-Copy1.txt",'r')
    lines = f.readlines()
    urls_list1 = []
    urls_keyword1 = []
    for line in lines:
        line = line.replace('\n','')
        line = line.split(',')
        urls_list1.append(line[0])
        urls_keyword1.append(line[1])
    f.close()
    return urls_list, urls_keyword, urls_list1, urls_keyword1



def find_list1():
    f = open("D:/ChatBot/Untitled Folder/a_u_text1.txt",'r',encoding="utf-8")
    lines = f.readlines()
    urls_list = []
    urls_keyword = []
    for line in lines:
        line = line.replace('\n','')
        line = line.split(',')
        urls_list.append(line[0])
        urls_keyword.append(line[1])
    f.close()
    return urls_list, urls_keyword

def find_link1(query):
    tokens1 = query.split(' ')
    urls_list , urls_keyword = find_list1()
    index = 0
    length_url = float("inf")
    count_cont = 0
    for i in range(len(urls_list)):
        count = 0
        for word in tokens1:
            if word in urls_keyword[i]:
                count += 1
            if count > count_cont:
                index = i
                length_url = len(urls_list[i])
                count_cont = count
            if count == count_cont:
                if length_url > len(urls_list[i]):
                    index = i
                    length_url = len(urls_list[i])
    return urls_list[index]

def find_link(query):
    tokens1 = query.split(' ')
    urls_list , urls_keyword, urls_list1, urls_keyword1 = find_list()
    index = 0
    length_url = 5000
    count_cont = 0
    for i in range(len(urls_list)):
        count = 0
        for word in tokens1:
            if word in urls_keyword[i]:
                count += 1
            if count > count_cont:
                index = i 
                length_url = len(urls_list[i])
                count_cont = count
            if count == count_cont:
                if length_url > len(urls_list[i]):
                    index = i
                    length_url = len(urls_list[i])
    index1 = 0
    length_url = 5000
    count_cont = 0
    for i in range(len(urls_list1)):
        count = 0
        for word in tokens1:
            if word in urls_keyword1[i]:
                count += 1
            if count > count_cont:
                index1 = i 
                length_url = len(urls_list1[i])
                count_cont = count
            if count == count_cont:
                if length_url > len(urls_list1[i]):
                    index1 = i
                    length_url = len(urls_list1[i])
    return urls_list[index],urls_list1[index1]


def index(request):
    return render(request, "chat1/index3.html")

def specific(request):
    # return HttpResponse('This is specific')
    return render(request, "chat1/index3.html")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    userMessage,userMessage1 = find_link(userMessage.lower())
    # userMessage2 = find_link1(userMessage.lower())
    return HttpResponse(userMessage+","+userMessage1)


