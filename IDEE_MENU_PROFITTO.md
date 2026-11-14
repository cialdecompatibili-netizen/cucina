# Idee menu e piatti che vendono (ricerca del 14/11/2026)

File di lavoro: da qui, nella prossima sessione, si inseriscono i piatti nel sito con `automation/prodotto.py --lista`.

## 1. Premessa e limiti (leggere prima)

- Nessuno può garantire le vendite. Questo file riduce il rischio scegliendo piatti che gli altri già vendono bene, ma la prova vera è il sito online con ordini reali.
- Ho guardato: classifiche di Just Eat e Deliveroo, menu di ristoranti di pesce trovati online (Lazio e altre zone), articoli di settore su food cost e menu engineering, consigli di Uber Eats e DoorDash.
- NON ho potuto vedere i menu interni delle app di delivery (Just Eat, Deliveroo, Glovo): sono dietro app e login. I prezzi sotto vengono da menu di ristoranti a tavola trovati sul web.
- Alcune classifiche sono vecchie (2019-2020 e 2023-2024), le segno con la data.
- I numeri di margine in euro NON li ho: servono i tuoi costi reali di pescheria. Dove metto un prezzo mio lo scrivo come IPOTESI.

## 2. Cosa si ordina di più a domicilio in Italia (dati delle piattaforme)

- Just Eat (osservatorio, dati 2019-2020): piatti più ordinati a livello nazionale = pizza margherita, patatine fritte, pizza diavola, involtino primavera, supplì, pizza capricciosa, olive ascolane, riso alla cantonese. Il gelato e i dolci erano in forte crescita (+133% in quel periodo).
- Deliveroo 100 (varie edizioni): il piatto più ordinato in Italia era il poke al salmone; la piadina è risultata prima in Italia per popolarità; l'hamburger di McDonald's in testa nel 2023; nel 2024 la classifica mondiale non aveva pizze nei primi dieci.
- Roma (AGI, marzo 2026): in crescita ravioli alla griglia, involtini primavera, pita greca.
- Lezione: i piatti che portano più ordini sono pochi, riconoscibili e facili da fare. Il pesce non compare in queste classifiche, quindi per il pesce la domanda va costruita con piatti "classici" che il cliente già conosce (fritto, scoglio, risotto di scampi).

## 3. Prezzi reali di menu di pesce trovati online (ristoranti, a tavola)

Servono come riferimento per i prezzi del sito. Sono prezzi da sala, non da delivery.

| Piatto | Prezzo trovato |
|---|---|
| Spaghetti allo scoglio | 15 € (un locale) |
| Spaghetti alle vongole | 10 € e 15 € (due locali) |
| Linguine ai frutti di mare | 15 € |
| Fritto misto di pesce | 15 € |
| Baccalà fritto | 15 € |
| Alici fritte | 13 € |
| Insalata di mare | 10 € (antipasto) |
| Filetto di branzino o orata | 17 € |
| Paccheri con mazzancolle | 15 € |
| Spaghetti all'astice | 18 € |
| Menu fisso pesce (scoglio + frittura + acqua, vino, caffè) | 27-32 € |

- Un sito di recensioni indica a Mentana un pasto completo di pesce tra 25 e 40 € a persona, bevande incluse (dato non verificato da me, fonte di terzi).
- Il mio menu attuale (fritto misto 13 €, scoglio 13 €, insalata di mare 11 €) è già sotto i prezzi di sala. È una scelta commerciale valida per acquisire clienti, ma lascia margine da recuperare sui piatti "vetrina".

## 4. Il risotto alla crema di scampi (la tua idea)

- Una fonte di cucina romana scrive che è uno dei pochi risotti presenti quasi in ogni menu di Roma. In più menu di ristoranti del Lazio compare accanto a scoglio, vongole e fritto. È un piatto riconosciuto, quindi non va spiegato al cliente.
- Costo: gli scampi sono tra i prodotti più cari. Una fonte di settore indica per il pesce un food cost molto variabile (25-50%). Per questo il risotto di scampi è un piatto "vetrina": fa immagine e porta ordini, ma il margine in euro va calcolato con attenzione.
- Come si fa: fumetto di pesce + crema di scampi + riso (carnaroli o vialone nano), con gamberi saltati e prezzemolo sopra. La preparazione di fumetto e crema è la parte lunga, ma si fa in lotti.
- PROBLEMA IN DELIVERY: il risotto continua a cuocere nel contenitore e si scuoce. IPOTESI mia da provare: cuocerlo a circa tre quarti, consegnarlo e indicare di scaldarlo 1-2 minuti con un goccio d'acqua. Da testare con un assaggio dopo 20-30 minuti di trasporto prima di venderlo.
- Prezzo IPOTESI: 14 € (i primi di pesce nei menu trovati vanno da 10 a 18 €). Da confermare dopo il calcolo del costo scampi.

## 5. La logica del menu: piatti "ancora", "vetrina" e piatti per acquisire clienti

Da articoli di Italia a Tavola e di menu engineering:

- Piatti "ancora": costo della materia prima basso, margine percentuale alto. Pagano le spese. Per il pesce: frittura di calamari, baccalà fritto, insalata di mare con polpo, pasta con vongole.
- Piatti "vetrina": costo alto, margine percentuale basso ma margine in euro comunque buono, fanno immagine. Per il pesce: risotto crema di scampi, spaghetti all'astice, gamberi.
- Menu engineering (4 categorie): stelle (vendono molto e rendono molto), cavalli da tiro (vendono molto, rendono poco), enigmi (rendono molto, vendono poco), cani (né l'uno né l'altro). Si decide guardando le vendite reali dopo qualche settimana, non prima.
- Regola di una fonte: conta il margine in euro per piatto (prezzo meno costo del cibo), non solo la percentuale.
- Un piatto per ACQUISIRE clienti è economico, riconoscibile e facile da provare: il cliente lo ordina la prima volta senza rischio. Nel pesce: panino con frittura, cono di calamari fritti.

## 6. Proposta menu pesce a livelli (da inserire nel sito)

Già online (14/11/2026): calamari e gamberi fritti 12, fritto misto di mare 13, insalata di mare 11, polpo e patate 12, spaghetti allo scoglio 13, panino con frittura 8.

