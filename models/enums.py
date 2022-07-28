import enum


class UserRole(enum.Enum):
    complainer = "Complainer"
    approver = "Approver"
    admin = "Admin"


class ComplaintState(enum.Enum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"

