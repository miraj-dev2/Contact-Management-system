
'''Simple Contact Book
Store, search, and delete contacts using a dictionary.'''
import json
contact_1={"name":"Miraj",
           "phone":"01989322549",
           "email":"mirazkhan012007@gmail.com"
           }

contact_2={"name":"Rafi",
           "phone":"01989345549",
           "email":"rafikhan012007@gmail.com"
           }
contact_3={"name":"Minhaj",
           "phone":"01983422549",
           "email":"minhajkhan012007@gmail.com"
           }
contact_4={"name":"Jhon",
           "phone":"01946322549",
           "email":"jhon@gmail.com"
           }
contact=[contact_1,contact_2,contact_3,contact_4]   #Store 4 dictionary in a list
def show_all(contact):  
    for i in contact:
        print(f"name: {i['name']}")
        print(f"phone: {i['phone']}")
        print(f"email: {i['email']}")
        print(".............................")
#for adding new contact
def add_contact():
    new_contact={}
    name=input("Enter your name:")
    phone=input("Enter your contact number:")
    email=input("Enter your email: ")
    for person in contact:
        if person["name"].lower()==name.lower():
    
            print("Contact already exist")
            break
    else:
        new_contact.update({"name":name,"phone":phone,"email":email})
        contact.append(new_contact)
        print("Contact added")
def search_contact():
    name=input("Enter the name you want to search:")
    for person in contact:
        if person["name"].lower()==name.lower():
            print(f"name: {person['name']}")
            print(f"phone: {person['phone']}")
            print(f"email: {person['email']}")
            print("......Contact found......")
            break
    else:
        print("......Name not found........")
def delete_contact():
    dele=input("Enter the name you wanted to delete: ")
    for person in contact:
        if person["name"].lower()==dele.lower():
            contact.remove(person)
            print("Contact deleted")
            break
    else:
        print("Contact not found")
def save_contact(contact,filename):
    data=json.dumps(contact)
    with open(filename, "w") as file:
        file.write(data)
def load_contacts(filename):
    
    with open (filename,"r") as file:
        data=file.read()
    contact=json.loads(data)
    return contact
                             
def main():
    global contact
    contact=load_contacts("contacts.json")
    
    while True:
        print("....Contact Managemenent System....") 
        
        show = ["1. Show contacts", "2. Add contact", "3. Search contact", "4. Delete contact", "5. Exit"]
        
        for i in show:
            print(i)
        choice=int(input("Enter Your choice(1-5):"))
        if choice==1:
            show_all(contact)
            save_contact(contact,"contacts.json")
        elif choice==2:
            add_contact()
            save_contact(contact,"contacts.json")
        elif choice==3:
            search_contact()

        elif choice==4:
            delete_contact()
            save_contact(contact,"contacts.json")
        elif choice==5:
            print("Exiting.Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
main()
