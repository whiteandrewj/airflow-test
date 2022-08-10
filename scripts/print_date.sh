#!/bin/bash

echo "Time in IST: "$(date '+%m/%d/%Y %H:%M' --date="TZ=\"Asia/Kolkata\" $1")
