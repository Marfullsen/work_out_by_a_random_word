import sys

excersiseCards = {
    "a":[50,"jumping jacks"],
    "b":[20,"crunches"],
    "c":[30,"squats"],
    "d":[15,"pushups"],
    "e":[60,"wall sit"],
    "f":[10,"burpees"],
    "g":[20,"arm circles"],
    "h":[20,"squats"],
    "i":[30,"jumping jacks"],
    "j":[15,"crunches"],
    "k":[10,"pushups"],
    "l":[120,"wall sit"],
    "m":[20,"burpees"],
    "n":[25,"burpees"],
    "o":[40,"jumping jacks"],
    "p":[15,"arm circles"],
    "q":[30,"crunches"],
    "r":[15,"pushups"],
    "s":[30,"burpees"],
    "t":[15,"squats"],
    "u":[30,"arm circles"],
    "v":[180,"wall sit"],
    "w":[20,"burpees"],
    "x":[60,"jumping jacks"],
    "y":[10,"crunches"],
    "z":[20,"pushups"],
    " ":[60,"rest"]
}

if len(sys.argv) < 2:
    print("Usage:./workout.py word")
    sys.exit(0)

name = ' '.join(sys.argv[1:])
print("Workout for %s:\n" % (name))

for c in name.lower():
    print("%d\t%s" % (excersiseCards[c][0], excersiseCards[c][1]))
