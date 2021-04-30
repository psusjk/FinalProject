from . import db
from .table import Books, Author, Customer, Comments

# c1 = Customer(loginName='sumit1',
# 	password=generate_password_hash("password", method='sha256'),
# 	fullName="Sumit",
#     phoneNumber=5404495670,
#     address="1900 Lane Foxhunt"
#     )
# db.session.add(manager)
# db.session.commit()