import os
import time

print("\n")
#
print("Dit is de eerste beroepsopdracht die ik op het Mediacollege Amsterdam bij de opleiding Software development gekregen heb.")
print("Het is een verhaal over een nieuwkomer in Nederland.")
print("Dit is gebaseerd op allerlei verhalen die ik gelezen en gehoord heb. ")
print("Hiervan heb ik een tekstbased applicatie in Python gemaakt om het verhaal ook door anderen te laten beleven. ")
print("Door verschillende keuzes in het verhaal te maken zullen er verschillende verhaallijnen komen die ook een andere einde zullen hebben.")
input()
os.system("cls")
print("\n")
#
print("Welkom bij mijn game!")
print("De game die je nu gaat spelen heet *Siham op de vlucht*")
input()
print("\n")
#
print("""Uitleg: Je krijgt straks tekst te zien die je moet lezen. Aan het eind van het stukje tekst krijg je een keuze. Bij die keuze kies je A of B. 
als er geen A of B staat klik je op enter na het lezen van de tekst. 
Door de keuze die je maakt verandert het volgende stukje tekst en het einde veranderd. Er zijn 4 verschillende eindes.""")
input()
os.system("cls")
#
print("INTRO")
print("\n")
print("Dit verhaal begint in Damascus, Syrië 2011. Dit verhaal gaat over een vluchteling genaamd Siham.")
print("Siham is 17 jaar en studeert geneeskunde.")
print("Siham heeft een broertje Aziz. Hij is 12 jaar.")
print("Ze heeft ook een vriendje die kort geleden een huwelijksaanzoek deed en nu haar verloofde is.")
print("In 2011 begint de oorlog in Syrië.")
input()
os.system("cls")
print("\n")
#
def stukje_1():
    while True:
        print("Het is een mooie maandag ochtend. Je wordt wakker om 07:00 omdat je naar school toe moet.")
        print("Je zet je alarm uit en stapt uit bed. Het is allemaal nog een beetje wazig voor je, maar het lukt je om je kleren aan te trekken.")
        print("Je wilt je telefoon pakken maar je ziet dat het niet op je nachtkastje zit.")
        print("Je kijkt om je heen en ziet je telefoon naast je laptop op je bureau.")
        print("Het schiet je te binnen dat je gister laat op was om nog te studeren voor de toets die je vandaag hebt.")
        print("Je herinnert je dat je in slaap viel op je bureau maar je herinnert je niet hoe je in je bed kwam.")
        print("Het maakt je ook niet uit. Je haast je naar beneden om te ontbijten.")
        print("Je eet snel een broodje en pakt je tas om te vertrekken naar school.")
        print("Eerder was aangekondigd dat als het luchtalarm afgaat het leger van de president de protesterende mensen dood gaat maken en dat het een mogelijk begin van een oorlog kan zijn.")
        print("Je weet dat dit geen goed teken is.")
        print("\n")
        print("""Wat ga je doen? ...
        a. Naar je familie toe om te vluchten. 
        b. Naar je verloofde Mohamed toe om te vluchten.""") #a --> stukje 2 b --> stukje 3#
        antwoord = input(">>>")
        if antwoord == "a":
            os.system("cls")
            time.sleep(1)
            stukje_2()
            break
        elif antwoord == "b":
            os.system("cls")
            time.sleep(1)
            stukje_3()
            break
        else:
            print("Dat is geen geldig antwoord. Antwoord met a of b")
            time.sleep(2)
            os.system("cls")
#
def stukje_2():
    while True:
        print("Je rent zo snel als je kan naar je familie toe.")
        print("Onderweg zie je allemaal mensen die ook hun huis uitvluchten.")
        print("Eenmaal thuis aangenomen zie je dat je moeder helemaal in paniek is.")
        print("Terwijl je moeder geld bij elkaar pakt probeert Aziz met de huistelefoon je vader te bereiken die op werk is.")
        print("Je vader neemt op en zegt dat hij bijna thuis is.")
        print("Siham gaat naar haar kamer om haar spullen in te pakken, maar ze hoort haar vader binnenkomen dus ze rent naar beneden.")
        print("Haar vader probeert eerst Sihams moeder kalm te maken die helemaal in paniek is.")
        print("Na dat ze kalm is legt sihams vader uit dat het voor nu het beste is dat hij alleen het land uit vlucht,")
        print("en dat hij later de rest mee zal nemen omdat ze het geld er nu niet voor hebben.")
        print("Sihams vader heeft een 2de huis die goed verborgen zit voor noodgevallen zoals deze.") 
        print("Er is daar genoeg eten voor 2 jaar en het heeft toegang tot schoon water.")
        print("Het is dus beter als de familie daar gaat wonen voor een tijdje. Sihams vader neemt al het geld mee en de auto en vertrekt.")
        print("De familie maakt zich klaar om te verhuizen en vertrekken daarna naar het 2de huis. Het huis is niet ver dus ze kunnen er lopend heen.")
        print("Eenmaal aangekomen pakken ze hun spullen uit. Siham is erg bezorgd om haar verloofde en zit erover na te denken om te kijken of het goed met hem gaat. ")
        print("\n")
        print("""Gaat siham ...
        a. Naar haar verloofde toe.
        b. Niet naar haar verloofde toe.""") #a --> stukje 4 b --> stukje 5#
        antwoord = input(">>>")
        if antwoord == "a":
            os.system("cls")
            time.sleep(1)
            stukje_4()
            break
        elif antwoord == "b":
            os.system("cls")
            time.sleep(1)
            stukje_5()
            break
        else:
            print("Dat is geen geldig antwoord. Antwoord met a of b")
            time.sleep(2)
            os.system("cls")
