import platform
import sublime

get_bitness = platform.architecture()[0]
print(get_bitness)

get_bitness = sublime.arch()
print(get_bitness)
