import wikipedia
import time

for i in range(3):
    try:
        result = wikipedia.summary("coral reef", sentences=2)
        print(f"Attempt {i+1} SUCCESS:", result[:50])
        break
    except Exception as e:
        print(f"Attempt {i+1} FAILED:", type(e).__name__, str(e))
        time.sleep(3)