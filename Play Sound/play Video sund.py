from ffpyplayer.player import MediaPlayer
import cv2


def playvideo(path):
    video = cv2.VideoCapture(path)
    player = MediaPlayer(path)
    while True:
        grabbed , frame = video.read()
        audio_frame,val = player.get_frame()
        if not grabbed:
            print("End of video")
        if cv2.waitKey(28) & 0xFF == ord('q'):
            break
        cv2.imshow("Video",frame)
        if val != 'eof' and audio_frame is not None:
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()
playvideo('./islamic.mp4')

