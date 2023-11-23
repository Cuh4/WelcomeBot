# // ---------------------------------------------------------------------
# // ------- [Welcome Bot] Guild Config
# // ---------------------------------------------------------------------

# // ---- Imports
import sqlite3
import os
import pathlib
import json
import discord

# // ---- Classes
# // guild config class
# main class
class guildConfig:
    # // setup
    def __init__(self, pathForDb: str):
        # // attributes
        # paths
        self.path = os.path.abspath(pathForDb)
        self.dbPath = os.path.join(self.path, "guild_config.db")
        
        # // setup
        # validate database path
        self.validateDatabasePath()
        
        # create db
        self.database = sqlite3.connect(
            database = self.dbPath
        )
        
        self.createDatabaseSchema()
        
    # // private methods (primarily helpers)
    def __getCursor(self):
        return self.database.cursor()
    
    def __execute(self, query: str, *parameters):
        cursor = self.__getCursor()
        cursor.execute(query, parameters)
        self.database.commit()

        return cursor
    
    def __guildDataExists(self, guild: discord.Guild):
        return self.__execute("SELECT * FROM Configuration WHERE guild_id = ?", guild.id).fetchone() != None
    
    def __giveGuildDataIfNotExists(self, guild: discord.Guild):
        if self.__guildDataExists(guild):
            return
        
        self.__execute("INSERT INTO Configuration VALUES (?, ?)", guild.id, json.dumps({}))
                       
    def __loadConfig(self, guild: discord.Guild) -> dict|None:
        # setup
        self.__giveGuildDataIfNotExists(guild)
        
        # get data
        data = self.__execute("SELECT * FROM Configuration WHERE guild_id = ?", guild.id).fetchone()
        
        # return
        if data is None:
            return None
        
        return json.loads(data[1])
        
    # // public methods
    # validate db path
    def validateDatabasePath(self):
        path = pathlib.Path(self.path)
        
        if path.exists():
            return
        
        path.mkdir(
            parents = True,
            exist_ok = True
        )
        
    # database schema
    def createDatabaseSchema(self):
        # create table
        # note that "config" is a json dict. good practice? probably not
        self.__execute("""
            CREATE TABLE IF NOT EXISTS Configuration (
                guild_id INTEGER PRIMARY KEY,
                config TEXT
            )            
        """)
        
    # set config for a guild
    def save(self, guild: discord.Guild, name: str, value: any):
        # setup
        self.__giveGuildDataIfNotExists(guild)
        
        # get data
        config = self.__loadConfig(guild)
        
        # none check
        if config is None:
            return
        
        # save config value
        config[name] = value
        
        # update data
        self.__execute("UPDATE Configuration SET config = ? WHERE guild_id = ?", guild.id, json.dumps(config))
        
    def get(self, guild: discord.Guild, name: str, default: any = None):
        # get data
        data = self.__loadConfig(guild)
        
        # none check
        if data is None:
            return None
        
        # return
        return data.get(name, default)