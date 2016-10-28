#!/bin/sh -e

~/Code/Personal/jenkins-tools/bin/delete-job.sh lsl-processor || true
~/Code/Personal/jenkins-tools/bin/put-job.sh lsl-processor job.xml
