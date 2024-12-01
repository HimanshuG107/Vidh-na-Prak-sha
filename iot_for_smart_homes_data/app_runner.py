import subprocess
# Run the service corresponding to the user_app
def run_iot_service():
    subprocess.Popen(["D:/iot_for_smart_homes_data/venv/Scripts/python", "app.py"])

if __name__ == '__main__':
    run_iot_service()

    # Graceful Termination of the subprocesses
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nTerminating the processes. Alvida!")
