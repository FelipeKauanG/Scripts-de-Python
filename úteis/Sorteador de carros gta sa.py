from random import sample
tipos = ['Sports Cars', 'SUVs & Pickup', 'Lowriders', 'Tuners', 'Vans', 'Industrial', 'Coupes & Hatchbacks', 'Sedans & Station Wagons', 'Public Service', 'Novelty', 'Government']

carros = [['Alpha', 'Banshee', 'Buffalo', 'Bullet', 'Cheetah', 'Comet', 'Euros', 'Hotknife', 'Infernus', 'Phoenix', 'Super', 'GT', 'Turismo', 'Windsor', 'ZR-350'], #Sports Cars
          ['Bobcat', 'Huntley', 'Landstalker', 'Mesa', 'Monster', 'Patriot', 'Picador', 'Rancher', 'Sadler', 'Sandking', 'Walton', 'Yosemite'] #SUVs & Pickup
    , ['Blade', 'Broadway', 'Remington', 'Savanna', 'Slamvan', 'Tahoma', 'Tornado', 'Voodoo'], #Lowriders
          ['Elegy', 'Flash', 'Jester', 'Stratum', 'Sultan', 'Uranus'], #Tunners
          ["Berkley's", 'RC', 'Van', 'Burrito', 'Hotdog', 'Moonbeam', 'Mr', 'Whoopee', 'Newsvan', 'Pony', 'Rumpo', 'Securica'], #Vans
          ['DFT-30', 'Dozer', 'Dumper', 'Flatbed', 'Forklift', 'Linerunner', 'Mule', 'Packer', 'Roadtrain', 'Tanker', 'Tractor', 'Yankee'], #Industrial
          ['Blista', 'Compact', 'Bravura', 'Buccaneer', 'Cadrona', 'Clover', 'Club', 'Esperanto', 'Feltzer', 'Fortune', 'Hermes', 'Hustler', 'Majestic', 'Manana', 'Previon', 'Sabre', 'Stallion', 'Tampa', 'Virgo'], #Coupes & Hatchbacks
          ['Admiral', 'Elegant', 'Emperor', 'Glendale', 'Greenwood', 'Intruder', 'Merit', 'Nebula', 'Oceanic', 'Perennial', 'Premier', 'Primo', 'Regina', 'Romero', 'Sentinel', 'Solair', 'Stafford', 'Stretch', 'Sunrise', 'Vincent', 'Washington', 'Willard'], #Sedans & Station Wagons
          ['Baggage', 'Bus', 'Cabbie', 'Coach', 'Sweeper', 'Taxi', 'Tow', 'Truck', 'Trashmaster', 'Tug', 'Utility', 'Van'], #Public Service
          ['Bandito', 'BF', 'Injection', 'Caddy', 'Camper', 'Dune', 'Journey', 'Kart', 'Mothership', 'Mower', 'Quad', 'Vortex'], #Novelty
          ['Ambulance', 'Barracks', 'Enforcer', 'FBI', 'Rancher', 'FBI', 'Truck', 'Fire', 'Truck', 'HPV-1000', 'Police', 'Ranger', 'Rhino', 'S.W.A.T.']] #Government

while True:
    for i in range(1, 12):
        print(f"\033[0;36m{i}\033[m para escolher \033[0;36m{tipos[i-1]}\033[m")

    per = int(input("Escolheu qual ?"))-1

    print(f"\nEscolheu a categoria \033[0;36m{tipos[per]}\033[m")
    print(f"\n{sample(carros[per],k=1)} Vs {sample(carros[per], k=1)}".replace("[", "").replace("]", "").replace("'", ""))
