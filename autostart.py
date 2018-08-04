from xbmcswift2 import Plugin, xbmc


if __name__ == '__main__':
    plugin = Plugin()
    my_stations = plugin.get_storage('my_stations.json', file_format='json')

    if plugin.get_setting('autostart', bool):
        for station in my_stations.values():
            plugin.log.info(my_stations.values())
            if 'autostart' in station:
                xbmc.executebuiltin('XBMC.PlayMedia(%s)' % station['stream_url'])