### A. Piatti per acquisire clienti (ingresso, prezzo basso)
- Panino con frittura (già online, 8 €).
- Cono di calamari fritti, porzione piccola. IPOTESI prezzo 7 €.
- Cono di alici fritte. IPOTESI prezzo 6 €.
- Descrizione tipo: "Croccante, caldo, pronto da mangiare con le mani."

### B. Piatti "ancora" (margine alto)
- Spaghetti alle vongole. IPOTESI 11 €.
- Filetti di baccalà fritti (già in lista idee). IPOTESI 10 €.
- Insalata di mare (già online).
- Pasta al tonno o al pesce spada (costo più basso degli scampi). IPOTESI 11 €.

### C. Piatti "vetrina" (immagine e margine in euro)
- Risotto alla crema di scampi. IPOTESI 14 € (vedi sezione 4).
- Spaghetti all'astice o ai gamberi rossi. IPOTESI 17-18 € (prezzo trovato nei menu: 18 €).
- Paccheri con mazzancolle. IPOTESI 14 € (prezzo trovato: 15 €).
- Gamberoni gratinati. IPOTESI 14 €.

### D. Box e combinazioni (per alzare lo scontrino)
- Box frittura per 2 persone (calamari, gamberi, alici, patatine). IPOTESI 22 €.
- Menu pesce per 1: primo di pesce + frittura piccola + acqua. IPOTESI 20 € (i menu fissi trovati in sala sono 27-32 € con vino e caffè).
- Cena a due: risotto di scampi + frittura + dolce. IPOTESI 38 €.

## 7. Tattiche per avere più clienti e più acquisti (dai consigli di Uber Eats, DoorDash, Cloud Kitchens)

- Foto buone per i piatti più venduti e più redditizi, con porzione e confezione visibili. Senza foto scadenti: meglio nessuna foto.
- Menu corto: solo piatti che reggono il trasporto e che vendono. Un menu breve riduce anche gli errori in cucina.
- Evidenziare i piatti redditizi con etichette tipo "Più ordinato" o "Consigliato dello chef" e metterli in alto.
- Upgrade e aggiunte al momento dell'ordine: "aggiungi patatine e bevanda", contorni, salse, dolce. Sono i suggerimenti che farebbe un cameriere.
- Combo e box: aumentano il valore dell'ordine.
- Sconto sul primo ordine o consegna gratis oltre una soglia: funzionano per provare, meglio se abbinati a piatti con margine alto.
- Il canale diretto (il tuo sito) evita la commissione delle piattaforme: è il vantaggio del tuo progetto.
- Descrizioni con parole sensoriali ("croccante", "cremoso"): una fonte di settore dice che aiutano a vendere.
- Rotazione stagionale: poche specialità fisse e circa metà del menu che cambia ogni stagione (consiglio di una guida di settore).

## 8. Attenzioni sul pesce prima di vendere

- Un articolo de Il Fatto Alimentare segnala che il fritto misto dei ristoranti spesso non è pescato del giorno ma semilavorato o surgelato. Se lo usi, scrivilo nel menu ("prodotto decongelato" dove serve): è obbligo di trasparenza e fa fiducia.
- Allergeni: pesce, crostacei e molluschi sono tra i 14 allergeni da indicare. Nei menu trovati online sono già riportati accanto ai piatti. Da aggiungere nelle descrizioni.
- Catena del freddo e HACCP sul pesce sono più delicati. Resta valido il dubbio già annotato: chiedere all'ASL del Comune se la cucina di casa (IAD) può vendere piatti caldi pronti con consegna.
- Il costo del pesce cambia con stagione e fornitore: ricalcolare i prezzi ogni volta che cambia il listino.
- Fonte non verificata: il range 25-50% di food cost per il pesce viene da un blog di software per ristoranti. Va sostituito con i tuoi costi.

## 9. Prossima passata: cosa inserire (in questo ordine)

1. Risotto alla crema di scampi (vetrina, 14 €) con foto.
2. Spaghetti alle vongole (ancora, 11 €).
3. Filetti di baccalà fritti (ancora, 10 €).
4. Cono di calamari fritti (ingresso, 7 €).
5. Box frittura per 2 (22 €).
6. Spaghetti all'astice o gamberi rossi (vetrina, 17-18 €).
7. Evidenziare "Più ordinato" e "Consigliato" sulla pagina Pesce.
8. Aggiungere contorni, salse e bevande come extra.

Prima di inserire: confermare i prezzi con i costi reali della pescheria. Dopo 3-4 settimane di ordini: classificare i piatti con il menu engineering (stelle, cavalli, enigmi, cani) e tenere solo quelli che rendono.

## 10. Fonti principali

- Classifiche: scattidigusto.it (Deliveroo e Just Eat), dissapore.com (Deliveroo 100), fortuneita.com e ladige.it (Just Eat), agi.it (Roma, marzo 2026).
- Menu e prezzi pesce: menu PDF di ristoranti pubblicati su cdn.website.dish.co, sluurpy.it (Mentana), memoriediangelina.com (risotto di scampi a Roma).
- Menu engineering e food cost: italiaatavola.net (2026), qamarero.com, beancount.io.
- Delivery: merchants.doordash.com, merchants.ubereats.com, cloudkitchens.com, upmenu.com.
- Fritto misto: ilfattoalimentare.it.

---

# PARTE 2 - Ricerca per categoria (14/11/2026, seconda passata)

## 11. Nota: "menu romano" NON è una categoria
Nella sezione 4 ho scritto che il risotto di scampi è "presente in quasi ogni menu di Roma". Era solo la fonte che dice che il piatto è conosciuto. Non ho creato nessuna categoria "romano" sul sito.
Però i dati dicono che i piatti della tradizione romana vendono molto in delivery (supplì al primo posto, poi amatriciana, carbonara, pinsa romana, gricia). Per questo più sotto propongo "Cucina romana" come categoria OPZIONALE da decidere insieme.

