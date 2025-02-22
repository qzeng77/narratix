import pytest
from src.models.game_state import GameState, Character

def test_character_creation():
    """Test character creation with default stats"""
    character = Character(name="Test", character_class="Warrior")
    assert character.name == "Test"
    assert character.character_class == "Warrior"
    assert character.stats["health"] == 100
    assert character.stats["mana"] == 100
    assert len(character.inventory) == 0

def test_game_state_initialization():
    """Test game state initialization"""
    character = Character(name="Test", character_class="Warrior")
    game_state = GameState(player=character)
    
    assert game_state.current_location == "Starting Area"
    assert len(game_state.quest_log) == 0
    assert len(game_state.game_flags) == 0

def test_game_state_updates():
    """Test game state update methods"""
    character = Character(name="Test", character_class="Warrior")
    game_state = GameState(player=character)
    
    # Test location update
    game_state.update_location("Forest")
    assert game_state.current_location == "Forest"
    
    # Test quest addition
    game_state.add_quest("Find the magic sword")
    assert len(game_state.quest_log) == 1
    assert game_state.quest_log[0] == "Find the magic sword"
    
    # Test flag setting
    game_state.set_flag("met_wizard")
    assert game_state.game_flags["met_wizard"] is True