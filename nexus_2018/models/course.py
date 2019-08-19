from app.config import Table_Prefix

from app.database import Base

from sqlalchemy import Column
from sqlalchemy import Enum
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import UniqueConstraint

# class Training_Course_Status(Enum):
#     inactive
#     active
#     beta

class training_course(Base):
    '''Training course table'''
    __tablename__ = '%s%s' % (Table_Prefix, 'training_course')

    record_id = Column(Integer, primary_key=True)
    label = Column(String(255), nullable=False)
    status = Column(Enum('inactive', 'active', 'beta'), default='inactive')
    concentration = Column(String(255), nullable=False)
    replaces = Column(Integer)
    replaced_by = Column(Integer)

    __table_args__ = (
        UniqueConstraint('label', name='label'),
        )

    @property
    def serialize(self):
        return {
            'record_id': self.record_id,
            'label': self.label,
            'status': self.status,
            'concentration': self.concentration,
            'replaces': self.replaces,
            'replaced_by': self.replaced_by
        }
