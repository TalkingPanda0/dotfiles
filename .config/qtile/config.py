from os import system
import subprocess
import datetime
from time import sleep
from platform import release
from typing import List
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
import os
# defaults
mod = "mod4"

terminal = "alacritty"
browser = "firefox"
media = "stremio"
fileManager = "nemo"
game="lutris"
ide = "idea"
photo = "gimp-2.99"
passmanager="bwmenu"
configFolder = "/home/user/.config/qtile"
scriptFolder = "/home/user/.bin"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),
        # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

     Key([], "XF86PowerOff", lazy.spawn(f"{scriptFolder}/sysmenu_full"),),
     Key([mod], "d", lazy.screen.next_group(),),
     Key([mod], "a", lazy.screen.prev_group(),),
    # Switch window focus to other pane(s) of stack
    Key(["mod1"], "Tab", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),
    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    #fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Full screen"),
    #programs
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod,"mod1"], "Return", lazy.spawn("alacritty -e cmatrix "), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "e", lazy.spawn(fileManager), desc="Launch file manager"),
    Key([mod], "m", lazy.spawn(media), desc="Launch media player"),
    Key([mod], "t", lazy.spawn(ide), desc="Launch IDE"),
    Key([mod], "y", lazy.spawn(photo), desc="Launch Photo Editor"),
    Key([mod], "g", lazy.spawn(game), desc="Launch Games"),
    Key([mod], "p", lazy.spawn(passmanager), desc="Launch passmanager"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    # Qtile controls
    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([], "Scroll_Lock", lazy.spawn("betterlockscreen -l")),
    Key([], "Pause", lazy.spawn("betterlockscreen -s")),
    # dmenu
    #Key([mod], "r", lazy.spawn("dmenu_run"),
     #   desc="Spawn a command using a prompt widget"),

    # rofi
     Key([mod], "r", lazy.spawn("rofi -combi-modi window,drun,ssh -theme solarized -show combi -icon-theme Papirus -show-icons"),
         desc="Spawn a command using a prompt widget"),


    # Sound
    Key([mod], "Up", lazy.spawn("pulsemixer --change-volume +5"),),
    Key([mod], "Down", lazy.spawn("pulsemixer --change-volume -5")),
    Key(["mod1"], "Up", lazy.spawn("playerctl volume 0.05+"),),
    Key(["mod1"], "Down", lazy.spawn("playerctl volume 0.05-")),
    Key([mod], "x", lazy.spawn("pulsemixer --toggle-mute")),
    Key([mod], "Right", lazy.spawn("playerctl next")),
    Key([mod], "Left", lazy.spawn("playerctl previous")),
    Key([mod], "z", lazy.spawn("playerctl play-pause")),

    # shutdown
    Key([mod, "shift"], "Escape", lazy.spawn(f"{scriptFolder}/sysmenu_full"), desc="shutdown settings"),



    # printScreen
    Key([], "Print", lazy.spawn("flameshot gui")),
]


groups = [
    Group("1", label="www" ),
    Group("2", label="dev"),
    Group("3", label="msg"),
    Group("4", label="gam"),
    Group("5", label="fil"),
    Group("6", label="msc"),
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {i.name}"),

        # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {i.name}"),
    ])

layouts = [
    layout.Max(),
    #layout.Stack(num_stacks=2),
    layout.Bsp(),
    layout.TreeTab(),
    layout.Zoomy(),
    #layout.Columns(),
    #layout.Matrix(),
    #layout.MonadTall(),
    #layout.MonadWide(),
    layout.RatioTile(),
    #layout.Tile(),
    #layout.TreeTab(),
    #layout.VerticalTile(),
]

widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
            widget.Sep(linewidth= 0,padding=6,background="#292d3e"),
            widget.GroupBox(spacing=3,background="#292d3e",highlight_method="block",font="nerd-fonts-terminus"),
            widget.WindowName(background="#292d3e",foreground="#e1acff"),
            widget.Spacer(background="#292d3e"),
            widget.TextBox(text="",background="#292d3e",foreground="#668bd7",padding=-9,fontsize=45),
            widget.ThermalSensor(background="#668bd7"),
            widget.TextBox(text="",background="#668bd7",foreground="#8d62a9",padding=-9,fontsize=45),
            widget.Net(format="{down} ↓↑ {up}  ", background="#8d62a9",padding=0),
            widget.TextBox(text="",background="#8d62a9",foreground="#668bd7",padding=-9,fontsize=45),
            widget.CurrentLayoutIcon(custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                background = "#668bd7",
                padding = 0,scale = 0.7),
            widget.CurrentLayout(
                foreground = "#ffffff",
                background = "#668bd7",
                padding = 5
            ),
            widget.TextBox(text="",background="#668bd7",foreground="#8d62a9",padding=-9,fontsize=45),
            widget.Systray(background="#8d62a9"),
            widget.TextBox(text="",background="#8d62a9",foreground="#668bd7",padding=-9,fontsize=45),
            widget.Clock(format='  ⏲ %I:%M %m-%d (%a) ', background="#668bd7",padding=0),
            ],
            17,
            ),
    ),
    ]
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])


@hook.subscribe.startup_once
def autostart():
    subprocess.Popen(f"{scriptFolder}/autostart.sh")


auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
