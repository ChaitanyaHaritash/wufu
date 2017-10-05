# WuFu
A type of fuzzing framework in which you can add fuzzers like modules and can use it almost like Metasploit/Empire :)
It was a small idea i had in my mind not a big contribution for now, but i request you to show your creativity 
with it and make pull requests, I'd really appricialte it:)

Currently in development stage and yet to have more functionalities. So i recommend you to DM us on twitter,
and let us know what you have in your mind for it :) 

### POC

[![wufu.png](https://s1.postimg.org/5p45kcuymn/wufu.png)](https://postimg.org/image/4t7o4wla6j/)

### Installation
    > pip install -r requirements.txt
    > python wufu.py
### Usage

    banner            Reload/change banner
    clear             clears the screen
    execute           Execute a fuzzer/module
    help              List available commands with "help" or detailed help with "help cmd".
    info              Info on a fuzzer/module
    main              Return to main
    processes         Listing all process running
    quit              quit wufu
    reload            Reloading Module during development/glitch
    search            Will search if module exists
    set               Sets option for a fuzzer/module
    show              Show fuzzers or options
    use               Use a fuzzer/module
### How to develop module/fuzzer?
###### Check out "template.py" inside lib/fuzzers dir,
###### A complete documentation will be provided once we able to make stable release :)
### NOTE :
  ##### WE mainly focused on windows testing, so if something didn't work in linux.. please dont raise issue for it :)
  ### Known Bugs
      > self.prompt variable doesn't loose value inserted after implementation
      > reload option doesn't works (currently)
      > tab auto-completition limited to main menu..
      *for any other bug or PR you can notify on github :)*
### Contact:
  #### [Twitter:] @vvalien1 | @bofheaded       
   
