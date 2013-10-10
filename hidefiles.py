import sublime, sublime_plugin

class HideFilesNextCommand(sublime_plugin.TextCommand):
  def run(self,edit):
    print 'next command'
    hidefiles = sublime.load_settings("hidefiles.sublime-settings")
    # print hidefiles.get('coffeescript')
    for i, val in enumerate(hidefiles):
      print i + ' ' + val



class HideFilesPreviousCommand(sublime_plugin.TextCommand):
  def run(self,edit):
    # load the next settings in list
    print 'previous command'

class HideFiles:
  def __init__(self,settings):
    # load the hide file settings
    # set the current
    self.file_exclude_patterns = settings.get('file_exclude_patterns')
    self.folder_exclude_patterns = settings.get('folder_exclude_patterns')

  def next(self):
    print self.file_exclude_patterns
    # move to the next
    # then load

#   def prev(self):
#     # move to prev
#     # then load

#   def load(self):
#     # load then save

#   def save(self):
#     # save the current files





class HideFilesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.test()
        # print self.getSettings()
        # self.insertSettings()
        # print self.getSettings()
        # self.removeSettings()
        # print self.getSettings()

        # files = Files(settings='test')

        settings = sublime.load_settings("Preferences.sublime-settings")
        f = Files(settings)
        print settings
        f.toString()


    def test(self):
      print 'inside test'

    def getSettings(self):
      s = sublime.load_settings("Preferences.sublime-settings")
      return s.get("file_exclude_patterns")

    def insertSettings(self):
      s = sublime.load_settings("Preferences.sublime-settings")
      l = s.get("file_exclude_patterns")
      l.append("*.zzz")
      s.set("file_exclude_patterns", l)
      sublime.save_settings("Preferences.sublime-settings")

    def removeSettings(self):
      s = sublime.load_settings("Preferences.sublime-settings")
      l = s.get("file_exclude_patterns")
      l.remove("*.zzz")
      s.set("file_exclude_patterns", l)




#   def __init__(self):
#     print 'inside constructor'

    # def __init__(self, settings):
#       self.file_exclude_patterns = ''
#       self.folder_exclude_patterns = ''




#     s = sublime.load_settings("Preferences.sublime-settings")
#     p = s.get("folder_exclude_patterns")
#     print p



###
# run:
# view.run_command('example')
# TODO
# Preferences.sublime-settings
#  add to array
#   folder_exclude_patterns
#   file_exclude_patterns
#  remove from array
#   folder_exclude_patterns
#   file_exclude_patterns
#
# read from json
# s = sublime.load_settings("Preference Helper.sublime-settings")
#       exclude_packages = s.get("exclude_packages", [])
#       if package_name not in exclude_packages:
#         exclude_packages += [package_name]
#       s.set("exclude_packages", exclude_packages)
#       sublime.save_settings("Preference Helper.sublime-settings")


# >>> s = sublime.load_settings("Preferences.sublime-settings")
# >>> s.get("ignored_packages")
# ['Vintage']
# >>> l = s.get("ignored_packages")
# >>> l.append("RestructuredText")
# >>> s.set("ignored_packages", l)
# ignored packages updated to: [Vintage, RestructuredText]
# >>> sublime.save_settings("Preferences.sublime-settings")
# >>> s.get("ignored_packages")
# ['Vintage', 'RestructuredText']
