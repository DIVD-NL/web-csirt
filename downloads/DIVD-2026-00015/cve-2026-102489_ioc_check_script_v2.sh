#!/bin/sh
#
# Zammad log check (.gz ok) for IoCs related to cve-2026-102489
# Usage: sh <script> [files/dirs ...]   default: /var/log/zammad /var/log/nginx
#
# shellcheck disable=SC2086  # LOGS is a deliberate space-separated list (POSIX sh has no arrays)
set -u

LOG_PATHS=""

# ANSI colors (auto-disabled when not a terminal)
if [ -t 1 ] && command -v tput >/dev/null 2>&1 && [ "$(tput colors)" -ge 8 ]; then
    RED=$(tput setaf 1); GRN=$(tput setaf 2); BLD=$(tput bold); RST=$(tput sgr0)
else
    RED=""; GRN=""; BLD=""; RST=""
fi

usage() { awk 'NR>1 && /^set /{exit} /^# shellcheck/{next} NR>1{sub(/^# ?/,""); print}' "$0"; exit 0; }

while [ $# -gt 0 ]; do
    case "$1" in
        -h|--help) usage ;;
        --)  shift; while [ $# -gt 0 ]; do LOG_PATHS="$LOG_PATHS $1"; shift; done ;;
        -*)  echo "unknown option: $1" >&2; usage ;;
        *)   LOG_PATHS="$LOG_PATHS $1"; shift ;;
    esac
done

[ -n "$LOG_PATHS" ] || LOG_PATHS="/var/log/zammad /var/log/nginx"

collect_logs() {
    _out=""
    for _d in $LOG_PATHS; do
        if [ -f "$_d" ]; then
            _out="$_out $_d"
        elif [ -d "$_d" ]; then
            _out="$_out $(find "$_d" -type f \( -name 'production.log*' -o -name 'railsserver.log*' -o -name 'websocket.log*' -o -name 'scheduler.log*' -o -name 'nginx.log*' -o -name 'access.log*' -o -name 'error.log*' \) 2>/dev/null)"
        else
            echo "warning: $_d not found" >&2
        fi
    done
    echo "$_out"
}

LOGS=$(collect_logs)
LOGS=${LOGS# }
[ -n "$LOGS" ] || { echo "error: no log files found"; exit 0; }
N_LOGS=$(echo "$LOGS" | wc -w | tr -d ' ')

printf '%s\n' "$(basename "$0") -- Zammad IOC check"
printf 'logs scanned : %d file(s)\n' "$N_LOGS"
printf '\n%s=== session material in error output ===%s\n' "$BLD" "$RST"

HITS=$(zgrep -En 'ERROR -- :.*("Cookie"=>"|@clients=\{)' $LOGS 2>/dev/null | cut -c1-240)
N=0
[ -n "$HITS" ] && N=$(printf '%s\n' "$HITS" | grep -c .)

if [ "$N" -gt 0 ]; then
    printf '\n'
    printf '%s%s######################################################################%s\n' "$RED" "$BLD" "$RST"
    printf '%s%s#                                                                    #%s\n' "$RED" "$BLD" "$RST"
    printf '%s%s#   INDICATORS FOUND -- SESSION MATERIAL IN ERROR OUTPUT             #%s\n' "$RED" "$BLD" "$RST"
    printf '%s%s#   Investigate further.                                             #%s\n' "$RED" "$BLD" "$RST"
    printf '%s%s#                                                                    #%s\n' "$RED" "$BLD" "$RST"
    printf '%s%s######################################################################%s\n' "$RED" "$BLD" "$RST"
    printf '\n  %s%s%d%s matching line(s):\n' "$RED" "$BLD" "$N" "$RST"
    printf '%s\n' "$HITS" | head -10 | sed 's/^/        /'
    [ "$N" -gt 10 ] && printf '        ... %d more\n' $(( N - 10 ))
    COOKIES=$(zgrep -Eh 'ERROR -- :.*("Cookie"=>"|@clients=\{)' $LOGS 2>/dev/null | grep -oE '"Cookie"=>"[^"]*"' | sort -u)
    if [ -n "$COOKIES" ]; then
        printf '\n  %s%sdistinct cookies exposed:%s\n' "$RED" "$BLD" "$RST"
        printf '%s\n' "$COOKIES" | sed 's/^/        /'
    fi
    exit 0
fi

printf '  no session material in error output\n'
printf '\n%s%s----------------------------------------------------------------------%s\n' "$GRN" "$BLD" "$RST"
printf '%s%s  NO INDICATORS in these logs. However, please investigate other signs of abuse like unfamiliar processes and files as well to ensure. %s\n' "$GRN" "$BLD" "$RST"
printf '%s%s----------------------------------------------------------------------%s\n' "$GRN" "$BLD" "$RST"
exit 0