## 12. Cosa ho trovato in più in questa passata
- Alcune pagine di menu sulle app (Glovo) sono leggibili da internet: ho usato prezzi reali di piadinerie, burger, kebab, poke, polleria. Sono prezzi di città diverse (Roma, Milano, Padova ecc.).
- Sushi: nel 2025 in Italia sono stati ordinati oltre 714 mila kg, il 8,71% degli ordini, spesa media 46,37 € per ordine, Roma prima città (Just Eat, giugno 2026). È una categoria grande che non abbiamo (vedi sezione 25).
- Carbonara: per Just Eat i piatti "alla carbonara" più ordinati sono supplì alla carbonara, carbonara burger, mezze maniche alla carbonara (2023).
- Pizza (Deliveroo): top 10 gusti = margherita, diavola, capricciosa, marinara, bufala, Napoli, wurstel e patatine, 4 formaggi, salsiccia, ortolana.
- Cheeseburger (Just Eat): classico, bacon, double, triplo, egg bacon. Gli abbinamenti più ordinati sono patatine, anelli di cipolla, alette di pollo.
- Tiramisù (Just Eat): dolce più ordinato, oltre 27 mila kg nel 2022. Gusti: classico, pistacchio, caffè, Nutella, fragola, Oreo, Nutella e banana, Pan di Stelle.
- Piadine: la più venduta in Italia è crudo, squacquerone e rucola; circa 1 piadina su 5 è con il pollo (La Piadineria, 2026).
- Prezzi mia ipotesi sono sempre segnati IPOTESI: vanno confermati con i tuoi costi.

## 13. PIZZA (id: pizza)
Già online: Pizza Margherita, Pizza Diavola, Pizza al taglio.
Dati: i gusti più ordinati sono margherita, diavola, capricciosa, marinara, bufala, Napoli, wurstel e patatine (amata dai bambini), 4 formaggi, salsiccia, ortolana. Prezzi trovati nei menu: margherita 7 €, diavola 8-9 €, capricciosa 9-10 €, bufalina 10 €, 4 formaggi 10 €, americana 8-9 €, ortolana 8 €.
Da aggiungere (IPOTESI prezzo):
- Pizza Marinara - 6,00
- Pizza Napoli (alici) - 8,00
- Pizza Capricciosa - 9,50
- Pizza Wurstel e patatine - 9,00
- Pizza Quattro formaggi - 9,50
- Pizza Salsiccia - 9,00
- Pizza Ortolana - 8,50
- Pizza Bufala - 10,00
- Calzone - 8,50
Civetta (ingresso): Marinara a 6 €.

## 14. PIADINE E WRAP (id: piadine-wrap)
Già online: Piadina crudo e squacquerone, Piadina pollo e verdure, Wrap tonno e insalata.
Dati: la piadina è prima in Italia nella classifica Deliveroo 100 (2025). La più venduta è crudo, squacquerone e rucola; circa 1 su 5 è con il pollo. Le combo (piadina + insalatina + bibita) servono a un prezzo più accessibile. Prezzi trovati: crudo e squacquerone 8,20 €, con stracciatella e datterini 9,40 €, rotolo 9,70 €.
Da aggiungere (IPOTESI prezzo):
- Piadina crudo, stracciatella e pomodorini gialli - 8,50
- Piadina pollo, maionese, lattuga e patate arrosto - 8,00
- Piadina pollo piccante (paprika) - 8,00
- Piadina salsiccia e cipolla - 7,50
- Piadina hummus e zucchine grigliate - 7,50
- Piadina alici, misticanza e cipolla - 7,50
- Rotolo crudo, squacquerone e rucola - 9,00
- Piadina alla Nutella - 4,50
- Menu piadina + insalatina + bibita - 12,00
- Menu bimbi (piadina piccola + bibita) - 6,00
Civetta: Piadina alla Nutella a 4,50 €.

## 15. PRIMI DA FORNO (id: primi-forno)
Già online: Lasagne alla bolognese, Pasta al forno, Cannelloni ricotta e spinaci.
Dati: la pasta è tra i primi 4 piatti più ordinati su Deliveroo; a Bologna la preferenza va alle tagliatelle al ragù; una rosticceria milanese ha in menu parmigiana di melanzane (15 € in sala), cannelloni, lasagna alla bolognese (15 €).
Da aggiungere (IPOTESI prezzo):
- Parmigiana di melanzane - 9,00
- Gnocchi alla sorrentina (al forno) - 8,50
- Lasagna al pesto - 8,50
- Lasagne vegetariane (verdure e besciamella) - 8,00
- Lasagne formato famiglia (2-3 persone) - 18,00
Le carbonare e le amatriciane sono nella categoria romana (sezione 24).

## 16. HAMBURGER (id: hamburger)
Già online: Hamburger classico, Hamburger bacon, Patatine fritte.
Dati: i tipi più ordinati sono hamburger classico, cheeseburger, "componi il tuo hamburger", bacon burger, chicken burger. Cheeseburger più ordinati: classico, bacon, double, triplo, egg bacon. Gli abbinamenti più ordinati sono patatine, anelli di cipolla e alette di pollo. Prezzi trovati: burger 9-13 € (Milano), 9,70 € bacon cheese, combo panino + patatine + bibita 13-15,60 € (San Benedetto), menu con sconto 14,70 €.
Da aggiungere (IPOTESI prezzo):
- Cheeseburger - 8,50
- Double cheeseburger - 11,00
- Egg bacon cheeseburger - 10,00
- Crispy chicken burger - 8,50
- Burger BBQ (bacon e cipolla fritta) - 10,00
- Burger veggie - 9,00
- Componi il tuo hamburger - 9,00 (extra a pagamento)
- Carbonara burger - 10,00
- Anelli di cipolla - 4,50
- Menu burger (panino + patatine + bibita) - 13,00
Civetta: Menu burger a 13 € e anelli di cipolla come aggiunta.

## 17. POLLO E ROSTICCERIA (id: pollo-rosticceria)
Già online: Pollo arrosto intero, Mezzo pollo con patate, Cosce di pollo al forno.
Dati: il pollo è tra i primi 4 piatti per Deliveroo; la cotoletta di pollo è il piatto preferito della cucina italiana su Just Eat. Prezzi trovati: mezzo pollo arrosto 10,90 €, pollo intero con patate 18,99 €, coscia con patate 7-8 €, cotoletta di pollo con patate 11,50-14,90 €, alette 5 pz 6,93-9,90 €, nuggets 6,40 €, patate al forno 4-5 €, box 10 alette con patatine e bibita 12,99 €.
Da aggiungere (IPOTESI prezzo):
- Cotoletta di pollo con patate al forno - 11,00
- Alette di pollo (5 pz) - 7,50
- Box alette (10 pz) con patatine e salse - 14,00
- Nuggets di pollo (6 pz) - 6,00
- Coscia di pollo con patate - 7,50
- Patate al forno (porzione) - 4,00
- Wrap di pollo - 7,00
Civetta: Alette 5 pz a 7,50 €.

