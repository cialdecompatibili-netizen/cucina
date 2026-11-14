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
