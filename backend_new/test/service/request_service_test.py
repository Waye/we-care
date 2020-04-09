
import unittest
from datetime import datetime
from config import *
from mongoengine import *
from service import UserService
from model import UserModel
from service import RequestService
from model import RequestModel
import json

# TODO: The tests need to be updated with respect to current models

print('IN THE FILE')


class TestRequestService(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        connect("david", host=HOST_IP, port=PORT,
                username=USERNAME, password=PASSWORD,
                authentication_source=AUTHENTICATION_SOURCE)
        print("connected")

    
    
#    def setUp(self) -> None:
        # add some users with profile and preferences here
        
        du1 = UserService.User.objects(email = 'fred@gmail.com')
        du1.delete()
        du2 = UserService.User.objects(email = 'sean@gmail.com')
        du2.delete()
        du3= UserService.User.objects(email = 'nathan@gmail.com')
        du3.delete()
        du4 = UserService.User.objects(email = 'chris@gmail.com')
        du4.delete()
        du5 = UserService.User.objects(email = 'elaine@gmail.com')
        du5.delete()

        pu1 = UserService.Profile.objects(email = 'fred@gmail.com')
        pu1.delete()
        pu2 = UserService.Profile.objects(email = 'sean@gmail.com')
        pu2.delete()
        pu3= UserService.Profile.objects(email = 'nathan@gmail.com')
        pu3.delete()
        pu4 = UserService.Profile.objects(email = 'chris@gmail.com')
        pu4.delete()
        pu5 = UserService.Profile.objects(email = 'elaine@gmail.com')
        pu5.delete()

        su1 = UserService.Settings.objects(email = 'fred@gmail.com')
        su1.delete()
        su2 = UserService.Settings.objects(email = 'sean@gmail.com')
        su2.delete()
        su3= UserService.Settings.objects(email = 'nathan@gmail.com')
        su3.delete()
        su4 = UserService.Settings.objects(email = 'chris@gmail.com')
        su4.delete()
        su5 = UserService.Settings.objects(email = 'elaine@gmail.com')
        su5.delete()
 
        ru1 = RequestService.Request.objects(requestor_email = 'fred@gmail.com')
        ru1.delete()
        ru2 = RequestService.Request.objects(requestor_email = 'sean@gmail.com')
        ru2.delete()
        ru3= RequestService.Request.objects(requestor_email = 'nathan@gmail.com')
        ru3.delete()
        ru5= RequestService.Request.objects(requestor_email = 'elaine@gmail.com')
        ru5.delete()

 
        
        
        
        
        u1 = UserService.create_user("fred@gmail.com", [43.653117, -79.383192])
        u2 = UserService.create_user("sean@gmail.com", [51.561482, -87.906550])
        u3 = UserService.create_user("nathan@gmail.com", [51.561482, -87.906550])
        u4 = UserService.create_user("chris@gmail.com", [43.653225, -79.383186])
        u5 = UserService.create_user("elaine@gmail.com", [43.653742, -79.383906])

        p1 =  UserService.create_profile(
            "fred@gmail.com", "Fred", "Arrow", "1990-11-18", 30, "Male", "Toronto", "url_1")
        p2 =  UserService.create_profile(
            "sean@gmail.com", "Sean", "Penn", "2001-08-10", 18, "Male", "Fort Hope", "url_1")
        p3 =  UserService.create_profile(
            "nathan@gmail.com", "Nathan", "Grove", "1996-01-05", 24, "Male", "Toronto", "url_1")
        p4 =  UserService.create_profile(
            'chris@gmail.com', 'Chris', 'Jones', '1995-05-22', 25, 'Male', 'Toronto', 'url_1')
        p5 =  UserService.create_profile(
            'elaine@gmail.com', 'Elaine', 'Doe', '1985-02-20', 35, 'Female', 'Toronto', 'url_1')
        
        
        s1 =  UserService.create_settings(
            "fred@gmail.com", True, ["OPC", "OQC", "OQE"], days, time_of_day)
        s2 =  UserService.create_settings(
            "sean@gmail.com", True, ["OQC"], ["Monday"], ["Evening"])
        s3 =  UserService.create_settings(
            "nathan@gmail.com", True, ["OPC", "OQC"], ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], ["Morning", "Afternoon", "Evening"])
        s4 =  UserService.create_settings(
            'chris@gmail.com', True, ["OPC", "OQC", "OQE"], days, time_of_day)
        s5 = UserService. create_settings(
            'chris@gmail.com', True, ["OPC", "OQC", "OQE"], days, time_of_day)
        

        u1.profile = p1
        u1.settings = s1
        u1.save()

        u2.profile = p2
        u2.settings = s2
        u2.save()
        
        u3.profile = p3
        u3.settings = s3
        u3.save()

        u4.profile = p4
        u4.settings = s4
        u4.save()

        u5.profile = p5
        u5.settings = s5
        u5.save()
        

        
