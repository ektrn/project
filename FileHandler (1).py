class FileHandler:

    def __init__(self, path):
        try:
            self.file = open(path, "r")
            self.text = self.file.readlines()
            self.file.close()
            self.numbers = self.get_numbers()
            self.numbers_count = len(self.numbers)
            self.fileExist = True
        except FileNotFoundError:
            self.numbers = []
            self.numbers_count = 0
            self.fileExist = False


    def get_numbers(self):
        numbers = []
        for line in self.text:
            for number in line.split(" "):
                numbers.append(int(number))
        return numbers

    def get_sum(self):
        summary = 0
        for number in self.numbers:
            summary += number
        return summary

    def get_product(self):
        if self.numbers_count == 0:
            return "no numbers"
        if 0 in self.numbers:
            return 0
        product = 1
        for number in self.numbers:
            try:
                product *= number
            except MemoryError:
                print("Memory error!")
                return "error"
        return product

    def get_min(self):
        if self.numbers_count == 0:
            return "no minimum"
        return min(self.numbers)

    def get_max(self):
        if self.numbers_count == 0:
            return "no maximum"
        return max(self.numbers)

    def get_numbers_as_string(self):
        s = ""
        for el in self.numbers:
            s += str(el)
            s += " "
        return s