#
def stukje_3():
    while True:
        print("Siham rent zo hard als ze kan naar het huis van Mohamed en ziet de familie van Mohamed in paniek.") 
        print("Mohamed ziet siham naar haar toe rennen en rent ook naar siham toe.")
        print("Ze omhelzen elkaar. De familie van Mohamed pakt al hun benodigdheden in om te vluchten.")
        print("De moeder van Mohamed zegt tegen siham dat haar moeder had gebeld om te zeggen dat ze samen het land uit moeten vluchten.") 
        print("Sihams familie pakt ook al hun spullen nu in. Als Mohameds familie klaar is met inpakken rijden ze naar sihams familie.")
        print("15 minuten later zijn ze klaar en gaan ze met de auto richting sihams familie. Eenmaal aangekomen rent siham naar binnen en omhelst haar familie.") 
        print("Siham rent naar boven, leegt haar schooltas en vult die met benodigdheden. Nadat ze alles heeft ingepakt rent ze naar beneden. Iedereen is klaar voor vertrek.") 
        print("Iedereen loopt naar buiten en ziet dat ze moeilijk met ze allen in 1 auto gaan passen.")
        print("Mohameds vader stelt voor om met 1 auto te gaan maar sihams vader stelt voor om met 2 auto's te gaan. ")
        print("\n")
        print(""""Gaan ze met ...
        a. 1 auto.
        b. 2 auto's.""") #a --> stukje 17 b --> stukje 18#
        antwoord = input(">>>")
        if antwoord == "a":
            os.system("cls")
            time.sleep(1)
            stukje_17()
            break
        elif antwoord == "b":
            os.system("cls")
            time.sleep(1)
            stukje_18()
            break
        else:
            print("Dat is geen geldig antwoord. Antwoord met a of b")
            time.sleep(2)
            os.system("cls")
#
def stukje_4():
    print("Siham rent zo hard als ze kan naar het huis van haar verloofde.")
    print("Ze komt heel erg moe aan. Ze klopt op de deur maar niemand doet open.")
    print("Ze klopt nog harder, nog steeds niks. Ze kijkt door het raam en ziet dat er niemand is.")
    print("Alle spullen zijn er ook niet. Ze weet zeker dat ze al gevlucht zijn.")
    print("Ze loopt terug naar haar eigen huis maar wordt door iemand van het leger gezien die denkt dat ze protesteert omdat ze geen hoofddoek op heeft.")
    print("Siham probeert uit te leggen dat haar hoofddoek vast gevallen moet zijn toen ze naar het huis van haar verloofde rende.")
    print("De militair gelooft haar niet en schiet met zijn pistool 3 keer in sihams buik. ")
    print("\n")
    input()
    time.sleep(1)
    os.system("cls")
    stukje_6()
#
def stukje_5():
    while True:
        print("Sihams moeder probeert haar uit te leggen dat dat niet kan omdat ze dan het huis moet verlaten en dat dat hun leven in risico kan brengen.")
        print("Haar moeder zegt dat ze hem beter kan bellen met de telefoon. Siham weet het nummer uit haar hoofd en belt maar niemand neemt op.")
        print("Ze belt nog een keer en weer neemt niemand op. Siham denkt dat ze al vertrokken zijn maar ze is nog steeds heel bezorgd.")
        print("Sihams baas belt. Siham werkte als verkoopmedewerkster in een groot bedrijf.")
        print("Haar baas vertelt siham dat er een mogelijkheid is om via een laptop te werken en dat hij dat ook doet. Hij zegt dat hij nu in Amerika zit.")
        print("Hij stuur siham een email met hoe het allemaal moet.")
        print("Siham is blij dat er nog een beetje geld verdient kan worden want haar vader is weg en haar moeder heeft geen baan meer.")
        print("\n")
        print(""""De tijd wordt versneld met ...
        a. 1 jaar
        b. 2 jaar""") #a --> stukje 7 b --> stukje 8#
        antwoord = input(">>>")
        if antwoord == "a":
            os.system("cls")
            time.sleep(1)
            stukje_7()
            break
        elif antwoord == "b":
            os.system("cls")
            time.sleep(1)
            stukje_8()
            break
        else:
            print("Dat is geen geldig antwoord. Antwoord met a of b")
            time.sleep(2)
            os.system("cls")
#
def stukje_6():
    print("Siham probeert naar huis te kruipen maar door haar ernstige wonden lukt dat bijna niet. Siham ziet mensen weg rennen en ziet dat niemand haar wil helpen.") 
    print("Ze hadden haar wel ziet liggen. Siham ziet dat ze te veel bloed verliest. Ze sterf uit eindelijk midden op straat.")
    print("\n")
    print("Je bent dood gegaan.")
    print("Bedankt voor het spelen.")
    time.sleep(4)
    exit
