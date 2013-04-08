class StatusLine(object):
    VALID_TICKERS = ['/', '-', '\\', '|']

    def __init__(self, status_line):
        super(StatusLine, self).__init__()
        self._status_line = status_line

        status_line_parts = self._status_line.split()

        ticker = status_line_parts[0]
        if not ticker in StatusLine.VALID_TICKERS:
            raise InvalidTickerException("Invalid ticker '%s' in status line" % ticker)
        self.ticker = ticker

        peers = status_line_parts[1].split('/')
        self.connected_seeders = int(peers[0])
        self.connected_leeches = int(peers[1])
        self.swarm_peers = int(peers[2])

        pieces = status_line_parts[2].strip('[]').split('/')
        self.completed_pieces = int(pieces[0])
        self.total_pieces = int(pieces[1])
        self.available_pieces = int(pieces[2])


class InvalidTickerException(BaseException):
    def __init__(self, *args, **kwargs):
        super(InvalidTickerException, self).__init__(*args, **kwargs)