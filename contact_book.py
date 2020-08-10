from contact import Contact

# class ContactBook


class ContactBook:

    # init for ContactBook()

    def __init__(self):

        #
        # instance attributes
        #

        self.contacts = list()

    #
    # instance methods
    #

    # add(contact)
    def add(self, contact):
        self.contacts.append(contact)

    # get_contact(contact, keyword)
    def get_contact(self, contact, keyword):
        if contact.fname.lower() or contact.lname.lower() or contact.email.lower() == keyword.lower():
            return contact
        else:
            return None

    # delete_contact(contact)
    def delete_contact(self, contact):
        if contact in self.contacts:
            print("Removing contact...")
            self.contacts.remove(contact)
        else:
            print("Contact does not exist.")

    # search(keyword)
    def search(self, keyword=""):

        # declare a local variable 'results'
        results = list()

        # loop over every contact in self.contacts
        for contact in self.contacts:

            # call get_contact(contact, keyword)
            contact = self.get_contact(contact, keyword)

            # check if contact exists
            if contact != None:
                # append to list of results
                results.append(contact)

            # check if we found any matches
            if len(results) > 0:
                print(
                    f"Found {len(results)} results matching the keyword '{keyword}'.")
                for contact in results:
                    print(contact)
            else:
                print(f"No results found matching the keyword: '{keyword}'.")

    def search_by_label(self, label):
        print(f"Searching for '{label}'")

        # declare a local variable 'results'
        results = list()

        # loop over every contact in self.contacts
        for contact in self.contacts:
            if contact.check_label(label):
                results.append(contact)

        # check if we found any matches
        if len(results) > 0:
            print(
                f"Found {len(results)} contacts with the label: '{label}'.")
            for contact in results:
                print(contact)
        else:
            print(f"No results found matching the keyword: '{label}'.")

    # print_all_contacts()
    def print_all_contacts(self):
        # print all contacts in contact book
        for contact in self.contacts:
            print(contact)

    # print_book()
    def print_book(self):

        print(f"Printing the book...\n")

        total_number_of_contacts = len(self.contacts)
        contacts_without_phone = 0
        contacts_without_email = 0

        for contact in self.contacts:
            if len(contact.phone_numbers) == 0:
                contacts_without_phone += 1

            if len(contact.emails) == 0:
                contacts_without_email += 1

        print(f"The contact book has {total_number_of_contacts} contacts.")
        print(f"{contacts_without_phone} contacts without a phone number.")
        print(f"{contacts_without_email} contacts without an email address.\n")

        # return contacts_without_phone, contacts_without_email
    def search_by_label(self,label):
        results = list()
        print(f" Searching for {label}")
        for contact in self.contacts:
            # check contact not equals none
            
            if contact.check_label(label):
                # appeand list of results
                results.append(contact)

        if len(results)!=0:
            for contact in results:
                print(contact)
        else:
            print("Not Found")        

    
    def print_book(self):
        print(f"All contacts {len(self.contacts)}")
        count_without_phone=0
        count_without_email=0
        for contact in self.contacts:
          if len(contact.phone_numbers)==0:
              count_without_phone+=1

          if len(contact.emails)==0:
                count_without_email+=1        
        print(f"Total contacts without phone numers {count_without_phone} \n total contacts without emails {count_without_email}")
        
    def pretty_name(self,contact):
        return f"Fullname contact is {contact.fname.capitalize()} {contact.lname.capitalize()}"

    # save information about all contacts
    def save_file(self):
        file_save=open("text_file.csv","w")
        contact_number=1
        for contact in self.contacts:
            file_save.writelines(f"Contact number {contact_number} is  {contact}")
            contact_number+=1
        print(f"Successful Saving {contact}")
        file_save.close()

    # read contact information from all_data_saving.csv
    def read_data(self):
        contact_number=1
        print("Reading Data ....")
        print(f"Contacts info :") 
        read_file=open("text_file.csv","r")
        for line_file in read_file:
            print(f"{line_file}",end="" )
            contact_number+=1
        read_file.close()

    def load_data(self):
        read_file=open("text_file.csv","r")
        count_load=len(self.contacts)
        print(f"Total count of loaded contacts as posible {count_load}")
        read_file.close()

    def export_file(self):
        filename=input("Please enter file namen and source of file")
        if  not '.' in filename:
            print("Oops ! invalid file please again....")
        else:
            read_data=open("text.file.csv","r")
            export_info=open(filename,"w")
            for file in read_data:
                export_info.writelines(file)   
            print("Exporting Successful...")

     

    def add_contact_info(self):
        contact=input("Enter Contact:")
        self.contacts.append(contact)
        file_ter=open("all_data_saving.csv","a+")
        for contact in file_ter:
            file_ter.writelines(contact)
        print(f"Successful adding {contact}")  
        file_ter.close()
        self.read_data()

    def del_contact_info(self):
        contact=input("Input contact that need to remove")
        if contact in self.contacts:
                print("Successful removing Contact...")
                self.contacts.remove(contact)
        else:
             print("contact not exist.")

    def generate_report(self):
        print("Statistics about contacts info:")
        #print(f"Total contacts {len(self.contacts)}")
        count_without_phone=0
        count_without_email=0
        count_contact_email=0
        count_contact_phone=0
        try:
            for contact in self.contacts:
                if len(contact.phone_numbers)==0 and len(contact.emails)==0:
                    count_without_phone+=1
                    count_without_email+=1

                if len(contact.phone_numbers)==0:
                    count_without_phone+=1  

                if len(contact.emails)==0:
                    count_without_email+=1

                if len(contact.phone_numbers)>0:
                    count_contact_phone+=1  

                if len(contact.emails)>0:
                    count_contact_email+=1

            #print(f"Total contacts without phone numers {count_without_phone} \n total contacts without emails {count_without_email}")
                print(f"Total contacts are {len(self.contacts)}\n and the total contacts without email is {count_without_email} and \n  contacts without phone numbers are {count_without_phone} and \n total contact numbers without emails and phone numbers are {count_without_phone+count_without_email} and \n total count contacts with email {count_contact_email} and \n totla count contacts with phone numbers {count_contact_phone}")
        except:
            pass
