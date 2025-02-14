class Book():
    uid  = 0
    def __init__(self,bname,bauthor,avail):
        self.bname = bname
        self.bauthor = bauthor
        self.avail = avail
        self.id = Book.uid
        Book.uid +=1
    
    def to_list(self):
        return [self.bname,self.bauthor,self.avail]

class library:
    def __init__(self):
        self.book  = {}
    
  
    def add_book(self,book):
        self.book[book.id] = book.to_list()
    
    def remove_book(self,id):
        if id in self.book:
            del self.book[id]
        else:
            print(f"There is no such book as {id}")

    def view_collections(self):
        for uid, details in self.book.items():
            print(f"UID: {uid}, Name: {details[0]}, Author: {details[1]}, Available: {details[2]}")
    
    
class User:

    def __init__(self,name,registerNo):
        self.name = name
        self.registerNo = self.check_registerNo(registerNo)
        self.limit = 3
        self.borrow_list = []
        

    def check_registerNo(self,registerNo):
        if len(registerNo) != 8:
            print("Enter valid Register Number")
            return registerNo
        else:
            print("Welcome to the library " + self.name)
    
    def available_books(self, library):
        for details in library.book.values():
            print(f"Name: {details[0]}, Author: {details[1]}, avail: {details[2]}")
            
    def borrow_book(self,book_name,library):
        def check_limit(borrow_list, uid,nbook):
            if len(borrow_list) < self.limit:
                lis = [uid,nbook[0],nbook[1]]
                borrow_list.append(lis)
                nbook[2] = nbook[2]-1
                print(f"Book '{nbook[0]}' borrowed successfull!!")
            else:
                print("You reached your borrowing limit!")

        for uid,nbook in library.book.items():
            if nbook[2] > 0 and nbook[0] == book_name:
                check_limit(self.borrow_list,uid,nbook)
                break
            else:
                if nbook[2] == 0:
                    print(f"Soory,Not Availabale {nbook[2]}:")

    def return_book(self,library):
        if not self.borrow_list:
            print("You have no books to return!")
            return
        print("Which Book do you wants to return?")
        for i, book in enumerate(self.borrow_list):
            print(f"{i}: {book[1]} by {book[2]}")
        inp = int(input("Select the number to return: "))
        if inp < 0 or inp >= len(self.borrow_list):
            print("Invalid selection.")
            return
        book_data = self.borrow_list.pop(inp) 
        book_uid = book_data[0]  

        for uid,_ in library.book.items():
            if book_uid == uid:
                library.book[book_uid][2]+=1
                print(f"Book '{library.book[book_uid][0]}' returned successfully!")
            else:
                print("Error: Book UID not found in library.")
                


        


b1  = Book("hii","hello",1)
b2 = Book("Hello","hi",7)

lib = library()
lib.add_book(b1)
lib.add_book(b2)


u1 = User("Vignesh","21ALL065")
print("before")
u1.available_books(lib)
u1.borrow_book("Hello",lib)

print("after")
u1.available_books(lib)
u1.borrow_book("hii",lib)

User.return_book(u1,lib)

print("after")

lib.view_collections()
u1.available_books(lib)