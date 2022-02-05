import face_recognition
import numpy
import cv2

#functions contained in this file
#
#check_for_contact_name(name, uid, db)      //checks for the name in a user's contact list
#create_contact(name, file, uid, db)        //creates a new contact and adds name and encoding of image to db
#retrieve_all_contacts(uid, db)             //puts all user's contacts into list
#facial_recog_app(our_encodings, our_names) //don't worry about it yet


def check_for_contact_name(name, uid, db):
    cursor = db.cursor()
    cursor.execute("SELECT name FROM contacts WHERE uid = %s", (uid, ))

    for x in cursor.fetchall():
        if x == name:
            print("Name already in use")
            return True

    return False

def create_contact(name, file, uid, db):
    cursor = db.cursor()

    #create variable of encoded face's array
    img = face_recognition.load_image_file(file)
    encoded = face_recognition.face_encodings(img)[0]

    #convert encoded string for datatable and insert it 
    string_of_array = ""
    for x in encoded:
        string_of_array = string_of_array + " " + str(x)

    cursor.execute("INSERT INTO contacts (name, encoded, uid) VALUES (%s, %s, %s)", (name, string_of_array, uid))
    db.commit()
    print("Contact created successfully")


def retrieve_all_contacts(uid, db):
    cursor = db.cursor()
    user_contacts = []
    cursor.execute("SELECT name FROM contacts WHERE uid = %s", (uid, ))
    result = cursor.fetchall()
    for x in result:
        x = str(x)
        x = x[2 : len(x)-3]
        user_contacts.append(x)


def facial_recog_app(our_encodings, our_names):
    #reference to camera
    video_capture = cv2.VideoCapture(0)

    #Intialize variables
    face_locations = []
    face_encodings = []
    face_names = []
    process = True

    while True:
        #Grab frame from video and convert
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0,0), fx =0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        if process:
            #find all locations of faces
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            
            face_names = []
            for x in face_encodings:
                match = face_recognition.compare_faces(our_encodings, x)
                name = "Unknown"

                face_distances = face_recognition.face_distance(our_encodings, x)
                best_match_index = numpy.argmin(face_distances)
                if match[best_match_index]:
                    name = our_names[best_match_index]

                face_names.append(name)

        process = not process

        if len(face_names) > 0:
            print(face_names)

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()


