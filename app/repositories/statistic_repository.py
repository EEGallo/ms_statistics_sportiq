from app import db
from app.models import Statistic
from .repository_base import Create, Read, Update, Delete


class StatisticRepository(Create, Read, Update, Delete):
        
    def __init__(self):
            self.__model = Statistic

    def create(self, model: Statistic):
        db.session.add(model)
        db.session.commit()
        return model


    def find_all(self):
        try:
            statistics = db.session.query(self.__model).all()
            return statistics
        except Exception as e:
            raise Exception('Error a obtener la lista de estadísticas'  + str(e))
    

    def find_by_id(self, id):
        try:
            entity = db.session.query(self.__model).filter(self.__model.id == id).one()
            return entity
        except Exception as e:
            raise Exception('Error a obtener estadísticas por id' + str(e))


    def update(self, entity: Statistic):
            db.session.merge(entity)
            db.session.commit()
            return entity


    def delete(self, statistic_id) -> bool:
        statistic = Statistic.query.get(statistic_id)
        if statistic:
            db.session.delete(statistic)
            db.session.commit()
            return True
        return False