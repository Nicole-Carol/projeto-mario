import cv2

camera = cv2.VideoCapture(0)
print("\n--- TEMPLATE CAPTURE ---")
print("Press '1': Crouch (abaixar_template.png)")
print("Press '2': Walk Left (mao_andar_left_template.png)")
print("Press '3': Walk Right (mao_andar_right_template.png)")
print("Press '4': Jump (mao_pular_template.png)")
print("Press '5': Spin Jump (mao_pular_quebrar_template.png)")
print("Press '6': Flower (flor_template.png)")
print("Press '7': Stop (mao_stop_template.png)")
print("Press 'q': Quit\n")

while True:
    success, frame = camera.read()
    if not success:
        break
    
    frame = cv2.flip(frame, 1)
    height, width, _ = frame.shape
    
    # Square region for template capture
    start_x, start_y = int(width/2) - 75, int(height/2) - 75
    end_x, end_y = int(width/2) + 75, int(height/2) + 75
    
    cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (255, 0, 0), 2)
    cv2.imshow("Template Capture - Place gesture inside box", frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key in [ord('1'), ord('2'), ord('3'), ord('4'), ord('5'), ord('6'), ord('7')]:
        region_of_interest = frame[start_y:end_y, start_x:end_x]
        gray_roi = cv2.cvtColor(region_of_interest, cv2.COLOR_BGR2GRAY)
        
        if key == ord('1'):
            cv2.imwrite("abaixar_template.png", gray_roi)
            print("[SAVED] abaixar_template.png")
        elif key == ord('2'):
            cv2.imwrite("mao_andar_left_template.png", gray_roi)
            print("[SAVED] mao_andar_left_template.png")
        elif key == ord('3'):
            cv2.imwrite("mao_andar_right_template.png", gray_roi)
            print("[SAVED] mao_andar_right_template.png")
        elif key == ord('4'):
            cv2.imwrite("mao_pular_template.png", gray_roi)
            print("[SAVED] mao_pular_template.png")
        elif key == ord('5'):
            cv2.imwrite("mao_pular_quebrar_template.png", gray_roi)
            print("[SAVED] mao_pular_quebrar_template.png")
        elif key == ord('6'):
            cv2.imwrite("flor_template.png", gray_roi)
            print("[SAVED] flor_template.png")
        elif key == ord('7'):
            cv2.imwrite("mao_stop_template.png", gray_roi)
            print("[SAVED] mao_stop_template.png")
            
    elif key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()