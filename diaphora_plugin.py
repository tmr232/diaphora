import idaapi

import sark

idaapi.require('diaphora')
from diaphora import diff_or_export_ui, import_definitions, load_results



class Diaphora(idaapi.plugin_t):
    flags = 0
    comment = 'Diaphora'
    help = 'Diaphora'
    wanted_name = 'Diaphora'
    wanted_hotkey = ''

    def init(self):
        self._menu_manager = sark.ui.MenuManager()
        self._menu_manager.add_menu('Diaphora')

        # The `add_menu_item` API is deprecated, but is used here for compatibility with pre-6.7 IDA versions.
        idaapi.add_menu_item('Diaphora/', 'Diff or Export', '', 0, diff_or_export_ui, None)
        idaapi.add_menu_item('Diaphora/', 'Import Definitions', '', 0, import_definitions, None)
        idaapi.add_menu_item('Diaphora/', 'Load Results', '', 0, load_results, None)
        return idaapi.PLUGIN_KEEP

    def term(self):
        self._menu_manager.clear()

    def run(self, arg):
        pass


def PLUGIN_ENTRY():
    return Diaphora()
