#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------------------------------------
	PROJECT BLACKBOX - https://comunidadconocimiento.org
----------------------------------------------------------------------------

BlackBox
~~~~~~~~~~~~~~
Project by Comunidad de Conocimiento to automate the analysis of
wireless networking.

With this project we want to learn about raspberry, unix, networking,
programming python collaboratively and have fun.

Based on the crozono idea.

"""

def banner():
    from pyfiglet import figlet_format
    print(figlet_format('Black', font='isometric3'))
    print(figlet_format(' Box', font='isometric3'))
    print(figlet_format('  Version 0.1', font='slant'))

    print("Comunidad de Conocimiento - https://comunidadconocimiento.org")
    #cprint(figlet_format('missile!', font='starwars'),'yellow', 'on_red', attrs=['bold'])

def main():
    banner()

# Mainprocess
main()
