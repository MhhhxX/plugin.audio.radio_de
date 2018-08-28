from xbmcswift2 import Plugin, xbmc
import xbmcgui


Strings = {
    'no-station-notification': 30700
}

if __name__ == '__main__':
    plugin = Plugin()
    my_stations = plugin.get_storage('my_stations.json', file_format='json')
    found = False

    if plugin.get_setting('autostart', bool):
        for station in my_stations.values():
            if 'autostart' in station:
                found = True
                plugin.log.info("Play startup radio station: %s" % station['name'])
                listitem = xbmcgui.ListItem(station['name'])
                listitem.setArt({'thumb': station['thumbnail']})
                listitem.setRating("radio.de", float(station.get('rating', '0.0')))
                listitem.setInfo('music', {'title': station['name'],
                                           'genre': station['genre'],
                                           'size': station['bitrate'],
                                           'comment': station['current_track']})
                xbmc.Player().play(item=station['stream_url'], listitem=listitem)

        if not found:
            plugin.notify(plugin.get_string(Strings['no-station-notification']).encode('utf-8'), delay=25000,
                          image=plugin.addon.getAddonInfo('path') + "/icon.png")
