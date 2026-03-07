from app.extensions import db
from app.models.break_rule import BreakRule
from app.models.job import Job


def get_rules_for_job(job_id: int):
    return (
        BreakRule.query
        .filter_by(job_id=job_id)
        .order_by(BreakRule.min_shift_hours)
        .all()
    )


def create_rule(job_id: int, min_shift_hours: float, break_minutes: int) -> BreakRule:
    rule = BreakRule(
        job_id=job_id,
        min_shift_hours=min_shift_hours,
        break_minutes=break_minutes
    )
    db.session.add(rule)
    db.session.commit()
    return rule


def delete_rule(rule: BreakRule) -> None:
    db.session.delete(rule)
    db.session.commit()


def get_rule_or_404(rule_id: int, job_id: int) -> BreakRule:
    return BreakRule.query.filter_by(id=rule_id, job_id=job_id).first_or_404()


def get_job_or_404_scoped(job_id: int, user_id: int) -> Job:
    return Job.query.filter_by(id=job_id, user_id=user_id).first_or_404()