#
def stukje_7():
    while True:
        print("Het is een jaar later. Er is een grote oorlog in Syrië. Sihams familie zit nog steeds veilig in hun 2de huis.")
        print("Door sihams baan is er genoeg geld om uit het land te vluchten. Siham bespreekt dit met haar moeder.")
        print("Haar moeder denkt dat haar vader het niet heeft gehaald en vind ook dat ze het land uit moeten vluchten.")
        print("De familie pakt hun spullen in. Ze gaan naar buiten en pakken de oude verroestte fietsen die voor de deur liggen.") 
        print("Ze beginnen zo hard als ze kunnen te fietsen naar de grens van Syrië en libanon. Na lang gefietst te hebben komen ze aan bij de grens.") 
        print("De grens is erg druk. Siham ziet dat een man naar hun toe komt. De man vraagt: jullie willen zeker het land uit vluchten.") 
        print("Ik smokkel jullie naar Turkije voor 3000 euro. Sihams moeder vraagt aan de man: is dat voor ons drieën.") 
        print("De man antwoord: ja. Sihams moeder vraagt aan siham wat ze wil doen aangezien ze maar 3500 euro hebben")
        print("\n")
        print(""""Hoe gaat de familie het land uit vluchten? ...
        a. mensensmokkelaar
        b. zonder mensensmokkelaar""") #a --> stukje 9 b --> stukje 10#
        antwoord = input(">>>")
        if antwoord == "a":
            os.system("cls")
            time.sleep(1)
            stukje_9()
            break
        elif antwoord == "b":
            os.system("cls")
            time.sleep(1)
            stukje_10()
            break
        else:
            print("Dat is geen geldig antwoord. Antwoord met a of b")
            time.sleep(2)
            os.system("cls")
#
def stukje_8():
    while True:
        print("Het is 2 jaar later. Het eten raakt langzaam op. Sihams familie zit voor nu nog veilig maar wie weet voor hoe lang nog.")
        print("Siham denk dat haar vader het niet heeft gehaald. Ze vindt dat ze zelf nu moeten vluchten.")
        print("Siham gaat naar haar moeder toe om het te bespreken. Haar moeder denkt er net zo over als siham.") 
        print("Door sihams baan hebben ze genoeg geld om te vluchten. Iedereen pakt hun spullen in om de volgende dag te vertrekken.")
        print("Ze weten dat het een zware reis gaat worden dus ze pakken alleen dingen in die echt nodig zijn zoals het resterende eten, geld en kleding.")
        print("Nadat iedereen heeft ingepakt besluiten ze te slapen. ")
        print("\n")
        print("Na het slapen.")
        print("\n")
        print("Siham wordt wakker en ziet dat het 07:30 is. Ze maakt haar moeder en broertje wakker.") 
        print("Nadat iedereen wakker is pakken ze hun spullen en verlaten ze het huis.")
        print("Ze hebben voor de deur oude fietsen liggen die erg versleten zijn maar nog wel te berijden dus ze pakken die en fietsen.")
        print("Via de kaart zien ze dat het 40 km is van Damascus naar de dichtbij zijnde stad in libanon. Ze beginnen te fietsen")
        print("\n")
        print("Halve dag later.")
        print("\n")
        print("Sihams familie komt aan bij de grens van Syrië en libanon. Nu moeten ze verder te voet dus ze leggen de fietsen neer en lopen.")
        print("De grens is heel erg druk met mensen die ook het land uit willen vluchten. Ze sluiten zich aan bij de rij en wachten. Na lang gewacht te hebben zij ze nu in libanon.") 
        print("Na de grens is er een auto die vluchtelingen vervoert naar Beiroet. De reis duurt 2 uur en kost 150.000 Libanese pond per persoon dat is omgerekend 100 euro per persoon.")
        print("Siham heeft omgerekend 4000 euro. Siham moeder zegt dat ze het moeten nemen en siham is het er mee eens. Siham gaat naar de man bij de auto en betaalt.") 
        print("De familie zit nu met meer dan 20 mensen in een 11 persoons auto. De auto vertrekt. Na 2.5 uur zijn ze aangekomen in Beiroet.")
        print("De auto was oud en niet veilig waardoor de reis langer duurde. Iedereen stapt uit en begint te rennen naar de kust van Beiroet.")
        print("Siham hoorde in de auto dat er daar mensen zijn die je over zee varen naar Turkije. De familie aarzelt niet en begint ook naar de kust te rennen.") 
        print("Eenmaal aangekomen zien ze 3 bootjes vertrekken. Ze rennen naar de man toe die plaatsen verkoopt voor het bootje. Siham vraagt aan de man hoeveel het kost.") 
        print("De man antwoord: 200 euro per persoon voor het slome bootje en 500 euro voor het snelle bootje.")
        print("Het slome bootje brengt je in 10 dagen naar Turkije en de snelle in 4. Sihams moeder hoorde het gesprek en vraagt aan siham welk bootje nemen we.") 
        print("We hebben nog 3700 euro over.")
        print("\n")
        print(""""Welk bootje neem je? ...
        a. Het slome bootje
        b. Het snelle bootje""") #a --> stukje 11 b --> stukje 12#
        antwoord = input(">>>")
        if antwoord == "a":
            os.system("cls")
            time.sleep(1)
            stukje_11()
            break
        elif antwoord == "b":
            os.system("cls")
            time.sleep(1)
            stukje_12()
            break
        else:
            print("Dat is geen geldig antwoord. Antwoord met a of b")
            time.sleep(2)
            os.system("cls")
