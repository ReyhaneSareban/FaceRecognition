import cv2
import face_recognition as fr

reference_img=fr.load_image_file("images/image1.jpg")
reference_enc=fr.face_encodings(reference_img)[0]

camera=cv2.VideoCapture(0)

while True:
  grabbed,frame=camera.read()
  if not grabbed:
    continue

  rgb=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)

  faces=fr.face_locations(rgb)

  if faces:
    top,right,bottom,left=faces[0]

    cv2.rectangle(frame,(left,top),(right,bottom),(120,40,200),3)

    try:
      current_enc=fr.face_encodings(rgb,[faces[0]])[0]
      match=fr.compare_faces([reference_enc],current_enc)[0]
      color=(70,220,120)

      if fr.compare_faces([reference_enc],current_enc)[0]:
         text="Elon Musk detected:)"

      else:
          text="Unknown detected"
          color=(50,180,255)

      cv2.putText(
        frame,
        text,
        (left,top-10),
        cv2.FONT_HERSHEY_COMPLEX_SMALL,
        0.9,
        color,
        2
      )

    except:
      pass

  cv2.imshow("Face scanner",frame)
  if cv2.waitKey(1)& 0xFF==ord('q'):
    break

camera.release()
cv2.destroyAllWindows()