""" all routes will end up here or loaded here for flask """
# pylint:disable=cyclic-import

from flask import make_response

from app import MONGO as mongo
from app.main import BP as blueprint


def user_metrics():
    """ Query mongo for the disabled users """
    disabled_users = mongo.db.users.count_documents({"disabled": True})
    online_users = mongo.db.clients.count_documents({})
    total_users = mongo.db.users.count_documents({})
    return f"""# HELP pritunl_disabled_users A summary of disabled pritunl users
# TYPE pritunl_disabled_users summary
pritunl_disabled_users_sum 1
pritunl_disabled_users_count {disabled_users}
# HELP pritunl_online_users A summary of pritunl users
# TYPE pritunl_online_users summary
pritunl_online_users_sum 1
pritunl_online_users_count {online_users}
# HELP pritunl_total_users A summary of pritunl users
# TYPE pritunl_total_users summary
pritunl_total_users_sum 1
pritunl_total_users_count {total_users}"""


@blueprint.route('/metrics', methods=['GET'])
def metrics_route():
    """ call user metrics and return 200 response """
    response = make_response(user_metrics(), 200)
    response.mimetype = "text/plain"
    return response
