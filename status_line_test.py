import unittest
from status_line import StatusLine, InvalidTickerException

SAMPLE_STATUS_LINE = "/ 0/33/110 [672/672/672] 0MB,1130MB | 0,20K/s | 0,0K E:0,31"
DIFFERENT_SAMPLE_STATUS_LINE = "/ 42/12/88 [123/456/789] 12MB,225MB | 21,17K/s | 3,8K E:3,17"

class StatusLineTest(unittest.TestCase):
    def test_ticker_should_be_parsed(self):
        for valid_ticker in StatusLine.VALID_TICKERS:
            status_line = StatusLine(valid_ticker + SAMPLE_STATUS_LINE[1:])
            self.assertEquals(valid_ticker, status_line.ticker)

    def test_invalid_ticker_should_throw_exception(self):
        status_line_with_valid_ticker = "R blah blah"
        try:
            StatusLine(status_line_with_valid_ticker)
            self.fail("Should raise InvalidTickerException")
        except InvalidTickerException as ex:
            self.assertEquals("Invalid ticker 'R' in status line", ex.message)

    def test_valid_tickers_has_the_right_values(self):
        self.assertEquals(['/', '-', '\\', '|'], StatusLine.VALID_TICKERS)

    def test_connected_seeders_count_is_parsed(self):
        status_line = StatusLine(SAMPLE_STATUS_LINE)
        self.assertEquals(0, status_line.connected_seeders)

    def test_different_connected_seeders_count_is_parsed(self):
        status_line = StatusLine(DIFFERENT_SAMPLE_STATUS_LINE)
        self.assertEquals(42, status_line.connected_seeders)

    def test_connected_leeches_count_is_parsed(self):
        status_line = StatusLine(SAMPLE_STATUS_LINE)
        self.assertEquals(33, status_line.connected_leeches)

    def test_different_connected_leeches_count_is_parsed(self):
        status_line = StatusLine(DIFFERENT_SAMPLE_STATUS_LINE)
        self.assertEquals(12, status_line.connected_leeches)

    def test_swarm_peers_count_is_parsed(self):
        status_line = StatusLine(SAMPLE_STATUS_LINE)
        self.assertEquals(110, status_line.swarm_peers)

    def test_different_swarm_peers_count_is_parsed(self):
        status_line = StatusLine(DIFFERENT_SAMPLE_STATUS_LINE)
        self.assertEquals(88, status_line.swarm_peers)

    def test_completed_pieces_count_is_parsed(self):
        status_line = StatusLine(SAMPLE_STATUS_LINE)
        self.assertEquals(672, status_line.completed_pieces)

    def test_different_completed_pieces_count_is_parsed(self):
        status_line = StatusLine(DIFFERENT_SAMPLE_STATUS_LINE)
        self.assertEquals(123, status_line.completed_pieces)

    def test_total_pieces_count_is_parsed(self):
        status_line = StatusLine(SAMPLE_STATUS_LINE)
        self.assertEquals(672, status_line.total_pieces)

    def test_different_total_pieces_count_is_parsed(self):
        status_line = StatusLine(DIFFERENT_SAMPLE_STATUS_LINE)
        self.assertEquals(456, status_line.total_pieces)

    def test_available_pieces_count_is_parsed(self):
        status_line = StatusLine(SAMPLE_STATUS_LINE)
        self.assertEquals(672, status_line.available_pieces)

    def test_different_available_pieces_count_is_parsed(self):
        status_line = StatusLine(DIFFERENT_SAMPLE_STATUS_LINE)
        self.assertEquals(789, status_line.available_pieces)
