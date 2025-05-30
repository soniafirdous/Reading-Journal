######### DATA STORAGE /FILE HANDLING

# LOADS BOOK AND QUOTE FROM .txt files  when the  programs starts
books=[]
def load_books():
    with open ("books.txt","r")as f:
        for line in f:
            title,author,year,genres,status=line.strip().split("|")
            book= {
                "title":title,
                "author":author,
                "year":year,
                "genres": set(genres.split(",")),
                "status":status
            }
            books.append(book)

quotes=[]
def load_quotes():
    with open("quotes.txt","r") as f:
        for line in f:
            text,title,page_number=line.strip().split("|")     
            quote={
                "text":text,
                "title":title,
                "page_number":page_number
            }     
            quotes.append(quote)

# SAVE BOOKS AND QUOTES
def save_books():
    with open ("books.txt","w") as f:
        for book in books:
            line = f"{book['title']}|{book['author']}|{book['year']}|{','.join(book['genres'])}|{book['status']}\n"
            f.write(line)
def save_quotes():
    with open("quotes.txt","w")as f:
        for quote in quotes:
            line=f"quote['text'],quote['title'],quote['page_number']"
            f.write(line)




######## FILE FEATURES(FUNCTIONS)


# FUNCTION TO Add a new book entry (unique title + author)


def add_unique_book(books):
 title=input("enter book title : ")
 author=input("enter book author :")

 # for unique book

 for b in books:
     if b["title"]==title and b["author"]==author :
        print("book already exists")
        return

 year=int(input("enter year published:"))
 genres=set(input("enter geners  seperated by commas:").strip().split(","))
 status=input("enter  status (reading/completed/on hold)")

 book={
        "title": title,
        "author": author,
        "year": year,
        "genres": genres,
        "status": status
    }
 books.append(book)
 print("Book added.")

# function to View all books (sorted by year published):


def view_books(books):
    for b in sorted(books,key=lambda x:x["year"]):
      print(f"all books :\n {b['year']}-----{b['title']}")



#Search books by genre or status


def search_books(books):

 choice=input("enter choice(search by  genre or status) :")
 keyword=input("enter search key word :")
 for b in books:
    if  choice=="genre" and keyword in b["genres"]:
       print(f"{b['title']} belongs to {','.join(b['genres'])}")
    elif choice=="status" and keyword==b["status"]:
       print(f"{b['title']} is currently {b['status']}")


# Function to Update a book’s status or add genres

def update_books(books):


    title=input("enter title:")
    author=input("enter author:")
    for b in books:
        if b["title"]==title and b["author"]==author:
           new_status=input("enter new status:")
           b["status"]=new_status
           new_genres=input("enter new genre :").strip().split(",")
           b["genres"].update(new_genres)
    print("book updated")



# Function to Delete a book entry

def del_books(books):

    title=input("enter title:")
    author=input("enter author:")
    for b in books:
     if b["title"]==title and b["author"]==author:
        books.remove (b)

    print("book deleted")

####### Quote Collection

# Function to Add a new quote (text, book title, page number)

def add_quotes(quotes):
   text=input("enter quote:")
   title=input("enter title:")
   page_number=int(input("enter page number"))
   quote={"text":text,"title":title,"page_number":page_number}
   quotes.append(quote)
   print("quote added")



# Function to View all quotes (sorted by book or author)


def view_quotes(quotes):
    choice=input("enter choice (sorted by book title or author)")
    if choice=="book":
      for q in sorted(quotes,key=lambda x:x["title"]):
          print(f"Quote sorted by books title :{q['title']}-------\"{q['text']}\"")



# Function to Search quotes by keyword


def search_quote(quotes):
    keyword=input("enter search keyword :")
    for q in quotes:
     if keyword in q["text"]:
        print(f"{q['title']}-----\"{q['text']}\"")


# Function to Delete a quote 

def del_quote(quotes):
   del_text=input("enter the quote :")
   for q in quotes:
      if q["text"]==del_text:
         quotes.remove(q)
         print("quote deleted")



        
######## ANALYSIS FEATURE


# Functin to List all books completed in a user-given year

def books_compelted_year(books):
   year=input("enter year :")
   for b in books:
      if b["year"]==year and b["status"]=="completed" :
         print(f"books completed in {b['year']} are {b['title']}")

#Function to Show the book with the most collected quotes

def count_quotes(quotes):
   
   count={}
   for q in quotes:
      count[q["title"]]=count.get(q["title"],0)+1
      most_quotes=max(count,key=count.get)
      
      print(f"the book  is {most_quotes} with the most collected quotes with a count of {count['most_quotes']}")

# function to Find the author(s) with the most entries


def most_author_enteries(books):
   count={}
   for b in books:
      count[b["author"]]=count.get(b["author"],0)+1
      entries_author=max(count,key=count.get)
      print(f" the {entries_author} has the maximum enteries  {count[entries_author]} ")



######## Menu 
def menu():
   print("\" \t MENU:\"")

   
   print("1. Book collection")
   print("2. Quote collection")
   print("3. Analysis Feature")
   print("4. Exit")


def book_collection_menu():
    print("sub choice:")
    print("a. Add Book")
    print("b. View Books")
    print("c. Search Books")
    print("d. Update Book")
    print("e. Delete Book")
    print("f. return")
def quote_collection_menu():
    print("sub choice:")
    print("a. Add Quote")
    print("b. View Quotes")
    print("c. Search Quotes")
    print("d. Delete Quote")
    print("e. return")
def analysis_menu():
    print("sub choice:")
    print("a. Completed Books in Year")
    print("b. Most Quotes in a book")
    print("c. Author with Most books")
    print("d. return")


def main():
   load_books()
   load_quotes()

   while True:   
    menu()
    choice=input("enter your choice 1-4 :")
    if choice=="1":
      while True:
       book_collection_menu()
       sub_choice=input("enter sub choice a-f :")

       if sub_choice=="a":
          add_unique_book(books)
       elif sub_choice=="b":
          view_books(books)
       elif sub_choice=="c":
          search_books(books)
       elif sub_choice=="d":
          update_books(books)
       elif sub_choice=="e":
          del_books(books)
       elif sub_choice == "f":
          print("return to main choices")
          break
       else:
          print("invalid input") 
          sub_choice=input("enter sub choice a-f")

    elif choice=="2":
      while True:
       quote_collection_menu()
       sub_choice=input("enter sub choice a-e :")

       if sub_choice=="a":
        add_quotes(quotes)
       elif sub_choice=="b":
        view_quotes(quotes)
       elif sub_choice=="c":
        search_quote(quotes)
       elif sub_choice=="d":
        del_quote(quotes)
       elif sub_choice=="e":
        print("return to main choices")
        break
       else:
         print("invalid input") 

    elif choice=="3":
      while True:
        analysis_menu()
        sub_choice=input("enter sub choice a-d :")
        if sub_choice=="a":
          books_compelted_year()
        elif sub_choice=="b":
          count_quotes()
        elif sub_choice=="c":
          most_author_enteries()
        elif sub_choice=="d":
          print("return to main choices")
          break   
    elif choice=="4":
        save_books()
        save_quotes()
        print("exiting-----")
        print("Have a nice day,bye")
        break
    else :
       print("invalid input")
main()
   