#        r1 = Request(requestor_email = "abcdefg@gmail.com", title = "ABCDEFG", point = [-89.252003, 48.392225], 
#                    time_of_request = datetime(2020, 3, 28, 21), request_type = "RWL", description = "Hello").save()

#        UserService.update_user_settings({
#            "email": "jane@gmail.com",
#            "education_navigation": ["OPC"],
#            "health_care_support": ["OPC", "OQC", "OQE"],
#            "well_being_leisure": ["OQC"]
#        })
#        UserService.update_user_settings({
#            "email": "mike@gmail.com",
#            "education_support": ["OPC", "OQC", "OQE"],
#            "employment_support": ["OPC", "OQC"],
#            "local_support": ["OPC", "OQC"],
#            "pick_up_and_drop_off": ["OPC", "OQC", "OQE"],
#            "homemaking_supports": ["OQC"]
#        })

    def test_create_request(self):
        # for now create the request_id manually here
        desc = "I need to borrow a Macbook charger for 30 minutes"
        req1 =  RequestService.create_request(
            "fred@gmail.com", "Fred Arrow", [43.653117, -79.383192], datetime(2020, 3, 28, 21), "RHMS", desc)

        self.assertEqual(req1.requestor_email, "fred@gmail.com")
        self.assertEqual(req1.request_type, "RHMS")
        self.assertEqual(req1.title, "Fred Arrow")
        self.assertEqual(req1.description, desc)



    def test_create_request_2(self):
        # for now create the request_id manually here
        desc2 = "I need someone to talk to"
        req2 =  RequestService.create_request(
            "sean@gmail.com", "Sean Penn", [51.561482, -87.906550], datetime(2020, 3, 30, 19), "RWL", desc2)

        self.assertEqual(req2.requestor_email, "sean@gmail.com")
        self.assertEqual(req2.request_type, "RWL")
        self.assertEqual(req2.title, "Sean Penn")
        self.assertEqual(req2.description, desc2)

 
    def test_create_request_3(self):
        # for now create the request_id manually here
        desc3 = "I would like to initiate a chat with someone"
        req3 =  RequestService.create_request(
            "nathan@gmail.com", "Nathan Grove", [43.655878, -79.380382], datetime(2020, 3, 27, 11), "RWL", desc3)

        self.assertEqual(req3.requestor_email, "nathan@gmail.com")
        self.assertEqual(req3.request_type, "RWL")
        self.assertEqual(req3.title, "Nathan Grove")
        self.assertEqual(req3.description, desc3)
        
    def test_create_update_request(self):
        req5 = {"requestor_email": "elaine@gmail.com", 
            "title": "Elaine Doe", 
            "point": [43.653742, -79.383906],
            "time_of_request": "2020, 3, 29, 18",
            "request_type": "RWL",
            "description": "Need to talk on the phone",
            "status": "POSTED"
        }

        ru5 =  RequestService.create_update_request(json.dumps(req5))

        self.assertEqual(ru5.requestor_email, "elaine@gmail.com")
        self.assertEqual(ru5.request_type, "RWL")
        self.assertEqual(ru5.title, "Elaine Doe")
        self.assertEqual(ru5.description, "Need to talk on the phone")

    def test_get_open_requests(self):
        getopreq = RequestService.get_open_requests()

        self.assertEqual(len(getopreq), 4)
    
#    def test_accept_request(self):

#        request =  RequestService.get_requests_by_email("fred@gmail.com")
#        self.assertEqual(request[0].status, "POSTED") 
#        self.assertEqual(request[0].requestor_email, "fred@gmail.com")

#        accept = RequestService.accept_request('chris@gmail.com', request)
#        self.assertEqual(accept.status, "PENDING")
#        self.assertEqual(accept.acceptor_email, "chris@gmail.com")

    def test_isRegistered(self):
        checkuser =  RequestService.isRegistered("sean@gmail.com")

        self.assertEqual(checkuser, True)


    def test_get_all_user_preferences(self):
        allusers =  RequestService.get_all_user_preferences()
        firstuserpref = len(allusers[0].preferences)
        seconduserpref = len(allusers[1].preferences)
        thirduserpref = len(allusers[2].preferences)

        self.assertTrue(firstuserpref>0)
        self.assertTrue(seconduserpref>0)
        self.assertTrue(thirduserpref>0)

    def test_get_requests_by_email(self):
        getreq =  RequestService.get_requests_by_email("elaine@gmail.com")

        self.assertEqual(getreq[0].requestor_email, "elaine@gmail.com")
        self.assertEqual(getreq[0].status, "POSTED")



        
    
    # todo: add any further tests you feel appropriate


        
    


if __name__ == "__main__":
    unittest.main()