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
        b.  auto's.""") #a --> stukje 17 b --> stukje 18#
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
    input()
    time.sleep(1)
    os.system("cls")
    stukje_6()
