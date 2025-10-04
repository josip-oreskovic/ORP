from pony.orm import *

db = Database()

class CompanyType(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    clients = Set('Client')

class CompanySize(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    clients = Set('Client')

class Client(db.Entity):
    id_client = PrimaryKey(int, auto=True)
    name = Required(str)
    id_company_type = Required(CompanyType)
    id_size = Required(CompanySize)
    address = Optional(str)
    city = Optional(str)
    post_number = Optional(str)
    country = Optional(str)
    tel = Optional(str)
    mob = Optional(str)
    email = Optional(str)
    fax = Optional(str)
    id_director = Optional(str)
    pin = Optional(str)
    vat_num = Optional(str)
    reg_numb = Optional(str)
    stat_num = Optional(str)
    activity_num = Optional(str)
    activity_desc = Optional(str)
    hzmo_num = Optional(str)
    hzzo_num = Optional(str)
    vat_period = Optional(str)
    employee_num = Optional(int)
    price = Optional(float)