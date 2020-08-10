from contact import Contact
from contact_book import ContactBook

# create contact for Cookie Monster
cookie = Contact("Cookie", "Monster")

# call add_phone() on cookie
cookie.add_phone("12345678", "work")
cookie.add_phone("00123456", "Cookie Line")
cookie.add_label("Cookie")
cookie.add_label("Friend")

# call update_name() on cookie
# cookie.update_name(lname="Monster Too")
# cookie.update_name(fname="Yummy Cookie")
# cookie.update_name(fname="Yummy Cookie", lname="Monster Too")
# print(cookie)

# create contact for Don Music
don = Contact("Don", "Music")

# call add_label on don
don.add_label("Music")
don.add_label("Friend")

# call add_phone on don
don.add_phone("12345678", "work")
print(don)

# create contact for Roosevelt Franklin
roosevelt = Contact("Roosevelt", "Franklin")

# call add_email() on roosevelt
roosevelt.add_email("roosevelt@sesame.com")
roosevelt.add_email("frankie@sesame.com")

# call print_emails()
roosevelt.print_emails()

# create a contact book
sesame_street = ContactBook()

# add contacts to contact book
sesame_street.add(cookie)
sesame_street.add(don)
sesame_street.add(roosevelt)

# print the number of contacts in contact book
print(len(sesame_street.contacts))

# print all contacts
sesame_street.print_all_contacts()

# print book
sesame_street.print_book()

# call search_by_label()
sesame_street.search_by_label("Friend")
sesame_street.search_by_label("Music")

# call delete_contact()
sesame_street.delete_contact(roosevelt)
sesame_street.delete_contact(roosevelt)

# using decorator  
fullname=sesame_street.pretty_name
print(fullname(roosevelt))

# call save_info method 
sesame_street.save_file()

# call method read_file to read contact information and print total loaded contacts
sesame_street.read_data()
sesame_street.load_data()

# export file by user choose and print file info and error hundling if user enter invalid file
sesame_street.export_file()
# create object check if contatt include or not 
# smesm=Contact("jeorge","khorye")
# sesame_street.handling_error(smesm)
# sesame_street.handling_error(don) 

# call method to add file from terminal
sesame_street.add_contact_info()
sesame_street
sesame_street.save_file()
sesame_street.add_contact_info()
sesame_street.save_file()

sesame_street.add(smesm)
smesm.add_email("sesime_street@pixcer.com")
smesm.add_phone("gamer","23456")
# call method to delete contact from terminal
sesame_street.del_contact_info()

# call method generate_report()
sesame_street.generate_report()

