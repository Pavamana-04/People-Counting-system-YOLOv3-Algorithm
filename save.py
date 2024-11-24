import cv2

def save_video(output_frames):
    # Check if output_frames has been populated
    if output_frames:
        height, width, _ = output_frames[0].shape
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(r"E:\Mini PROJECT\Person_counting\output data\output_video.avi", fourcc, 20.0, (width, height))

        for frame in output_frames:
            out.write(frame)  # Write each frame to the video file

        out.release()  # Release the video writer
        print("Video saved as output_video.avi in 'E:\\Mini PROJECT\\Person_counting\\output data'")
    else:
        print("No frames to save.")
