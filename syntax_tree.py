import sublime
import sublime_plugin
import subprocess

class SyntaxTreeOnSave(sublime_plugin.EventListener):
  def on_post_save_async(self, view):
    settings = sublime.load_settings("syntax_tree.sublime-settings")
    stree_command_path = settings.get("stree_command_path")

    if not stree_command_path:
      sublime.error_message("SyntaxTree: Please specify the path to your `stree` command with the `stree_command_path` setting.")
    else:
      format_on_save = settings.get("format_on_save", False)

      if format_on_save == True and view.file_name().endswith('.rb'):
        print("SyntaxTree: Running `write` on save.")

        output = subprocess.check_output([stree_command_path, 'write', view.file_name()], stderr=subprocess.STDOUT, universal_newlines=True)

class FormatSyntaxTreeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    settings = sublime.load_settings("syntax_tree.sublime-settings")
    stree_command_path = settings.get("stree_command_path")

    if not stree_command_path:
      sublime.error_message("SyntaxTree: Please specify the path to your `stree` command with the `stree_command_path` setting.")

    if view.file_name().endswith('.rb'):
      print("SyntaxTree: Running `write` on command.")

      output = subprocess.check_output([stree_command_path, 'write', view.file_name()], stderr=subprocess.STDOUT, universal_newlines=True)
