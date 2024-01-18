import sublime
import sublime_plugin
import subprocess

class SyntaxTreeOnSave(sublime_plugin.EventListener):
  def on_post_save_async(self, view):
    settings = sublime.load_settings("syntax_tree.sublime-settings")
    format_on_save = settings.get("format_on_save", False)

    if format_on_save == True and view.file_name().endswith('.rb'):
      print("SyntaxTree: Running on save")

      stree_command_path = settings.get("stree_command_path")
      output = subprocess.check_output([stree_command_path, 'write', view.file_name()], stderr=subprocess.STDOUT, universal_newlines=True)
