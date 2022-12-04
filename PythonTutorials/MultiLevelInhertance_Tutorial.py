class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    def isdance(self):
        return f'Yes, i dance {self.dance} time(s)'

class Grandson(Son):
    dance=6
    def isdance(self):
        return f'Yes, i dance very well, {self.dance} no. of times '

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.isdance())
print(harry.basketball)

