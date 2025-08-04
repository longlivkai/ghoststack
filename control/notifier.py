def notify(summary):
    with open("log.txt", "a") as log:
        log.write(json.dumps(summary, indent=2) + "\n\n")
    print("[LOGGED] New interaction saved.")
