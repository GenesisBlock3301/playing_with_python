from ffpyplayer.player import MediaPlayer
import cv2
import os


def playvideo(path):
    video = cv2.VideoCapture(path)
    player = MediaPlayer(path)
    while True:
        grabbed, frame = video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
        if cv2.waitKey(28) & 0xFF == ord('q'):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()


files = os.listdir('./')
MP4 = []
for file in files:
    if file.endswith(".MP4") or file.endswith('.mp4'):
        MP4.append(file)
print(MP4)

song = 0
while MP4:
    try:
        print("Enter your action")
        present, next, prev = [i for i in input().split(',')]
        print( present,next, prev,song)
        if present == 'present':
            playvideo(MP4[song])
        if next == 'next':
            song += 1
            if song > len(MP4)-1:
                song = 0
            playvideo(MP4[song])
        if prev == 'prev':
            song -= 1
            if song < 0:
                song = len(MP4)-1
            playvideo(MP4[song])
    except Exception as e:
        print(e)
song = 0
