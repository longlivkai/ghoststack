def notify(summary):
    with open("log.txt", "a") as log:
        log.write(summary + "\n\n")
    print("[LOGGED] New interaction saved.")
