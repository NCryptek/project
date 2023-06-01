Po wpisaniu rozmiaru mapy oraz ilości jednostek na gracza można wybrać typy dla swoich jednostek.
Aby przełączać się pomiędzy poszczególnymi jednostkami używa się strzałek w górę i w dół, enterem przechodzi się do zmiany typu obecnie wybranej jednostki.
Podobnie jak w przypadku jednostek nawigacja odbywa się za pomocą strzałek, enterem zatwierdza się nowy typ obecnej jednostki.
Aby rozpoczać grę trzeba wybrać opcję "Kontynuuj" znajdującą się poniżej listy jednostek i zatwierdzić ją enterem.

W trakcie gry gracz może znajdować się w jednym z 4 trybów sterowania:
 - **Domyślny**, służy do wyświetlania informacji o swoich jednostkach i prostego wyboru jednej z nich za pomocą strzałek
 - **Ruch kamerą**, pozwala graczowi na bezpośrednią kontrolę nad kamerą, w tym trybie na planszy widoczny jest kursor, jeśli pod kursorem znajduje się jednostka to pod planszą wyświetlone zostaną jej dane
 - **Ruch jednostką**, służy do przemieszczania obecnie wybranej jednostki po planszy, pola przez które przejdzie jednostka zostaną podświetlone na żółto, zatwierdzić ruch można tylko jeśli pole docelowe jest w zasięgu ruchu jednostki i jest puste
 - **Atak jednostką**, służy do zaatakowania przeciwnika za pomocą wybranej jednostki, pola które są w zasięgu jednostki zostana podświetlone na żółto, a przeciwnicy którzy mogą być zaatakowani na jasnoniebiesko

W dowolnym momencie można przełączyć się pomiędzy poszczególnymi trybami sterowania za pomocą klawiszy C (ruch kamerą), M (ruch jednostką), A (atak jednostką).
W przypadku takiego przełączenia zachowana zostanie obecnie wybrana jednostka jak i pozycja kursora.
Klawisze 1-5 służą do szybkiego przełączania się pomiędzy poszczególnymi jednostkami bez powrotu do podstawowego trybu sterowania, w tym przypadku pozycja kursora nie jest zachowana, ale zachowany jest obecny tryb sterowania.

Gra zakończy się automatycznie w momencie gdy tylko jeden z graczy ma dalej żywe jednostki.

Każda jednostka jest charakteryzowana przez 6 atrybutów:
 - **Życie**, przedstawia obecne punkty życia jednostki, jeśli jest mniejsze lub równe 0 to oznacza to, że jednostka jest martwa
 - **Atak**, przedstawia wartość ataku jednostki, jest to podstawowa ilość obrażeń jaką otrzyma cel w przypadku ataku
 - **Zasięg**, przedstawia maksymalną odległość z jakiej jednostka może zaatakować cel
 - **Prędkość**, przedstawia ilość pól jaką może przemieścić się jednostka w trakcie jednej tury
 - **Typ broni**, przedstawia jaki rodzaj obrażen zostanie zadany celowi w przypadku ataku
 - **Typ pancerza**, przedstawia jaki rodzaj pancerza posiada jednostka

Typy broni:
 - SA - broń przeciwpiechotna,  100% efektywności przeciwko lekkiemu pancerzowi, 50% efektywności przeciwko ciężkiemu pancerzowi
 - HE - broń wybuchowa,         75% efektywności zarówno przeciwko lekkiemu i ciężkiemu pancerzowi
 - AT - broń przeciwpancerna,   50% efektywności przeciwko lekkiemu pancerzowi, 100% efektywności przeciwko ciężkiemu pancerzowi

Typy pancerza:
 - LK - lekki pancerz
 - CK - ciężki pancerz
 
W przypadku ataku obrażenia jakie otrzyma cel można otrzymać poprzez pomnożenie wartości Ataku atakującego przez efektywność Typu broni atakującego względem Typu pancerza broniącego.
Jeśli jednostka będąca celem ataku przeżyje go i jednostka atakująca jest w jej zasięgu to wykonany zostanie atak odwetowy, którego efektywność wynosi tylko 50%.
