import BigRobot

run = BigRobot.Move("w",1)

back = BigRobot.Move("s",1)

left = BigRobot.Move("a",1)

right = BigRobot.Move("d",1)

stop = BigRobot.Move("p",1)


run.mover()
back.mover()
left.mover()
right.mover()
stop.mover()
