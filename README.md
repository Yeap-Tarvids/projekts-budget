Projekta uzdevums: Programma ir izstrādāta, lai palīdzētu lietotājam sekot līdzi savam personīgajam budžetam, sadalot to kategorijās un kontrolējot izdevumus katrā no tām. Lietotājs var iestatīt kopējo budžetu, noteikt budžeta limitus katrai kategorijai, pievienot izdevumus konkrētās kategorijās un sekot līdzi kopējiem un kategoriju budžeta atlikumiem. Programma arī dod iespēju vizuāli attēlot budžetu izmantojot sektoru diagrammu.

Programma saglabā datus failā, tādējādi nodrošinot, ka budžeta informācija paliek pieejama arī pēc programmas aizvēršanas un atkārtotas palaišanas.

Izmantotās python bibliotēkas:

1)json: Bibliotēka tiek izmantota, lai saglabātu un ielādētu budžeta datus no ārēja faila (budget_data.json). Lai dati tiku saglabāti starp programmas palaišanas reizēm.

2)collections.defaultdict: Šī bibliotēka ļauj ērti pārvaldīt kategoriju budžeta limitus un izdevumu apjomus. Tā automātiski inicializē atslēgas ar noklusēto vērtību (šajā gadījumā 0.0), izvairoties no kļūdām, kad tiek pievienoti vai lasīti dati jaunām kategorijām.

3)os: Bibliotēka tiek izmantota, lai pārbaudītu, vai datu fails pastāv, un lai to dzēstu, ja lietotājs izvēlas notīrīt visus datus.

4)matplotlib.pyplot: Bibliotēka nodrošina vizuālu sektoru diagrammas attēlošanu, kas parāda, kā tiek sadalīts budžets starp dažādām kategorijām un cik daudz ir palicis vai pārtērēts kopējā budžetā.
