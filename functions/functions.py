from subprocess 		import run
import os

def openApp(appName):
    appName = appName.strip()
    appName = appName.lower()
    try:
        run(["open", "-a", appName+".app"])
        return "opening "+appName+".app"
    except Exception:
        return "unable to open application "+appName


# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))