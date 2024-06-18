from flask import jsonify, Blueprint, request
from app.services.statistic_services import StatisticService
from app.models.response_message import ResponseBuilder
from app.mapping import ResponseSchema, StatisticSchema
import random

statistic = Blueprint('statistic', __name__)
statistic_schema = StatisticSchema()
response_schema = ResponseSchema()

"""
id: int ingresado por el usuario
return: json con los datos del usuario
"""

@statistic.route('/', methods=['GET'])
def index():
    resp = jsonify({"microservicio": "3", "status": "ok"})
    resp.status_code = random.choice([200, 404])
    return resp

@statistic.route('/compensation', methods=['GET'])
def compensation():
    resp = jsonify({"microservicio": "Compensation 3", "status": "ok"})
    resp.status_code = 200
    return resp

@statistic.route('/add', methods=['POST'])
def post_statistic():
    try:
        service = StatisticService()
        statistic = statistic_schema.load(request.json)
        created_statistic = service.create(statistic)
        response = {"statistic": statistic_schema.dump(created_statistic)}
        return jsonify(response), 201
    except Exception as e:
        error_message = f"Error al agregar estadísticas: {str(e)}"
        return jsonify({"error": error_message}), 400


@statistic.route('/<int:id>', methods=['GET'])
def find(id):
    service = StatisticService()
    raffle = service.find_by_id(id)

    if raffle:
        response_builder = ResponseBuilder()
        response_builder.add_message("estadística encontrada").add_status_code(100).add_data(statistic_schema.dump(raffle))
        return jsonify(response_schema.dump(response_builder.build()))
    else:
        return jsonify({"error": "estadística no encontrada"}), 404


@statistic.route('/all', methods=['GET'])
def find_all():
    service = StatisticService()
    response_builder = ResponseBuilder()
    statistics = service.find_all()
    statistics_json = [statistic_schema.dump(statistic) for statistic in statistics]
    response_builder.add_message("estadísticas encontradas").add_status_code(100).add_data({'statistics': statistics_json})
    return response_schema.dump(response_builder.build())
  

@statistic.route('/update/<int:statistic_id>', methods=['PUT'])
def update_statistic(statistic_id):
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Datos de estadísticas no proporcionadas"}), 400

        service = StatisticService()
        updated_statistic = service.update(statistic_id, data)

        if updated_statistic:
            response_builder = ResponseBuilder()
            response_builder.add_message("Estadísticas actualizadas con éxito").add_status_code(200).add_data(statistic_schema.dump(updated_statistic))
            return response_schema.dump(response_builder.build())

        return jsonify({"error": "La estadística no se pudo actualizar"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@statistic.route('/delete/<int:statistic_id>', methods=['DELETE'])
def delete_statistic(statistic_id):
    try:
        service = StatisticService()
        deleted = service.delete(statistic_id)

        if deleted:
            return jsonify({"message": "Estadística eliminada con éxito", "status_code": 200}), 200

        return jsonify({"error": "Estadística no encontrada", "status_code": 404}), 404
    except Exception as e:
        return jsonify({"error": str(e), "status_code": 500}), 500