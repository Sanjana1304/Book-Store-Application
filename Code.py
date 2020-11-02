#CODE FOR BOOK_STORE_APLLICATION.

import time
import csv

print("Hey bookworm ! \nWorried where to store your books?")
time.sleep(1)
print("I have created an application for you :) ")
time.sleep(1)

def store_book():   ### this function will store all the books provided by the user.
    global book_list
    book=input("\n\nEnter the name of the book : ")
    author=input("Enter the name of the author : ")
    genre=input("What is the genre of your book ? ")
    publisher=input("Name of the publisher : ")
    published_date=input("Published Date : " )
    
    book_list=[book,author,genre,publisher,published_date]
    with open("June_Challenge.csv", 'a') as file_obj:
        details=csv.writer(file_obj)
        details.writerow(book_list)

def access_book():
    print("On what basis you want to search your book ? ")
    print("OPTIONS :\n","1.BOOK NAME","2.AUTHOR","3.GENRE","4.PUBLISHER","5.PUBLISHED DATE",sep="\n")
    time.sleep(1)
    choice=input("\nEnter your choice from 1-5 : ")
    if choice=="1":
        count=0
        give_name=input("Enter the name of the book to be searched : ")
        print("\n")
        with open("June_Challenge.csv",'r') as read_file:
            get_detail=csv.reader(read_file)
            print("S.No  Book Name           Author              Genre           Publisher             Published Date ")
            print("*****************************************************************************************************")
            for i in get_detail:
                if i!=[]:
                    if i[0]==give_name:
                        count+=1
                        print(str(count).ljust(4),i[0].ljust(20),i[1].ljust(20),i[2].ljust(15),i[3].ljust(20),i[4].ljust(5))
                        print("-----------------------------------------------------------------------------------------------------")
            print("\nNo of books found = ",count)
    elif choice=="2":
        count=0
        give_auth=input("Enter the name of the author to search the book : ")
        print("\n")
        with open("June_Challenge.csv",'r') as read_file:
            get_detail=csv.reader(read_file)
            print("S.No  Book Name           Author              Genre           Publisher             Published Date ")
            print("*****************************************************************************************************")
            for i in get_detail:
                if i!=[]:
                    if i[1]==give_auth:
                        count+=1
                        print(str(count).ljust(4),i[0].ljust(20),i[1].ljust(20),i[2].ljust(15),i[3].ljust(20),i[4].ljust(5))
                        print("-----------------------------------------------------------------------------------------------------")
            print("\nNo of books found = ",count)
    elif choice=="3":
        count=0
        give_gen=input("Enter the genre to search the book : ")
        print("\n")
        with open("June_Challenge.csv",'r') as read_file:
            get_detail=csv.reader(read_file)
            print("S.No  Book Name           Author              Genre           Publisher             Published Date ")
            print("*****************************************************************************************************")
            for i in get_detail:
                if i!=[]:
                    if i[2]==give_gen:
                        count+=1
                        print(str(count).ljust(4),i[0].ljust(20),i[1].ljust(20),i[2].ljust(15),i[3].ljust(20),i[4].ljust(5))
                        print("-----------------------------------------------------------------------------------------------------")
            print("\nNo of books found = ",count)
    
    elif choice=="4":
        count=0
        give_pub=input("Enter the name of the publisher to search the book : ")
        print("\n")
        with open("June_Challenge.csv",'r') as read_file:
            get_detail=csv.reader(read_file)
            print("S.No  Book Name           Author              Genre           Publisher             Published Date ")
            print("*****************************************************************************************************")
            for i in get_detail:
                if i!=[]:
                    if i[3]==give_pub:
                        count+=1
                        print(str(count).ljust(4),i[0].ljust(20),i[1].ljust(20),i[2].ljust(15),i[3].ljust(20),i[4].ljust(5))
                        print("-----------------------------------------------------------------------------------------------------")
            print("\nNo of books found = ",count)
    elif choice=="5":
        count=0
        print("How do you want to retrieve your book?")
        print("1.SPECIFIC YEAR","2. BETWEEN ANY 2 YEARS","3.BOOKS BEFORE A YEAR","4. BOOKS AFTER A YEAR",sep="\n")
        give_choice=input("Enter your choice : ")
        if give_choice=="1":
            give_pubd=input("Enter the published date to search the book : ")
            print("\n")
            with open("June_Challenge.csv",'r') as read_file:
                get_detail=csv.reader(read_file)
                print("S.No  Book Name           Author              Genre           Publisher             Published Date ")
                print("*****************************************************************************************************")
                for i in get_detail:
                    if i!=[]:
                        if i[4]==give_pubd:
                            count+=1
                            print(str(count).ljust(4),i[0].ljust(20),i[1].ljust(20),i[2].ljust(15),i[3].ljust(20),i[4].ljust(5))
                            print("-------------------------------------------------------------------------------------------------")
        elif give_choice=="2":
            give_pubd1=int(input("Enter the starting published date to search the book : "))
            give_pubd2=int(input("Enter the ending published date to search the book : "))
            print("\n")
            print("Books published between these two years are : ")
            with open("June_Challenge.csv",'r') as read_file:
                get_detail=csv.reader(read_file)
                print("S.No  Book Name           Author              Genre           Publisher             Published Date ")
                print("*****************************************************************************************************")
                for i in get_detail:
                    if i!=[]:
                        if int(i[4])>=give_pubd1 and int(i[4])<=give_pubd2:
                            count+=1
                            print(str(count).ljust(4),i[0].ljust(20),i[1].ljust(20),i[2].ljust(15),i[3].ljust(20),i[4].ljust(5))
                            print("--------------------------------------------------------------------------------------------------")
            print("\nNo of books found = ",count)
        elif give_choice=="3":
            give_pubd1=int(input("Enter the published date to search all books published before that year : "))
            print("\n")
            print("Books published before that year is : ")
            with open("June_Challenge.csv",'r') as read_file:
                get_detail=csv.reader(read_file)
                print("S.No  Book Name           Author              Genre           Publisher             Published Date ")
                print("*****************************************************************************************************")
                for i in get_detail:
                    if i!=[]:
                        if int(i[4])<=give_pubd1:
                            count+=1
                            print(str(count).ljust(4),i[0].ljust(20),i[1].ljust(20),i[2].ljust(15),i[3].ljust(20),i[4].ljust(5))
                            print("--------------------------------------------------------------------------------------------------")
            print("\nNo of books found = ",count)
        elif give_choice=="4":
            give_pubd1=int(input("Enter the published date to search all books published after that year : "))
            print("\n")
            print("Books published after that year is : ")
            with open("June_Challenge.csv",'r') as read_file:
                get_detail=csv.reader(read_file)
                print("S.No  Book Name           Author              Genre           Publisher             Published Date ")
                print("*****************************************************************************************************")
                for i in get_detail:
                    if i!=[]:
                        if int(i[4])>=give_pubd1:
                            count+=1
                            print(str(count).ljust(4),i[0].ljust(20),i[1].ljust(20),i[2].ljust(15),i[3].ljust(20),i[4].ljust(5))
                            print("--------------------------------------------------------------------------------------------------")
            print("\nNo of books found = ",count)
        else:
            print("Pls enter from 1-4")
    else:
        print("Pls enter from 1-5")
