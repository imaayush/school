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
                  "parents": [], opitional
                  "password": "123456",
                  "user_class": 1 opitional
              }
     
     Response: {
                   "id": 1,
                   "username": "aayush",
                   "first_name": "",
                   "last_name": "",
                   "email": "",
                   "user_type": "STUDENT",
                   "parents": [],
                   "classes": 1
               }

#### API which will list the users.
     GET api/v1/users/
     HEADER : Authorization Token 0fa8f31a25492c04a03f02a2467daddf06b12de2
     
     Response : [
                   {
                       "id": 1,
                       "username": "aayush",
                       "first_name": "",
                       "last_name": "",
                       "email": "",
                       "user_type": "STUDENT",
                       "parents": [],
                       "user_class": 
                   }
               ]

#### API which will create,list,update and delete the classes.
     HEADER : Authorization Token 0fa8f31a25492c04a03f02a2467daddf06b12de2
     Create Post api/v1/classes/
          Request:{"name" : "english",}
          
          Response:{id:1,
                    "name" : "english",}
     
     LIST GET api/v1/classes/
        Response:   [{id:1,
                    "name" : "english",}]
     
     Update PUT api/v1/clasess/:id
          Request:{"name" : "enlish",}
          
          Response:{id:1,
                    "name" : "english",}
     
     Delete DELETE api/v1/classes/:id
     
     GET api/v1/classes/:id   
          Response:{id:1,
                    "name" : "english",}

#### API which will create,list,update and delete the subjects.
     HEADER : Authorization Token 0fa8f31a25492c04a03f02a2467daddf06b12de2
     Create Post api/v1/subjects/
          Request:{
                    "name" : "english",
                    "teachers": [2],
                    "classes" : [1],
	
                    }
          
          Response:{
                        "id": 1,
                        "name": "english",
                        "teachers": [
                            2
                        ],
                        "classes": [
                            1
                        ]
                    }
 `
     
     LIST GET api/v1/subjects/
          Response :[
                        {
                            "id": 1,
                            "name": "english",
                            "teachers": [
                                2
                            ],
                            "classes": [
                                1
                            ]
                        }
                    ]
     
     Update PUT api/v1/subjects/:id
          Request:{
                    "name" : "english",
                    "teachers": [2],
                    "classes" : [1],
	
                    }
          
          Response:{
                        "id": 1,
                        "name": "english",
                        "teachers": [
                            2
                        ],
                        "classes": [
                            1
                        ]
                    }
     
     Delete DELETE api/v1/subjects/:id
     
     GET api/v1/subjects/:id   
          Response:{
                        "id": 1,
                        "name": "english",
                        "teachers": [
                            2
                        ],
                        "classes": [
                            1
                        ]
                    }

#### API which will list the student,student subjects , subject teachers and his parents.
     HEADER : Authorization Token 0fa8f31a25492c04a03f02a2467daddf06b12de2
     GET api/v1/users/?user_type=STUDENT
     Response : [ {
                  "id": 4,
                  "username": "aayush+3",
                  "first_name": "",
                  "last_name": "",
                  "email": "",
                  "user_type": "STUDENT",
                  "parents": [
                      {
                          "id": 3,
                          "username": "aayush+2",
                          "first_name": "",
                          "last_name": "",
                          "email": "",
                          "user_type": "PARENT"
                      }
                  ],
                  "user_class": 
                      {
                          "id": 1,
                          "name": "endglish",
                          "subjects": [
                              {
                                  "id": 1,
                                  "name": "endglish",
                                  "teachers": [
                                      2
                                  ],
                     
                              }
                          
                      }
                  ]
