import valve.source
import valve.source.a2s
import valve.source.master_server

ip = "149.62.15.106"
port = 7777
address = (ip, port)

def playercount():
    try:
        with valve.source.a2s.ServerQuerier(address) as server:
            info = server.info()
            return "{player_count}/{max_players} {map} {server_name}".format(**info)
    except valve.source.NoResponseError:
        return "Server {}:{} timed out!".format(*address)

def playerlist():
    players = []
    plen = ''
    try:
        with valve.source.a2s.ServerQuerier(address) as server:
            for player in server.players()["players"]:
                players.append(player["name"])
            for i in players:
                plen = plen + i + '\n'
            if plen != '':
                return(plen)
            else: return('There are no players on the server')
    except valve.source.NoResponseError:
        return "Server {}:{} timed out!".format(*address)
