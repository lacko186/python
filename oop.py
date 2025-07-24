class Auto:
    def __init__(self,marka,tipus,uzemanyag,fogyasztas,evjarat,allapot,leiras,ar):
        self.marka = marka
        self.tipus = tipus
        self.uzemanyag = uzemanyag
        self.fogyasztas = float(fogyasztas)
        self.evjarat = int(evjarat)
        self.allapot = allapot
        self.leiras = leiras 
        self.ar = int(ar)
        
car1 = Auto('Volkswagen', "Golf 5", "diesel", 4.8, 2001, "megkimelt", "jó állaőpotban lévő autó", 1100000)
car2 = Auto('Audi', "A4", "benzin", 6.5, 2005, "jó", "szép állapotú autó", 1500000)
car3 = Auto('Honda', "Civic", "benzin", 5.2, 2008, "kitűnő", "kitűnő állapotú autó", 1800000)


print(f'....................Használtautók....................\n\nEladó {car1.marka} {car1.tipus} {car1.evjarat}-es évjáratú {car1.uzemanyag} üzemű autó.\nFogyasztása {car1.fogyasztas} liter/100km, ára {car1.ar} Ft.\nÁllapota: {car1.allapot}, Leírás: {car1.leiras}\n....................')
print(f'\nEladó {car2.marka} {car2.tipus} {car2.evjarat}-es évjáratú {car2.uzemanyag} üzemű autó.\nFogyasztása {car2.fogyasztas} liter/100km, ára {car2.ar} Ft.\nÁllapota: {car2.allapot}, Leírás: {car2.leiras}\n....................')
print(f'\nEladó {car3.marka} {car3.tipus} {car3.evjarat}-es évjáratú {car3.uzemanyag} üzemű autó.\nFogyasztása {car3.fogyasztas} liter/100km, ára {car3.ar} Ft.\nÁllapota: {car3.allapot}, Leírás: {car3.leiras}\n....................')

rendelkezesrealloosszeg = input('Rendelkezésre álló összeg: ')

for car in [car1, car2, car3]:
    if int(rendelkezesrealloosszeg) >= car.ar:
        print(f'\n{car.marka} {car.tipus} autó megvásárolható, ára: {car.ar} Ft.')
    else:
        print(f'\n{car.marka} {car.tipus} autó nem vásárolható meg, ára: {car.ar} Ft.')
