from subprocess 		import run

def openApp(appName):
    appName = appName.strip()
    appName = appName.lower()
    try:
        run(["open", "-a", appName+".app"])
        return "opening "+appName+".app"
    except Exception:
        return "unable to open application "+appName