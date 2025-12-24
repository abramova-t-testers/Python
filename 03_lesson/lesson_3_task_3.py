from address import Address
from mailing import Mailing

to_address = Address('196158', 'Санкт-Петербург', 'Московское шоссе', '32', '189')
from_address = Address('125009', 'Москва', 'Большая Никитская', '9', '12')
mailing = Mailing(to_address, from_address, 200, "письмо")

print(mailing)
