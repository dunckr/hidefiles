import sublime, sublime_plugin

# class Files():

#   def __init__(self,file_type):
#     self.file_type = file_type.split('.').pop()
#     self.setExlcusions()
#     self.getPreferences()

#   def setExlcusions(self):
#     custom_settings = sublime.load_settings("hidefiles.sublime-settings")
#     self.exclusions = custom_settings.get(self.file_type)

#   def getPreferences(self):
#     settings = sublime.load_settings("Preferences.sublime-settings")
#     self.preferences = settings.get("file_exclude_patterns")

#   def append(self):
#     if exclusions is not None:
#       for pattern in patterns:
#         if pattern not in self.preferences:
#           self.exclusions.append(pattern)
#           # self.remove(patterns)
#     preferences.set("file_exclude_patterns", zzzzzz!!!)
#     sublime.save_settings("Preferences.sublime-settings")

    # file_type = self.view.file_name().split('.').pop()
    # hidefiles = sublime.load_settings("hidefiles.sublime-settings")
    # exclusions = hidefiles.get(file_type)
    # if exclusions is not None:
    #   settings = sublime.load_settings("Preferences.sublime-settings")
    #   current_list = settings.get("file_exclude_patterns")
    #   for exclude in exclusions:
    #     if exclude not in current_list:
    #       current_list.append(exclude)
    #   settings.set("file_exclude_patterns", current_list)
    #   sublime.save_settings("Preferences.sublime-settings")


  # def remove(self, patterns):
  #   print 'refactor'

  # def run(self):
  # def load(self):
  #   exclusions = hidefiles.get(file_type)
  #   custom_settings = sublime.load_settings("hidefiles.sublime-settings")


class Files():

  def __init__(self,file_name):
    self.file_type = file_name.split('.').pop()

  def hide(self):
    hidefiles = sublime.load_settings("hidefiles.sublime-settings")
    exclusions = hidefiles.get(self.file_type)
    if exclusions is not None:
      settings = sublime.load_settings("Preferences.sublime-settings")
      current_list = settings.get("file_exclude_patterns")
      for exclude in exclusions:
        if exclude not in current_list:
          current_list.append(exclude)
      settings.set("file_exclude_patterns", current_list)
      sublime.save_settings("Preferences.sublime-settings")

  def show(self):
    hidefiles = sublime.load_settings("hidefiles.sublime-settings")
    exclusions = hidefiles.get(self.file_type)
    if exclusions is not None:
      settings = sublime.load_settings("Preferences.sublime-settings")
      current_list = settings.get("file_exclude_patterns")
      for exclude in exclusions:
        current_list.remove(exclude)
      settings.set("file_exclude_patterns", current_list)
      sublime.save_settings("Preferences.sublime-settings")


class HideFilesCommand(sublime_plugin.TextCommand):
  def run(self,edit):
    print 'hide files'

    file_name = self.view.file_name()
    f = Files(file_name)
    f.hide()

    # file_type = self.view.file_name().split('.').pop()
    # hidefiles = sublime.load_settings("hidefiles.sublime-settings")
    # exclusions = hidefiles.get(file_type)
    # if exclusions is not None:
    #   settings = sublime.load_settings("Preferences.sublime-settings")
    #   current_list = settings.get("file_exclude_patterns")
    #   for exclude in exclusions:
    #     if exclude not in current_list:
    #       current_list.append(exclude)
    #   settings.set("file_exclude_patterns", current_list)
    #   sublime.save_settings("Preferences.sublime-settings")


class ShowFilesCommand(sublime_plugin.TextCommand):
  def run(self,edit):
    print 'show files'
    file_name = self.view.file_name()
    f = Files(file_name)
    f.show()

    # file_type = self.view.file_name().split('.').pop()
    # hidefiles = sublime.load_settings("hidefiles.sublime-settings")
    # exclusions = hidefiles.get(file_type)
    # if exclusions is not None:
    #   settings = sublime.load_settings("Preferences.sublime-settings")
    #   current_list = settings.get("file_exclude_patterns")
    #   for exclude in exclusions:
    #     current_list.remove(exclude)
    #   settings.set("file_exclude_patterns", current_list)
    #   sublime.save_settings("Preferences.sublime-settings")