## 18. FRITTI E STREET FOOD (id: fritti)
Già online: Supplì al telefono, Arancini siciliani, Fritto misto.
Dati: nella classifica nazionale Just Eat compaiono patatine fritte, supplì, olive ascolane, crocchette di patate; il supplì è primo tra i piatti romani su Deliveroo; i supplì alla carbonara sono la variante alla carbonara più ordinata. Prezzi trovati: patatine 4,50 €, patatine con bacon e cheddar 8 €, mozzarella sticks 5,99 €, falafel 4 pz 5 €, panelle 5 €, fiori di zucca 2 € l'uno, crocchette di patate 6-7 € (rosticceria).
Da aggiungere (IPOTESI prezzo):
- Supplì alla carbonara - 2,50
- Olive ascolane (8 pz) - 6,00
- Crocchette di patate (6 pz) - 5,00
- Mozzarella sticks (6 pz) - 5,50
- Fiori di zucca e alici (2 pz) - 4,50
- Panelle (porzione) - 4,50
- Patatine fritte grandi - 4,50
- Patatine con bacon e cheddar - 7,00
Civetta: Supplì alla carbonara a 2,50 € (prodotto virale, facile da provare).
Attenzione: i fritti arrivano molli se l'imballo non traspira (già annotato).

## 19. CUCINA ASIATICA (id: asiatico)
Già online: Gyoza di maiale (6 pz), Noodles al pollo, Bao al maiale.
Dati: il cinese è tra le prime 4-5 cucine più ordinate in Italia con tre classici: involtini primavera, riso alla cantonese, ravioli alla griglia. Altri piatti in classifica: spaghetti di soia, nuvolette di gamberi, tartare di salmone. Per la cucina thailandese i più ordinati sono pad thai, riso thai, pollo satay. Il ramen è cresciuto del 295% su Glovo (2021). In una grande città, 46 mila porzioni di involtini primavera e 42 mila di gyoza ordinate con il sushi in un anno (Just Eat 2024).
Da aggiungere (IPOTESI prezzo):
- Involtini primavera (4 pz) - 5,00
- Riso alla cantonese - 6,00
- Ravioli al vapore di gamberi (6 pz) - 6,50
- Spaghetti di soia con verdure - 6,00
- Nuvolette di gamberi - 4,50
- Pad thai - 9,00
- Pollo satay con riso - 9,50
- Ramen (brodo in vasetto separato) - 11,00 (da testare in trasporto)
Civetta: Involtini primavera a 5 €.

## 20. KEBAB (id: kebab)
Già online: Kebab in piadina, Kebab nel panino, Kebab box con patatine.
Dati: il panino kebab è tra i piatti più ordinati a livello nazionale (Just Eat); a Bari spingono falafel, kebab e patatine. Prezzi trovati a Roma e altre città: piatto kebab 9-10,50 €, panino kebab 6-8,50 €, piadina kebab 8,50-8,90 €, piadina falafel 7,50-8 €, piatto falafel 6 pz 7,90 €, menu kebab + patatine + bibita circa 9,50 €, menu con 2 sambusa 16-19 €, menu con baklava 12 €.
Da aggiungere (IPOTESI prezzo):
- Piatto kebab (carne, patate, insalata) - 9,00
- Piadina falafel - 7,50
- Piatto falafel (6 pz) - 7,50
- Menu kebab + patatine + bibita - 10,00
- Menu famiglia (2 kebab + patatine + 2 bibite) - 19,00
- Piatto riso basmati con kebab - 8,00
- Hummus - 4,00
- Baklava (3 pz) - 4,00
Civetta: Menu kebab + patatine + bibita a 10 €.

## 21. PRANZO DA LAVORO (id: pranzo-ufficio)
Già online: Menu ufficio, Insalatona completa, Piatto del giorno.
Dati: i clienti del pranzo sono in gran parte impiegati; le formule (piatto + insalata + bibita) vengono proposte a prezzo accessibile (La Piadineria); una rosticceria milanese ha come piatti amati dai clienti abituali il vitello tonnato e il pollo allo spiedo con patate. Prezzi trovati: Caesar salad con pollo 11,90 €, cotoletta con patate 13,50 € (sala).
Da aggiungere (IPOTESI prezzo):
- Cotoletta di pollo con patate - 10,50
- Pollo arrosto e patate (monoporzione) - 9,50
- Caesar salad con pollo - 9,50
- Vitello tonnato - 9,00
- Parmigiana di melanzane (monoporzione) - 8,50
- Abbonamento 5 pranzi (una settimana) - 45,00
Civetta: abbonamento settimanale (ordini ricorrenti, meno spreco).

## 22. BOWL E POKE (id: bowl-poke)
Già online: Poke al salmone, Bowl pollo e verdure, Bowl vegetariana.
Dati: il poke al salmone è il piatto più ordinato in Italia su Deliveroo e il più ordinato a Roma; è anche il piatto degli studenti di ingegneria. Prezzi trovati: poke "crea la tua" S 10,90 €, M 11,90 €, L 14,90 €; spicy tuna 11,90 €; chicken teriyaki 10,90 €; hummus e avocado 10,90 €; gamberi e mango 13,50 €; caesar 11,90 €; poke con pesce cotto in panatura 8,90 €; contorni (edamame, patate dolci al rosmarino, hummus e ceci) 3,90 €; 2 mochi 4 €; smoothie 6,90 €.
Da aggiungere (IPOTESI prezzo):
- Poke tonno piccante - 11,90
- Poke pollo teriyaki - 10,50
- Poke con pesce cotto in panatura - 10,00
- Poke gamberi e mango - 13,00
- Poke hummus e avocado - 10,00
- Crea la tua poke (piccola 10,90 / media 12,90 / grande 14,90)
- Caesar salad bowl - 11,00
- Contorni: edamame, patate dolci al rosmarino, hummus e ceci - 3,90 ciascuno
- Mochi (2 pz) - 4,00
Attenzione: il pesce crudo richiede abbattimento e controllo ASL (vedi sezione 8).

