# Cyberdream colorscheme for ranger
# Matches the cyberdream Neovim colorscheme
# Colors: https://github.com/scottmckendry/cyberdream.nvim
#
# Cyberdream palette:
#   bg:       #16181a
#   bg_alt:   #1e2124
#   fg:       #ffffff
#   grey:     #7b8496
#   blue:     #5ea1ff
#   green:    #5eff6c
#   cyan:     #5ef1ff
#   red:      #ff6e5e
#   yellow:   #f1ff5e
#   magenta:  #ff5ef1
#   pink:     #ff5ea0
#   orange:   #ffbd5e
#   purple:   #bd5eff

from __future__ import absolute_import, division, print_function

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import (
    black, blue, cyan, green, magenta, red, white, yellow, default,
    normal, bold, reverse, dim, BRIGHT,
    default_colors,
)

# Cyberdream colors using 256-color palette
PINK = 207      # #ff33ff - closest to cyberdream magenta #ff5ef1


class cyberdream(ColorScheme):
    progress_bar_color = blue

    def use(self, context):
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        elif context.in_browser:
            attr = normal

            if context.empty or context.error:
                bg = red

            if context.border:
                fg = default

            if context.media:
                if context.image:
                    fg = yellow
                else:
                    fg = magenta

            if context.container:
                fg = red

            if context.directory:
                attr |= bold
                fg = magenta  # cyberdream: directories in magenta (#ff5ef1)
                fg += BRIGHT

            elif context.executable and not \
                    any((context.media, context.container,
                         context.fifo, context.socket)):
                attr |= bold
                fg = green  # cyberdream: executables in green (#5eff6c)
                fg += BRIGHT

            if context.socket:
                attr |= bold
                fg = magenta
                fg += BRIGHT

            if context.fifo or context.device:
                fg = yellow
                if context.device:
                    attr |= bold
                    fg += BRIGHT

            if context.link:
                fg = cyan if context.good else red  # cyberdream: links in cyan (#5ef1ff)

            if context.tag_marker and not context.selected:
                attr |= bold
                if fg in (red, magenta):
                    fg = white
                else:
                    fg = red
                fg += BRIGHT

            if not context.selected and (context.cut or context.copied):
                attr |= bold
                fg = black
                fg += BRIGHT
                if BRIGHT == 0:
                    attr |= dim
                    fg = white

            if context.main_column:
                if context.selected:
                    attr |= bold
                if context.marked:
                    attr |= bold
                    fg = yellow

            if context.badinfo:
                if attr & reverse:
                    bg = magenta
                else:
                    fg = magenta

            if context.inactive_pane:
                fg = cyan

            # cyberdream: selected items have pink background (#ff5ef1)
            if context.selected:
                attr |= bold
                bg = PINK
                fg = black

        elif context.in_titlebar:
            if context.hostname:
                fg = red if context.bad else green  # cyberdream: green for good (#5eff6c)
            elif context.directory:
                fg = magenta  # cyberdream: directory path in magenta (#ff5ef1)
            elif context.tab:
                if context.good:
                    bg = magenta  # cyberdream: active tab in magenta
            elif context.link:
                fg = cyan
            attr |= bold

        elif context.in_statusbar:
            if context.permissions:
                if context.good:
                    fg = cyan  # cyberdream: good permissions in cyan (#5ef1ff)
                elif context.bad:
                    fg = red   # cyberdream: bad permissions in red (#ff6e5e)
            if context.marked:
                attr |= bold | reverse
                fg = yellow
                fg += BRIGHT
            if context.frozen:
                attr |= bold | reverse
                fg = cyan
                fg += BRIGHT
            if context.message:
                if context.bad:
                    attr |= bold
                    fg = red
                    fg += BRIGHT
            if context.loaded:
                bg = self.progress_bar_color
            if context.vcsinfo:
                fg = blue  # cyberdream: vcs info in blue (#5ea1ff)
                attr &= ~bold
            if context.vcscommit:
                fg = yellow
                attr &= ~bold
            if context.vcsdate:
                fg = cyan
                attr &= ~bold

        if context.text:
            if context.highlight:
                attr |= reverse

        if context.in_taskview:
            if context.title:
                fg = blue

            if context.selected:
                attr |= reverse

            if context.loaded:
                if context.selected:
                    fg = self.progress_bar_color
                else:
                    bg = self.progress_bar_color

        if context.vcsfile and not context.selected:
            attr &= ~bold
            if context.vcsconflict:
                fg = magenta
            elif context.vcsuntracked:
                fg = cyan
            elif context.vcschanged:
                fg = red  # cyberdream: changed files in red (#ff6e5e)
            elif context.vcsunknown:
                fg = red
            elif context.vcsstaged:
                fg = green  # cyberdream: staged files in green (#5eff6c)
            elif context.vcssync:
                fg = green
            elif context.vcsignored:
                fg = default

        elif context.vcsremote and not context.selected:
            attr &= ~bold
            if context.vcssync or context.vcsnone:
                fg = green
            elif context.vcsbehind:
                fg = red
            elif context.vcsahead:
                fg = blue  # cyberdream: ahead in blue (#5ea1ff)
            elif context.vcsdiverged:
                fg = magenta
            elif context.vcsunknown:
                fg = red

        return fg, bg, attr
