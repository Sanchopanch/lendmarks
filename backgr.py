import cv2
import mediapipe as mp
import numpy as np

from contours import get_cont


def get_current_contour(cap):
    mp_face_mesh = mp.solutions.face_mesh
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_pose = mp.solutions.pose

    mp_drawing = mp.solutions.drawing_utils
    mp_selfie_segmentation = mp.solutions.selfie_segmentation

    # For webcam input:

    bg_image = None

    with mp_selfie_segmentation.SelfieSegmentation(
            model_selection=1) as selfie_segmentation:
        # while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            return None

        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        results = selfie_segmentation.process(image)

        with mp_pose.Pose(
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5) as pose:
            result_pose = pose.process(image)

        with mp_face_mesh.FaceMesh(
                max_num_faces=1,
                refine_landmarks=True,
                min_detection_confidence=0.8,
                min_tracking_confidence=0.8) as face_mesh:
            results_face = face_mesh.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        cont = get_cont(image)

        if bg_image is None:
            bg_image = np.ones(cont.shape, dtype=np.uint8) * 255

        output_image = np.where(results.segmentation_mask > 0.2, cont, bg_image)
        output_image = cv2.cvtColor(output_image, cv2.COLOR_GRAY2BGR)

        draw_spec = mp_drawing.DrawingSpec()
        draw_spec.color = (255, 150, 150)
        draw_spec.circle_radius = 1
        draw_spec.thickness = 1
        draw_spec2 = mp_drawing.DrawingSpec()
        draw_spec2.color = (0, 255, 0)
        draw_spec2.circle_radius = 1
        draw_spec2.thickness = 1

        mp_drawing.draw_landmarks(
            output_image,
            result_pose.pose_landmarks,
            None,
            landmark_drawing_spec=draw_spec)
        with mp_face_mesh.FaceMesh(
                max_num_faces=1,
                refine_landmarks=True,
                min_detection_confidence=0.8,
                min_tracking_confidence=0.8) as face_mesh:
            results_face2 = face_mesh.process(output_image)

        if results_face.multi_face_landmarks:
            for face_landmarks in results_face.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=output_image,
                    landmark_list=face_landmarks,
                    connections=None,
                    landmark_drawing_spec=draw_spec2)
        if results_face2.multi_face_landmarks:
            for face_landmarks in results_face2.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=output_image,
                    landmark_list=face_landmarks,
                    connections=None,
                    landmark_drawing_spec=draw_spec)
        return output_image


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
    while True:
        output_image = get_current_contour(cap)
        if not output_image is None:
            cv2.imshow('very good picture', output_image)
        cv2.waitKey(0)
