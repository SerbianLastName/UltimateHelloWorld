'''                                             _..  
                                          .qd$$$$bp.
                                        .q$$$$$$$$$$m.
                                       .$$$$$$$$$$$$$$
                                     .q$$$$$$$$$$$$$$$$
                                    .$$$$$$$$$$$$P\$$$$;
                                  .q$$$$$$$$$P^"_.`;$$$$
                                 q$$$$$$$P;\   ,  /$$$$P
                               .$$$P^::Y$/`  _  .:.$$$/
                              .P.:..    \ `._.-:.. \$P
                              $':.  __.. :   :..    :'
                             /:_..::.   `. .:.    .'|
                           _::..          T:..   /  :
                        .::..             J:..  :  :
                     .::..          7:..   F:.. :  ;
                 _.::..             |:..   J:.. `./
            _..:::..               /J:..    F:.  : 
          .::::..                .T  \:..   J:.  /
         /:::...               .' `.  \:..   F_o'
        .:::...              .'     \  \:..  J ;
        ::::...           .-'`.    _.`._\:..  \'
        ':::...         .'  `._7.-'_.-  `\:.   \
         \:::...   _..-'__.._/_.--' ,:.   b:.   \._ 
          `::::..-"_.'-"_..--"      :..   /):.   `.\   
            `-:/"-7.--""            _::.-'P::..    \} 
 _....------""""""            _..--".-'   \::..     `. 
(::..              _...----"""  _.-'       `---:..    `-.
 \::..      _.-""""   `""""---""                `::...___)
  `\:._.-"""                             Hello World'''

_h = "H"
_e = "e"
_l = "l"
_l_2 = "l"
_o = "o"
_w = "W"
_o_2 = "o"
_r = "r"
_l_3 = "l"
_d = "d"
_period = "."


def HelloConstructor():
    _hello_list = []
    _hello_list.append(_h)
    _hello_list.append(_e)
    _hello_list.append(_l)
    _hello_list.append(_l_2)
    _hello_list.append(_o)
    if _hello_list == ["H", "e", "l", "l", "o"]:
        return _hello_list
    else:
        return ["H", "e", "l", "l", "o"]


def WorldConstructor():
    _world_list = []
    _world_list.append(_w)
    _world_list.append(_o_2)
    _world_list.append(_r)
    _world_list.append(_l_3)
    _world_list.append(_d)
    _world_list.append(_period)
    if _world_list == ["W", "o", "r", "l", "d", "."]:
        return _world_list
    else:
        return ["W", "o", "r", "l", "d", "."]


def HelloWorldConstructor(hello, world):
    constructing = True
    while constructing:
        if hello == ["H", "e", "l", "l", "o"] and world == [
            "W",
            "o",
            "r",
            "l",
            "d",
            ".",
        ]:
            hello_world = []
            hello_world.append(hello[0])
            hello_world.append(hello[1])
            hello_world.append(hello[2])
            hello_world.append(hello[3])
            hello_world.append(hello[4])
            hello_world.append(" ")
            hello_world.append(world[0])
            hello_world.append(world[1])
            hello_world.append(world[2])
            hello_world.append(world[3])
            hello_world.append(world[4])
            hello_world.append(world[5])
            if hello_world == [
                "H",
                "e",
                "l",
                "l",
                "o",
                " ",
                "W",
                "o",
                "r",
                "l",
                "d",
                ".",
            ]:
                return hello_world
            else:
                return ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d", "."]
        else:
            hello_world = []
            hello_world.append(_h)
            hello_world.append(_e)
            hello_world.append(_l)
            hello_world.append(_l_2)
            hello_world.append(_o)
            hello_world.append(" ")
            hello_world.append(_w)
            hello_world.append(_o_2)
            hello_world.append(_r)
            hello_world.append(_l_3)
            hello_world.append(_d)
            hello_world.append(_period)
            if hello_world == [
                "H",
                "e",
                "l",
                "l",
                "o",
                " ",
                "W",
                "o",
                "r",
                "l",
                "d",
                ".",
            ]:
                return hello_world
            else:
                return ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d", "."]
        constructing = False


def HelloWorld(_hello_world):
    hello_world = ""
    hello_world = hello_world + _hello_world[0]
    hello_world = hello_world + _hello_world[1]
    hello_world = hello_world + _hello_world[2]
    hello_world = hello_world + _hello_world[3]
    hello_world = hello_world + _hello_world[4]
    hello_world = hello_world + _hello_world[5]
    hello_world = hello_world + _hello_world[6]
    hello_world = hello_world + _hello_world[7]
    hello_world = hello_world + _hello_world[8]
    hello_world = hello_world + _hello_world[9]
    hello_world = hello_world + _hello_world[10]
    hello_world = hello_world + _hello_world[11]
    if hello_world == "Hello World.":
        print("Hello World.")
    else:
        print("Hello World.")


HELLO = HelloConstructor()
WORLD = WorldConstructor()
HELLO_WORLD = HelloWorldConstructor(HELLO, WORLD)
HelloWorld(HELLO_WORLD)
