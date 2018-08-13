from flask import current_app, jsonify
from flask.views import MethodView

from .models import Tours

class ToursAPI(MethodView):
    def get(self):
        tours = Tours.query.all()

        list_of_tours = [tour.to_dict() for tour in tours]
        payload = {'tours': list_of_tours}
        res = jsonify(payload)
        return res
