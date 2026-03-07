from flask import Blueprint

break_rules_bp = Blueprint("break_rules", __name__, url_prefix="/jobs/<int:job_id>/break-rules")

from app.break_rules import routes