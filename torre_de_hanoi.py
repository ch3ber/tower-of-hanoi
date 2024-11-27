# Author: Eber Alejo (ch3ber)
# External refecences:
# https://en.wikipedia.org/wiki/Tower_of_Hanoi (Description)
# https://www.geogebra.org/m/NqyWJVra (Visualization and playground)

# Description:
# ----------------
#
# The Tower of Hanoi is a mathematical game or puzzle.
# It consists of three rods and a number of disks of different sizes, which can be slid onto any rod.
# The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape.
# The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
# 1. Only one disk can be moved at a time.
# 2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack.
# 3. No disk may be placed on top of a smaller disk.


import time

stack1 = []
stack2 = []
stack3 = []
totalMovements = 0

DISK_ICON = "█"  # Change to any character you want
MOVEMENT_DELAY = (
    0.35  # Change to adjust the speed in seconds of the sorting. 0 is no delay.
)


def fillStacks(n):
    for i in range(1, n + 1):
        width = 2 * i - 1
        padding = " " * (n - i)
        stack1.append(padding + DISK_ICON * width + padding)
    stack2.extend([" " * (2 * n - 1)] * n)
    stack3.extend([" " * (2 * n - 1)] * n)


def convertStacksToTable(stack1, stack2, stack3, totalDisks):
    table = []
    for i in range(totalDisks):
        row = []
        row.append(stack1[i] if stack1[i].strip() else " " * len(stack1[i]))
        row.append(stack2[i] if stack2[i].strip() else " " * len(stack2[i]))
        row.append(stack3[i] if stack3[i].strip() else " " * len(stack3[i]))
        table.append(row)
    return table


def printStatus():
    print("\u001b[H\u001b[J", end="")  # Clear screen
    table = convertStacksToTable(stack1, stack2, stack3, len(stack1))
    for row in table:
        print(
            f"{row[0]:<{len(stack1[0]) + 4}} | {row[1]:<{len(stack1[0]) + 4}} | {row[2]:<{len(stack1[0]) + 4}}"
        )
    print("-" * (len(stack1[0]) * 3 + 10))


def moveDisk(fromStack, toStack, totalDisks):
    global totalMovements
    # Find the topmost disk in fromStack
    for i in range(totalDisks):
        if fromStack[i].strip():
            disk = fromStack[i]
            fromStack[i] = " " * len(fromStack[i])
            break
    print(f"Move disk {disk.strip()}")

    # Place the disk in toStack
    for i in range(totalDisks - 1, -1, -1):
        if not toStack[i].strip():
            toStack[i] = disk
            break

    totalMovements += 1


def hanoi(n, fromStack, toStack, auxStack, totalDisks):
    if n == 1:
        moveDisk(fromStack, toStack, totalDisks)
        printStatus()
        time.sleep(MOVEMENT_DELAY)
        return
    hanoi(n - 1, fromStack, auxStack, toStack, totalDisks)
    moveDisk(fromStack, toStack, totalDisks)
    printStatus()
    time.sleep(MOVEMENT_DELAY)
    hanoi(n - 1, auxStack, toStack, fromStack, totalDisks)


def main():
    totalDisks = int(input("Enter the number of disks: "))
    fillStacks(totalDisks)
    printStatus()

    hanoi(totalDisks, stack1, stack3, stack2, totalDisks)

    print("[*] Sorting completed!")
    print("Total movements: ", totalMovements)


if __name__ == "__main__":
    main()
