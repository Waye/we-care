from datetime import datetime
from mongoengine import *
from config import *
from model.UserModel import User, Settings
# from service.UserService import get_user_profile_by_email


# def get_matches(data, pref=True, day=True, time=True, loc=True):
#     """
#     Returns a list of profile objects that satisfy requested criteria.

#     data: JSON data of the form
#         {
#         "requestor_email" : <requestor's email>,
#         "title" : <name of request>,
#         "location" : [latitude, longitude],
#         "datetime" : <datetime object>,
#         "category" : <codename of category>,
#         "description" : <description of request>
#     }

#     pref, day, time, loc act like "switches" in that they enable wanted filters

#     Output: [Profile], False otherwise
#     """
#     # TODO: Consider adding switches to enable wanted filters
#     # TODO: Sort list by distance
#     rs = []

#     if not isinstance(data["datetime"], datetime) or data["category"] not in d_rules:
#         return False

#     if not isinstance(data["location"], list):
#         return False

#     corresp_pref = service_to_pref[data["category"]]
#     day = data["datetime"].strftime('%A')
#     time = data["datetime"].time()
#     time_of_day = get_time_of_day(time.hour)

#     if not time_of_day or day not in days or corresp_pref not in p_rules:
#         return False

#     qSet = Settings.objects(Q(corresp_pref=True) & Q(
#         day=True) & Q(time_of_day=True)).only('email')

#     # # Perform filters
#     # qSet1 = Settings.objects.filter_by_pref(corresp_pref)
#     # qSet2 = Settings.objects.filter_by_time(time_of_day)
#     # qSet3 = Settings.objects.filter_by_day(day)
#     # qSet4 = User.objects.filter_by_location(data["location"])

#     # # For each qSet, project out emails
#     # set1 = set([s1.email for s1 in qSet1])
#     # set2 = set([s2.email for s2 in qSet2])
#     # set3 = set([s3.email for s3 in qSet3])
#     # set4 = set([s4.email for s4 in qSet4])

#     # # Join above sets i.e. compute the intersection
#     # final_set = set1.intersection(set2).intersection(set3).intersection(set4)

#     # # Now get the corresponding profile objects
#     # rs = [get_user_profile_by_email(e) for e in final_set]
#     rs = [get_user_profile_by_email(e) for e in qSet]
#     # TODO: settings.x, x is a variable. How do I make it work?
#     # return User.filter_by_location(data["location"]).filter(Q(settings.corresp_pref=True) & Q(settings.day=True) & Q(settings.time_of_day=True)).only('profile')
#     return rs


def get_matches(data, max_dist=5000, n=10) -> list:
    # Improved querying with respect to the updated models
    corresp_pref = service_to_pref[data["category"]]
    day = data["datetime"].strftime('%A')
    time = get_time_of_day(data["datetime"].time().hour)
    loc = data["location"]

    # print(corresp_pref, day, time, loc)

    good_settings = list(Settings.objects(
        Q(preferences=corresp_pref) & Q(days=day) & Q(time_of_day=time)))
    # print("Good settings: ", good_settings)

    qSet = User.objects.filter_by_location(loc, max_dist)
    # print("Localized: ", qSet)

    candidates = qSet.filter(settings__in=good_settings)
    # print("Candidates: ", candidates)

    profiles = [candidate.profile for candidate in candidates]
    # print("Profiles: ", profiles)

    rs = list(profiles)[:n]
    return rs


def get_time_of_day(hour) -> str:
    if 0 <= hour <= 5:
        return "Night"
    if 6 <= hour <= 11:
        return "Morning"
    if 12 <= hour <= 17:
        return "Afternoon"
    if 18 <= hour <= 23:
        return "Evening"
    else:
        return False


if __name__ == "__main__":
    connect("david", host=HOST_IP, port=PORT,
            authentication_source=AUTHENTICATION_SOURCE, username=USERNAME, password=PASSWORD)
    print("connected")
