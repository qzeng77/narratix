from dataclasses import dataclass, field
from typing import Dict, List, Optional
from src.config.settings import GAME_CONFIG

@dataclass
class Character:
    name: str
    character_class: str
    stats: Dict[str, int] = field(default_factory=lambda: GAME_CONFIG["default_character_stats"].copy())
    inventory: List[str] = field(default_factory=list)

@dataclass
class GameState:
    player: Character
    current_location: str = "Starting Area"
    quest_log: List[str] = field(default_factory=list)
    game_flags: Dict[str, bool] = field(default_factory=dict)
    
    def update_location(self, new_location: str):
        self.current_location = new_location
    
    def add_quest(self, quest: str):
        self.quest_log.append(quest)
    
    def set_flag(self, flag_name: str, value: bool = True):
        self.game_flags[flag_name] = value
    
    def get_state_summary(self) -> str:
        """Returns a summary of the current game state"""
        return f"""
        Character: {self.player.name} ({self.player.character_class})
        Location: {self.current_location}
        Health: {self.player.stats['health']}
        Active Quests: {len(self.quest_log)}
        """