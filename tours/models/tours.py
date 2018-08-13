from tours.extensions import db
from sqlalchemy.dialects.postgresql import (
        BIGINT,
        VARCHAR,
        NUMERIC,
        TIMESTAMP)


class Tours(db.Model):
    __tablename__ = 'tours'
    __table_args__ = {'schema': 'iti'}

    id = db.Column(BIGINT, primary_key=True)
    name = db.Column(VARCHAR, nullable=False)
    location = db.Column(VARCHAR, nullable=False)
    min_budget = db.Column(NUMERIC, nullable=True)
    max_budget = db.Column(NUMERIC, nullable=True)
    ctime = db.Column(TIMESTAMP, nullable=False)
    mtime = db.Column(TIMESTAMP, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location':  self.location,
            'min_budget': self.min_budget,
            'max_budget': self.max_budget,
            'ctime': self.ctime,
            'mtime': self.mtime}
