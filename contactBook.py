# To do:
# add, delete, search, edit, list contacts X
# save and load contacts from a JSON file
# gui
import json

class Contact:

    contacts = []

    def __init__(self, firstname, lastname, address, number, email):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.number = number
        self.email = email

    def toDict(self): # convert to dict to pass through json
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "address": self.address,
            "number": self.number,
            "email": self.email,
        }

    def __str__(self):
        return (
            f"Name: {self.firstname} {self.lastname}\n"
            f"Address: {self.address}\n"
            f"Phone Number: {self.number}\n"
            f"Email: {self.email}"
        )

    @classmethod 
    def fromDict(cls, data): # convert dict back to object
        return cls(
            data["firstname"],
            data["lastname"],
            data["address"],
            data["number"],
            data["email"],
        )

    @staticmethod
    def saveContacts():
        # convert to dicts
        contactDicts = []
        for obj in Contact.contacts:
            contactDicts.append(Contact.toDict(obj))

        # save to json
        with open('contacts.json', 'w') as file:
            json.dump(contactDicts, file, indent = 4)
        print('Contact list saved. \n')

    @staticmethod
    def loadContacts():
        # convert to objects
        try:
            with open('contacts.json', 'r') as file:
                contactDicts = json.load(file)

            Contact.contacts = [] # clear list to prevent duplicates

            for contact in contactDicts:
                Contact.contacts.append(Contact.fromDict(contact))
            print('Loaded contact list. \n')

        except FileNotFoundError:
            Contact.contacts = []

    @staticmethod
    def addContact():
        firstname = input('Input first name:\n')
        lastname = input('Input last name:\n')
        address = input('Input address:\n')
        number = input('Input phone number:\n')
        email = input('Input email:\n')
        newContact = Contact(firstname, lastname, address, number, email)
        Contact.contacts.append(newContact)
        print('\n'+firstname, lastname, 'added to contacts.\n')
        Contact.saveContacts()

    @staticmethod
    def getContact():
        firstnameInput = input('Input first name:\n')
        lastnameInput = input('Input last name:\n')
        for item in Contact.contacts:
            if item.firstname == firstnameInput and item.lastname == lastnameInput:
                return item
        
            print('Contact not found.\n')
            return None

    @staticmethod
    def editContact():
        contact = Contact.getContact()

        if contact is None:
            return
        
        edit = True
        while edit == True:
            print('Type a number to edit:\n' 
                    '1. Edit first name\n'
                    '2. Edit last name\n'
                    '3. Edit address\n'
                    '4. Edit phone number\n'
                    '5. Edit email\n'
                    '6. Exit\n')
            editChoice = int(input())
            match editChoice:
                case 1:
                    editValue = input('Enter new first name:\n')
                    contact.firstname = editValue
                    Contact.saveContacts()
                case 2:
                    editValue = input('Enter new last name:\n')
                    contact.lastname = editValue
                    Contact.saveContacts()
                case 3:
                    editValue = input('Enter new address:\n')
                    contact.address = editValue
                    Contact.saveContacts()
                case 4:
                    editValue = input('Enter new phone number:\n')
                    contact.number = editValue
                    Contact.saveContacts()
                case 5:
                    editValue = input('Enter new email:\n') 
                    contact.email = editValue
                    Contact.saveContacts()
                case 6:
                    edit = False
                case default:
                    print('Invalid input.\n')

    @staticmethod
    def deleteContact():
        contact = Contact.getContact()
        if contact != None:
            Contact.contacts.remove(contact)
            Contact.saveContacts()
            print('\n'+contact.firstname, contact.lastname, 'deleted from contacts.\n')
        else:
            print('Contact could not be deleted.\n')

    @staticmethod
    def listContactDetails(contact):
        print(contact)

    @staticmethod
    def menu():
        run = True
        while run == True:
            print('Type a number to navigate: \n'
            '1. Add contact \n'
            '2. Edit contact \n'
            '3. Delete contact \n'
            '4. Contact details \n'
            '5. Exit program \n')

            menuChoice = int(input())
            match menuChoice:
                case 1:
                    Contact.addContact()
                case 2:
                    Contact.editContact()
                case 3:
                    Contact.deleteContact()
                case 4:
                    print('1. List all contact details\n' \
                    '2. List specific contacts details\n')
                    listChoice = int(input())
                    if listChoice == 1:
                        for person in Contact.contacts:
                            print('-----------------------------')
                            Contact.listContactDetails(person)
                        print('-----------------------------')
                    elif listChoice == 2:
                        person = Contact.getContact()
                        if person != None:
                            print('-----------------------------')
                            Contact.listContactDetails(person)
                            print('-----------------------------')
                        else:
                            print('Contact details could not be listed.')
                    else:
                        print('Invalid input.\n')
                case 5:
                    Contact.saveContacts()
                    print('Closing contact book.\n')
                    run = False
                case default:
                    print('Invalid input.\n')

Contact.loadContacts()
Contact.menu()