#
def stukje_9():
    print("Siham zegt dat het het beste is als we met de smokkelaar gaat en siham betaalt de man.") 
    print("De man lijdt de familie naar een plekje iets verder dan de grens.")
    print("Er zit een gat in de grens waar door ze erdoor kunnen. Er staat ook een bus te wachten. Ze gaan door de grens en zijn nu in libanon.")
    print("Ze lopen naar de bus en stappen in. De bestuurder zegt tegen siham dat ze gaan reizen naar Beiroet en vanaf daar een boot gaan nemen naar Turkije.") 
    print("Hij zegt ook dat de reis 2 uur gaat duren naar Beiroet. Sihams familie is uitgeput door het fietsen en gaan slapen.")
    print("Eenmaal aangekomen in Beiroet maakt de bestuurder de familie wakker. Hij zegt dat ze er zijn. iedereen stapt uit en kijkt om zich heen.")
    print("Het is donker en het is avond. Ze lopen naar het water waar een bootje op ze wacht met 6 mensen erin. Ze stappen in het bootje.")
    print("De kapitein zegt dat de reis 21 dagen gaat duren. Op de 16e dag begint sihams moeder erg ziek te worden.")
    print("De kapitein zegt dat het zeeziek kan zijn of het gebrek aan eten. Later die dag sterft sihams moeder.") 
    print("Siham en Aziz zijn heel erg verdrietig en huilen veel. De kapitein zegt dat ze overboord gegooid moet worden.") 
    print("Siham en Aziz zeggen voor de laatste keer gedag tegen hun moeder. De kapitein gooit hun moeder overboord.") 
    print("Na 20 dagen komen ze aan in Turkije. De reis duurde korter doordat sihams moeder overboord gegooid werd zegt de kapitein.") 
    print("De kapitein zegt gedag tegen iedereen en gaat weg.") 
    print("Siham en Aziz lopen 10 km naar de dichtstbijzijnde stad. Daar kopen ze eten en verblijven ze voor de nacht in een goedkoop 1 sterren hotel.")
    input()
    time.sleep(1)
    os.system("cls")
    stukje_13()
#
def stukje_10():
    print("Siham zegt dat het beter is om geld te besparen omdat de man veelste veel vraagt.") 
    print("De man loopt weg en de familie wacht in de rij om de grens over te steken.")
    print("Siham moeder zegt tegen siham dat ze vervoer nodig hebben om bij de kust van Beiroet aan te komen omdat er vanaf daar boten naar Turkije gaan.")
    print("Siham zegt dat als ze een auto zien ze er meteen heen moeten rennen als ze de grens over zijn. Na een uur zijn ze de grens over.") 
    print("Ze zien een taxi die stopt bij de weg. Ze rennen met ze drieën zo hard als ze kunnen richting de taxi en stappen in.")
    print("De taxibestuurder rijdt een stukje door om weg te komen van de drukte. Daarna zegt de man: waar heen? Siham antwoord: de kust bij Beiroet.")
    print("De taxibestuurder zegt weer: dat is 1 uur rijden dus dat gaat 50 euro kosten. Siham accepteert het en betaalt de man.")
    print("Na een uur zijn ze aangekomen bij de kust van Beiroet. Siham bedankt de man en ze stappen uit. Ze komen een stukje naar de boten.") 
    print("Bij de boten staat een man die mensen over zee smokkelt. Siham loopt naar de man een vraagt hoeveel het kost en hoelang het duurt.") 
    print("De man antwoord: 500 euro per persoon en het duurt 15 dagen. Siham accepteert het en geeft de man zijn geld.")
    print("De man telt het geld en zegt tegen siham dat ze hem moet volgen naar de boten. In de boot zitten 10 mensen.")
    print("De man zegt dat ze ook in de boot moeten zitten. De familie gaat in de boot zitten. De boot vertrekt.")
    print("Na 10 dagen op de boot voelt sihams moeder zich heel erg ziek. De kapitein zegt dat het zeeziek kan zijn of het gebrek aan eten.") 
    print("Later die dag sterft sihams moeder. Siham en Aziz zijn heel erg verdrietig en huilen veel. De kapitein zegt dat ze overboord gegooid moet worden.") 
    print("Siham en Aziz zeggen voor de laatste keer gedag tegen hun moeder. De kapitein gooit hun moeder overboord. Na 15 dagen is de boot aangekomen in Turkije")
    print("De kapitein zegt gedag tegen iedereen en gaat weg.")
    print("Siham en Aziz lopen 10 km naar de dichtstbijzijnde stad. Daar kopen ze eten en verblijven ze in een illegaal vluchtelingenkamp")
    input()
    time.sleep(1)
    os.system("cls")
    stukje_13()
#
def stukje_11():
    print("Siham besluit om het slome bootje te nemen om geld te besparen. Siham betaalt de man en ze stappen aan boort.")
    print("Na 5 dagen varen begint de moeder van siham ziek te worden. De kapitein zegt dat het zeeziek kan zijn of het gebrek aan eten.")
    print("Later die dag sterft sihams moeder. Siham en Aziz zijn heel erg verdrietig en huilen veel. De kapitein zegt dat ze overboord gegooid moet worden.")
    print("Siham en Aziz zeggen voor de laatste keer gedag tegen hun moeder. De kapitein gooit hun moeder overboord. De kapitein zegt gedag tegen iedereen en gaat weg.") 
    print("Siham en Aziz lopen 10 km naar de dichtstbijzijnde stad. Daar kopen ze eten en verblijven ze in een illegaal vluchtelingenkamp. ")
    input()
    time.sleep(1)
    os.system("cls")
    stukje_13()
