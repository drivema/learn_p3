#!/usr/bin/python3

import argparse


def process_command():
    parser = argparse.ArgumentParser()
    g1 = parser.add_argument_group('ahq', '還我西門')
    #g1.add_argument('--ahq', action='store_true', default=False, help='Choose ahq')
    g1.add_argument('--ahq', action='store_true', default=True, help='Choose ahq')
    g1.add_argument('--text1', '-t1', type=str, default='westdoor will be back', help='note for ahq')

    g2 = parser.add_argument_group('jteam', '雷我Fo哥')
    g2.add_argument('--jteam', action='store_true', default=False, help='Choose jteam')
    g2.add_argument('--text2', '-t2', type=str, default='FoFo QQ', help='note for jteam')

    return parser.parse_args()


if __name__ == '__main__':
    args = process_command()
    if args.ahq:
        print(args.text1)
    if args.jteam:
        print(args.text2)