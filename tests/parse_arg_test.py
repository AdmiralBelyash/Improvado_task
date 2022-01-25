from unittest import TestCase
from report.parser_main import parse_arg
import argparse


class ParseArgTest(TestCase):
    def test_parse_arg_token(self):
        parsed = parse_arg(['-t', 'long', '-u', '123'])
        self.assertEqual(parsed.token, 'long')

    def test_parse_arg_user_id(self):
        parsed = parse_arg(['-t', 'long', '-u', '123'])
        self.assertEqual(parsed.user_id, 123)

    def test_parse_arg_format(self):
        parsed = parse_arg(['-t', 'long', '-u', '123', '-f', 'json'])
        self.assertEqual(parsed.format, 'json')

    def test_parse_arg_no_format(self):
        parsed = parse_arg(['-t', 'long', '-u', '123'])
        self.assertEqual(parsed.format, 'csv')

    def test_parse_arg_uncorrect_user_id(self):
        self.assertRaises(parse_arg(['-t', 'long', '-u', 'bebra']), (ValueError, argparse.ArgumentError, SystemExit))
