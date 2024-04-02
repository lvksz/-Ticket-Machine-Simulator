# Ticket Machine Simulator
<details>
<summary>Etap I</summary>
<ul style="font-size:larger;">

<li>
    <span style="font-size:22px;">Wstępny opis działania programu</span><br>
    Symulator automatu biletowego jest aplikacją zaprojektowaną do naśladowania funkcjonalności rzeczywistego automatu 
    biletowego. Symulator oferuje szereg funkcji, odzwierciedlających te dostepne w fizycznych automatach biletowych:
    <ul>
        <li>
        wybór rodzaju biletu
        </li>
        <li>
        wybór sterfy biletowej
        </li>
        <li>
        określenie liczby biletów
        </li>
        <li>
        wybór metody płatności
        </li>
        <li>
        generowanie i drukowanie biletu
        </li>
    </ul>

</li>

<li>
    <span style="font-size:22px;">Analiza MoSCoW</span>
    <ul>
        <li>
            Must:<br> funkcjonalnośći w obrębie zarządzania biletami, responsywność interefejsu użytkownika
        </li>
        <li>
            Should:<br> dostępność kilku wersji językowych apliakcji, możliwośc dostosowania motywu interfejsu użytkownika 
        </li>
        <li>
            Could:<br> interaktywna instrukcja obsługi biletomatu
        </li>
        <li>
            Wont:<br> możliwość zakupu biletu miesięcznego 
        </li>
    </ul>
</li>

<li>
    <span style="font-size:22px;">Diagram przypadków użycia.</span>

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

</li>

<li>
    <span style="font-size:22px;"> Wymagania funkcjonalne i niefunkcjonalne</span>
    </br><span> 
        Wymagania funkcjonalne 
    </span>
<ul>
<li>Dodawanie biletów do koszyka:</br>
Użytkownik może dodawać nowe bilety do koszyka</li>
<li>Edytowanie ilości biletów w koszyku:</br>
Użytkownik może edytować bilety w swoim koszyku</li>
<li>Usuwanie biletów z koszyka:</br>
Użytkownik może usuwać bilety z koszyka</li>
<li>Przeglądanie dostępnych typów biletu (czasowy, typ ulgi):</br>
Użytkownik może wybierać pożądany typ biletu oraz rodzaj ulgi</li>
<li>Wybór metody płatności:</br>
Użytkownik może wybrać którą z metod płatności chce użyć, aby opłacić należną sumę</li>

</ul>
<br><span>Wymagania niefunkcjonalne</span>
<ul>

<li>Wydajność:</br>
Aplikacja powinna działać płynnie nawet przy dużej ilości biletów.</li>
<li>Interfejs użytkownika:</br>
Interfejs powinien być intuicyjny, łatwy w nawigacji i estetyczny.</li>
<li>Elastyczna płatność:</br>
Biletomat powinien obsługiwać różne metody płatności, takie jak karta płatnicza, karta zbliżeniowa, gotówka, płatności zbliżeniowe.</li>
<li>Responsywność:</br>
Aplikacja powinna reagować bez opóźnień na interakcje użytkownika</li>

</ul>
</li>

<li>
    <span style="font-size:22px;">
    Wybranie systemu kontroli wersji oraz platformy hosting dla niej, utworzenie repozytorium
    </span>
    <span>
        Jako system kontroli wersji wybrano Git, platformą hostingową jest GitHub.
        Projekt został zainicjalizowany na platformie.
    </span>
    <img src="ReadmeAssets/EtapI/github-repo.png" alt="Inicjalizacja repozytorium" title="Inicjalizacja repozytorium"/>
</li>

<li>
    <span style="font-size:22px;">
    Raport ze stosowania metodologii programowania zwinnego.
    </span> <br>
    <span>
    W trakcie realizacji projektu zadania będą realizowane w sprintach. W Jira utworzony został zespół, 
    wydzielone zadania i przydzielone dla każdego członka zespołu.
    </span>
<img src="ReadmeAssets/EtapI/img_5.png" alt="Screenshot tablicy Jira" title="Screenshot tablicy Jira">
    
</li>
</ul>

</details>