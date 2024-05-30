import unittest

def enumerate_sistema(osTest):
    result = []
    for indice, nombre in enumerate(osTest):
        result.append((indice, nombre))
    return result

def enumerate_sistema_name(osTest):
    result = []
    for indice, nombre in enumerate(osTest):
        result.append((indice, nombre))
    return result

def enumerate_sistema_date(osTest):
    result = []
    for indice, nombre in enumerate(osTest):
        result.append((indice, nombre))
    return result

class TestEnumerateFrutas(unittest.TestCase):
    
    def test_positive_name(self):
        names = ["Windows", "Debian"]
        expected_output = [(0, "Windows"), (1, "Debian")]
        self.assertEqual(enumerate_sistema_name(names), expected_output)
        
    def test_positive_date(self):
        names = ["2020", "2015"]
        expected_output = [(0, "2020"), (1, "2015")]
        self.assertEqual(enumerate_sistema_date(names), expected_output)
    
    def test_negative_case(self):
        names = []
        expected_output = []
        self.assertEqual(enumerate_sistema(names), expected_output)

class Os:
    def __init__(self, name, version, date=None):
      self.name = name
      self.version = version
      self.date = date

    def __str__(self):
        if (self.date != None):
            return "{} {} {}\n".format(self.name, self.version, self.date)
        else:
            print("-Warning!-\n-El sistema {} no tiene una fecha especificada, se sugiere etiquetarla correctamente-\n-Warning!-\n".format(self.name))
            return "{} {}".format(self.name, self.version)

    def __repr__(self):
      return ("Os('{}', {})").format(self.name, self.version)
  
    def setDate(self,date):
        self.date = date
        print ("\nEl sistema {} se ha modificado y se etiqueto con la fecha {}\n".format(self.name, self.date))

    def __len__(self):
      return self.date

def main():
    frutas = ["manzana", "banana", "cereza"]
    sistema = Os("Windows", "10")
    sistema.setDate("2020")
    sistema2 = Os("Debian", "9")
    osTest = [sistema, sistema2]
    print(sistema)
    print(sistema2)
    sistema2.setDate("2015")
    for nombre in osTest:
        if (nombre.date != None):
            print("{} {} {}".format(nombre.name, nombre.version, nombre.date))
        else:
            print("{} {}".format(nombre.name, nombre.version))
    
if __name__ == "__main__":
    main()
    unittest.main()