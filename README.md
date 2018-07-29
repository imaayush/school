# school
school management system

#### Login API
     POST api/v1/user/login
        Request : {
                    username: "aayush",
                    password: 123456
                   }
        Response : {
                   "username": "aayush",
                   "token": "a0dc9927e4454cb34ff67796b6658b4fead4b0b2",
                   "user_id": 1
                    }

#### Registration API
     POST api/v1/user/
        Request : {
    
                  "username": "aayush",
                  "first_name": "",
                  "last_name": "",
                  "email": "",
                  "user_type": "STUDENT",
                  "parents": [],
                  "password": "pbkdf2_sha256$36000$cPat0eqKPEAi$u+JBSwtJ2YW6A4PlbJDCsmssCQ30T2PUnYqo91n10FA=",
                  "classes": []
              }
     
     Response: {
                   "id": 1,
                   "username": "aayush",
                   "first_name": "",
                   "last_name": "",
                   "email": "",
                   "user_type": "STUDENT",
                   "parents": [],
                   "password": "pbkdf2_sha256$36000$cPat0eqKPEAi$u+JBSwtJ2YW6A4PlbJDCsmssCQ30T2PUnYqo91n10FA=",
                   "classes": []
               }

#### API which will list the users.

#### API which will create,list,update and delete the subjects.

#### API which will create,list,update and delete the class.

#### API which will list the student,student subjects , subject teachers and his parents.
