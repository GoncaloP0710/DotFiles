# pylint: disable=C0111
c = c  # noqa: F821 pylint: disable=E0602,C0103
config = config  # noqa: F821 pylint: disable=E0602,C0103
# pylint settings included to disable linting errors

c.content.user_stylesheets = ["~/.config/qutebrowser/custom.css"]

# Statusbar colors
c.colors.statusbar.normal.bg = "#00000000"  # Transparent background
c.colors.statusbar.command.bg = "#00000000"  # Transparent background
c.colors.statusbar.command.fg = "#ffffff"  # White foreground
c.colors.statusbar.normal.fg = "#86aaec"  # Blue foreground
c.colors.statusbar.passthrough.fg = "#86aaec"  # Blue foreground
c.colors.statusbar.url.fg = "#c296eb"  # Magenta foreground
c.colors.statusbar.url.success.https.fg = "#c296eb"  # Magenta foreground
c.colors.statusbar.url.hover.fg = "#93cee9"  # Cyan foreground

# Tab colors
c.colors.tabs.even.bg = "#00000000"  # Transparent tabs
c.colors.tabs.odd.bg = "#00000000"  # Transparent tabs
c.colors.tabs.bar.bg = "#00000000"  # Transparent tab bar
c.colors.tabs.even.fg = "#151720"  # Black foreground
c.colors.tabs.odd.fg = "#151720"  # Black foreground
c.colors.tabs.selected.even.bg = "#ffffff"  # White background
c.colors.tabs.selected.odd.bg = "#ffffff"  # White background
c.colors.tabs.selected.even.fg = "#000000"  # Black foreground
c.colors.tabs.selected.odd.fg = "#000000"  # Black foreground

# Hints
c.colors.hints.bg = "#000000"  # Black background
c.colors.hints.fg = "#ffffff"  # White foreground

# Completion colors
c.colors.completion.item.selected.match.fg = "#93cee9"  # Cyan
c.colors.completion.match.fg = "#93cee9"  # Cyan
c.colors.completion.odd.bg = "#000000"  # Black background
c.colors.completion.even.bg = "#000000"  # Black background
c.colors.completion.fg = "#ffffff"  # White foreground
c.colors.completion.category.bg = "#000000"  # Black background
c.colors.completion.category.fg = "#ffffff"  # White foreground
c.colors.completion.item.selected.bg = "#000000"  # Black background
c.colors.completion.item.selected.fg = "#ffffff"  # White foreground

# Messages
c.colors.messages.info.bg = "#000000"  # Black background
c.colors.messages.info.fg = "#ffffff"  # White foreground
c.colors.messages.error.bg = "#000000"  # Black background
c.colors.messages.error.fg = "#ffffff"  # White foreground

# Downloads
c.colors.downloads.error.bg = "#000000"  # Black background
c.colors.downloads.error.fg = "#ffffff"  # White foreground
c.colors.downloads.bar.bg = "#000000"  # Black background
c.colors.downloads.start.bg = "#90ceaa"  # Green background
c.colors.downloads.start.fg = "#ffffff"  # White foreground
c.colors.downloads.stop.bg = "#4f5572"  # Gray background
c.colors.downloads.stop.fg = "#ffffff"  # White foreground

# Tooltip
c.colors.tooltip.bg = "#000000"  # Black background
c.colors.webpage.bg = "#000000"  # Black background
c.hints.border = "#ffffff"  # White border

# Tabs
c.tabs.show = "multiple"
c.tabs.padding = {'top': 5, 'bottom': 5, 'left': 9, 'right': 9}
c.tabs.indicator.width = 0  # No tab indicators
c.tabs.width = '7%'

# Fonts
c.fonts.default_family = []
c.fonts.default_size = '13pt'
c.fonts.web.family.fixed = 'monospace'
c.fonts.web.family.sans_serif = 'monospace'
c.fonts.web.family.serif = 'monospace'
c.fonts.web.family.standard = 'monospace'

# Dark mode setup
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
c.colors.webpage.darkmode.policy.images = 'never'
config.set('colors.webpage.darkmode.enabled', False, 'file://*')

# Search engines
c.url.searchengines = {
    'DEFAULT': 'https://duckduckgo.com/?q={}',
    '!aw': 'https://wiki.archlinux.org/?search={}',
    '!apkg': 'https://archlinux.org/packages/?sort=&q={}&maintainer=&flagged=',
    '!gh': 'https://github.com/search?o=desc&q={}&s=stars',
    '!yt': 'https://www.youtube.com/results?search_query={}',
}

# Completion categories
c.completion.open_categories = ['searchengines', 'quickmarks', 'bookmarks', 'history', 'filesystem']

# Auto-config and session saving
config.load_autoconfig()  # Load settings done via the GUI
c.auto_save.session = True  # Save tabs on quit/restart

# Keybinding changes
config.bind('=', 'cmd-set-text -s :open')
config.bind('h', 'history')
config.bind('cs', 'cmd-set-text -s :config-source')
config.bind('tH', 'config-cycle tabs.show multiple never')
config.bind('sH', 'config-cycle statusbar.show always never')
config.bind('T', 'hint links tab')
config.bind('pP', 'open -- {primary}')
config.bind('pp', 'open -- {clipboard}')
config.bind('pt', 'open -t -- {clipboard}')
config.bind('qm', 'macro-record')
config.bind('<ctrl-y>', 'spawn --userscript ytdl.sh')
config.bind('tT', 'config-cycle tabs.position top left')
config.bind('gJ', 'tab-move +')
config.bind('gK', 'tab-move -')
config.bind('gm', 'tab-move')

# Privacy settings
config.set("content.webgl", False, "*")
config.set("content.canvas_reading", False)
config.set("content.geolocation", False)
config.set("content.webrtc_ip_handling_policy", "default-public-interface-only")
config.set("content.cookies.accept", "all")
config.set("content.cookies.store", True)

# Adblocking
c.content.blocking.enabled = True