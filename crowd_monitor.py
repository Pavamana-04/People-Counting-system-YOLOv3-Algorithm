import cv2

def crowd():
    output_path = r"E:\Mini PROJECT\Person_counting\output data\output_video.avi"  # Output path for the video

    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)  # Set width
    cap.set(4, 720)   # Set height
    cap.set(10, 70)   # Set brightness

    classNames = []
    classFile = 'coco.data'
    with open(classFile, 'rt') as f:
        classNames = f.read().rstrip('\n').split('\n')

    configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    weightsPath = 'frozen_inference_graph.pb'

    net = cv2.dnn_DetectionModel(weightsPath, configPath)
    net.setInputSize(320, 320)
    net.setInputScale(1.0 / 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)

    # Define video writer
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (1280, 720))

    while True:
        success, img = cap.read()
        
        if not success:
            print("Failed to capture video.")
            break

        classIds, confs, bbox = net.detect(img, confThreshold=0.5)
        person_count = 0

        if len(classIds) != 0:
            for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
                if classId - 1 == 0:  # Detect only 'person'
                    person_count += 1
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    cv2.putText(img, f'Person: {confidence:.2f}', (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.putText(img, f'Total Persons: {person_count}', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

        # Write the frame to the video file
        out.write(img)

        cv2.imshow("crowd_monitor", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break

    cap.release()
    out.release()  # Release the video writer
    cv2.destroyAllWindows()
    print(f"Video saved as {output_path}")  # Confirmation messag