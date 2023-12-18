class Customer:
    def __init__(self, name, country, passport, gender, from_date, to_date):
        self.name = name
        self.country = country
        self.passport = passport
        self.gender = gender
        self.from_date = from_date
        self.to_date = to_date

    def __str__(self):
        return f"Customer Name: {self.name}\nCountry: {self.country}\nPassport: {self.passport}\nGender: {self.gender}\nFrom: {self.from_date}\nTo: {self.to_date}"