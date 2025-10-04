# ORP - Organizator Računovodstvenih Poslova

**ORP - Organizator Računovodstvenih Poslova** je web aplikacija namijenjena računovodstvenim servisima za učinkovito upravljanje evidencijom klijenata, organizaciju računovodstvenih zadataka i praćenje zakonskih obveza. Aplikacija omogućuje unos bilješki, kreiranje zadataka za klijente te automatsko generiranje ponavljajućih zadataka na temelju vrste klijenta i njegovih specifičnih zakonskih obveza.

### **Vrste klijenata i specifične obveze**

Aplikacija podržava različite vrste klijenata u Hrvatskoj, uključujući:

- **Trgovačka društva (d.o.o., j.d.o.o.)**

  - Obveza podnošenja mjesečnih ili tromjesečnih PDV obrazaca (PDV, PDV-S) za obveznike PDV-a
  - Prijava financijskih izvještaja (GFI-POD) FINA-i
  - Predaja Obrasca JOPPD za obračun plaća, honorara i drugih isplata
  - Priprema godišnjeg financijskog izvještaja i porezne prijave (PD)

- **Obrtnici**

  - Vođenje knjiga prema sustavu poreza na dohodak (KPR, KPI, DI) ili poreza na dobit
  - Predaja Obrasca PO-SD za paušalne obrtnike
  - Obračun PDV-a ako su u sustavu PDV-a
  - Izrada godišnjih financijskih izvještaja i prijava poreza na dohodak (DOH)

- **Udruge i neprofitne organizacije**

  - Vođenje dvojnog ili jednostavnog knjigovodstva ovisno o prihodima
  - Predaja financijskih izvještaja FINA-i i Poreznoj upravi
  - Obveza prijave donacija i izvještaja o financiranju iz javnih izvora

- **Slobodna zanimanja i fizičke osobe**
  - Obračun doprinosa i poreznih obveza prema paušalnom ili stvarnom dohotku
  - Predaja godišnje porezne prijave
  - Mogućnost izdavanja e-računa i praćenja naplate

### **Ključne funkcionalnosti**

✅ **Evidencija klijenata** – Pregled svih klijenata s ključnim podacima, zakonskim obvezama i statusom zadataka  
✅ **Kreiranje zadataka** – Ručno dodavanje zadataka i bilješki za pojedine klijente  
✅ **Automatski ponavljajući zadaci** – Generiranje zadataka temeljem vrste klijenta (npr. PDV obveznici, paušalni obrtnici, neprofitne organizacije) i zakonskih rokova  
✅ **Notifikacije i podsjetnici** – Obavijesti o nadolazećim rokovima kako bi računovođe mogle pravovremeno izvršiti obveze  
✅ **Praćenje statusa zadataka** – Pregled zadataka prema prioritetima, rokovima i odgovornim osobama

### **Prednosti korištenja ORP-a**

🔹 Povećava produktivnost računovodstvenih servisa kroz automatizaciju zadataka  
🔹 Smanjuje rizik od kašnjenja u predaji izvještaja i plaćanju poreznih obveza  
🔹 Olakšava organizaciju i komunikaciju unutar tima računovođa  
🔹 Omogućuje fleksibilno prilagođavanje zadataka prema potrebama klijenata

ORP je idealno rješenje za moderne računovodstvene servise koji žele optimizirati svoje poslovne procese i osigurati pravovremeno izvršavanje svih računovodstvenih obveza. 🚀

## Use Case Diagram

![ORP Use Case Diagram](ORP%20-%20Use%20Case.png)

## Instalacija

```
cd ~/Downloads
git clone https://github.com/josip-oreskovic/ORP
cd orp
```

```
docker build -t orp .
docker ps
docker run -p 5000:5000 orp
```
