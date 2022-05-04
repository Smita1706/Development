'''
@Author: Smita Chichkar
@Date: 2022-04-30 09:00:00
@Last Modified by: Smita Chichkar
@Last Modified time:  2022-04-30 09:00:00
@Title :  Write a Stopwatch Program for measuring the time that elapses between
the start and end clicks
'''
import time
def timeConvert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
input("Press Enter to start")
startTime = time.time()
input("Press Enter to stop")
endTime = time.time()
timeLapsed = endTime - startTime
timeConvert(timeLapsed)