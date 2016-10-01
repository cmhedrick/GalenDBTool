#!/usr/bin/env python

import os
import csv
import sqlite3


class GalenDBTool(object):

    def __init__(self, db=None, csv=None):
        self.data_dir = None
        self.file_loc = None
        self.db = None
        self.csv = None

    def set_data_dir(self, path=None):
        if path and os.path.isdir(path):
            self.data_dir = path
        else:
            try:
                if __name__ == '__main__':
                    path = raw_input('Set data directory: ')
                    if path != '' and os.path.isdir(path):
                        self.set_data_dir(path)
                    elif path == '':
                        print 'No characters were provided.'
                        print 'Proceeding to next step.'
                    elif not os.path.isdir(path):
                        print 'Directory does not exist.'
                    else:
                        print 'Something horrible happend.'
            except:
                print 'Failed to set dir.'

    def select_file(self, path=None):
        if path and os.path.isfile(path):
            self.file_loc = path
        else:
            try:
                if __name__ == '__main__':
                    path = raw_input('Path to csv/db: ')
                    if os.path.isfile(path):
                        self.file_loc = path
                    elif path == '':
                        print 'No characters provided'
                        print 'Proceeding to next step.'
                    elif not os.path.isfile(path):
                        print 'File does not exist.'
                    else:
                        print 'Something horrible happend.'
            except:
                print 'Failed to get file'

if __name__ == '__main__':
    g_tool = GalenDBTool()
    g_tool.set_data_dir()
    g_tool.select_file()