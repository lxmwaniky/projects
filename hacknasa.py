import time

progress_symbols = [" ####", " ########", " ############", " ################", " ####################"]

for i in range(len(progress_symbols)):
    print("\rHacking NASA", end='', flush=True)
    time.sleep(1)
    print(progress_symbols[i], end='', flush=True)
    time.sleep(3)
    print(" {}%".format((i + 1) * 20), end='', flush=True)

    if (i + 1) * 20 == 80:
        time.sleep(5)

    time.sleep(1)

print("\nNasa Hacked Successfully!!!")

for i in range(len(progress_symbols)):
    print("\rDownloading Files", end='', flush=True)
    time.sleep(1)
    print(progress_symbols[i], end='', flush=True)
    time.sleep(2)
    print(" {}%".format((i + 1) * 20), end='', flush=True)

    if (i + 1) * 20 == 80:
        time.sleep(5)

    time.sleep(1)

print("\n...........Download Complete")

for i in range(len(progress_symbols)):
    print("\rClearing Log", end='', flush=True)
    time.sleep(1)
    print(progress_symbols[i], end='', flush=True)
    time.sleep(1)
    print(" {}%".format((i + 1) * 20), end='', flush=True)

    if (i + 1) * 20 == 80:
        time.sleep(1)

    time.sleep(1)

print("\nLog Cleared!!!!")

time.sleep(5)
