wifite
======

An automated wireless attack tool.


What's New?
-----------

The biggest change from version 1 is support for ["reaver"](http://reaver-wps.googlecode.com/), a Wifi-Protected Setup (WPS) attack tool.  Reaver can compromise the PIN and PSK for many routers that have WPS enabled, usually within hours.

Other changes include a complete code re-write with bug fixes and added stability.  Due to problems with the Python Tkinter suite, the GUI has been left out of this latest version.


About
-----

_Wifite is for Linux only._

Wifite was designed for use with pentesting distributions of Linux, such as [Kali Linux](http://www.kali.org/), [Pentoo](http://www.pentoo.ch/), [BackBox](http://www.backbox.org); any Linux distributions with wireless drivers patched for injection. The script appears to also operate with Ubuntu 11/10, Debian 6, and Fedora 16.

Wifite must be run as __root__. This is required by the suite of programs it uses. Running downloaded scripts as root is a bad idea. I recommend using the Kali Linux bootable Live CD, a bootable USB stick (for persistent), or a virtual machine. Note that Virtual Machines cannot directly access hardware so a wireless USB dongle would be required.

Wifite assumes that you have a wireless card and the appropriate drivers that are patched for injection and promiscuous/monitor mode.

