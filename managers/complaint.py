from db import db
from models import UserRole, ComplaintState
from models.complaint import Complaint


class ComplaintManager:
    @staticmethod
    def get_complaints(user):
        if user.role == UserRole.complainer:
            return Complaint.query.filter_by(complainer_id=user.id).all()
        # no filter required for approvers
        return Complaint.query.all()

    @staticmethod
    def create(data, user):
        data["complainer_id"] = user.id
        complaint = Complaint(**data)
        db.session.add(complaint)
        return complaint

    @staticmethod
    def approve(complaint_id):
        Complaint.query.filter_by(id=complaint_id).update({"status": ComplaintState.approved})

    @staticmethod
    def reject(complaint_id):
        Complaint.query.filter_by(id=complaint_id).update({"status": ComplaintState.rejected})



