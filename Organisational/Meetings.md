## Erstgespräch

Was sind Einflussfaktoren? -pressure vibration usw. 
Wie sehen die Daten aus? Wo und welche Daten werden gespeichert? Log Datein und Maschinendaten (Leere Werte = auch wichtig)
Wie kann man aktuell gegensteuern?  - reaktiv
Wann fällt die Produktion aus? - Wenn Maschine gewartet werden muss. Label: 
Lieber false positiv
Welchen Einfluss haben ausfälle? -200.000 € pro Stunde Kunde
Können Wartungen in geplanten Stillständen ausgeführt werden?  -nachts keine Produktion

für nächstes gespräch Data Understanding und gegebenenfalls Data Preparation

## Meeting 29.01.24

Produktionsindex = Wie zufrieden MA's mit aktueller Produktion waren
vermutlich raus die Spalte.

Methoden zur Behandlung von fehlerhaften Daten dürfen selbst gewählt werden. Bei wenigen fehlerhaften Daten können die Daten auch einfach entfernt werden

Bis zum nächsten mal:
Data Cleaning fertig und mal erste analyse mit Zielvariable Ausschuss und Ausfall
Daten in SQL Datenbank und Mongo DB hochladen

Unstrukturierte Daten (LOG Dateien) anschauen Data Understanding machen
Process Mining aus LOG Daten macht keinen Sinn eher Text analysieren

Gegenenfalls noch LOG Dateien und Wartungsdaten verknüpfen um neue Kenntnisse zu gewinnen

## Meeting 21.02.2024

Thema 1: Datenanalyse zeigen
Balancing versuchen
Feature Importance - für modelle um Einflussfaktoren zu bestimmen
klassifikation bestimmen für logmessage und service ok
1. teil alle modelle durchlaufen lassen - 2 besten wählen und vergleichen
2. teil klassifikations modell zu service ok und logmessage
3. vergleichen von den einflussfaktoren - korrelation

Thema 2: APIS und Skalierung 
Deployment in Docker - ausgeklammert
FastAPI
modell trainieren
analyse machen

parallelisierung
dask
datenbanken auf ram bringen
nur auf 2 Folien

Thema 3: Abgabe
jeder punkt crisp dm ein themensatz folien
foliennummern und Quellen 
links zu bibliotheken
2 Tage vor Abgabe bis 10 Doku folien 26.02.2024 10:00