## 23. PASTA FRESCA E DOLCI (id: pasta-fresca, dolci)

### Pasta fresca
Già online: Ravioli ricotta e spinaci, Tortellini di carne, Tagliatelle all'uovo, Gnocchi di patate.
Dati: la carbonara è la prima ricetta di pasta preferita per 46% degli italiani (indagine AstraRicerche, 2026); le tagliatelle al ragù sono tra le più ordinate a Bologna; la pasta è nei primi 4 piatti Deliveroo.
Da aggiungere (IPOTESI prezzo):
- Tagliatelle al ragù (pasta + ragù) - 8,50
- Tortelloni ricotta e spinaci - 7,50
- Ragù (vasetto) - 4,50
- Sugo di pomodoro e basilico (vasetto) - 4,00

### Dolci
Già online: Tiramisù monoporzione, Panna cotta ai frutti di bosco, Crostata di marmellata, Cheesecake ai frutti di bosco.
Dati: il tiramisù è il dolce più ordinato (oltre 27 mila kg nel 2022). Gusti tiramisù: classico, pistacchio, caffè, Nutella, fragola, Oreo, Nutella e banana, Pan di Stelle. Top dolci al cioccolato: cornetto al cioccolato, cannolo siciliano, crepes, soufflé, gelato, torta al cioccolato, brownies, tiramisù, muffin, cheesecake al cioccolato; durante il lockdown tortino al cioccolato, cheesecake, salame al cioccolato.
Da aggiungere (IPOTESI prezzo):
- Tiramisù al pistacchio - 4,50
- Tiramisù al caffè - 4,50
- Tiramisù alla Nutella - 4,50
- Tiramisù alla fragola - 4,50
- Cannolo siciliano - 3,50
- Tortino al cioccolato cuore caldo - 5,00
- Brownies - 3,50
- Crepes alla Nutella - 5,00
- Salame al cioccolato - 3,50
- Torta al cioccolato (fetta) - 4,00
Civetta: Cannolo a 3,50 € e tiramisù gusti come aggiunta a ogni ordine.
Il gelato è il dolce con più crescita ma richiede freezer e catena del freddo: non lo propongo ora.

## 24. NUOVA CATEGORIA PROPOSTA: CUCINA ROMANA (id: romana) - DA DECIDERE
Dati: Deliveroo (Natale di Roma): supplì primo, poi amatriciana, carbonara, pinsa romana, pasta alla gricia; fuori Roma il supplì resta primo e il carciofo è il piatto romano più ordinato a livello nazionale. A Tor Bella Monaca (Roma est, vicina a noi) il podio è supplì, pizza margherita, pizza diavola (AGI, marzo 2026). Sky TG24: la carbonara è associata a Roma dal 94% degli italiani.
Prodotti (IPOTESI prezzo):
- Spaghetti alla carbonara - 9,00
- Rigatoni all'amatriciana - 8,50
- Mezze maniche alla gricia - 8,50
- Tonnarelli cacio e pepe - 8,50
- Pinsa romana (margherita) - 9,00
- Pizza-tasca ripiena di pollo alla cacciatora - 5,00 (NON chiamarla Trapizzino: è un marchio registrato)
- Carciofi alla romana - 6,00
- Filetti di baccalà fritti - 8,00
- Saltimbocca alla romana con patate - 12,00 (sala 20 €)
- Maritozzo con la panna - 3,50
Il supplì e il supplì alla carbonara restano in Fritti.
Attenzione: la carbonara in delivery si rapprende e perde cremosità: serve una prova di trasporto prima di venderla.

## 25. NUOVA CATEGORIA PROPOSTA: SUSHI (id: sushi) - RISCHIO ALTO, DA DECIDERE
Dati: nel 2025 oltre 714 mila kg ordinati, 8,71% degli ordini, spesa media 46,37 € per ordine, Roma prima città (Just Eat, giugno 2026). Nel 2024 gli ordini di sushi erano accompagnati da involtini primavera (46 mila porzioni), gyoza (42 mila), riso alla cantonese, spaghetti di soia, nuvolette di gamberi, tartare di salmone.
RISCHI: il pesce crudo richiede abbattimento a temperatura per uso crudo, tracciabilità e controllo sanitario: per una cucina di casa (IAD) può non essere permesso. Prima va chiesto all'ASL.
Versione a rischio più basso (pesce cotto o senza pesce), IPOTESI prezzo:
- Uramaki di gambero in tempura (8 pz) - 9,00
- Uramaki di pollo croccante (8 pz) - 8,00
- Uramaki di avocado e verdure (8 pz) - 7,00
- Hosomaki di cetriolo (6 pz) - 4,50
- Gyoza (in categoria Asiatica)
- Edamame - 3,90
Con abbattimento certificato si potrebbero aggiungere uramaki e nigiri di salmone.

## 26. Fonti della seconda passata
- Piatti romani e carbonara: dissapore.com e techprincess.it (Deliveroo), mixerplanet.com (Just Eat carbonara), tg24.sky.it (Carbonara Day 2026), agi.it (Roma, marzo 2026).
- Pizza: techprincess.it e tg24.sky.it (gusti), menu PDF di pizzerie su cdn.website.dish.co.
- Piadine: lasicilia.it, leccecronaca.it, riviera24.it (La Piadineria), pagine Glovo di piadinerie.
- Hamburger: mixerplanet.com (Just Eat e Glovo), pagine Glovo di burger (Monster Burger, Jackburger, Burgez).
- Asiatico e sushi: ladige.it, dissapore.com, italiaatavola.net, tgcom24.mediaset.it (Just Eat 2025-2026), macitynet.it (Glovo ramen).
- Kebab: pagine Glovo di kebab a Roma (Ciro Kebab, Al Bab, Kebab World, Casa del Kebab).
- Poke: scattidigusto.it (Roma), pagine Glovo di Poke House.
- Pollo e rosticceria: pagine Glovo (Pollo & Co, La Polleria, Chicken Master), menu PDF di una rosticceria milanese.
- Dolci: mixerplanet.com e dissapore.com (Just Eat tiramisù e cioccolato).
- Limiti: molti dati di classifica sono del 2017-2023; i prezzi sono di città diverse e non di Monterotondo.

