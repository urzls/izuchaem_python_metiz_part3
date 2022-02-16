# from pygal_maps_world import i18n
from pygal.maps.world import COUNTRIES


# выводим код страны и ее название в принятом международном формате
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])

