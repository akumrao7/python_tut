class Contact:
    phone_direcotery=[]


    def __init__(self, name, phone_number):
        self.name = name
        self.phone = phone_number
        Contact.phone_direcotery.append(self)

    def show_contact(self):
        return f"Name: {self.name}, Contact Number: {self.phone}"

    @classmethod
    def show_all_contacts(cls):
        if len(cls.phone_direcotery) == 0:
            print("No contact in the phone book!")
        else:
            for contact in cls.phone_direcotery:
                print(contact.show_contact())

    @classmethod
    def seach_contact(cls, search_name):
        for contact in cls.phone_direcotery:
            if contact.name.lower==search_name.lower:
                return contact.phone

        return f"No contact found for {search_name}"

    @staticmethod
    def validate_phone_number(number):
        if len(number) >=8 and number.isdigit():
            return True
        else:
            return False

n_contact=int(input("How many contacts do you want to add?: "))

for i in range(n_contact):
    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    if Contact.validate_phone_number(phone_number):
        Contact(name, phone_number)
    else:
        print(f"Invalid phone number for {name}")

# c1=Contact("Ram", 62894981462890)
# c2=Contact("Arav", 628949813762890)
# c3=Contact("Sam", 628998472456)
#
# # print(c1.show_contact())
# # print(c2.show_contact())
Contact.show_all_contacts()
# print(Contact.seach_contact("ram"))
# print(Contact.seach_contact("Anaya"))