from app import db

step_tool = db.Table(
	'step_tool',
	db.Column('step_id', db.Integer, db.ForeignKey('step.id')),
	db.Column('tool_id', db.Integer, db.ForeignKey('tool.id'))
)

class Guide(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    author = db.Column(db.Integer,db.ForeignKey('user.id'))
    subject = db.Column(db.String(100))
    content = db.Column(db.String(200))
    image   = db.Column(db.String(200))
    rating = db.Column(db.Float)
    num_of_ratings = db.Column(db.Integer)
    steps = db.relationship('Step', backref='its_guide')
    reviews = db.relationship('Rating', backref='ratings')
    accepted = db.Column(db.Boolean, nullable=False)
    category = db.Column(db.Integer,db.ForeignKey('category.id'))
    items   =  db.relationship('Item', backref='guide_fixed_with')


class Step(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    subject = db.Column(db.String(50))
    content = db.Column(db.String(200))
    image   = db.Column(db.String(100))
    guide =  db.Column(db.Integer, db.ForeignKey('guide.id'))
    tools = db.relationship('Tool', secondary=step_tool, back_populates='steps')
    accepted = db.Column(db.Boolean, nullable=False)


class Rating(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    author = db.Column(db.Integer,db.ForeignKey('user.id'))
    content = db.Column(db.String(200))
    rate    = db.Column(db.Integer)
    guide   = db.Column(db.Integer,db.ForeignKey('guide.id'))


class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(100))
    image   = db.Column(db.String(100))
    usage = db.Column(db.String(100))
    steps = db.relationship('Step', secondary=step_tool, back_populates='tools')
    accepted = db.Column(db.Boolean, nullable=False)


class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    image   = db.Column(db.String(200))
    guides = db.relationship('Guide', backref='its_category')


class Item(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    seller = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(200))
    description = db.Column(db.String(200))
    guide =  db.Column(db.Integer, db.ForeignKey('guide.id'))
    fixed = db.Column(db.Boolean)
    price = db.Column(db.Integer)
    sold  = db.Column(db.Boolean)
    image = db.Column(db.String(200))
