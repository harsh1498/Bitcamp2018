# Bitcamp2018
## PUDUI Project for Bitcamp 2018

PUDUI is a django web application reunite patients, doctors, and the insurance company once again. We want to bring back a time when the doctor and the patient were able to communicate without intermediates in between. We used to be able to call our doctor on their phone and they would answer, not their assistant, and they would talk to you about your symptoms over the phone and give you advice.



## Technologies being used
*TODO: Implement Nginx, uwsgi and Django together and pfsense*
* Django python web framework
* Sqlite3 database management system
* React.js javascript framework
* Bootstrap, Html, Css, and jinga templating language for the frontend



## The Patient

The patient will want to use this service because it provides them with a convienient method of communicating with their doctor and their insurance company. They will not have to wait on a phone, take time off from work, sit in a waiting room just until the assistant guides them to the exam room, where the doctor will do a few tests and probably say, 'Get some rest, take some cough medicine, drink a lot of water.' Why waste this time when the entire transaction of communication can be started (and potentially ended) online. 

* Running production server ```uwsgi --http :8000 --module PUDUI.wsgi```*
