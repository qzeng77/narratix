import pytest
from src.main import GameMaster

@pytest.fixture
def game_master():
    """Create a GameMaster instance"""
    return GameMaster()

def test_game_master_initialization(game_master):
    """Test GameMaster initialization"""
    assert game_master.dialogue_manager is not None
    assert game_master.game_state is None

def test_start_new_game(game_master):
    """Test starting a new game"""
    intro = game_master.start_new_game("Test", "Warrior")
    assert isinstance(intro, str)
    assert game_master.game_state is not None
    assert game_master.game_state.player.name == "Test"
    assert game_master.game_state.player.character_class == "Warrior"

def test_process_turn_without_game(game_master):
    """Test processing turn without starting game"""
    response = game_master.process_turn("Hello")
    assert response == "Please start a new game first."

def test_process_turn_with_game(game_master):
    """Test processing turn with active game"""
    game_master.start_new_game("Test", "Warrior")
    response = game_master.process_turn("Look around")
    assert isinstance(response, str)
    assert len(response) > 0