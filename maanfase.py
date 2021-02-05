from skyfield import api
from skyfield import almanac

efemeriden = api.load('de421.bsp')

timescale = api.load.timescale()

nu = timescale.now()

maanfase = almanac.moon_phase(efemeriden, nu)

print(nu.utc_strftime())
print(str(maanfase.degrees) + ' graden')
