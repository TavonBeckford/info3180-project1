from . import db

class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    propertytitle = db.Column(db.String(80))
    description = db.Column(db.String(1000))
    noofrooms = db.Column(db.String(20))
    noofbathrooms = db.Column(db.String(20))
    price = db.Column(db.String(200))
    propertytype = db.Column(db.String(80))
    location = db.Column(db.String(200))
    photo = db.Column(db.String(200))

    def __init__(self, propertytitle, description, noofrooms, noofbathrooms, price, propertytype, location, photo):
        self.propertytitle = propertytitle
        self.description = description
        self.noofrooms = noofrooms
        self.noofbathrooms = noofbathrooms
        self.price = price
        self.propertytype = propertytype
        self.location = location
        self.photo = photo

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
