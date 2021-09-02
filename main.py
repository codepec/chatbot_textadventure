import random

zufallsantworten=["Oh, wirklich", "Interessant ...", "Das kann man so sehen", "Ich verstehe ...", "Ich verstehe ..."]

reaktionsantworten = {			"hallo": 	"aber Hallo",
					"eintreten": 	"Schön, dass Sie sich für den schwierigeren Weg entschieden haben. Möchten Sie ein Bier? 'Bier' oder 'sterben' ", 
					"geht": 	"Was verstehst du darunter?", 
					"essen": 	"Ich habe leider keinen Geschmackssinn :(",
				 	"bier": 	"Bitte schön hier ist Ihr Bier. Möchten Sie ein weiteres Bier? 'Bier' oder müssen Sie auf die Toilette 'Toilette'",
					"toilette": 	"Ach du heilige Sche...! Wie sieht es den hier aus und wie bestialisch es hier stinkt... Zurück in die 'Kneipe'",
					"kneipe": 	"Hallo geht's noch? Können Sie nicht aufpassen. Sie hätten mich beinahe über den Haufen gerempelt und dann nicht einmal entschuldigen. 'enschuldigen' oder 'wegschubsen'",
					"entschuldigen": "Entschuldigung angenommen. Was war denn da drin los? Sie sehen ja ganz benommen aus und entschuldigen Sie, dass ich das so offen sage, aber Sie stinken ein wenig.. Ach wie unhöflich von mir. Ich habe mich ja noch gar nicht vorgestellt. Mein Name ist Silly. Du bist auch neu in der Stadt oder? Dann hör mal gut zu 'zuhören' oder 'wegschubsen'",
					"wegschubsen":	"Da hat es jemand aber sehr eilig. Aber so schnell entkommst du Silly nicht. Viel mehr Freunde wie mich wirst du als Neuer in dieser Stadt nicht finden. Also hör gut zu. 'zuhören'",
					"zuhören":	"In der Stadt verschwinden ab und zu Leute. Es trifft vorallem die Neuankömmlinge.. Leute wie Du und ich.. Ich bin nicht alleine hier angekommen. Meine Zwillingsschwester Sally hat mich begleitet. Doch Sie ist seit zwei Tagen spurlos verschwunden. Ich habe schon überall nach ihr gesucht. Doch bis jetzt keine Spur von ihr. Und die Einwohner sind mir keine große Hilfe. Die meisten haben Angst selber verschleppt zu werden. Hilfst du mir meine Schwester zu finden? 'helfen' oder 'bier'",
					"helfen":	"Huch, das freut mich aber sehr. Komm mit wir suchen uns einen ungestörteren Platz in diesem Gemäuer. Dort hinten gibt es ein paar Stuben, sogenannte Schmuddelstuben. Folgst du mir? 'folgen'",
					"folgen":	"So, nimm neben mir auf der Bettkante platz. Ich weiß es ist eher praktisch eingerichtet. Außer einem Bett und einem Schrank gibt es hier nicht viel. Möchtest du einen Drink oder lieber gleich die Geschichte hören? 'drink' oder 'geschichte'",
					"geschichte":	"Also, alles was ich weiß ist, dass ..." 'flüchten' oder 'kämpfen',
					"drink":	"Ein Whiskey eisgekühlt, kommt sofort... Bitte schön. So und nun bereit für die Suche? 'geschichte'",
					"kämpfen":	"tot",
					"flüchten":	"über die stinkende Toilette in den Hinterhof. zwielichtige Gestalt der Insider",
					"befragen":	"Insider befragen",
					"feuerleiter":	"'geschoss'",
					"geschoss":	"Geschoss mit unbekannten Zimmern eine art zwischengeschoss",
					"rotes":	"rotes zimmer",
					"blaues":	"blaues zimmer",
					"abstellkammer": "abstellkammer",


						}
                      
print("Willkommen in unserer dreckigen Stadt Wallach")
print("Treten Sie näher und stolpern Sie nicht über die halb verfaulten Schädel die hier überall verstreut sind?")
print("Geben Sie 'eintreten' ein oder suchen Sie mit 'sterben' für immer das Weite")
print("")

nutzereingabe = ""
while nutzereingabe != "sterben":
    nutzereingabe = ""
    while nutzereingabe == "":
        nutzereingabe = input("Ihre Antwort: ")
        
    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()
    
    intelligenteAntworten = False
    for einzelwoerter in nutzerwoerter:
        if einzelwoerter in reaktionsantworten:
            print(reaktionsantworten[einzelwoerter])
            intelligenteAntworten = True
    if intelligenteAntworten == False:
        print(random.choice(zufallsantworten))
        
    print("")

print("Einen schönen Tag wünsche ich Dir. Bis zum nächsten Mal")