#
def stukje_12():
    print("Siham besluit het snelle bootje te nemen. Siham betaalt de man en ze stappen aan boort.")
    print("Na 2 dagen varen begint de moeder van siham ziek te worden. De kapitein zegt dat het zeeziek kan zijn of het gebrek aan eten.")
    print("Later die dag sterft sihams moeder. Siham en Aziz zijn heel erg verdrietig en huilen veel. De kapitein zegt dat ze overboord gegooid moet worden.")
    print("Siham en Aziz zeggen voor de laatste keer gedag tegen hun moeder. De kapitein gooit hun moeder overboord. De kapitein zegt gedag tegen iedereen en gaat weg.")
    print("Siham en Aziz lopen 10 km naar de dichtstbijzijnde stad. Daar kopen ze eten en verblijven ze in een illegaal vluchtelingenkamp. ")
    input()
    time.sleep(1)
    os.system("cls")
    stukje_13()
#
def stukje_13():
    while True:
        print("Na een paar dagen verbleven te hebben in het kamp komt siham in aanraking met een mensensmokkelaar die je naar Griekenland smokkelt.")
        print("Hij zegt dat je binnen 2 dagen in Griekenland bent. Siham vraagt aan de man hoeveel het kost. De man antwoord 500 euro per persoon.") 
        print("Siham gaat er mee akkoord. Siham geeft het geld aan de man. De man telt het geld en zegt daarna dat ze met hem mee moeten komen naar de bus.")
        print("Siham en Aziz lopen naar de bus en ze zien dat de bus vol zit met mensen. Ze stappen de bus in en de bus rijdt naar de kust.")
        print("Eenmaal aangekomen stapt iedereen uit. Siham en Aziz zien heel veel schepen die mensen smokkelen. Ze worden door de man geleid naar 1 van de schepen.")
        print("De man vertelt iedereen om aan boord te gaan. Iedereen die in de bus zat zit nu in op de boot.")
        print("De kapitein legt iedereen uit dat ze altijd de veiligheidsvest moeten dragen voor het geval dat de boot zinkt.") 
        print("Iedereen doet wat de kapitein zegt. De kapitein zegt dat ze nu gaat vertrekken.")
        print("\n")
        print("2 dagen later.")
        print("\n")
        print("De boot is aangekomen in Griekenland. De kapitein legt de boot goed zodat de vluchtelingen kunnen uitstappen.") 
        print("Voordat siham en Aziz uitstappen zegt de kapitein tegen siham dat Aziz heel erg veel lijkt op een man die hij een paar jaar terug heeft gesmokkeld.")
        print("Siham en Aziz zijn verbaasd. Ze denken of dat hun vader kan zijn want Aziz lijkt heel erg op zijn vader.") 
        print("Siham vraagt de kapitein of hij weet waar hij naar toe ging.")
        print("De kapitein denkt even na en zegt: hij ging of naar Nederland of naar Oostenrijk maar ik kan me niet herinneren welk van de 2.")
        print("Siham bedankt de man en zegt tegen Aziz: waar gaan we eerst heen Nederland of Oostenrijk? ")
        print("\n")
        print(""""Waar wil je eerst heen? ...
        a. Nederland
        b. Oostenrijk""") #a --> stukje 14 b --> stukje 15#
        antwoord = input(">>>")
        if antwoord == "a":
            os.system("cls")
            time.sleep(1)
            stukje_14()
            break
        elif antwoord == "b":
            os.system("cls")
            time.sleep(1)
            stukje_15()
            break
        else:
            print("Dat is geen geldig antwoord. Antwoord met a of b")
            time.sleep(2)
            os.system("cls")
#
def stukje_14():
    print("Aziz antwoord: Nederland. Siham zegt dan is het nu gekozen we gaan naar Nederland.")
    print("Siham en Aziz lopen enthousiast weg van de kust richting een stad. Ze hebben 10 km gelopen en zijn aangekomen in een stad.")
    print("Siham vraagt in het Engels aan een voorbijganger waar het station is. De voorbijganger wijst naar een bord en zegt: als je dat bord volgt kom je er.")
    print("Siham bedankt de vrouw en loopt naar de richting die het bord aangeeft. Na een stukje gelopen te hebben komen siham en Aziz bij het station.")
    print("Ze vragen aan een medewerker van het station hoe ze het snelst in Nederland komen.") 
    print("De medewerker zegt dat ze op perron 4 de trein naar Frankrijk moeten nemen en vanaf Frankrijk kunnen ze naar Nederland.") 
    print("Siham vraagt ook of ze een kaartje bij hem kan kopen. De medewerker knikt ja en verkoopt ze een 2 persoonskaartje naar Frankrijk.")
    print("Siham en Aziz gaat naar perron 4 en wachten op de trein.")
    print("Na 10 minuten gewacht te hebben zien ze de trein aankomen. De trein stopt en ze stappen in. De trein rit duurt 14 uur ziet siham op het scherm.")
    print("\n")
    print("14 uur later.")
    print("\n")
    print("Ze zijn aangekomen in Parijs Frankrijk. Siham en Aziz stappen uit en vragen aan een medewerker met welke trein ze in Nederland komen.")
    print("De medewerker zegt dat ze naar perron 5 moeten en daar de trein naar Amsterdam Nederland moeten nemen en hij verkoopt ze ook de kaartjes.")
    print("Siham en Aziz hebben de kaartjes gekocht en lopen naar perron 5. Op perron 5 zien ze dat de trein over 5 minuten komt.") 
    print("Na 5 minuten wachten zien ze de trein en de trein stopt. Ze stappen in en nemen plaatst. Siham ziet dat het 5 uur duurt. ")
    print("\n")
    print("5 uur later")
    print("\n")
    print("Ze zijn aangekomen in Amsterdam Nederland. Siham en Aziz stappen uit en lopen naar buiten.")
    print("Daar nemen ze een taxi naar het dichtstbijzijnde hotel. Eenmaal aangekomen boekt siham een kamer voor 2 voor een week.")
    print("Dat kost haar 100 euro. Ze betaalt en loopt samen met Aziz naar de kamer. eenmaal op de kamer kijken ze tv.")
    print("Ze kijken het nieuws van deze week. Ze zien dat er een cruiseschip is waar vluchtelingen verblijven.")
    print("De vluchtelingen worden ook geïnterviewd en 1 van die geïnterviewde is siham en Aziz hun vader.")
    print("Ze zijn dolblij dat ze weten waar hun vader is. Siham zegt tegen Aziz dat ze er morgen heen gaan en beginnen allebei te slapen. ")
    input()
    time.sleep(1)
    os.system("cls")
    stukje_16()
