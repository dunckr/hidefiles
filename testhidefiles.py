import sublime, sublime_plugin

import unittest, json

import hidefiles

class TestHideFilesCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    print 'running...'


    settings = self.loadFixtures()
    print settings
    # f = HideFiles.HideFiles(settings)
    # print f

  def loadFixtures(self):
    json_data= open('./fixtures/settings.json')
    data = json.load(json_data)
    json_data.close()
    return data

