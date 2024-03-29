import os
import dlib
import glob
from scipy.spatial import procrustes


def calculate_face_landmarks(faces_folder):
    predictor_path = "./model/shape_predictor_81_face_landmarks.dat"
    faces_folder_path = "./faces/"

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)
    win = dlib.image_window()

    for f in glob.glob(os.path.join(faces_folder_path, "*.png")):
        print("Processing file: {}".format(f))
        img = dlib.load_rgb_image(f)

        win.clear_overlay()
        win.set_image(img)

        # Ask the detector to find the bounding boxes of each face. The 1 in the
        # second argument indicates that we should upsample the image 1 time. This
        # will make everything bigger and allow us to detect more faces.
        dets = detector(img, 1)
        print("Number of faces detected: {}".format(len(dets)))
        for k, d in enumerate(dets):
            print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                k, d.left(), d.top(), d.right(), d.bottom()))
            # Get the landmarks/parts for the face in box d.
            shape = predictor(img, d)
            print("Part 0: {}, Part 1: {} ...".format(shape.part(0),
                                                    shape.part(1)))
            
            for x in range(0, shape.num_parts):
                print (str(shape.part(x)))
            
            print("Shape: " + str(shape))
            
            # Draw the face landmarks on the screen.
            win.add_overlay(shape)

        win.add_overlay(dets)
        dlib.hit_enter_to_continue()

def calculate_procrustes(arr_a, arr_b):
    mtx1, mtx2, disparity = procrustes(arr_a, arr_b)
    return disparity


calculate_face_landmarks("./faces/")

#https://stackoverflow.com/questions/47325944/put-values-inside-multiple-columns-in-same-family-in-hbase





#image hash