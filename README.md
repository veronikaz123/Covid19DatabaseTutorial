# Covid19DatabaseTutorial

Vi skal arbejde med det underliggende data der ligger under visualiseringen af covid-19, [(CSSE), Johns Hopkins University Hospital](https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6)

### øvelse
I skal undersøge informationen på websitet.
* Lav en liste med de informationer I kan finde,(lande, antal smittede, ).
* Beskriv hvordan informaitonerne bliver repræsenteret.
* Beskriv interaktionen, hvordan vælger brugeren og hvilke informationer kommer der.


### Tre-lags-arkitektur, [iftek](http://iftek.dk/leksikon:tre-lags-arkitektur)
I en trelagsarkitur indeles et program i tre lag, hvilket er er nyttigt i implementeringen af programmer, da de tre lag så vidt mulig holdes adskilte og dermed er hele programmet lettere at overskue.

*Præsentationslag:* Det øverste lag der håndterer modtagelse og præsentation af data. Dette lag er kendetegnet ved at være ”tæt” på brugeren af programmet.
*Logiklag:* Det midterste lag der håndterer udvekslingen af data mellem præsentationslaget og datalaget.
*Datalag:* Det nederste lag der opbevarer og håndterer data. Dette lag er også kendetegnet ved at være ”tæt” på computeren.

*Datalaget* er her en database som er lagt offentligt tilgængelig på Github [https://github.com/CSSEGISandData/COVID-19](https://github.com/CSSEGISandData/COVID-19)
*Logiklaget* behandler data.
![dataeksempel](images/database1.png)
eks.
pseudokode til valg af grønland:
```
Hvis mus klik med koordinaterne (-6.92,61) vis data fra række 94
```
I *Præsentationslaget* bliver resultatet af logiklaget vist.
eks.
![færøerne](images/database2.png,images/database3.png)

### Øvelse