def book_application():
    print("Here are my features : ")
    print("----------------------------")
    print("| 1. STORE MY BOOK          |")
    print("| 2. FIND MY BOOK           |")
    print("| 3. DISPLAY ALL MY BOOKS : |")
    print("----------------------------")
    print("First try storing your books,so that you can retreive it whenever u want :)) ")
    time.sleep(1)
    print("\nWhat do you want to do now ?")
    ur_choice=input("Enter your Choice : ")
    if ur_choice=="1":                                                ### This will open the store_book function and store the user's books
        print("Cool ! Give me the details and I will store your book ;) ")
        store_book()
        print("\n\nThanks for the information ! I will store your book")
        
    elif ur_choice=="2":                                               ### This will go to the access_book function and find the user's book
        print("\nOkay! Let's find your book")
        access_book()
        print("\nHope you found your book ;) ")

    elif ur_choice=="3":                                                ### This will open the file and show all the book collections 
        print("\nOkay ! Let me show your book collection !")
        time.sleep(1)
        print("S.No  Book Name           Author              Genre           Publisher             Published Date ")
        print("*****************************************************************************************************")
        with open("June_Challenge.csv",'r') as file_obj:
            get_all=csv.reader(file_obj)
            count=0
            for i in get_all:
                if i!=[]:
                    count+=1
                    print(str(count).ljust(4),i[0].ljust(20),i[1].ljust(20),i[2].ljust(15),i[3].ljust(20),i[4].ljust(5))
                    print("-----------------------------------------------------------------------------------------------------")
            print("Total no of books = ",count)
    else:
        print("Pls Choose between 1-3")
choice='yes'
while choice[0]=="y" or choice[0]=="Y":
    book_application()
    choice=input("\nDo you wanna use me again ? ")
