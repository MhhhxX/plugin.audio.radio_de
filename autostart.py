from xbmcswift2 import Plugin, xbmc
import xbmcgui


if __name__ == '__main__':
    plugin = Plugin()
    my_stations = plugin.get_storage('my_stations.json', file_format='json')

    if plugin.get_setting('autostart', bool):
        for station in my_stations.values():
            if 'autostart' in station:
                plugin.log.info("Play startup radio station: %s" % station['name'])
                listitem = xbmcgui.ListItem(station['name'])
                listitem.setArt({'thumb': station['thumbnail']})
                listitem.setRating("radio.de", float(station.get('rating', '0.0')))
                listitem.setInfo('music', {'title': station['name'],
                                           'genre': station['genre'],
                                           'size': station['bitrate'],
                                           'comment': station['current_track']})
                xbmc.Player().play(item=station['stream_url'], listitem=listitem)