## 27. CUCINA ROMANA - prezzi da menu veri di trattorie (terza passata, 14/11/2026)
Prezzi da SALA trovati online (non delivery), usati come riferimento. Fonti: scattidigusto.it (Romanè, Bianca Trattoria), menu PDF Eufrosino, travel365.it (costi medi).
| Piatto | Prezzo trovato in sala |
|---|---|
| Polpette di bollito | 10 € |
| Trippa alla romana | 9 € |
| Coda alla vaccinara | 12 € (Romanè), costo medio 18 € (travel365) |
| Carciofo alla giudia | 5 €, 7 € e 9 € (tre locali) |
| Saltimbocca alla romana | 15-16 € |
| Abbacchio allo scottadito | 15 € |
| Pollo alla cacciatora | 16 € |
| Melanzane fritte e al forno con fiordilatte | 13 € |
| Ricotta romana croccante con pomodori infornati | 9 € |
| Tenerina al cioccolato | 6 € |
| Maritozzo con la panna | 3,50 € (costo medio) |
| Primi romani (carbonara, amatriciana, gricia, cacio e pepe) | circa 12 € (costo medio) |
Stagione: i carciofi sono sul menu da dicembre ad aprile; picco marzo-maggio. Fuori stagione NON venderli.
Cosa regge il trasporto (IPOTESI mia, da provare): i piatti in umido e al forno (polpette al sugo, coda, trippa, abbacchio, melanzane) migliorano o restano uguali; i piatti "mantecati" (carbonara, cacio e pepe) e i fritti (carciofo alla giudia) peggiorano.
Da aggiungere alla categoria "Cucina romana" (IPOTESI prezzo, sala meno circa 20-30%):
- Polpette al sugo (4 pz) - 8,00
- Trippa alla romana - 8,00
- Coda alla vaccinara - 12,00
- Saltimbocca alla romana con patate - 12,00
- Abbacchio al forno con patate - 13,00
- Pollo alla cacciatora - 10,00
- Gnocchi alla romana (semolino, al forno) - 8,00
- Melanzane alla parmigiana romana - 9,00
- Porchetta in panino - 6,00
- Fiori di zucca ripieni (2 pz, stagione) - 4,50
- Carciofi alla romana (dic-apr) - 6,00
- Ricotta romana con pomodori infornati - 7,00
- Tenerina al cioccolato - 5,00
- Maritozzo con la panna - 3,50
Civetta: Maritozzo 3,50 € e Porchetta in panino 6 €. Piatto vetrina: Coda alla vaccinara (richiesta, margine in euro, regge il trasporto).

# PARTE 3 - Cucina italiana, contorni, bevande, controllo realismo (14/11/2026, terza passata)

## 28. Cosa manca al sito rispetto ai menu reali
Ho confrontato il sito con menu veri: pizzerie e trattorie su Glovo (Roma, Ladispoli, Empoli, Pisa, Grosseto, Ancona, Abbiategrasso), menu PDF di pizzerie e trattorie romane, menu di rosticcerie e osterie romane.
Risultato: TUTTI hanno tre blocchi che il nostro sito non ha: **Bevande** (quasi sempre con le **Birre** separate), **Contorni** e i **Secondi** (carne). Quasi tutte le pizzerie delivery hanno anche il "Menu Coca-Cola" (pizza + lattina). Senza bevande si perde l'aggiunta più facile all'ordine.
Categorie da creare alla prossima passata (id tra parentesi):
1. Cucina romana (romana): sez. 24 e 27.
2. Cucina italiana (italiana): secondi e classici non romani (sez. 29).
3. Contorni (contorni): sez. 30.
4. Bevande (bevande): reparto con 5 sottocategorie (sez. 31).
Come funziona lo shop: le categorie sono a DUE livelli, il reparto non ha genitore e le sottocategorie hanno il campo `genitore` (vedi CLAUDE.md, "Categorie a DUE LIVELLI"). Quindi Bevande > Acqua, Bibite e tè, Birre, Vini e bollicine, Amari. Non si può fare un terzo livello: rosso/bianco/bollicine si distinguono nel nome del prodotto.

## 29. CUCINA ITALIANA (id: italiana) - secondi e classici non romani
Perché: nei menu reali i secondi di carne (cotoletta, polpette, scaloppine, brasato) sono sempre presenti e da noi mancano. Prezzi trovati in sala (non delivery): cotoletta con patatine 12 € (un locale romano) e 20 € alla milanese (altro locale); cotoletta di pollo 12-16 €; polpette al sugo 12-16 € (6 pezzi 15 € su Glovo a Sassari); scaloppine di pollo al limone 16 €; brasato di guancia 14-18 €; ossobuco alla milanese 20 €; tagliata di manzo 20 €; coniglio alla cacciatora 15 €; zuppa pasta e fagioli 12 €; zuppa ortolana 10 €; parmigiana 9-11 €.
Da aggiungere (IPOTESI prezzo, circa 20-30% sotto la sala):
- Cotoletta alla milanese con patatine - 11,00
- Scaloppine di pollo al limone - 10,00
- Brasato di manzo - 13,00
- Ossobuco alla milanese (stagione fredda) - 16,00
- Tagliata di manzo con rucola e grana - 15,00
- Coniglio alla cacciatora - 11,00
- Zuppa di pasta e fagioli - 7,00
- Zuppa ortolana - 6,00
Già coperti altrove: cotoletta di pollo (sez. 17 e 21), parmigiana (sez. 15), vitello tonnato (sez. 21).
Stufati e zuppe reggono bene il trasporto (IPOTESI da provare). Il fritto no.

