from main import CheckingAccount, LifeInsurance, TaxableMixIn, Client
from manipulator import TaxableHandler

if __name__ == "__main__":
    client_1 = Client("José", "Silva", "555.444.777-95")
    client_2 = Client("Mariana", "Golcanvez", "111.211.333-14")
    client_3 = Client("Paulo", "Pereira", "333.999.888-74")
    client_4 = Client("Joaquina", "Santos", "333.444.111-95")

    ca_1 = CheckingAccount("123-4", client_1, 1000.0)
    ca_2 = CheckingAccount("124-8", client_2, 1000.0)
    insurance_1 = LifeInsurance(100.0, "Paulo", "354-77")
    insurance_2 = LifeInsurance(200.0, "Joaquina", "237-98")

    list_taxables = [ca_1, ca_2, insurance_1, insurance_2]

    handler = TaxableHandler()
    total = handler.calculate_tax(list_taxables)

    print(total)
