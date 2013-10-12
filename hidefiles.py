import sublime, sublime_plugin

class Exclusions():

  def __init__(self,file_name):
    self.file_type = file_name.split('.').pop()
    self.setExclusions()
    self.getSettings()

  def setExclusions(self):
    custom_settings = sublime.load_settings("hidefiles.sublime-settings")
    self.exclusions = custom_settings.get(self.file_type)

  def getSettings(self):
    self.settings = sublime.load_settings("Preferences.sublime-settings")
    self.patterns = self.settings.get("file_exclude_patterns")

  def saveSettings(self):
    self.settings.set("file_exclude_patterns", self.patterns)
    sublime.save_settings("Preferences.sublime-settings")

  def hide(self):
    if self.exclusions is not None:
      for exclude in self.exclusions:
        if exclude not in self.patterns:
          self.patterns.append(exclude)
      self.saveSettings()

  def show(self):
    if self.exclusions is not None:
      for exclude in self.exclusions:
        self.patterns.remove(exclude)
      self.saveSettings()


class HideFilesCommand(sublime_plugin.TextCommand):
  def run(self,edit):
    file_name = self.view.file_name()
    f = Exclusions(file_name)
    f.hide()

class ShowFilesCommand(sublime_plugin.TextCommand):
  def run(self,edit):
    file_name = self.view.file_name()
    f = Exclusions(file_name)
    f.show()
