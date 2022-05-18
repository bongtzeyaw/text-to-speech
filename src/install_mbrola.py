import subprocess

def install():

    # To do before the installation
    subprocess.call(["sudo","apt-get","update"])

    # Install mbrola

    subprocess.call(["sudo","apt","install","mbrola"])

    # Install all 7 french voices
    for i in range(1,8):
        subprocess.call(["sudo", "apt", "install","mbrola-fr{}".format(i)])

        # Install english voices (1 britannic and 3 us)

    subprocess.call(["sudo", "apt", "install","mbrola-en1"])
    for i in range(1,4):
        subprocess.call(["sudo", "apt", "install","mbrola-us{}".format(i)])



if __name__ == "__main__":
    install()
