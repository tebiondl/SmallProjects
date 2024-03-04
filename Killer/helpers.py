list_helper = """
Screen:
    ScrollView:
        pos_hint: {'center_y': 0.3}
        MDList:
            id: gamelist
"""

element_item = """
CustomListItem:
    text: "{}"
    MDRectangleFlatButton:
        text: "Delete"
        on_release: root.delete_item()
"""

screen_helper = """
ScreenManager: 
    MenuScreen:
    OfflineStart:
    OfflineGameCreation:
    ActiveGame:
    StartGame:
    PlayerInfo:
    
<MenuScreen>
    name: 'menu'
    MDRectangleFlatButton:
        text:   'Offline'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press: root.manager.current = 'offline'
    MDRectangleFlatButton:
        text:   'Login'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
    MDTextField: 
        hint_text: "Introduce tu contraseña"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: 0.5
    MDTextField: 
        hint_text: "Introduce tu nombre"
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x: 0.5
        
<OfflineStart>
    name: 'offline'
    MDRectangleFlatButton:
        text:   'Back'
        pos_hint: {'center_x': 0.05, 'center_y': 0.95}
        on_press: root.manager.current = 'menu'
    MDRectangleFlatButton:
        text:   'Add Game'
        pos_hint: {'center_x': 0.2, 'center_y': 0.95}
        on_press:  root.manager.current = 'offlineGameCreation'
    BoxLayout:
        orientation: 'vertical'
        size_hint_y: 0.9
        pos_hint: {'center_x': 0.5}
        ScrollView:
            MDList:
                id: gamelist

<OfflineGameCreation>
    name: 'offlineGameCreation'
    MDRectangleFlatButton:
        text:   'Back'
        pos_hint: {'center_x': 0.05, 'center_y': 0.95}
        on_press: root.manager.current = 'offline'
    MDRectangleFlatButton:
        text:   'Add Player'
        pos_hint: {'center_x': 0.2, 'center_y': 0.95}
        on_press: root.open_dialog('Player')
    MDRectangleFlatButton:
        text:   'Add Weapon'
        pos_hint: {'center_x': 0.4, 'center_y': 0.95}
        on_press: root.open_dialog('Weapon')
    MDRectangleFlatButton:
        text:   'Add Place'
        pos_hint: {'center_x': 0.6, 'center_y': 0.95}
        on_press: root.open_dialog('Place')
    MDRectangleFlatButton:
        text:   'Start'
        pos_hint: {'center_x': 0.8, 'center_y': 0.95}
        on_press: root.open_next_dialog()
    BoxLayout:
        orientation: 'vertical'
        size_hint_y: 0.9
        pos_hint: {'center_x': 0.5}
        ScrollView:
            MDList:
                id: playerList
        ScrollView:
            MDList:
                id: weaponList
        ScrollView:
            MDList:
                id: placeList
                
<ActiveGame>
    name: 'activeGame'
    MDRectangleFlatButton:
        text:   'Back'
        pos_hint: {'center_x': 0.05, 'center_y': 0.95}
        on_press: root.manager.current = 'offline'
    MDLabel:
        text:   'Who are you?'
        pos_hint: {'center_x': 0.95, 'center_y': 0.95}
    BoxLayout:
        orientation: 'vertical'
        size_hint_y: 0.9
        pos_hint: {'center_x': 0.5}
        ScrollView:
            MDList:
                id: actualPlayerList
                
<StartGame>
    name: 'startGame'
    MDRectangleFlatButton:
        text:   'Start Shuffle'
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        on_press: root.shuffle()
        id: shuffleBtn
    MDRectangleFlatButton:
        text:   'Show Information'
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        on_press: root.show_victims()
        opacity: 0
        disabled: True
        id: showInfoBtn
    MDRectangleFlatButton:
        text:   'Hide Information'
        pos_hint: {'center_x': 0.7, 'center_y': 0.9}
        on_press: root.hide_victims()
        opacity: 0
        disabled: True
        id: hideInfoBtn
    MDLabel:
        text:   'Give the phone to: '
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        opacity: 0
        id: playerMessage
    BoxLayout:
        orientation: 'vertical'
        id: infoContainer

<PlayerInfo>
    name: 'playerInfo'
    MDRectangleFlatButton:
        text:   'Back'
        pos_hint: {'center_x': 0.05, 'center_y': 0.95}
        on_press: root.back()
    MDRectangleFlatButton:
        text:   'Show Information'
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        on_press: root.show_info()
    MDLabel:
        text:   '[NAME HIDDEN]'
        pos_hint: {'center_x': 0.95, 'center_y': 0.75}
        id: playerInfoName
    MDLabel:
        text:   '[VICTIM HIDDEN]'
        pos_hint: {'center_x': 0.95, 'center_y': 0.55}
        id: playerInfoVictim
    MDLabel:
        text:   '[WEAPON HIDDEN]'
        pos_hint: {'center_x': 0.95, 'center_y': 0.35}
        id: playerInfoWeapon
    MDLabel:
        text:   '[PLACE HIDDEN]'
        pos_hint: {'center_x': 0.95, 'center_y': 0.15}
        id: playerInfoPlace
"""