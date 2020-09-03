#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for count in dir(hidden_4):
        if count[:2] != "__":
            print("{}".format(count))
