from base_project.main import Base

class MyThing(Base):

    def __repr__(self):
        return f'<MyThing color={self.color} size={self.size}>'
    
