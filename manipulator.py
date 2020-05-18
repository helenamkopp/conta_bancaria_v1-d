class TaxableHandler:

    def calculate_tax(self, list_taxables):
        total = 0
        for t in list_taxables:
            total += t.get_tax_amount()

        return total
