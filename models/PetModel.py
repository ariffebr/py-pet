from configs import db, ma


class PetModel(db.Model):
    __tablename__ = 'pet'

    id = db.Column(name='id', primary_key=True, autoincrement=True, type_=db.Integer)
    name = db.Column(name='name', type_=db.String(100))
    owner = db.Column(name='owner_id', type_=db.Integer)
    age = db.Column(name='age', type_=db.SmallInteger)
    photo = db.Column(name='photo', type_=db.String(100))
    createdAt = db.Column(name='created_at', type_=db.DateTime)
    createdBy = db.Column(name='created_by', type_=db.String(150))
    modifiedAt = db.Column(name='modified_at', type_=db.DateTime)
    modifiedBy = db.Column(name='modified_by', type_=db.String(150))


class PetSchema(ma.ModelSchema):
    class Meta:
        model = PetModel
        sqla_session = db.session
