from DateTime import DateTime
from plone import api
from plone.api.exc import CannotGetPortalError


def get_ip(request):
    """
    Extract the client IP address from the HTTP request in a
    proxy-compatible way.

    @return: IP address as a string or None if not available
    """
    if "HTTP_X_FORWARDED_FOR" in request.environ:
        # Virtual host
        ip = request.environ["HTTP_X_FORWARDED_FOR"]
    elif "HTTP_HOST" in request.environ:
        # Non-virtualhost
        ip = request.environ["REMOTE_ADDR"]
    else:
        # Unit test code?
        ip = None
    return ip


def user_registered(user, event):

    # catch https://github.com/kitconcept/kitconcept.dsgvo/issues/2
    try:
        member = api.user.get(userid=user.getId())
    except CannotGetPortalError:
        return
    now = DateTime()
    portal = api.portal.get()
    ip = get_ip(portal.REQUEST)
    member.setMemberProperties(
        mapping={"dsgvo_registration_date": now, "dsgvo_registration_ip": ip}
    )
