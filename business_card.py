from faker import Faker

fake = Faker()


class BaseContact:
    def __init__(self, name, surname, phone, mail):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.mail = mail

    def __str__(self):
        return f"{self.name} {self.surname} {self.phone} {self.mail}"

    def contact(self, phone):
        return f"Choose {phone} and contact with {self.name} {self.surname}"

    @property
    def label_length(self):
        return len(self.name) + len(self.surname)


class BusinessCard(BaseContact):
    def __init__(self, name, surname, phone, mail, company, position, company_phone, *args, **kwargs):
        super().__init__(name, surname, phone, mail)
        self.company = company
        self.position = position
        self.company_phone = company_phone

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info} {self.company} {self.position} {self.company_phone}"


def get_name(card):
    return card.name


def create_list_of_business_card():
    list_business_card = []

    for i in range(5):
        business_card = BusinessCard(fake.first_name(), fake.last_name(), fake.phone_number(), fake.email(),
                                     fake.company(), fake.job(),
                                     fake.phone_number())
        list_business_card.append(business_card)

    for card in list_business_card:
        print(card)
    print("--------------------")

    by_name = sorted(list_business_card, key=get_name)

    for business_card_by_name in by_name:
        print(f"{business_card_by_name}")
    print("----------------------")

    by_surname = sorted(list_business_card, key=lambda card_element: card_element.surname)

    for business_card_by_surname in by_surname:
        print(business_card_by_surname)
    print("-------------------------")

    by_mail = sorted(list_business_card, key=lambda card_element: card_element.mail)

    for business_card_by_mail in by_mail:
        print(business_card_by_mail)
    print("--------------------")

    return list_business_card

@BusinessCard.label_length.setter
def displaying_contact():
    base_contact = BaseContact(fake.first_name(), fake.last_name(),
                               f"{fake.country_calling_code()} {fake.phone_number()}", fake.email())

    print(base_contact)

    business_card = BusinessCard(fake.first_name(), fake.last_name(), fake.phone_number(), fake.email(), fake.company(),
                                 fake.job(),
                                 fake.phone_number())
    print(business_card)
    print("-------------------------------------------")

    print(base_contact.contact(base_contact.phone))
    print(f"Length is {base_contact.label_length}")

    print(business_card.contact(business_card.company_phone))
    print(f"Length is {business_card.label_length}")


def create_contacts(counter_of_cards, type_of_card):
    list_of_base_contact = []
    list_of_business_card = []

    if type_of_card == "base":
        for i in range(counter_of_cards):
            base_contact = BaseContact(fake.first_name(), fake.last_name(),
                                       f"{fake.country_calling_code()} {fake.phone_number()}", fake.email())
            list_of_base_contact.append(base_contact)
        for card in list_of_base_contact:
            print(card)

    elif type_of_card == "business":
        for i in range(counter_of_cards):
            business_card = BusinessCard(fake.first_name(), fake.last_name(), fake.company(), fake.job(),
                                         fake.phone_number(), fake.email(), fake.phone_number())
            list_of_business_card.append(business_card)
        for card in list_of_business_card:
            print(card)

    else:
        print("Wrong option")


create_list_of_business_card()
displaying_contact()

print("-----------------------------------")
counter = input("Input number of card ")
correct_counter = int(counter)
card_type = input("Input type of card ")

create_contacts(correct_counter, card_type)