#
def stukje_15():
    print("Aziz antwoord: Oostenrijk. Siham zegt dan is het nu gekozen we gaan naar Oostenrijk.")
    print("Siham en Aziz lopen enthousiast weg van de kust richting een stad. Ze hebben 10 km gelopen en zijn aangekomen in een stad.")
    print("Siham vraagt in het Engels aan een voorbijganger waar het station is. De voorbijganger wijst naar een bord en zegt: als je dat bord volgt kom je er.")
    print("Siham bedankt de vrouw en loopt naar de richting die het bord aangeeft. Na een stukje gelopen te hebben komen siham en Aziz bij het station.") 
    print("Ze vragen aan een medewerker van het station hoe ze het snelst in Oostenrijk komen.")
    print("De medewerker zegt dat ze op perron 8 de trein naar Oostenrijk moeten nemen. Siham vraagt ook of ze een kaartje bij hem kan kopen.")
    print("De medewerker knikt ja en verkoopt ze een 2 persoonskaartje naar Oostenrijk. Siham en Aziz gaat naar perron 8 en wachten op de trein.")
    print("Na 15 minuten gewacht te hebben zien ze de trein aankomen.")
    print("De trein stopt en ze stappen in. De trein rit duurt 7 uur ziet siham op het scherm. ")
    print("\n")
    print("7 uur later.")
    print("\n")
    print("Ze zijn aangenomen in wenen Oostenrijk. Siham en Aziz stappen uit de trein en lopen naar buiten. Buiten zien ze roepen ze een taxi.")
    print("Er komt een man naar hun toe die zegt dat hij taxichauffeur is en vraagt waar ze heen moeten. Siham zegt dat ze een plek nodig hebben om te slapen.")
    print("De man zegt dat er een vluchtelingenkamp hier dichtbij is en dat hij ze er heen wil brengen. De man zegt dat ze met hem mee moeten lopen naar zijn taxi.") 
    print("Siham en Aziz stappen in en de man brengt ze naar het kamp. Siham betaalt de man en ze stappen uit. Op het kamp krijgen siham en Aziz een bed.") 
    print("Ze kunnen voorlopig in het kamp blijven. Siham laat op het bed liggen en begint na te denken om wat het beste is om te doen.")
    print("Na lang na gedacht te hebben zegt ze tegen Aziz dat ze gaat solliciteren bij ziekenhuizen om geld te verdienen.")
    print("Siham studeerde in Syrië om dokter te worden. Ze had bijna haar studie afgemaakt maar door de oorlog lukte dat niet.")
    print("Ze heeft wel alle officiële papieren mee waarop staat dat ze daadwerkelijk gestudeerd heeft om dokter te worden.")
    print("Siham zegt verder tegen Aziz terwijl ik solliciteer moet jij rond gaan vragen naar papa. Aziz zegt dat hij dat zal doen.")
    print("De volgende dag pakt siham haar papieren en gaat van ziekenhuis naar ziekenhuis. Aan het eind van de dag komt ze naar Aziz en zegt dat het haar niet is gelukt.")
    print("Een week gaat voorbij en siham is nog steeds nergens aangenomen maar plots komt er een man naar haar toe. De man is strak in pak en ziet er verzorgd uit.")
    print("Hij zegt dat hij op zoek is naar siham. Siham zegt dat ben ik.") 
    print("De man legt uit dat hij de baas van een ziekenhuis is en dat hij over haar heeft gehoord omdat ze op heel veel plekken heeft gesolliciteerd.") 
    print("De man zegt dat ze siham een baas wil geven en dat hij haar de kans wil geven om haar studie af te maken. Siham is dolblij. ")
    print("\n")
    print("maanden later.")
    print("\n")
    print("Siham heeft nu een verblijfsvergunning in Oostenrijk. Ze is een dokter en ze heeft een huis. Aziz leert de taal en gaat naar school.") 
    print("op een dag zaten siham en Aziz thuis tv te kijken. Ze keken naar het nieuws van vandaag.")
    print("Op het nieuws ging het over een cruiseschip in Nederland waar vluchtelingen verbleven. De vluchtelingen werden ook geïnterviewd.")
    print("1 van de geïnterviewde vluchtelingen was siham en Aziz hun vader. Siham en Aziz keken verbaasd naar de tv en daarna dolblij.")
    print("Ze wisten eindelijk waar hun vader was. Siham pakt haar laptop en koopt een 2 persoons ticket naar Nederland en belt daarna haar baas om te zeggen dat ze 2 weken vrij neemt.")
    print("Siham kocht vliegtickets voor de volgende dag dus siham en Aziz beginnen hun spullen in te pakken. De volgende dag vliegen ze naar Nederland.")
    print("Aangekomen op Schiphol lopen ze naar buiten naar de taxi’s. siham spreekt een man aan en vraagt hem om hun naar een hotel te brengen.")
    print("De man gaat akkoord. Siham en Aziz stappen in en de man brengt ze naar een hotel. Eenmaal aangekomen betaald siham de man en lopen ze het hotel binnen.")
    print("Siham boekt een kamer voor een week. Siham betaalt en krijgt de sleutels.")
    print("Ze loopt met Aziz naar de kamer. Ze rusten allebei uit om de volgende dag het cruiseschip te bezoeken.")
    input()
    time.sleep(1)
    os.system("cls")
    stukje_16()
