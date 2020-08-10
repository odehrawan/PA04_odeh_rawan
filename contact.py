# Class Contact

class Contact:

    # init for Contact(fname, lname)
    def __init__(self, fname, lname):

        #
        # instance attributes
        #

        self.fname = fname
        self.lname = lname
        self.emails = list()
        self.phone_numbers = dict()
        self.labels = list()

        print(f"A new contact for '{self.fname}' has been created.")

    #
    # instance methods
    #

    # override __str__()
    def __str__(self):
        # override __str__
        return f"""
        Contact information for {self.lname.capitalize()}, {self.fname.capitalize()}.
        Contact has {len(self.phone_numbers)} phone numbers and {len(self.labels)} labels.
        """

    # add_phone(phone_number, label)
    def add_phone(self, phone_number, label):

        # check if this is the first number added
        if len(self.phone_numbers) == 0:
            label = "primary"

        # add the phone_number to the contact list of phone numbers
        self.phone_numbers[label.lower()] = phone_number

    # add_label(label)
    def add_label(self, label):
        # append label to the contact list of labels
        self.labels.append(label)

    # add_email(label)
    def add_email(self, email):
        self.emails.append(email)

    # update_name(fname, lname)
    def update_name(self, fname="", lname=""):
        if fname != "":
            self.fname = fname

        if lname != "":
            self.lname = lname

    # check_label()
    def check_label(self, label):
        if label in self.labels:
            return True
        else:
            return False


#     def make_pretty(some_func):
#     def wrap_func(fname, lname):
#       some_func(fname.capitalize(), lname.capitalize())
#     return wrap_func
 
# # Define my decorated functions
# @make_pretty
#     def pretty_name(fname , lname):
#     print(fname, lname)
 
# # Call my decorated functions
# pretty_name("rawan", "odeh")        

    # print emails()
    def print_emails(self):
        for email in self.emails:
            print(f"{self.fname} has email: '{email}'")



