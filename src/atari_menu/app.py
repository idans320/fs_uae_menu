from atari_menu.games import GameInterface
from atari_menu.config import Config

from simple_term_menu import TerminalMenu
import subprocess
import os 

def start_exec():
    cmd = Config.cmd
    subprocess.run(cmd.split(" "), stdout=open(os.devnull, 'wb'))
    main()

def games_selection_menu():
    options = ["0-9","A-C","D-F","G-I","J-L","M-O","P-R","S-U","V-X","Y-Z"]
    terminal_menu = TerminalMenu(
        options
    )
    menu_entry_indices = terminal_menu.show()
    if menu_entry_indices is not None:
       option = options[menu_entry_indices]
       f,l = tuple(option.split("-"))
       games_selection_by_characters(f,l)
    else:
        main()

def games_selection_by_characters(f,l):
    games = GameInterface.get_games_by_first_character_range(f,l)
    names = [game.name for game in games]
    selected = [game[0] for game in enumerate(games) if game[1].enabled == 1]
    terminal_menu = TerminalMenu(
        names,
        multi_select=True,
        show_multi_select_hint=True,
        multi_select_select_on_accept=False,
        multi_select_empty_ok=True,
        preselected_entries=selected
    )
    menu_entry_indices = terminal_menu.show()
    if menu_entry_indices is not None:
        if menu_entry_indices:
            enabled = [games[i] for i in menu_entry_indices]
            disabled = [game for game in games if game not in enabled]
            GameInterface.save_selection_to_db(enabled,disabled)
        else:
            GameInterface.save_selection_to_db([],games)
        GameInterface.save_selection_to_config_file()
        
    games_selection_menu()

def selected_games():
    games = GameInterface.get_all_enabled_games()
    names = [game.name for game in games]
    selected = [game[0] for game in enumerate(games) if game[1].enabled == 1]
    terminal_menu = TerminalMenu(
        names,
        multi_select=True,
        show_multi_select_hint=True,
        multi_select_select_on_accept=False,
        multi_select_empty_ok=True,
        preselected_entries=selected
    )
    menu_entry_indices = terminal_menu.show()
    if menu_entry_indices is not None:
        if menu_entry_indices:
            enabled = [games[i] for i in menu_entry_indices]
            disabled = [game for game in games if game not in enabled]
            GameInterface.save_selection_to_db(enabled,disabled)
        else:
            GameInterface.save_selection_to_db([],games)
        GameInterface.save_selection_to_config_file()

    main()

def main():
   options = ["Games Menu","Selected Games","Start"]
   terminal_menu = TerminalMenu(
        options,
        title="Amiga Manager",
   )
   menu_entry_indices = terminal_menu.show()
   if menu_entry_indices is not None:
    option = options[menu_entry_indices]
    if option == "Games Menu":
        games_selection_menu()
    if option == "Selected Games":
        selected_games()
    if option == "Start":
        start_exec()
        




if __name__ == "__main__":
    main()