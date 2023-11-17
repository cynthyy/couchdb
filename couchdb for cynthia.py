import couchdb
server = couchdb.Server('http://cynthyy:cynthyy@localhost:5984/')  # Replace the URL with your CouchDB server URL , REPLACE admin_user YOUR USERNAME AND admin_password with PASSWORD
#CREATE A DATABASE
db_name = 'cynthiadatabase'
try:
    db = server.create(db_name)
except couchdb.http.PreconditionFailed as e:
    db = server[db_name]  # If the database already exists, use itv
#WRITE DATA
data = {
    'firstname': 'Cynthia',#Change values
    'email': 'chinwe.onuoha@stu.cu.edu.ng'
}

doc_id, doc_rev = db.save(data)
#READ DATA
doc = db.get(doc_id)
print(doc)

#UPDATE DATA
doc = db.get(doc_id)
doc['firstname'] = 'chinwe'#CHANGE VALUES
db.save(doc)

#MODIFY DATA
def modify_data(doc_id, new_data):
    doc = db.get(doc_id)
    doc.update(new_data)
    db.save(doc)

new_data = {'matric number': '20CJ027481'}#CHANGE VALUES
modify_data(doc_id, new_data)

#DELETE A DOCUMENT
#doc = db.get(doc_id)
#db.delete(doc)


