alias la='ls -latr'
alias vi=/usr/bin/vim
alias venvs="source $HOME/.venvs/ovos/bin/activate"    # start an OVOS venv
export LOG="$HOME/.local/state/mycroft"                # OVOS logs
export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$HOME/.venvs/ovos/bin"
export SYS="/etc/systemd/system"
export USR="/etc/systemd/user"
export Z="/usr/local/sbin"
export DBUS_SESSION_BUS_ADDRESS="/run/user/1000/bus"
export XDG_RUNTIME_DIR="/run/user/1000"
source $HOME/.venvs/ovos/bin/activate