#
def stukje_16():
    print("Het is ochtend siham wordt wakker en maakt daarna Aziz wakker. Ze doen hun kleren aan en gaan het hotel uit.")
    print("Buiten nemen ze een taxi naar het cruiseschip. Eenmaal aangekomen betaalt siham de taxichauffeur en stappen ze uit.")
    print("Ze lopen het schip op en beginnen rond te vragen.")
    print("Na een uur rond vragen zijn ze erachter gekomen dat hun vader daadwerkelijk op het schip woont maar waar hij is weet niemand.")
    print("Siham en Aziz besluiten te ontbijten in de kantine. Siham en Aziz lopen de kantine binnen en ze zien aan 1 van de tafels hun vader zitten eten.") 
    print("Siham schreeuwt: papa en haar vader kijkt sihams kant op. Ze beginnen naar elkaar toe te rennen en omhelzen elkaar. Ze beginnen alle 3 te huilen van blijdschap.")
    print("Siham vader zegt tegen siham en Aziz om aan tafel te komen zitten zodat hij alles kan uitleggen.")
    print("Ze gaan met ze drieën zitten en sihams vader legt uit dat hij het heel moeilijk heeft gehad.")
    print("""Hij zegt dat hij in eerste instantie naar Oostenrijk wilde gaan maar toen hij daar was moest hij de gevangenis in 
    omdat hij een gevecht uit elkaar probeerde te halen maar er zelf in belandde.""")
    print("Hij zegt ook dat hij daarna naar Nederland is gevlucht en vanaf daar contact heeft proberen op te zoeken maar dat lukte hem niet.") 
    print("Zijn plan was om wat geld te verdienen en het daarna nog een keer te proberen. Sihams vader vraagt ook naar zijn vrouw.") 
    print("Siham barst in tranen uit en zegt dat zijn de boot tocht niet heeft overleefd. Ze beginnen met ze drieën te huilen. Sihams vader krijgt een hartaanval.") 
    print("Siham belt de ambulance. De ambulance is heel snel gekomen en heeft hun vader naar het ziekenhuis gebracht. Siham en Aziz reisde mee in de ambulance.") 
    print("Eenmaal in het ziekenhuis wordt hun vader opgenomen. Terwijl siham en Aziz wachten komt er een man naar siham toe en zegt dat hij haar herkent.") 
    print("De man stelt zich eerst voor als de baas van het ziekenhuis. Siham had in Oostenrijk een beroemde Nederland geopereerd genaamd Marco Borsato.")
    print("Marco had over haar vertelt in een podcast. De man biedt siham een baas aan met een salaris die heel veel beter betaald dan in Oostenrijk.")
    print("Siham neemt de baas meteen aan. De man zegt dat ze later terug kan komen met haar papieren en loopt weg. Siham belt haar baas in Oostenrijk op en neemt ontslag.")
    print("Siham en Aziz verhuizen nu naar Nederland. Paar uur later heeft siham al een mooi huis gekocht in Nederland dichtbij het ziekenhuis. ")
    print("\n")
    print("Aantal jaren verder.")
    print("\n")
    print("Siham leeft nu met Aziz in een grote villa. Siham vader is een aantal maanden geleden dood gegaan aan nog een hartaanval.")
    print("Hij had te veel verdriet voor zijn vrouw. Siham kent de taal nu al erg goed en werkt nog steeds als dokter. Aziz gaat naar school en kan al vloeiend Nederlands.") 
    print("Aziz blijkt ook slimmer te zijn dan siham. Siham en Aziz hebben het erg naar hun zin en ze leven nog lang en gelukkig. ")
    print("\n")
    print("Dit was het einde. Bedankt voor het spelen")
    time.sleep(3)
    exit
#
def stukje_17():
    print("Beide moeders zeggen met 1 auto te willen gaan dus ze stappen met ze alle in de auto van Mohameds vader omdat die het grootst is.")
    print("Ze rijden naar de grens. Eenmaal aangekomen bij de grens wachten ze met de auto in de rij om het land te verlaten.")
    print("Na een tijdje zijn ze het land uit en zijn ze in libanon. nu rijden ze richting de kust van libanon om daar de boot te pakken.")
    print("Weer een tijdje later zijn ze aangekomen bij de kust. Daar staat een man plekken voor de boot te verkopen.")
    print("Terwijl sihams vader plekken gaat kopen naar Mohameds vader afscheid van zijn auto. Sihams vader heeft plekken gekocht en ze gaan nu allemaal aanboord.")
    print("Na dagen gevaren te hebben komen ze aan in Griekenland. ")
    input()
    time.sleep(1)
    os.system("cls")
    stukje_19()
