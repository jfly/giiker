from subprocess import call
import argparse

import giiker
import kodi
import kobo

T_PERM = "B D B' D' B' L B B D' B' D' B D B' L'".split()
SEXY_MOVE = "B D B' D'".split()
TOGGLE_REMOTE = ("U U' "*2).split()

move_history = []

kodi_event_client = None
remote_control = True

def kodi_on_state_change(giiker_state):
    global remote_control, move_history, kodi_event_client
    if kodi_event_client is None:
        kodi_event_client = kodi.KodiEventClient()

    last_move = giiker_state.last_move
    move_history.append(last_move)

    if alg_just_applied(TOGGLE_REMOTE):
        remote_control = not(remote_control)
        if remote_control:
            kodi_event_client.send_notification("Welcome back", "Your cube is now a remote control again.")
        else:
            kodi_event_client.send_notification("Happy cubing!", "Toggle the white face to go back to being a remote control.")
        move_history = []
        return

    if not remote_control:
        return

    if alg_just_applied(SEXY_MOVE):
        kodi.json_rpc("Player.PlayPause", [1, "toggle"])
        return

    if last_move.face == "U":
        if last_move.amount == 1:
            kodi.json_rpc("Application.SetVolume", {"volume": "increment"})
        elif last_move.amount == -1:
            kodi.json_rpc("Application.SetVolume", {"volume": "decrement"})
        return

    if last_move.face == "R":
        if last_move.amount == 1:
            kodi_event_client.press_button("right")
        elif last_move.amount == -1:
            kodi_event_client.press_button("left")

    if last_move.face == "L":
        if last_move.amount == 1:
            kodi_event_client.press_button("down")
        elif last_move.amount == -1:
            kodi_event_client.press_button("up")

    if last_move.face == "F":
        if last_move.amount == 1:
            kodi_event_client.press_button("enter")
        elif last_move.amount == -1:
            kodi_event_client.press_button("backspace")

def kobo_on_state_change(giiker_state):
    global remote_control, move_history

    last_move = giiker_state.last_move
    move_history.append(last_move)

    if last_move.amount == 1:
        kobo.next_page()
    elif last_move.amount == -1:
        kobo.previous_page()

def alg_just_applied(alg):
    if len(move_history) < len(alg):
        return False

    for correct_move_str, actual_move in zip(alg, move_history[-len(alg):]):
        if correct_move_str != str(actual_move):
            return False

    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["kodi", "kobo"])
    args = parser.parse_args()

    if args.mode == "kodi":
        giiker.initialize(on_state_change=kodi_on_state_change)
    elif args.mode == "kobo":
        giiker.initialize(on_state_change=kobo_on_state_change)
    else:
        assert False

if __name__ == "__main__":
    main()
