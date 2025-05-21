Projekta uzdevums: Programma ir izstrādāta, lai palīdzētu lietotājam sekot līdzi savam personīgajam budžetam, sadalot to kategorijās un kontrolējot izdevumus katrā no tām. Lietotājs var iestatīt kopējo budžetu, noteikt budžeta limitus katrai kategorijai, pievienot izdevumus konkrētās kategorijās un sekot līdzi kopējiem un kategoriju budžeta atlikumiem. Programma arī dod iespēju vizuāli attēlot budžetu izmantojot sektoru diagrammu.

Programma saglabā datus failā, tādējādi nodrošinot, ka budžeta informācija paliek pieejama arī pēc programmas aizvēršanas un atkārtotas palaišanas.

Izmantotās python bibliotēkas:

1)json: Bibliotēka tiek izmantota, lai saglabātu un ielādētu budžeta datus no ārēja faila (budget_data.json). Lai dati tiku saglabāti starp programmas palaišanas reizēm.

2)collections.defaultdict: Šī bibliotēka ļauj ērti pārvaldīt kategoriju budžeta limitus un izdevumu apjomus. Tā automātiski inicializē atslēgas ar noklusēto vērtību (šajā gadījumā 0.0), izvairoties no kļūdām, kad tiek pievienoti vai lasīti dati jaunām kategorijām.

3)os: Bibliotēka tiek izmantota, lai pārbaudītu, vai datu fails pastāv, un lai to dzēstu, ja lietotājs izvēlas notīrīt visus datus.

4)matplotlib.pyplot: Bibliotēka nodrošina vizuālu sektoru diagrammas attēlošanu, kas parāda, kā tiek sadalīts budžets starp dažādām kategorijām un cik daudz ir palicis vai pārtērēts kopējā budžetā.

Izmantotās datu struktūras:

float mainīgie kopējam budžetam (total_budget) un kopējajiem izdevumiem (total_spent), lai precīzi aprēķinātu naudas daudzumu.

collections.defaultdict(float) kategoriju budžeta limitu un izdevumu glabāšanai:

category_limits — glabā katras kategorijas budžeta limitu.

category_spent — glabā katras kategorijas iztērēto summu.

Programmatūras izmantošanas metodes:

Programmas palaišana

Programma piedāvā izvēlni ar sekojošām iespējām:

Parādīt kopējo un kategoriju budžetu statusu — attēlo, cik ir kopējais budžets, cik iztērēts un cik atlikums, kā arī detalizētu pārskatu par katras kategorijas izdevumiem un atlikumiem.

Iestatīt kopējo budžetu — nosaka sākotnējo vai jauno budžetu.

Atjaunināt vai pievienot budžeta limitu konkrētai kategorijai — ļauj definēt vai palielināt budžetu kādai kategorijai.

Pievienot izdevumu noteiktā kategorijā — reģistrē izdevumus, kas tiks atņemti no attiecīgās kategorijas limita un kopējā budžeta.

Pievienot naudu kopējam budžetam — ļauj palielināt kopējo budžeta summu.

Notīrīt visus datus — izdzēš visus saglabātos datus un sāk no jauna.

Iziet no programmas — saglabā datus un aizver programmu.

Rādīt izdevumu sektoru diagrammu — atver vizuālu attēlojumu, kurā redzams izdevumu sadalījums starp kategorijām un atlikums vai pārtērējums.

Programma brīdina, ja:

Tiek mēģināts pievienot izdevumu kategorijai, kas nav iepriekš definēta.

Izdevumi pārsniedz konkrētās kategorijas vai kopējo budžeta atlikumu.

Kopējais budžets tiek pārtērēts.

Datu saglabāšana un ielāde Visi veiktie labojumi tiek automātiski saglabāti failā budget_data.json.