#
def stukje_18():
    print("Beide moeders zeggen met 2 auto te willen gaan omdat het anders te kramp wordt. Ze rijden naar de grens.")
    print("Eenmaal aangekomen bij de grens wachten ze met de auto’s in de rij om het land te verlaten. Na een tijdje zijn ze het land uit en zijn ze in libanon.")
    print("nu rijden ze richting de kust van libanon om daar de boot te pakken. Weer een tijdje later zijn ze aangekomen bij de kust.")
    print("Daar staat een man plekken voor de boot te verkopen. Beide vader laten hun auto achter en gaan plekken kopen.")
    print("Na plekken gekocht te hebben stappen ze op de boot. Na dagen gevaren te hebben komen ze aan in Griekenland. ")
    input()
    time.sleep(1)
    os.system("cls")
    stukje_19()
#
def stukje_19():
    while True:
        print("Eenmaal bij de kust van Griekenland staat de politie de vluchtelingen op te wachten.")
        print("De kapitein van de boot en een paar andere springen het water in en beginnen te zwemmen. Siham familie en Mohameds familie geven hun netjes over.")
        print("De politie haalt beide families uit elkaar en neemt ze apart mee. Siham schreeuwt nog: dat is mijn verloofde. ")
        print("\n")
        print("""Wat doet de politie? ...
        a. samen meenemen
        b. apart meenemen""") #a --> stukje 20 b --> stukje 21#
        antwoord = input(">>>")
        if antwoord == "a":
            os.system("cls")
            time.sleep(1)
            stukje_20()
            break
        elif antwoord == "b":
            os.system("cls")
            time.sleep(1)
            stukje_21()
            break
        else:
            print("Dat is geen geldig antwoord. Antwoord met a of b")
            time.sleep(2)
            os.system("cls")
    #
    def stukje_20():
        print("De politie heeft medelijden omdat het 2 verloofden zijn en besluit om ze samen mee te nemen.") 
        print("Eenmaal op het bureau legde de politie uit dat ze zijn opgepakt omdat ze vluchtelingen zijn. de politie doorzoekt ook al hun spullen.") 
        print("Tijdens het doorzoeken komt de politie documenten tegen waarin ze zien dat siham een dokter in opleiding is en dat Mohamed 1 van de beste advocaten in Syrië.")
        print("De politie door beter onderzoek naar de documenten en haalt er ook een rechter bij.")
        print("""Nadat beide families een aantal dagen op bureau hebben geslapen komt de rechter naar ze toe om te vertellen
        dat ze een verblijfsvergunning krijgen als Mohamed voor de overheid gaat werken en siham na haar studie in 1 van de beste ziekenhuizen van Griekenland gaat werken.""")
        print("Siham en Mohamed gaat er mee akkoord en ze worden vrij gelaten.")
        input()
        time.sleep(1)
        os.system("cls")
        stukje_22()
#
def stukje_21():
    print("De politie toon geen medelijden en neemt ze apart mee naar andere politiebureaus.")
    print("Eenmaal op het politiebureau vraag siham heel vaak naar haar verloofde. Ze krijgt geen antwoord.")
    print("Alle spullen van de familie worden doorzocht. De politie vindt documenten over sihams studie waarop staat dat ze bijna dokter is.")
    print("De politie schakelt een rechter in.")
    print("""Nadat de familie een aantal dagen op bureau heeft geslapen komt de rechter naar ze toe om te vertellen dat ze in Griekenland mogen blijven 
en een verblijfsvergunning krijgen op de voorwaarde dat siham haar studie af maakt en in een ziekenhuis gaat werken omdat er dokters te kort is.""")
    print("Siham gaat er mee akkoord. Ze worden vrijgelaten en ze krijgen een tijdelijk huis. Voordat siham het politiebureau uit loopt vraagt ze nog naar haar verloofde.")
    print("De politie weet niet op welk kantoor ze zitten en zegt dat ze haar zullen informeren over hun. ")
    input()
    time.sleep(1)
    os.system("cls")
    stukje_23()
#
def stukje_22():
    print("Het is alweer 5 jaar later. Siham en Mohamed zijn gelukkig getrouwd.")
    print("Ze hebben ook een kindje die er aan komt. Siham is 1 van de beste doctoren van Griekenland en Mohamed is 1 van de beste advocaten van Griekenland.")
    print("Ze kunnen allebei vloeiend Grieks. Ze zijn ook allebei erg blij dat ze een goed leven hebben. En ze leefden lang en gelukkig.")
    print("\n")
    print("Dit is het einde. Bedankt voor het spelen.")
    time.sleep(2)
    exit()
#
def stukje_23():
    print("Een aantal dagen later komt de politie voor de deur bij siham om te vertellen dat ze ontdekt hebben wat er met Mohamed is gebeurd.") 
    print("Toen ze vanaf de kust naar het bureau reden kregen ze een ongeluk. Een vrachtwagen botste tegen het politievoertuig.")
    print("Iedereen in het politievoertuig is dood. Siham is helemaal kapot en barst uit in tranen. Siham viel op de grond omdat ze een hartaanval kreeg.")
    print("Ze was ter plekke dood. Sihams vader moeder en Aziz renden naar siham die dood op de grond lag.")
    print("Ze barstte in tranen. Siham is dood en de familie leefden lang maar niet gelukkig.")
    print("\n")
    print("Dit is het einde. Bedankt voor het spelen.")
    time.sleep(2)
    exit()

stukje_1()
