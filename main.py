from subprocess import call

import giiker

move_history = []

T_PERM = "B D B' D' B' L B B D' B' D' B D B' L'".split()

def on_state_change(giiker_state):
    last_move = giiker_state.last_move
    move_history.append(last_move)

    if alg_just_applied(T_PERM):
        print("Nice T perm!")
        call("xdotool key --clearmodifiers XF86AudioPlay", shell=True)

    if last_move.face == "U":
        if last_move.amount == 1:
            call("set_volume.py 5+", shell=True)
        elif last_move.amount == -1:
            call("set_volume.py 5-", shell=True)
        call("show-volume.sh", shell=True)

def alg_just_applied(alg):
    if len(move_history) < len(alg):
        return False

    for correct_move_str, actual_move in zip(alg, move_history[-len(alg):]):
        if correct_move_str != str(actual_move):
            return False

    return True

def main():
    giiker.initialize(on_state_change=on_state_change)

if __name__ == "__main__":
    main()
