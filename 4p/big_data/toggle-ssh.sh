#!/bin/bash
# toggle-ssh.sh
# Liga ou desliga o SSH no macOS

ACTION=$1

if [ "$ACTION" != "on" ] && [ "$ACTION" != "off" ]; then
    echo "Uso: $0 [on|off]"
    exit 1
fi

if [ "$ACTION" = "on" ]; then
    sudo launchctl load -w /System/Library/LaunchDaemons/ssh.plist
    echo "SSH ligado"
else
    sudo launchctl unload -w /System/Library/LaunchDaemons/ssh.plist
    echo "SSH desligado"
fi

