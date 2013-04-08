#!/usr/bin/env python2.7

from subprocess import Popen, PIPE
from status_line import StatusLine

process = Popen(['ctorrent', 'NZBDrop.dmg.torrent'], stdin=PIPE, stdout=PIPE, stderr=PIPE)

while True:
    line = process.stdout.readline()
    if line == '':
        break
    else:
        try:
            status_line = StatusLine(line)
            if status_line.completed_pieces == status_line.total_pieces:
                print "We're done!",
                break
            print status_line.ticker,
        except BaseException as ex:
            pass
process.terminate()