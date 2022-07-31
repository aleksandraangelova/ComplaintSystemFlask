from werkzeug.exceptions import BadRequest
from werkzeug.security import check_password_hash

from managers.auth import AuthManager
from models import ApproverModel


class ApproverManager:
    @staticmethod
    def login(data):
        # TODO: Refactor as sub-func and reuse in Complainer as well
        approver = ApproverModel.query.filter_by(email=data["email"]).first()
        if not approver:
            raise BadRequest("User does not exist")

        if check_password_hash(approver.password, data["password"]):
            return AuthManager.encode_token(approver)
        raise BadRequest("invalid credentials")
