#video enhancement
import cv2
import math

video = cv2.VideoCapture('../TemporalSegmentation/video/Screen Recording 2024-10-14 110235.mp4')

if not video.isOpened():
    print('Error opening video')

fps = video.get(cv2.CAP_PROP_FPS)
interval = 5.0

skip_frames = math.floor(fps * interval)
segment_num = 1000000

segment_frames = []

while True:
    ret, frame = video.read()
    if not ret:
        break

    if video.get(cv2.CAP_PROP_POS_FRAMES) % skip_frames == 0:
        segment_frames.append(frame)

    if len(segment_frames) >= 100:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(f'segment_{segment_num}.mp4', fourcc, fps, (frame.shape[1], frame.shape[0]))

        for frame in segment_frames:
            out.write(frame)

            out.release()
            segment_frames = []

            segment_num += 1

            video.release()
            out.release()


