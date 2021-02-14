import logging
from flask import Blueprint, make_response, jsonify
from ..utils.main import retrieve_request_parameters, get_defaut_collection         

api_data_blueprint = Blueprint('api_data', __name__)



@api_data_blueprint.route("/", methods=["GET"])
def get_data():

    member_coll = get_defaut_collection()
    try:
        member_data = list(member_coll.find(
            filter={
                "status": 1
            },
            limit=100,
            sort=[("_id", -1)],
            projection={"_id": 1, "name": 1, 'status': 1}
        ))            

        html = "<div><center style=""margin-top:40vh""><table><tr><th>Name</th><th>Status</th></tr>"
        for member in member_data:
            html += f"<tr><th>{member.get('name')}</th><th>{member.get('status')}</th></tr>"
        html += "<table></center></div>"
        return html

        # return make_response(jsonify({"status": 200, "data": {"message": "data fetched successfully", "data": member_data}}))
    except Exception as err:
        logging.info('Error while fetching data')
        return make_response(jsonify({"status": 500, "error": {"message": "data fetched failed", "error": err}}))

@api_data_blueprint.route("/", methods=["POST"])
@retrieve_request_parameters()
def post_data(**kwargs):
    name = kwargs.get('name')
    status = kwargs.get('status')
    data = {
        "name": name,
        "status": status,
    }

    member_coll = get_defaut_collection()
    try:
        member_data = member_coll.insert_one(data)
        logging.info('Data saved successfully')
        return make_response(jsonify({"status": 200, "data": {"message": "data saved successfully"}}))
    except Exception as err:
        logging.info('Error while saving data')
        return make_response(jsonify({"status": 500, "error": {"message": "data saving failed", "error": err}}))
        
