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
    steps = db.relationship('Step', backref='its_guide')
    accepted = db.Column(db.Boolean, nullable=False)


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
    subject = db.Column(db.String(100))
    content = db.Column(db.String(200))
    rate    = db.Column(db.Integer)
    accepted = db.Column(db.Boolean, nullable=False)



class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(100))
    image   = db.Column(db.String(100))
    usage = db.Column(db.String(100))
    steps = db.relationship('Step', secondary=step_tool, back_populates='tools')
    accepted = db.Column(db.Boolean, nullable=False)


