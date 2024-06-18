from app.repositories import StatisticRepository
from app import db
from sqlalchemy.orm.exc import NoResultFound

class StatisticService():
    def __init__(self):
        self.__repository = StatisticRepository()


    def create(self, entity):
        return self.__repository.create(entity)
    

    def find_all(self):
        try:
            statistics = self.__repository.find_all()
            if statistics:
                return statistics
            else:
                return []
            
        except Exception as e:
            raise Exception('Error al obtener la lista de estadísticas' + str(e))

    
    def find_by_id(self, entity_id):
        try:
            entity = self.__repository.find_by_id(entity_id)
            if entity:
                return entity
            else:
                return None 
        except NoResultFound:
            return None
        except Exception as e:
            raise Exception('Error al obtener estadisticas por id: ' + str(e))


    
    def update(self, entity_id, updated_fields):
        try:
            statistic = self.__repository.find_by_id(entity_id)

            if statistic:
                for field, value in updated_fields.items():
                    setattr(statistic, field, value)

                db.session.commit()

            return statistic
        except Exception as e:
            raise Exception('Error al actualizar las estadísticas: ' + str(e))
    
    def delete(self, entity_id):
        return self.__repository.delete(entity_id) 