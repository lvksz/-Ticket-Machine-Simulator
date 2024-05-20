# Ticket Machine Simulator
***
## Etap I

- **Wstępny opis działania programu**

    Symulator automatu biletowego jest aplikacją zaprojektowaną do naśladowania funkcjonalności rzeczywistego automatu 
    biletowego. Symulator oferuje szereg funkcji, odzwierciedlających te dostepne w fizycznych automatach biletowych:
  - wybór rodzaju biletu
  - wybór sterfy biletowej
  - określenie liczby biletów
  - wybór metody płatności
  - generowanie i drukowanie biletu


- **Analiza MoSCoW**
  - Must:
  
    funkcjonalności w obrębie zarządzania biletami, responsywność interefejsu użytkownika
  - Should:
  
    dostępność kilku wersji językowych apliakcji, możliwość dostosowania motywu interfejsu użytkownika 
  - Could:

    interaktywna instrukcja obsługi biletomatu
  - Won't:

    możliwość zakupu biletu miesięcznego 


- **Diagram przypadków użycia**<br>
        
```mermaid
graph LR
    
    Plb(Przeglądanie list biletów)
    Zlz(Zarządzanie listą zakupów)
    Db(Dodanie biletu)
    Ub(Usunięcie biletu)
    Wmp(Wybór metody płatności)
    Wtu(Wybór typu ulgi)
    Wtb(Wybór typu biletu)
    
    Użytkownik---Plb
    Plb---Zlz
    Zlz---Db
    Zlz---Wmp
    Zlz---Ub
    Wtu -.->|include|Db
    Wtb-.->|include|Db
    subgraph Symulator automatu biletowego
        Plb
        Zlz
        Wmp
        Ub
        Db
        Wtb
        Wtu
    end
```
**Przeglądanie listy biletów:**
<br>
**Aktor:** Użytkownik<br>
**Opis:** Użytkownik przegląda dostępne bilety w automacie.<br>
**Wyzwalacz:** Użytkownik znajduje się na ekranie głównym.<br>
**Przepływ zdarzeń:**<br>
1. System wyświetla listę dostępnych biletów.<br>

**Dodanie biletu:**
<br>
**Aktor:** Użytkownik<br>
**Opis:** Użytkownik dokonuje wyboru biletu do zakupu.<br>
**Wyzwalacz:** Użytkownik znajduje się na ekranie głównym.<br>
**Przepływ zdarzeń:**<br>
1. Użytkownik wybiera typ biletu.<br>
2. Użytkownik wybiera typ ulgi.<br>
3. Użytkownik potwierdza wybór.<br>

**Wybór typu biletu:**
<br>
**Aktor:** Użytkownik<br>
**Opis:** Użytkownik wybiera typ biletu z listy dostępnych opcji.<br>
**Wyzwalacz:** Użytkownik znajduje się na ekranie głównym.<br>
**Przepływ zdarzeń:**<br>
1. Użytkownik naciska na listę rozwijaną z typami biletów.<br>
2. Użytkownik wybiera pożądany typ biletu.<br>

**Wybór typu ulgi:**
<br>
**Aktor:** Użytkownik<br>
**Opis:** Użytkownik wybiera rodzaj ulgi, jeśli kupuje bilet ulgowy.<br>
**Wyzwalacz:** Użytkownik znajduje się na ekranie głównym.<br>
**Przepływ zdarzeń:**<br>
1. Użytkownik wybiera opcję wyboru ulgi.<br>
2. System prezentuje różne dostępne ulgi w formie listy rozwijanej.<br>
3. Użytkownik wybiera odpowiednią ulgę.<br>

**Usunięcie biletu:**
<br>
**Aktor:** Użytkownik<br>
**Opis:** Użytkownik usuwa wybrany bilet z listy.<br>
**Wyzwalacz:** Użytkownik znajduje się na ekranie głównym i posiada minimum jeden bilet w koszyku.<br>
**Przepływ zdarzeń:**<br>
1. Użytkownik wybiera bilet z listy zakupów.<br>
2. Użytkownik wybiera opcję usunięcia biletu.<br>
3. System usuwa bilet z listy.<br>

**Wybór metody płatności:**
<br>
**Aktor:** Użytkownik<br>
**Opis:** Użytkownik wybiera metodę płatności za bilet.<br>
**Wyzwalacz:** Użytkownik znajduje się na ekranie głównym.<br>
**Przepływ zdarzeń:**
1. Użytkownik wybiera preferowaną metodę płatności (np. gotówka, karta, płatność mobilna).
2. System przetwarza płatność i wydaje bilet.

**Wymagania funkcjonalnie i niefunkcjonalne**<br>
    Wymagania funkcjonalne:
  - Dodawanie biletów do koszyka: Użytkownik może dodawać nowe bilety do koszyka
  - Edytowanie ilości biletów w koszyku: Użytkownik może edytować bilety w swoim koszyku
  - Usuwanie biletów z koszyka: Użytkownik może usuwać bilety z koszyka
  - Przeglądanie dostępnych typów biletu (czasowy, typ ulgi): Użytkownik może wybierać pożądany typ biletu oraz rodzaj ulgi
  - Wybór metody płatności: Użytkownik może wybrać którą z metod płatności chce użyć, aby opłacić należną sumę
    <br><br>
    Wymagania niefukcjonalne:
  - Wydajność: Aplikacja powinna działać płynnie nawet przy dużej ilości biletów.
  - Interfejs użytkownika: Interfejs powinien być intuicyjny, łatwy w nawigacji i estetyczny
  - Elastyczna płatność: Biletomat powinien obsługiwać różne metody płatności, takie jak karta płatnicza, karta zbliżeniowa, gotówka, płatności zbliżeniowe.
  - Responsywność: Aplikacja powinna reagować bez opóźnień na interakcje użytkownika
 

- **Wybranie systemu kontroli wersji oraz platformy hosting dla niej, utworzenie repozytorium**

    Jako system kontroli wersji wybrano Git, platformą hostingową jest GitHub.
    Projekt został zainicjalizowany na platformie.
    ![Inicjalizacja repozytorium](ReadmeAssets/EtapI/github-repo.png)


- **Raport ze stosowania metodologii programowania zwinnego**

    W trakcie realizacji projektu zadania będą realizowane w sprintach. W Jira utworzony został zespół, 
    wydzielone zadania i przydzielone dla każdego członka zespołu.
    ![Screenshot tablicy Jira](ReadmeAssets/EtapI/img_5.png)

****
## Etap 2
- **Przygotowanie koncepcji wizualnej programu**

  ![koncepcja wizualna programu](ReadmeAssets/EtapII/figma_1.png)
  
  ![koncepcja wizualna programu](ReadmeAssets/EtapII/figma_2.png)
