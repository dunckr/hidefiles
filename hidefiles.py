import sublime, sublime_plugin

class HideFilesCommand(sublime_plugin.TextCommand):
  def run(self,edit):
    print 'hide files'
    file_type = self.view.file_name().split('.').pop()
    hidefiles = sublime.load_settings("hidefiles.sublime-settings")
    exclusions = hidefiles.get(file_type)
    if exclusions is not None:
      settings = sublime.load_settings("Preferences.sublime-settings")
      current_list = settings.get("file_exclude_patterns")
      for exclude in exclusions:
        if exclude not in current_list:
          current_list.append(exclude)
      settings.set("file_exclude_patterns", current_list)
      sublime.save_settings("Preferences.sublime-settings")


class ShowFilesCommand(sublime_plugin.TextCommand):
  def run(self,edit):
    print 'show files'
    file_type = self.view.file_name().split('.').pop()
    hidefiles = sublime.load_settings("hidefiles.sublime-settings")
    exclusions = hidefiles.get(file_type)
    if exclusions is not None:
      settings = sublime.load_settings("Preferences.sublime-settings")
      current_list = settings.get("file_exclude_patterns")
      for exclude in exclusions:
        current_list.remove(exclude)
      settings.set("file_exclude_patterns", current_list)
      sublime.save_settings("Preferences.sublime-settings")
