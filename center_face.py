#requires input from get_leftside_average(self) & get_rightside_average(self)

def center_face(self):
    leftside_face = self.get_leftside_average()
    rightside_face = self.get_rightside_average()
    face_width = leftside_face - rightside_face
    crop_and_center(face_width)
    

def crop_and_center(self, face_width):
    whitespace = (200 - face_width)/2
    self.crop((self.get_leftside_average - whitespace), 0, self.get_rightside_average + whitespace, self.size[1])
    
