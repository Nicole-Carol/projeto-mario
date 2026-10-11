import cv2
import keyboard
import time
import os

# ==========================================
# SETTINGS
# ==========================================
HAND_THRESHOLD = 0.60  # Increased confidence so it doesn't trigger on background noise

# Key press durations (in seconds)
TIME_CROUCH = 0.20
TIME_WALK_LEFT = 0.15
TIME_WALK_RIGHT = 0.15
TIME_JUMP = 0.30
TIME_SPIN_JUMP = 0.30
TIME_FLOWER = 0.15

GESTURE_COOLDOWN = 0.30  # Slightly increased to prevent spamming

active_key = None
command_start_time = 0.0
command_duration = 0.0
last_command_time = 0.0

# ==========================================
# LOAD TEMPLATES
# ==========================================
template_files = {
    "Crouch": "abaixar_template.png",
    "Walk Left": "mao_andar_left_template.png",
    "Walk Right": "mao_andar_right_template.png",
    "Jump": "mao_pular_template.png",
    "Spin Jump": "mao_pular_quebrar_template.png",
    "Flower": "flor_template.png",
    "Stop": "mao_stop_template.png"
}

templates = {}

print("\n--- CHECKING TEMPLATES ---")
for action_name, filepath in template_files.items():
    if not os.path.isfile(filepath):
        print(f"[MISSING] File not found: {filepath}")
        continue

    image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"[ERROR] Could not load: {filepath}")
        continue

    templates[action_name] = image
    print(f"[LOADED] {action_name} -> {filepath}")
print("---------------------------\n")

# ==========================================
# DETECT TEMPLATE
# ==========================================
def detect(frame_gray, template, threshold):
    if template is None:
        return None

    th, tw = template.shape
    fh, fw = frame_gray.shape

    if th > fh or tw > fw:
        return None

    result = cv2.matchTemplate(frame_gray, template, cv2.TM_CCOEFF_NORMED)
    _, confidence, _, position = cv2.minMaxLoc(result)

    if confidence >= threshold:
        x, y = position
        return {"x": x, "y": y, "w": tw, "h": th, "confidence": float(confidence)}

    return None

# ==========================================
# KEYBOARD CONTROL
# ==========================================
def start_command(key, duration):
    global active_key, command_start_time, command_duration, last_command_time

    now = time.monotonic()
    
    if active_key is not None or (now - last_command_time < GESTURE_COOLDOWN):
        return False

    keyboard.press(key)
    active_key = key
    command_start_time = now
    command_duration = duration
    last_command_time = now + duration
    return True

def update_key():
    global active_key

    if active_key is None:
        return

    now = time.monotonic()
    if now - command_start_time >= command_duration:
        keyboard.release(active_key)
        active_key = None

def release_all_keys():
    global active_key
    for key in ["down", "left", "right", "c", "a", "x"]:
        try:
            keyboard.release(key)
        except Exception:
            pass
    active_key = None

# ==========================================
# WEBCAM CAPTURE & EXECUTION
# ==========================================
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Could not open webcam.")

print("Camera started! Press Q to exit.\n")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image.")
            break

        frame = cv2.flip(frame, 1)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        update_key()
        best_match = None

        # Evaluates all templates and picks the highest confidence match
        for action_name, template in templates.items():
            detection = detect(gray_frame, template, HAND_THRESHOLD)
            
            if detection is not None:
                if best_match is None or detection["confidence"] > best_match["confidence"]:
                    detection["action"] = action_name
                    best_match = detection

        if best_match is not None:
            detected_action = best_match["action"]
            x, y, w, h = best_match["x"], best_match["y"], best_match["w"], best_match["h"]
            conf = best_match["confidence"]

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"{detected_action} ({conf:.2f})", 
                        (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            if detected_action == "Crouch":
                start_command("down", TIME_CROUCH)
            elif detected_action == "Walk Left":
                start_command("left", TIME_WALK_LEFT)
            elif detected_action == "Walk Right":
                start_command("right", TIME_WALK_RIGHT)
            elif detected_action == "Jump":
                start_command("c", TIME_JUMP)
            elif detected_action == "Spin Jump":
                start_command("a", TIME_SPIN_JUMP)
            elif detected_action == "Flower":
                start_command("x", TIME_FLOWER)
            elif detected_action == "Stop":
                release_all_keys()
        else:
            detected_action = "None"

        cv2.putText(frame, f"Current Action: {detected_action}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        
        cv2.imshow("Computer Vision - Mario Control", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

except KeyboardInterrupt:
    print("\nProgram interrupted.")

finally:
    release_all_keys()
    cap.release()
    cv2.destroyAllWindows()
    print("Camera closed.")