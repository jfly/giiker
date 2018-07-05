import giiker
from subprocess import call

def on_state_change(giiker_state):
    last_move = giiker_state.recent_moves[0]
    if last_move.amount == 1:
        call("set_volume.py 5+", shell=True)
    elif last_move.amount == -1:
        call("set_volume.py 5-", shell=True)
    call("show-volume.sh", shell=True)

def main():
    giiker.initialize(on_state_change=on_state_change)

if __name__ == "__main__":
    main()
