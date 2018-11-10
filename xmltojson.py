# -*- coding:utf-8 -*-

import sys
import json
import xmltodict


def xmltojson(path):
    # xmlファイルの読み込み
    with open(path, 'r') as xml_file:
        xml_str = xml_file.read()

    # xmlをパースし辞書型に格納
    tmp_dict = xmltodict.parse(xml_str)

    # json形式でファイル出力
    with open('data/Dam.json', 'w') as rslt_file:
        json.dump(tmp_dict, rslt_file, ensure_ascii=False, indent=2)


def main():
    # 引数指定
    args = sys.argv
    argc = len(args)

    if (argc != 2):
        print('Usage:  python %s [FILE]' % args[0])
        quit()

    xmltojson(args[1])


if __name__ == '__main__':
    main()
