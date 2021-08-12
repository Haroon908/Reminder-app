import time

from plyer import notification

if __name__ == "__main__":
    while True:
            notification.notify(
                title = "**Please start programming now!!",
                message = "Programming is really necessory for every programming student."
                          "You have to programm.Wake up from life of Baghairti",
                app_icon = "C:/Users/SOFTAGE/PycharmProjects/Reminder/icon.ico",
                timeout =10
                    )
            time.sleep(60*60)