import logging
from app import get_authenticated_user_profile
from app.config.role_access_manager import Role_access
from app.votation.models import StateVotation, Votation
from app.proposal.models import Proposal,Proposal_State
from app.vote.forms import Vote_Form
from flask import render_template, request, jsonify,flash,redirect
from flask_login import login_required

from . import vote_bp
from .models import Vote
from ..services import delete_entity, delete_entity_bulk
logger = logging.getLogger(__name__)


@vote_bp.route("/vote")
@login_required
def index():
    logger.info('Access vote index')

    return render_template("vote/index.html")


@vote_bp.route("/votation/<int:id>/vote",methods=["GET","POST"])
def create(id):
    if Role_access.user_not_allowed("vote","vote"):
        return Role_access.not_allowed_get_previous_page("vote","vote")

    form = Vote_Form()
    if request.method == 'POST' and form.validate_on_submit():
        #show operation not succeded in flash message
    
        description = form.description.data.strip()
        voted_yes = form.decision.data
        profile = get_authenticated_user_profile()
        user_id = profile.user.id

        vote = Vote(decision=voted_yes,votation_id=id,user_id=user_id,description=description)
        vote.save()
        update_votation(vote)
        flash("Voto computado","success")

        return redirect("/votation/view/"+str(id))

    else:
   
        return render_template("vote/create.html",form=form,votation_id=id)


def update_votation(vote):
    votes = Vote.query.filter_by(votation_id = vote.votation_id)
    total = 3
    number_of_true_votes = sum(v.decision for v in votes)
    number_of_false_votes = sum(1 for v in votes if  not v.decision)
    votation = Votation.query.get_or_404(vote.votation_id)
    proposal = Proposal.query.get_or_404(votation.proposal_id)
    if number_of_true_votes/total > 0.5:
        votation.state_votation = StateVotation.ACCEPTED
        proposal.state = Proposal_State.ON_PREPARATION
    elif number_of_false_votes/total > 0.5:
        votation.state_votation = StateVotation.REJECTED
        proposal.state = Proposal_State.REJECTED
    proposal.save()
    votation.save()


        
    
    


