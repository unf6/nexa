from os import system, name
from sys import stdout
from colorama import Fore
from pystyle import *

def banner():
    banner = Center.XCenter(r"""  
              ____   ___    _  __  ____ _
             / __ \ / _ \  | |/_/ / __ `/
            / / / //  __/ _>  <  / /_/ / 
           /_/ /_/ \___/ /_/|_|  \__,_/                               

        Type help or ? to see the Commands
Security Testing Tool for XSS, SQLi, SSTI, and RCE""")
    print(Colorate.Vertical(Colors.blue_to_purple, banner, 2))
    
def clear():
    if name == 'nt':
       system('cls')
    else:
       system('clear')

def tools():
    blue_to_purple = Colorate.Horizontal(Colors.blue_to_purple, """
                       ╔╦╗╔═╗╔═╗╦  ╔═╗
                        ║ ║ ║║ ║║  ╚═╗
                        ╩ ╚═╝╚═╝╩═╝╚═╝
            ══╦═════════════════════════════════╦══
    ╔═════════╩═════════════════════════════════╩═════════╗
    ║ • subfinder  | Subdomain Finder                     ║
    ║ • server     | Server Info                          ║
    ║ • ssltls     | Ssl/Tls Security                     ║
    ║ • log        | Check For Log Files                  ║
    ║ • backup     | Check For Backup Files               ║
    ╚═════════════════════════════════════════════════════╝
    """)
    print(blue_to_purple)

def scanners():
    blue_to_purple = Colorate.Horizontal(Colors.blue_to_purple, """
                    ╔═╗╔═╗╔═╗╔╗╔╔╗╔╔═╗╦═╗╔═╗
                    ╚═╗║  ╠═╣║║║║║║║╣ ╠╦╝╚═╗
                    ╚═╝╚═╝╩ ╩╝╚╝╝╚╝╚═╝╩╚═╚═╝
           ══╦═════════════════════════════════╦══
   ╔═════════╩═════════════════════════════════╩═════════╗
   ║ • rexss    | Reflected XSS                          ║
   ║ • dxss     | Dom-Based XSS                          ║
   ║ • sqli     | Sql Injection                          ║
   ║ • rce      | Remote Code Execution                  ║
   ║ • or       | Open Redirection                       ║
   ║ • ssrf     | Server-Side Template Injection         ║
   ║ • cj       | Click Jacking                          ║
   ║ • rfi      | Remote File Inclusion                  ║
   ║ • cors     | Cors Misconfiguration                  ║
   ║ • xxe      | Xml External Entity                    ║
   ║ • all      | Crawl and Test All                     ║
   ╚═════════════════════════════════════════════════════╝
    """)
    print(blue_to_purple)

def help():
    blue_to_purple = Colorate.Horizontal(Colors.blue_to_purple, """
                        ╦ ╦╔═╗╦  ╔═╗
                        ╠═╣║╣ ║  ╠═╝
                        ╩ ╩╚═╝╩═╝╩
           ══╦═════════════════════════════════╦══
   ╔═════════╩═════════════════════════════════╩═════════╗
   ║ • scanners | Show Scanners                          ║
   ║ • tools    | Show Tools                             ║
   ║ • license  | Show License                           ║                 
   ║ • exit     | Exit Nexa                              ║
   ╠═════════════════════════════════════════════════════╣
   ║ • THANK    | Thanks for using Nexa.                 ║
   ║ • YOU♥     | Plz star project :)                    ║
   ║ • github   | github.com/unf6/nexa                   ║
   ╚═════════════════════════════════════════════════════╝
    """)
    print(blue_to_purple)

def license():
    print(Colorate.Horizontal(Colors.blue_to_purple, r"""
Copyright (c) 2024 Xretic

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""))
