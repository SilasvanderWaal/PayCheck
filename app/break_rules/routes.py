from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from app.break_rules import break_rules_bp
from app.break_rules.forms import BreakRuleForm
from app.break_rules.services import (
    get_rules_for_job, create_rule, delete_rule,
    get_rule_or_404, get_job_or_404_scoped
)


@break_rules_bp.route("/")
@login_required
def index(job_id):
    job = get_job_or_404_scoped(job_id, current_user.id)
    rules = get_rules_for_job(job_id)
    return render_template("break_rules/index.html", job=job, rules=rules)


@break_rules_bp.route("/create", methods=["GET", "POST"])
@login_required
def create(job_id):
    job = get_job_or_404_scoped(job_id, current_user.id)
    form = BreakRuleForm()
    if form.validate_on_submit():
        create_rule(
            job_id=job_id,
            min_shift_hours=float(form.min_shift_hours.data),
            break_minutes=form.break_minutes.data
        )
        flash("Break rule added.", "success")
        return redirect(url_for("break_rules.index", job_id=job_id))
    return render_template("break_rules/form.html", form=form, job=job, title="Add Break Rule")


@break_rules_bp.route("/<int:rule_id>/delete", methods=["POST"])
@login_required
def delete(job_id, rule_id):
    job = get_job_or_404_scoped(job_id, current_user.id)
    rule = get_rule_or_404(rule_id, job_id)
    delete_rule(rule)
    flash("Break rule deleted.", "success")
    return redirect(url_for("break_rules.index", job_id=job_id))