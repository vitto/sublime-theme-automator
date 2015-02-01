Theme Automator
=======================

Sets a different color scheme for every file type in [Sublime Text 2](http://www.sublimetext.com/2) and [Sublime Text 3](http://www.sublimetext.com/3).

It can be very helpful mixed with [Colorsublime](https://github.com/Colorsublime/Colorsublime-Plugin) plugin.

It adds a context menu named ThemeAutomator:

![Image not found!](http://img30.imageshack.us/img30/4923/hoh0.png "ThemeAutomator context menu")

This image is showing **Big Duo** color scheme of [Theme Nil](https://github.com/nilium/st2-nil-theme)

###Changes in 1.0.7
Added context menu item to open plug-in user's config directly from context menu

###Changes in 1.0.6
Fixed the [bug #2](https://github.com/vitto/sublime-theme-automator/issues/2) caused by a missing load event when plug-in is reloaded.

###Changes in 1.0.4
To avoid a problem of Sublime Text 2 when switch focus between multiple windows instances, `automate_selection` is now set wo `false`.

###Changes in 1.0.3
Fixed the [bug #1](https://github.com/vitto/sublime-theme-automator/issues/1) based on a plugin error and `automate_selection` not worked properly.


###Changes in 1.0.2
Added property `automate_selection` in User settings `ThemeAutomator.sublime-settings` to apply themes automatically without using the context menu.


###Changes in 1.0.1
Added Package Setting preferences menu in `Preferences > Package Settings > ThemeAutomator`
