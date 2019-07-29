from socialmodel import UserProfile


# THIS IS THE FILE THAT DEALS WITH RETRIEVING A PROFILE AND SAVING THE EDITS


def save_profile(email, name, biography, location):
    p= get_user_profile(email)
    if p:
        p.name = name
        p.biography = biography
        p.location = location
        p.put()
    else:
        p = UserProfile(email=email, name=name, biography=biography, location = location)
        p.put()

def get_user_profile(email):
    q = UserProfile.query(UserProfile.email == email)
    results = q.fetch(1)
    for profile in results:
        return profile
    return None



