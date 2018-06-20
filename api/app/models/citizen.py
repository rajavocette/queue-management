from flask_restplus import fields
from qsystem import api, db
from .base import Base 
from sqlalchemy import BigInteger, Integer, String

class Citizen(Base):

    model = api.model('Citizen', {
        'citizen_id': fields.Integer,
        'office_id': fields.Integer,
        'ticket_number': fields.Integer,
        'citizen_name': fields.String,
        'citizen_comments': fields.String,
        'qt_xn_citizen': fields.Integer,
        'cs_id': fields.Integer
        })

    citizen_id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    office_id           = db.Column(db.Integer, db.ForeignKey('office.office_id'))
    ticket_number       = db.Column(String(50))
    citizen_name        = db.Column(String(150))
    citizen_comments    = db.Column(String(1000))
    qt_xn_citizen       = db.Column(Integer)
    cs_id               = db.Column(BigInteger, db.ForeignKey('citizenstate.cs_id'))

    service_reqs        = db.relationship('ServiceReq', backref='citizen', lazy=False)

    def __repr__(self, citizen_name):
        return '<Citizen: %r>' % self.citizen_name

    def __init__(self, **args):
        self.office_id          = args.get("office_id")
        self.ticket_number      = args.get("ticket_number")
        self.citizen_name       = args.get("citizen_name")
        self.citizen_comments   = args.get("citizen_comments")
        self.qt_xn_citizen      = args.get("qt_xn_citizen")
        self.cs_id              = args.get("cs_id")

    def json(self, **json_args):
        return {json_args['citizen_id']: self.citizen_id,
                json_args['office_id']: self.office_id,
                json_args['ticket_number']: self.ticket_number,
                json_args['citizen_name']: self.citizen_name,
                json_args['citizen_comments']: self.citizen_comments,
                json_args['qt_xn_citizen']: self.qt_xn_citizen,
                json_args['cs_id']: self.cs_id}
