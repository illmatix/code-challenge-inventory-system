from apscheduler.schedulers.background import BackgroundScheduler
from src.models import TokenBlocklist
from src.extensions import db
from datetime import datetime, timezone


def clean_expired_tokens():
    """
    Removes expired tokens from the TokenBlocklist.
    """
    now = datetime.now(timezone.utc)
    expired_tokens = TokenBlocklist.query.filter(TokenBlocklist.expires_at < now).all()
    for token in expired_tokens:
        db.session.delete(token)
    db.session.commit()


def setup_token_cleanup_scheduler(app):
    """
    Sets up a scheduled job to clean expired tokens.
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=clean_expired_tokens, trigger="interval", hours=3)
    scheduler.start()

    @app.teardown_appcontext
    def shutdown_scheduler(exception=None):
        if scheduler.running:
            scheduler.shutdown(wait=False)
