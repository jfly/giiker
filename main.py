from subprocess import call

import giiker

T_PERM = "B D B' D' B' L B B D' B' D' B D B' L'".split()
TOGGLE_REMOTE = ("U U' "*2).split()

remote_control = True
move_history = []


def on_state_change(giiker_state):
    global remote_control, move_history

    last_move = giiker_state.last_move
    move_history.append(last_move)

    if alg_just_applied(TOGGLE_REMOTE):
        remote_control = not(remote_control)
        if remote_control:
            print("Congratulations, you have entered remote control mode!")
        else:
            print("Happy cubing!")
        move_history = []
        return

    if not remote_control:
        return

    if alg_just_applied(T_PERM):
        print("Nice T perm!")
        call("xdotool key --clearmodifiers XF86AudioPlay", shell=True)
        return

    if last_move.face == "U":
        if last_move.amount == 1:
            call("set_volume.py 5+", shell=True)
        elif last_move.amount == -1:
            call("set_volume.py 5-", shell=True)
        call("show-volume.sh", shell=True)
        return

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
