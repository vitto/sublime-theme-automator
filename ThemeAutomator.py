import sublime, sublime_plugin, os

sublime_settings = None
plugin_settings = None
schemes = None
automate_selection = None

def plugin_loaded():
	global sublime_settings, plugin_settings, schemes, automate_selection
	sublime_settings = sublime.load_settings('Preferences.sublime-settings')
	plugin_settings = sublime.load_settings('ThemeAutomator.sublime-settings')
	schemes = plugin_settings.get('schemes')
	automate_selection = plugin_settings.get('automate_selection')
	if automate_selection is None:
		automate_selection = True

def check_empty_color_scheme(view):
	if plugin_settings.get('color_scheme') == '':
		plugin_settings.set('color_scheme', sublime_settings.get('color_scheme'))
		sublime.save_settings('ThemeAutomator.sublime-settings')

def extensions():
	extensions = []
	if schemes != None:
		for scheme in schemes:
			extensions.append(scheme.get('extension'))
		return extensions
	else:
		return []

def save_scheme(color_scheme):
		sublime_settings.set('color_scheme', color_scheme)
		sublime.save_settings('Preferences.sublime-settings')

def theme(ext):
	for index, scheme in enumerate(schemes):
		if scheme['extension'] == ext:
			return scheme.get('color_scheme')

def set_scheme(ext, color_scheme):
	for index, scheme in enumerate(schemes):
		if scheme['extension'] == ext and schemes[index]['color_scheme'] != color_scheme:
			schemes[index]['color_scheme'] = color_scheme
			plugin_settings.set('schemes', schemes)
			sublime.save_settings('ThemeAutomator.sublime-settings')

def add_scheme(ext, color_scheme):
	schemes.append({'color_scheme': color_scheme, 'extension': ext})
	plugin_settings.set('schemes', schemes)
	sublime.save_settings('ThemeAutomator.sublime-settings')

def set_scheme_for_extension(view):
	if view.file_name() is not None:
		root,ext = os.path.splitext(view.file_name())
		if ext in extensions():
			print('SET scheme for extension')
			set_scheme(ext, sublime_settings.get('color_scheme'))
		else:
			print('ADD scheme for extension')
			add_scheme(ext, sublime_settings.get('color_scheme'))

class ThemeAutomatorEvents(sublime_plugin.EventListener):
	def on_activated(self, view):
		check_empty_color_scheme(view)
		if view.file_name() is not None:
			root,ext = os.path.splitext(view.file_name())
			if ext in extensions():
				color_scheme = theme(ext)
				if sublime_settings.get('color_scheme') != color_scheme and schemes is not None:
					save_scheme(color_scheme)
			else:
				if automate_selection == True:
					print('add_scheme 2 scheme for extension')
					add_scheme(ext, sublime_settings.get('color_scheme'))
				if sublime_settings.get('color_scheme') != plugin_settings.get('color_scheme'):
					save_scheme(plugin_settings.get('color_scheme'))
	def on_deactivated(self, view):
		if automate_selection == True:
			set_scheme_for_extension(view)

class SetSchemeForExtensionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		set_scheme_for_extension(self.view)

class SetDefaultSchemeAndForExtensionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		plugin_settings.set('color_scheme', sublime_settings.get('color_scheme'))
		sublime.save_settings('ThemeAutomator.sublime-settings')
		set_scheme_for_extension(self.view)

class SetDefaultSchemeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		plugin_settings.set('color_scheme', sublime_settings.get('color_scheme'))
		sublime.save_settings('ThemeAutomator.sublime-settings')


