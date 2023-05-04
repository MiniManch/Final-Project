from app import db

#
# class Card(db.Model):
#     populate = False
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     image = db.Column(db.String(200))
#     type  = db.Column(db.String(100))
#     name = db.Column(db.String(100))
#     ability = db.Column(db.String(100))
#     attack = db.Column(db.Integer)
#     health = db.Column(db.Integer)
#     rarity = db.Column(db.Integer)
#     price = db.Column(db.Integer)
#     transaction = db.relationship('Transaction', backref='card-to-trade',uselist=False)


class Guide(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    author = db.Column(db.Integer,db.ForeignKey('user.id'))
    subject = db.Column(db.String(100))
    content = db.Column(db.String(200))
    comments = db.relationship('Comment', backref='post')


class Comment(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    subject = db.Column(db.String(50))
    content = db.Column(db.String(200))
    thread =  db.Column(db.Integer, db.ForeignKey('post.id'))

# each transaction can have, a card, an offer and cash offer.
# who posted the transaction, user_id foreign key
# offer- offer model, can be coin or can be another card and a coin
# accepted bool
