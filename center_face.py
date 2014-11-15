#requires input from get_leftside_average(self) & get_rightside_average(self)

def crop_and_center(self):
    leftside_face = self.get_leftside_average()
    rightside_face = self.get_rightside_average()
    face_center = (leftside_face + rightside_face) / 2
    left_edge_crop = face_center - self.size[1] / 2
    right_edge_crop = face_center + self.size[1] / 2
    self.bmp.crop(left_edge_crop, 0, right_edge_crop, self.size[1])    
