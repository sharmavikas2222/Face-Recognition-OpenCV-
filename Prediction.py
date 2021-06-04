# In[8]:

#function to draw rectangle on image 
#according to given (x, y) coordinates and 
#given width and heigh
def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)



# In[9]:

#this function recognizes the person in image passed
#and draws a rectangle around detected face with name of the 
#subject
def predict(test_img):

    img = test_img.copy()
    
    face, rect = detect_face(img)


    label, confidence = face_recognizer.predict(face)
    
    label_text = subjects[label]
    
    
    draw_rectangle(img, rect)
    
    draw_text(img, label_text, rect[0], rect[1]-5)
    
    return img