## 30. CONTORNI (id: contorni)
Prezzi trovati in sala (sono cifre molto diverse da locale a locale): patate al forno 4,50-8 € (il più comune 5 €); cicoria ripassata 5-8 €; verdure grigliate 5-10 €; insalata mista 5-7 €; fagioli all'uccelletto 6,50 €; broccoletti e friarelli 6-7 €; scarola alla romana 7 €; puntarelle 10 € (un locale); patatine fritte 4-6,50 €.
Da aggiungere (IPOTESI prezzo, vicino al basso della fascia):
- Patate al forno - 5,00
- Cicoria ripassata - 5,00
- Verdure di stagione grigliate - 5,50
- Insalata mista - 4,50
- Fagioli all'uccelletto - 5,50
- Broccoletti ripassati - 5,50
- Scarola alla romana - 6,00
- Puntarelle alla romana (stagionali) - 7,00
Uso: aggiunta a ogni piatto di carne e pesce ("Aggiungi un contorno"). Le patatine fritte sono già in Hamburger.

## 31. BEVANDE (id: bevande) - reparto con 5 sottocategorie
Prezzi reali trovati (menu delivery su Glovo e menu di locali, 2025-2026). Prima di leggerli: i prezzi di sala sono spesso più alti di quelli delivery, e variano molto da città a città.
| Prodotto | Prezzi reali trovati |
|---|---|
| Coca-Cola lattina 33 cl | 2 € (Roma), 3 €, 4 € (Empoli, Desenzano) |
| Coca-Cola vetro 33 cl | 2,50-3,50 € |
| Coca-Cola 1,5 l | 4-4,50 € |
| Coca-Cola 1 l vetro | 5-6 € |
| Fanta, Sprite, tè in lattina o vetro 33 cl | 2,50-3 € |
| Estathé 25-33 cl | 2,50-3,50 € |
| Lurisia (aranciata, limonata, chinotto) 27,5 cl | 4 € (un locale) |
| Acqua 50 cl | 1-1,80 € |
| Acqua 75 cl | 2-3 € |
| Birra 33 cl (Peroni, Moretti, Heineken) | 2-3,50 € |
| Birra 66 cl (Peroni, Moretti) | 3,50-4,80 € |
| Birre speciali 33 cl (Ichnusa, Corona, Messina, Menabrea) | 3-5 € |
| Birra senza glutine 33 cl | 3,50-5 € |
| Vino della casa, bottiglia 75 cl | 10-13 € |
| Vino della casa, 1/2 litro | 5-8 € |
| Vino della casa, calice | 2,80-4 € |
| Prosecco, bottiglia | 10-12 € |
| Spumante dolce o secco, bottiglia | 12 € |
| Vini DOC (Valcalepio, Chianti, Pietraia) | 12-18 € |
| Amari e liquori | 2,50-4 € |
| Caffè | 1-2 € |
Fonti: pagine Glovo (L'officina della pizza di Roma, Antica Pizzeria di Ladispoli, 53 Pasta Pizza, Pizza Delivery, Fanta Pizza, La Farina, Alice Pizza) e menu PDF di locali pubblicati online. I prezzi dei vini del Lazio in vendita online non li ho trovati: quelli sotto sono IPOTESI da confermare con il fornitore.

### 31.1 Acqua (sottocategoria: acqua)
- Acqua naturale 50 cl - 1,20
- Acqua frizzante 50 cl - 1,20
- Acqua 75 cl in vetro - 2,50

### 31.2 Bibite e tè (sottocategoria: bibite)
- Coca-Cola lattina 33 cl - 2,50
- Coca-Cola Zero lattina 33 cl - 2,50
- Fanta lattina 33 cl - 2,50
- Sprite lattina 33 cl - 2,50
- Estathé limone 33 cl - 2,50
- Estathé pesca 33 cl - 2,50
- Coca-Cola 1,5 l - 4,50
- Aranciata Lurisia 27,5 cl - 3,50
- Limonata Lurisia 27,5 cl - 3,50
- Chinotto Lurisia 27,5 cl - 3,50
Nomi di marchi: sono prodotti di terzi che si rivendono, ma foto e nomi vanno usati con cura (niente loghi nelle foto generate: già regola del flusso foto).

### 31.3 Birre (sottocategoria: birre)
- Peroni 33 cl - 2,50
- Moretti 33 cl - 2,50
- Heineken 33 cl - 3,00
- Ichnusa 33 cl - 3,00
- Peroni 66 cl - 4,50
- Moretti 66 cl - 4,50
- Peroni senza glutine 33 cl - 3,50
- Birra analcolica 33 cl - 3,00
Prodotti con alcol: vedi sez. 32.

### 31.4 Vini e bollicine (sottocategoria: vini)
Struttura reale: i menu hanno "vino della casa" (rosso e bianco) più poche bottiglie DOC. I vini del Lazio sono l'asso del territorio: Frascati e Est! Est!! Est!!! (bianchi), Cesanese del Piglio (unico rosso DOCG del Lazio, dal 2008).
- Vino della casa rosso 75 cl - 10,00
- Vino della casa bianco 75 cl - 10,00
- Frascati DOC 75 cl - 14,00 (IPOTESI)
- Est! Est!! Est!!! di Montefiascone 75 cl - 12,00 (IPOTESI)
- Cesanese del Piglio 75 cl - 16,00 (IPOTESI)
- Chianti 75 cl - 18,00 (prezzo trovato in un menu)
- Prosecco 75 cl - 11,00
Non propongo il vino al calice o in caraffa: in consegna non ha senso (IPOTESI mia).

### 31.5 Amari e liquori (sottocategoria: amari) - OPZIONALE
- Limoncello - 3,00
- Amaro - 3,00
Caffè: NON lo propongo in delivery (arriva freddo). I menu lo mettono solo a tavola.

### 31.6 Combo con bevanda (aumentano lo scontrino)
Menu reali trovati: "Margherita + lattina Coca-Cola" 8,50 € (Abbiategrasso); "Margherita + Coca 45 cl" 8 € (Roma); "Capricciosa + Coca-Cola" 14 € (Desenzano, prezzi più alti). Per noi (IPOTESI):
- Menu pizza (margherita + bibita) - 9,00
- Menu burger: già 13,00
- Menu kebab: già 10,00
- Cena per due (2 pizze + 2 bibite + 1 dolce) - 24,00

## 32. ALCOLICI IN CONSEGNA: regole da sapere (da verificare col Comune)
Cosa ho trovato su siti e fonti pubbliche (non sono un legale e non ho verificato Mentana e Monterotondo):
- Vendita ai minori di 18 anni vietata (birra, vino, liquori, premiscelati). Se l'età non è evidente va chiesto un documento, e una frase del cliente non basta. In delivery vuol dire controllo al momento della consegna. Idea per il sito: spunta "ho 18 anni" al checkout (non sostituisce il controllo del documento).
- Per vendere alcolici al dettaglio e online serve la comunicazione alla Dogana (licenza UTF). Per bar, ristoranti e negozi spesso basta una comunicazione al SUAP del Comune dentro la SCIA. Fonti: money.it, partitaiva.it.
- Divieto nazionale di vendita di alcolici dalle 3 alle 6 (studiocataldi.it). Molti Comuni aggiungono ordinanze: in quelle che ho letto (altre città) il divieto di vendita per asporto dalle 22 alle 7 lasciava la consegna a domicilio permessa, ma ogni Comune decide: va letta l'ordinanza di Mentana e di Monterotondo.
- Cucina di casa (IAD): non ho trovato nulla che dica se può vendere alcolici. Da chiedere con la domanda all'ASL/SUAP (sez. 8). Senza licenza: solo bevande analcoliche. Si può lanciare Bevande prima con Acqua e Bibite e aggiungere Birre e Vini quando c'è l'ok.

## 33. CONTROLLO DI REALISMO: i prezzi del SITO contro i menu reali
Prezzi attuali sul sito (14/11/2026) confrontati con quelli trovati. Non li ho cambiati (decidi tu): sono solo segnalazioni.
| Prodotto sito | Prezzo sito | Trovato | Giudizio |
|---|---|---|---|
| Pizza margherita | 7,50 | in combo con bibita 8-8,50 | un po' alta: o 6,50-7 o il combo a 9 |
| Supplì al telefono | 2,50 | 1,50 a Roma (L'officina della pizza) | alto di circa 1 €: allineare a 2 o giustificare con la dimensione |
| Piadina crudo e squacquerone | 6,50 | 8,20 (La Piadineria) | bassa: 7,50-8 |
| Hamburger classico | 8,50 | 9-13 (Milano) | ok, nella fascia bassa |
| Pollo arrosto intero | 12,00 | 18,99 (con patate) | molto basso: 16-18 se con patate |
| Mezzo pollo con patate | 7,50 | 10,90 | basso: 9-10 |
| Cosce di pollo al forno | 6,50 | 7-8 con patate | ok |
| Lasagne alla bolognese | 8,50 | 15 in sala | ok per delivery |
| Kebab (panino, piadina) | 6,00 | 6-8,50 | ok |
| Poke al salmone | 11,00 | 10,90-11,90 | ok |
| Tiramisù monoporzione | 4,50 | prezzo reale non trovato | da verificare |
| Pesce (calamari e gamberi 12, fritto misto 13, scoglio 13) | 12-13 | in sala 13-15 | ok, sotto la sala |
Errore tecnico corretto oggi: i prezzi della categoria Pesce erano salvati 100 volte più alti (120000 centesimi, cioè 1.200 €, invece di 1.200 centesimi, cioè 12 €). Ora sono giusti (12, 13, 11, 12, 13 e 8 €). Il resto del catalogo era già a posto.
Regola di realismo per i prezzi nuovi: partire dal basso della fascia trovata, poi alzare dove la domanda lo regge (si vede dopo 3-4 settimane di ordini).

## 34. Dubbi che restano aperti (onestà sui limiti)
- I prezzi dei menu trovati sono di città e anni diversi (alcuni menu PDF non hanno data) e non di Monterotondo o Mentana.
- I menu delle app di consegna che ho letto sono pagine pubbliche di singoli locali, non l'elenco completo di nessuna app.
- Tutti i prezzi che propongo sono IPOTESI finché non ci sono i tuoi costi reali (materie prime, imballi, forno e tempo).
- Il costo del vino del Lazio, la regola dei Comuni e l'idoneità alla IAD non li ho verificati: sono domande da fare prima di vendere.

## 35. RESOCONTO FINALE: categorie e prodotti (14/11/2026)
ONLINE sul sito (13 categorie, 44 prodotti): Pizza (3), Piadine e wrap (3), Primi da forno (3), Hamburger (3), Pollo e rosticceria (3), Fritti e street food (3), Cucina asiatica (3), Kebab (3), Pranzo da lavoro (3), Bowl e poke (3), Pasta fresca (4), Dolci (4), Pesce (6).
DA CREARE (4 reparti nuovi): Cucina romana (circa 14 piatti, sez. 24 e 27), Cucina italiana (8, sez. 29), Contorni (8, sez. 30), Bevande (30 prodotti in 5 sottocategorie, sez. 31).
DA AGGIUNGERE nelle categorie che ci sono: circa 105 piatti (sez. 4-6 e 13-23).
Totale prodotti nuovi: circa 165. Totale dopo l'inserimento: circa 210.
Ordine consigliato di inserimento:
1. Civette (ingresso, prezzo basso): Marinara 6 €, Piadina alla Nutella 4,50 €, Supplì alla carbonara 2,50 €, Cannolo 3,50 €, Involtini primavera 5 €, Maritozzo 3,50 €, Acqua e Coca-Cola.
2. Bevande Acqua e Bibite (senza alcol: niente licenza alcolici; resta da chiedere se la IAD può rivenderle, sez. 8).
3. Contorni e Menu pizza + bibita (alzano lo scontrino).
4. Piatti vetrina: Coda alla vaccinara, Risotto di scampi, Poke gamberi e mango.
5. Cucina romana e Cucina italiana.
6. Birre e Vini SOLO dopo l'ok su licenza e Comune (sez. 32).
Quando si inseriscono: `automation/prodotto.py --lista` (foto Gemini, un solo commit), dopo aver creato le 4 categorie e le 5 sottocategorie in `_data/catalogo.json` (le categorie `prodotto.py` non le crea). Prezzi: confermare con i costi reali.
Fonti della terza passata: menu su glovoapp.com (pizzerie di varie città), menu PDF pubblicati su cdn.website.dish.co, pizzium.com, me-menu.com, scattidigusto.it, travel365.it, dinnersite.nl (osterie romane), restaurantguru.com, piatti.menu; regole: money.it, partitaiva.it, studiocataldi.it, arsial.it (vini del Lazio).
