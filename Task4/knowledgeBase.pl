%Facts
city('Makati').
city('Washington D.C').
city('Los Angeles').
city('Butuan').
city('New York').
city('Callao').
city('Alexandria'). 
city('Cairo'). 
city('Melbourne'). 
city('Barcelona').
city('Leiria').
city('Lisbon'). 
city('Cuzco'). 
city('Manila').

country('United States of America').
country('India').
country('Greece').
country('Philippines').
country('Egypt').
country('Spain').
country('Bolivia').
country('Peru').
country('Libya').
country('Portugal').
country('Australia').

in_country('Makati', 'Philippines').
in_country('Washington D.C.', 'United States of America').
in_country('Los Angeles', 'United States of America').
in_country('Butuan', 'Philippines').
in_country('New York', 'United States of America').
in_country('Callao', 'Peru').
in_country('Alexandria', 'Egypt').
in_country('Cairo', 'Egypt').
in_country('Melbourne', 'Australia').
in_country('Barcelona', 'Spain').
in_country('Leiria', 'Portugal').
in_country('Lisbon', 'Portugal').
in_country('Cuzco', 'Peru').
in_country('Manila', 'Philippines').

capital('Washington D.C.', 'United States of America').
capital('Lima', 'Peru').
capital('Canberra', 'Australia').
capital('Cairo', 'Egypt').
capital('Lisbon', 'Portugal').
capital('Madrid', 'Spain').
capital('Manila', 'Philippines').

continent('Libya', 'Africa').
continent('Portugal', 'Europe').
continent('India', 'Asia').
continent('Philippines', 'Asia').
continent('Peru', 'South America').
continent('United States of America', 'North America').
continent('Australia', 'Australia').
continent('Greece', 'Europe').
continent('Spain', 'Europe').
continent('Egypt', 'Africa').
continent('Bolivia', 'South America').

%Rules
is_capital(City, Country) :- capital(City, Country).

is_in_country(City, Country) :- in_country(City, Country).

city_continent(City, Continent) :-
    in_country(City, Country),
    continent(Country, Continent).

country_continent(Country, Continent) :- continent(Country, Continent).   